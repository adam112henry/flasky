from flask import Flask
from flask import request
from flask import current_app

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Hello World!</h1>
    <a href=/user/adam>/user/adam</a><br/>
    <a href=/agent>/agent</a><br/>
    <a href=/name>/name</a>"""

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
    
@app.route('/agent')
def agent():
      user_agent = request.headers.get('User-Agent')
      return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/name')
def name():
      name = current_app.name
      return '<p>The name of the app is {}</p>'.format(name)
