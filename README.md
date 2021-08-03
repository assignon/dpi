# dpi

pipenv shell

pip install requirements.txt

python manage.py makemigration

python manage.py migrate && python manage.py runserver

### test the insert of csv data in DB
- in hotels/views.py file
- at the bottom there is a commented code.
- remove the # where there is only one
- and python manage.py runserver to run the code
- you should receive an msg in de cmd is the insert is succeed
