from flask import render_template, redirect, request, url_for, flash, session
from flask_login import login_user, logout_user, login_required
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm, DeleteUserForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.user_name.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            session['name'] = form.user_name.data
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password')

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session['name'] = ''
    flash('You have been logged out')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, role_id=3)
        db.session.add(user)
        db.session.commit()
        flash('User created, you can now log in')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    current_user = User.query.filter_by(username=session.get('name')).first()
    if not current_user.isAdmin:
        flash('You cannot perform this function unless you are an admin')
        return redirect(url_for('main.index'))

    form = DeleteUserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        db.session.delete(user)
        db.session.commit()
        flash(f'User {form.username.data} has been deleted')
        return redirect(url_for('main.index'))

    return render_template('auth/delete.html', form=form)
