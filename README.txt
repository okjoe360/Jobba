$ venv/Scripts/activate

FLASK DB MIGRATE
    - set FLASK_APP=run.py
    - flask db stamp head
    - flask db init
    - flask db migrate
    - flask db upgrade
    - flask db --help