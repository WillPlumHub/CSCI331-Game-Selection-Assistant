import os

from flask import Flask, session

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'gsa.db'),
	)
	
	if test_config is None: #load instance config when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)
		
	try: #ensure instance folder exists
		os.makedirs(app.instance_path)
	except OSError:
		pass

	#hello world
	@app.route('/')
	def index():
		test = session.get('user_id')
		return str(test) + ' Test Index Page'
	
	from . import db
	db.init_app(app)	
	
	from . import auth
	app.register_blueprint(auth.bp)
	
	from . import collection
	app.register_blueprint(collection.bp)

	return app
