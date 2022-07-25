### Incase venv is in the current directory
pip install coverage
coverage run --omit='*/venv/*' manage.py test
coverage html
