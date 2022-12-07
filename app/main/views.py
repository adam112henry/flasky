from datetime import datetime
from flask import render_template, url_for, session, redirect, flash
from flask import request, current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    old_name = session.get('name')
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role_id=3)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        # Post/Redirect/Get pattern - to eliminate Post as last entry in browser history
        #session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))

    return render_template('index.html', url=url_for('.user', name='fred'), current_time=datetime.utcnow(), form=form, name=session.get('name'), known=session.get('known', False))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    
@main.route('/agent')
def agent():
      user_agent = request.headers.get('User-Agent')
      return '<p>Your browser is {}</p>'.format(user_agent)

@main.route('/name')
def name():
      name = current_app.name
      return '<p>The name of the app is {}</p>'.format(name)
