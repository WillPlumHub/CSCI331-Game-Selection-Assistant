from howlongtobeatpy import HowLongToBeat

def get_games(name: str):
	results = HowLongToBeat().search(name)

	for game in results:

		if game != None:
			print(str(game.game_id))


if __name__ == "__main__":
	get_games("ratchet and clank")