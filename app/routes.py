from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, logout_user
from app import app
import mongoengine
from app.models.user import User
from app.forms import RegisterForm, LoginForm





@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects().filter(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        flash(form.password.data)
        user = User()
        user.username = form.username.data
        user.password = user.set_password(form.password.data)
        try:
            user.save()
            flash('Account created!')
            return redirect(url_for('index'))
        except mongoengine.errors.NotUniqueError:
            flash('You chose a name thats already taken')
        except mongoengine.errors.ValidationError:
            flash('validation error!')
        return redirect(url_for('create_account'))
    return render_template('createaccount.html', form=form)