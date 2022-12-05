from flask import Flask, render_template, url_for, session, redirect, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import request
from flask import current_app
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # Post/Redirect/Get pattern - to eliminate Post as last entry in browser history
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', url=url_for('user', name='fred'), current_time=datetime.utcnow(), form=form, name=session.get('name'))

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