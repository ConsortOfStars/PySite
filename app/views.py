from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm, RegistrationForm
from .models import User
from passlib.hash import pbkdf2_sha256
from datetime import timedelta

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=7)
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title = 'Home',
        username = g.user,
        posts = [
            {
                'author': 'John Smith',
                'body': 'This is a news article...'
            },
            {
                'author': 'Anonymous',
                'body': 'This is not a news article...'
            }
        ]
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember.data
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            flash("Username/password combo didn't work. Try again.")
            return redirect(url_for('login'))
        else:
            pw_hash = user.get_password()
            valid = pbkdf2_sha256.verify(form.password.data, pw_hash)
            if not valid:
                flash("Username/password combo didn't work. Try again.")
                return redirect(url_for('login'))
            else:
                login_user(user, remember = session['remember_me'])
                return redirect(request.args.get('next') or url_for('index'))
    return render_template(
        'login.html',
        title = 'Sign In',
        form = form
    )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember.data
        user = User.query.filter_by(username = form.username.data).first()
        if user is None and form.accept.data == True:
            pw_hash = pbkdf2_sha256.encrypt(form.password.data, rounds=200000)
            user = User(
                username = form.username.data,
                email = form.email.data,
                password = pw_hash,
                level = 1,
                banned = False
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login')) #Creation success
        else:
            return redirect(url_for('register')) #Duplicate username
    return render_template(
        'register.html',
        title = 'Register',
        form = form
    )
