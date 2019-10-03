# CP317-W2018-G3

### Documents
* Located at `documents/Subby-Requirements.md`
* Viewable at the following addresses:
  * Requirements: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Requirements.md.html
  * Requirements SQA: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/SQA-Requirements.html
  * Analysis: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Analysis.md.html
  * Analysis SQA: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/SQA-Analysis.html
  * Design: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Design.md.html
  * Analysis SQA: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/SQA-Design.html
  * Github IDs: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Github-IDs.html
  * Subgroup Assignments: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subgroup-Assignments.html
    * _Notes on work performed in documentation is generally more accurate_
  * Code Coverage Report: https://rawgit.com/Kuresov/CP317-W2018-G3/master/htmlcov/index.html

### Developer Notes
#### Running Subby (Development)
  * Install PostgreSQL with the default admin user settings, reachable at localhost:
    * DB Name: subby, use PSQL cmd line to create database with code `CREATE DATABASE subby;`
    * User: postgres
    * Password: postgres
    * Port: 5432
  * Ensure `python` and `pip` are installed (or the appropriate python 3.X and python3-pip for your platform). From the project directory, run `pip install -r requirements.txt`. Windows users need to put python and python/scripts path to the path of system variables before using python and pip in command line.
  * Check migrations with `python manage.py makemigrations --settings=subby_project.settings.development` first.
  * Ensure that migrations have been performed; run `python manage.py migrate --settings=subby_project.settings.development`.
  * From the project directory, run `python manage.py runserver --settings=subby_project.settings.development`. Subby will be running at `http://127.0.0.1:8000`. `localhost:8000` will be rejected by recaptcha.

#### Production
  * The project will be running at https://cp317-w2018-g3.herokuapp.com/ for a period of time after the submission date. Note that latent errors still listed in the SQA documentation, such as image uploading, will still be present.

#### Testing
  * Run tests (without coverage): `python manage.py test --settings=subby_project.settings.development`
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

#### Convenient aliases for Windows users:
* `doskey runserver=python manage.py runserver --settings=subby_project.settings.development`
* `doskey makemigrations=python manage.py makemigrations --settings=subby_project.settings.development`
* `doskey migrate=python manage.py migrate --settings=subby_project.settings.development`
* `doskey createsuperuser=python manage.py createsuperuser --settings=subby_project.settings.development`
* `doskey static=python manage.py collectstatic --settings=subby_project.settings.development`
