import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='')


@bp.route('/register', methods=('GET', 'POST'))
def register():

	if request.method == 'POST':
		db = get_db()
		error = None

		email = request.form['email']
		password = request.form['password']
		name = request.form['name']

		if email is None:
			error = 'Email is required.'
		elif password is None:
			error = 'Password is required.'
		elif name is None:
			error = 'Name is required.'
			
		if error is None:

			try:
				user = db.add_user(email, password, name)
				
				if user is None:
					error='Failed to register account'

			except Exception as e:
				error = "Failed to register account"
			else:
				set_session(user)
				return redirect(url_for("collection.view"))
				
		flash(error)
		
	return render_template('auth/register.html')
	

@bp.route('/login', methods=('GET', 'POST'))
def login():

	if request.method == 'POST':
		db = get_db()
		error = None

		email = request.form['email']
		password = request.form['password']

		user = db.get_user(email=email, password=password)

		if user is None:
			error = 'Login failed'
			
		if error is None:
			set_session(user)
			return redirect(url_for('collection.view'))
			
		flash(error)
		
	return render_template('auth/login.html')
	

@bp.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('auth.login'))


@bp.route('/view')
def view():

	if(g.user is None):
		return redirect(url_for('auth.login'))

	return render_template('auth/view.html')


@bp.before_app_request
def load_logged_in_user():
	db = get_db()
	userId = session.get('user.id')

	if userId is None:
		g.user = None
	else:
		g.user = db.get_user(id=userId)


def set_session(user):
	session.clear()
	session['user.id'] = user['id']
	g.user = user