from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title = 'Home',
        username = 'Alex',
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user: %s' % form.username.data)
        return redirect('/')
    return render_template(
        'login.html',
        title = 'Sign In',
        form = form
    )
