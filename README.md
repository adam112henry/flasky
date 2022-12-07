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
(venv)$ export FLASK_APP=flasky.py
(venv)$ export FLASK_DEBUG=1
(venv)$ flask shell
>>> from flasky import db
>>> db.create_all()
-- OR --
(venv)$ echo $FLASK_CONFIG # check which environment is active - there are separate dbs to upgrade for "development" and "production"
(venv)$ flask db upgrade  # apply after creating a new script
```

## Create migration script
```bash
(venv)$ flask db migrate -m "database updates"
```


## Create roles

```python
(venv)$ flask shell
>>> from flasky import db
>>> from flasky import Role, User
>>> admin_role = Role(name='Admin')
>>> db.session.add(admin_role)
>>> db.session.commit() 
# do the same for 'Moderator' and 'User' roles

-- OR --
# use the static functions
(venv)$ flask shell
>>> Role.insert_roles()
>>> # create function for users
```

## Run the app

```python
(venv)$ flask run --debugger --reload
then http://localhost:5000
```

## Run the tests

```python
(venv)$ flask test
```
