## Lorekeeper Link Crawler
_"Still faster than checking by hand!"_

This script will attempt to find every link on your Lorekeeper website, visit it, and see if it receives a 500 error. It generates an `errors.html` file at the end with all the errors it found.

![image](https://github.com/user-attachments/assets/c4ef3db6-8986-421b-a193-3cb0d08b6893)

#### How to use:
- Install [Python 3](https://www.python.org/downloads/).
- Clone this repo locally.
- Run these commands:
    - `pip install virtualenv`
    - `virtualenv venv`
    - `source venv/scripts/activate` (Linux) or `venv/scripts/activate.bat` (Windows) or `venv/scripts/activate.ps1` (Powershell) or however else you activate your virtualenvs
    - `pip install -r requirements.txt`
- Run `python crawler.py`.
- Answer the prompts then let it fly!
- Open the created `errors.html` file to view a report of all the errors the script found.

#### Precautions:
- This script can take a long time to run (over 15-30m). If you have a LOT of test data, it can take a long, _long_ time. I recommend creating a new database for this script and populating it with limited data if you have a lot in your current test database.
- **Run this on your local!** Do not run it on live for both the reasons above and you don't want to slam your live website with unnecessary requests.
