# Represents the environment of the game, including everything about its current state

from bag_of_tiles import BagOfTiles
import random

# Note that East has one more, and one more is needed for the final hands
TILES_PER_PLAYER = 13
NUM_PLAYERS = 4

class Environment:

	def __init__(self, east_player=-1):
		self.visible_tiles = BagOfTiles()
		self.hidden_tiles = BagOfTiles()
		if east_player >= 0 and east_player < NUM_PLAYERS:
			self.east_player = east_player
		else:
			self.east_player = random.choice(range(NUM_PLAYERS))
		self.hands = []
		for i in range(NUM_PLAYERS):
			self.hands.append(BagOfTiles())
		# First, all tiles are hidden : zero out the visible tiles and the hands
		self.visible_tiles.zero_out()
		for hand in self.hands:
			hand.zero_out()
		# Then, deal.
		self.deal()

	def __str__(self):
		ret = f"East: {self.east_player}\n"
		ret += f"Visible Tiles:\n{self.visible_tiles.simplified_str()}\n\n"
		ret += f"Hiddden Tiles:\n{self.hidden_tiles.simplified_str()}\n\n"
		for player in range(NUM_PLAYERS):
			ret += f"Player {player}:\n{self.hands[player].simplified_str()}\n\n"
		return ret

	def deal(self):
		for player in range(NUM_PLAYERS):
			for i in range(TILES_PER_PLAYER):
				chosen_tile_id = random.choice(self.hidden_tiles.ungrouped_bag)
				self.hands[player].increment(chosen_tile_id)
				self.hidden_tiles.decrement(chosen_tile_id)

		# Give one extra to East.
		chosen_tile_id = random.choice(self.hidden_tiles.ungrouped_bag)
		self.hands[self.east_player].increment(chosen_tile_id)
		self.hidden_tiles.decrement(chosen_tile_id)

e = Environment()
print(e)
