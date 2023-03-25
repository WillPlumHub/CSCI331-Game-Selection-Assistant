from flask import Blueprint, request, session, render_template, g
from .db import get_db

bp = Blueprint('collection', __name__, url_prefix='')


@bp.route('/', methods=['GET', 'POST'])
def games():
	return render_template('collection/games.html')


@bp.before_app_request
def get_users_games():

	if g.user is not None:
		db = get_db()

		g.collection = db.execute(
			'SELECT * FROM collection JOIN game 	\
			ON collection.gameId=game.id 			\
			WHERE userId=?',
			[g.user['id']]
			).fetchall()
	else:
		g.collection = []

