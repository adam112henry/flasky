from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import request
from flask import current_app
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', url=url_for('user', name='fred'), current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    
@app.route('/agent')
def agent():
      user_agent = request.headers.get('User-Agent')
      return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/name')
def name():
      name = current_app.name
      return '<p>The name of the app is {}</p>'.format(name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500