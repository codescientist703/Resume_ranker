from flasksite.models import User, Post
from flasksite import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from flasksite.form import RegistrationForm, LoginForm

posts = [
	{
		'author' : 'Nihal Mittal',
		'title' : 'Post 1'
	}

]

@app.route('/')
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created! You can now login !', 'success')
		return redirect(url_for('home'))
	return render_template('register.html',title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'nihalgreat@site.com' and form.password.data == '1234':
			flash('You are logged in!','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password.','danger')

	return render_template('login.html',title='login', form=form)
