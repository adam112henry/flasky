# hello Flasky

[Flasky book source code](https://github.com/miguelgrinberg/flasky)

[SQLite Web Viewer](https://sqliteviewer.app/?ref=vscode)

## Get Started

```python
$ python3 -m venv venv # create virtual environment
$ source venv/bin/activate # activate virtual environment
(venv)$ pip install -r requirements.txt
```

## Database Setup

```bash
$ source venv/bin/activate
(venv)$ export FLASK_APP=hello.py
(venv)$ export FLASK_DEBUG=1
(venv)$ flask shell
>>> from hello import db
>>> db.create_all()
-- OR --
(venv)$ flask db upgrade
```

## Run the app

```python
(venv)$ flask run --debugger --reload
then http://localhost:5000
```
