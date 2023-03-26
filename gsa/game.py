from flask import Blueprint, request, session, render_template, g

from .db import get_db

bp = Blueprint('game', __name__, url_prefix='')


@bp.route('/game/<gameId>', methods=['GET', 'POST'])
def view(gameId):
	db = get_db()

	g.game = db.get_game(id=gameId)
	g.in_collection = False

	if(g.user != None):
		# Try to add/remove based on the game page form selection
		if(request.method == 'POST'):

			if(request.form['do'] == 'add'):
				db.add_user_game(g.user['id'], g.game['id'])

			elif(request.form['do'] == 'remove'):
				db.remove_user_game(g.user['id'], g.game['id'])

		# Check if game is in the user's games
		for item in db.get_user_games(userId=g.user['id']):
			if item['gameId'] == g.game['id']:
				g.in_collection = True
				break

	return render_template('game/view.html')