# Represents the environment of the game, including everything about its current state

from bag_of_tiles import BagOfTiles
import random

# Note that East has one more, and one more is needed for the final hands
TILES_PER_PLAYERS = 13
NUM_PLAYERS = 4

class Environment:

	def __init__(self, east_player=-1):
		self.visible_tiles = BagOfTiles()
		self.hidden_tiles = BagOfTiles()
		if east_player >= 0 and east_player < NUM_PLAYERS:
			self.east_player = east_player
		else:
			self.east_player = random.choice(range(NUM_PLAYERS))
		self.hands = [BagOfTiles()] * NUM_PLAYERS
		# Currently all tiles are hidden : zero out the visible tiles and the hands
		self.visible_tiles.zero_out()
		for hand in self.hands:
			hand.zero_out()

	def __str__(self):
		ret = f"East: {self.east_player}\n"
		ret += f"Visible Tiles:\n{self.visible_tiles.simplified_str()}\n"
		ret += f"Hiddden Tiles:\n{self.hidden_tiles.simplified_str()}\n"
		for player in range(NUM_PLAYERS):
			ret += f"Player {player}: {self.hands[player].simplified_str()}\n"
		return ret