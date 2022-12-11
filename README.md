# hello Flasky

The Flasky app was created from the book [Flask Web Development](https://www.amazon.com/Flask-Web-Development-Developing-Applications/dp/1491991739).  The book's source code on Github is located here: [Flasky book source code](https://github.com/miguelgrinberg/flasky)

My version of the app is incomplete as I ran out of time after ch 9 and needed to move on to something else. Nonetheless, includes some good examples of basic Python/Flask idioms and usage.

## Get Started

```python
$ python3 -m venv venv # create virtual environment
$ source venv/bin/activate # activate virtual environment
(venv)$ pip install -r requirements.txt
```

## Database Setup (SQLite)

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
# then upgrade database(s)
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

## Docker usage

```bash
# this will kill everything in docker
$ docker system prune -a --volumes
# ensure shell script is executable
$ chmod +x boot.sh
# build the container
$ docker build -t flasky:latest .
# create and run the container - i.e. first time
$ docker run --name flasky -d -p 8000:5000 flasky:latest
# gunicorn running on port 5000 and mapped to localhost:8000
# -OR- start the existing container
$ docker start flasky
# get the container ID
$ docker container ls  # OR
$ docker ps
# open a shell session on the container
$ docker exec -it [container id] sh
# exit the shell
$ exit
# stop the container
$ docker stop flasky
```
