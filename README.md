## Lorekeeper Link Crawler/Tester
_"Still faster than checking by hand!"_

This script will attempt to find every link on your Lorekeeper website, visit it, and see if it receives a 500 error. It generates an `errors.html` file at the end with all the errors it found.

![image](https://github.com/user-attachments/assets/c4ef3db6-8986-421b-a193-3cb0d08b6893)

#### How to use:

**Make sure your local copy of Lorekeeper is currently running.**

1. Install [Python 3](https://www.python.org/downloads/).
2. Clone this repo locally -- NOT in your Lorekeeper directory. Put it somewhere else completely separate.
3. Run these commands to create a Python virtual environment:
    1. `pip install virtualenv`
    2. `virtualenv venv`
    3. `source venv/scripts/activate` (Linux) or `venv/scripts/activate.bat` (Windows) or `venv/scripts/activate.ps1` (Powershell) or however else you activate your virtualenvs.
       - On Windows, I recommend using Git bash and `source venv/scripts/activate`.
    5. `pip install -r requirements.txt`
4. Run `python crawler.py`.
5. Answer the prompts then let it fly!
6. Open the created `errors.html` file to view a report of all the errors the script found.

#### Precautions:
- This script can take a long time to run (over 15-30m). If you have a LOT of test data, it can take a long, _long_ time. I recommend creating a new database for this script and populating it with limited data if you have a lot in your current test database.
- **Run this on your local!** Do not run it on live for both the reasons above and you don't want to slam your live website with unnecessary requests.
