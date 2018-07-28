# CP317-W2018-G3

### Requirements Document
* Located at `documents/Subby-Requirements.md`
* Viewable at: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Requirements.md.html

### Developer Notes
#### Running Subby (Development)
  * Install PostgreSQL with the default admin user settings, reachable at localhost:
    * DB Name: subby
    * User: postgres
    * Password: postgres
    * Port: 5432
  * Ensure `python` and `pip` are installed (or the appropriate python 3.X and python3-pip for your platform). From the project directory, run `pip install -r requirements.txt`. Windows users need to put python and python/scripts path to the path of system variables.
  * Ensure that migrations have been performed; run `python manage.py migrate --settings=subby_project.settings.development`
  * From the project directory, run `python manage.py runserver --settings=subby_project.settings.development`. Subby will be running at `http://localhost:8000`
  * To create a super user run `python manage.py createsuperuser --settings=subby_project.settings.development`. You will now be able to login using the info you enter.
 
#### Testing
  * Run tests (without coverage): `python run manage.py test --settings=subby_project.settings.development`
  * Run tests (with coverage): `coverage run manage.py test --settings=subby_project.settings.development`
  * Generate coverage document: `coverage html`
  * View coverage document at: `... /CP317-W2018-G3/htmlcov/index.html`

#### Required dependencies:
  * PostgreSQL
  * Python3 and supporting packages

#### Optional Dependencies:
  * Node + npm (for Markdown generation)

#### Tasks
  * `gulp markdown` will generate clean HTML from the .md files in `documents/`. Use this instead of editing the HTML directly to avoid losing changes.

#### windows doskey alias:
* doskey runserver=python manage.py runserver --settings=subby_project.settings.development
* doskey makemigrations=python manage.py makemigrations --settings=subby_project.settings.development
* doskey migrate=python manage.py migrate --settings=subby_project.settings.development
* doskey createsuperuser=python manage.py createsuperuser --settings=subby_project.settings.development
* doskey static=python manage.py collectstatic --settings=subby_project.settings.development
