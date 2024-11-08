""" crawler.py - python script for finding lorekeeper error pages """

import os
import shutil
import sys
from bs4 import BeautifulSoup
import requests
from jinja2 import Environment, FileSystemLoader

# global vars
urls=[]
visitedurls=[]
error_urls={}

# recursion script
def get_all_links_on_page(session, link):
    response = session.get(link)
    soup = BeautifulSoup(response.text, features="html.parser")

    # if we found an error, record it
    # we look for the "noscript" tag because that's only gonna show up on laravel server error pages
    if soup.find("noscript"):
        print()
        print(RED + "Error found with URL: " + RESET + BLUE + url + RESET)
        print(RED + soup.find("noscript").text + RESET)
        print()
        error_urls[link] = soup.find("noscript").text

    for link in soup.find_all('a'):
        if (link.get('href') is not None and "localhost" in link.get('href')):
            urls.append(link.get('href'))


#########################################
# Setup our console
# Define some common ANSI color codes
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

os.system('color')

# Get our user input vars
home = input(YELLOW + "- Enter localhost URL (typically http://localhost): " + RESET)

email = input(YELLOW + "- Enter admin email: " + RESET)

password = input(YELLOW + "- Enter admin password: " + RESET)

# Create login payload
payload = {
    'email': email,
    'password': password
}

with requests.Session() as sess:
    # begin session by logging in with our payload + adding the csrf token
    res = sess.get(home + '/login')
    signin = BeautifulSoup(res._content, 'html.parser')
    payload['_token'] = signin.find('input', {"name" : "_token"})['value']
    res = sess.post(home + '/login', data=payload)
    print(GREEN + "Login successful!" + RESET)

    # initiate the recursion
    get_all_links_on_page(sess, home)

    for url in urls:
        if url not in visitedurls and "feeds" not in url:

            sys.stdout.write("\r" + (" " * shutil.get_terminal_size().columns))
            sys.stdout.flush()
            sys.stdout.write("\r Checking... " + BLUE + url + RESET)
            sys.stdout.flush()
            
            get_all_links_on_page(sess, url)
            visitedurls.append(url)

# when our recursion is complete, create the error log file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('resources/template.html')

rendered_template = template.render({'errors': error_urls})

with open("errors.html", "w", encoding="utf-8") as f:
    f.write(rendered_template)

print()
print(GREEN + "Done!" + RESET + " Please open the generated errors.html to view your error report.")
