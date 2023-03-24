from flask import Blueprint, request, session, render_template, g

bp = Blueprint('collection', __name__, url_prefix='/')

@bp.route('/games', methods=['GET', 'POST'])
def games():
	return str(session['user_id'])