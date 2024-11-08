## Lorekeeper Link Crawler/Tester
_"Still faster than checking by hand!"_

This script will attempt to find every link on your Lorekeeper website, visit it, and see if it receives a 500 error. It generates an `errors.html` file at the end with all the errors it found.

![image](https://github.com/user-attachments/assets/c4ef3db6-8986-421b-a193-3cb0d08b6893)

### Precautions:
- This script can take a long time to run (over 15-30m). If you have a LOT of test data, it can take a long, _long_ time. I recommend creating a new database for this script and populating it with limited data if you have a lot in your current test database.
- **Run this on your local!** Do not run it on live for both the reasons above and you don't want to slam your live website with unnecessary requests.

### How to use:

**Make sure your local copy of Lorekeeper is currently running.**

1. Install [Python 3](https://www.python.org/downloads/).
2. Clone this repo locally -- NOT in your Lorekeeper directory. Put it somewhere else completely separate.
3. Create a Python virtual environment. There are many ways to do this. I do it this way: 
    1. Open the directory for this repo on the command line.
    2. `pip install virtualenv`
    3. `virtualenv venv`
    4. `source venv/scripts/activate` (Linux) or `cd venv/scripts && activate.bat` (Windows)
       - If you are on windows you will also have to `cd ..` twice after the above command.
    6. `pip install -r requirements.txt`
5. Run `python crawler.py`.
6. Answer the prompts then let it fly!
7. Open the created `errors.html` file to view a report of all the errors the script found.
