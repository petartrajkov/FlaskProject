GITHub Link:
https://github.com/petartrajkov/FlaskTask

------------------------------------------
Terminal shortcuts:

mkdir NewFolder - creating new folder
cd Desktop - changing path to Desktop
ls - list files

How to kill a process that is a using port on macOS:

> sudo lsof -i :<PortNumber>  # returns list of processes using the port, with PID

> kill -9 <PID>  # kill the specific pid
For example, you can find out what’s running on port number 8080 by running the command:
❯ sudo lsof -i :8080
❯ kill -9 50693

---------------------------------------------------------------
FLASK:

Create an environment
Create a project folder and a venv folder within:
macOS/LinuxWindows
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv

Activate the environment
Before you work on your project, activate the corresponding environment:
macOS/LinuxWindows
$ . venv/bin/activate
Your shell prompt will change to show the name of the activated environment.
Install Flask
Within the activated environment, use the following command to install Flask:
$ pip install Flask

------------
to enable virtual environment in Terminal in VSCode ->
type: 
virtualenv env
or:
virtualenv flask => cd flask 

to activate virtual environment in Terminal in VSCode ->
source env/bin/activate  

to deactivate virtual environment in Terminal in VSCode ->
deactivate

to install Flask SQL Alchemy:
pip3 install flask flask-sqlalchemy

To run a python app in Terminal:
python3 main.py (main.py is the name of the app I chose)

or

FLASK_APP=<file>.py flask run (FLASK_APP=dbs.py flask run)


to install Requests and Supported Versions:
pip install requests

------------

POSTMAN:

To test the POST endpoint, I used Postman.

Steps to test:
1. Install Postman (https://www.postman.com)
2. Create a Workspace/Collection
3. Add Request > POST
4. In the URL enter: http://127.0.0.1:8000/stringcounter-response
5. In the Headers, add Content-Type: application/json
6. In the Body > select Raw > enter a JSON, example below

{
    "array" : ["Oracle Linux", "Debian", "Oracle Linux", "Debian", "Ubuntu"]
}

7. Press Send
8. Observe the Response, which should be:
{'Oracle Linux': 2, 'Debian': 2, 'Ubuntu': 1}

---------------

TESTING:

$ pip install pytest
$ pip install requests (only used for test.py which is a testing sandbox, not for test_tier2.py)

# to write a test we need to start a function that begins with test_
# to run the test in terminal we write pytest or pytest <name of file> example "pytest test.py"
# to check the data one can use the command in Terminal: "pytest test.py -v -s"

-----------------------------------------------------------

For Tier 4 - DB task:

Used resources:
https://youtu.be/Z1RJmh_OqeA
https://youtu.be/SYG1jQYIxfQ
https://youtu.be/Ny1g-Wk5nyM

https://eu.pythonanywhere.com/
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/models/
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/config/#connection-url-format
https://pypi.org/project/pymysql/
https://sqlite.org/download.html
https://sqlitebrowser.org/dl/ - GUI for SQLite


!Important: This Tier is partially complete

To create a DB, in terminal we make sure we're in the ENV and we type:

>>> from dbs import app, db
>>> app.app_context().push()
>>> db.create_all()

-----------

to avoid the error: RuntimeError: Working outside of application context do this:

in terminal we make sure we're in the ENV and we type

>>> from dbs import app, db, OSVersion, ComputeInstance
>>> app.app_context().push()
>>> db.create_all() / OSVersion.query.all()
>>> exit()

* app.app_context().push() is to be used all the time

- To check the schema of the DB via sqlite3: (be in the ENV, not in Python)
>>> sqlite3 db.sqlite3
>>> .tables
>>> .schema
>>> .exit() or control+D if .exit() fails

* TO ADD DATA IN THE DB:

in the Python terminal:
instance = ComputeInstance(os_version_id=1, ip_address="192.168.1.1", hostname="myhost")
db.session.add(instance)
db.session.commit()
-----------------------------------------------------------
data is being added successfully without errors
