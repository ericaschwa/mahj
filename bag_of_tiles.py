# Represents a "bag" of tiles - either the tiles that have not yet been
# revealed, the discard pile, or someone's hand

from constants import *

class BagOfTiles:
	# Represents all tiles available to the game

	def __init__(self):
		self.bag = [
			DOTS_1,
			DOTS_2,
			DOTS_3,
			DOTS_4,
			DOTS_5,
			DOTS_6,
			DOTS_7,
			DOTS_8,
			DOTS_9,
			BAMS_1,
			BAMS_2,
			BAMS_3,
			BAMS_4,
			BAMS_5,
			BAMS_6,
			BAMS_7,
			BAMS_8,
			BAMS_9,
			CRACKS_1,
			CRACKS_2,
			CRACKS_3,
			CRACKS_4,
			CRACKS_5,
			CRACKS_6,
			CRACKS_7,
			CRACKS_8,
			CRACKS_9,
			NORTH,
			EAST,
			WEST,
			SOUTH,
			SOAP,
			GREEN,
			RED,
			FLOWER,
			JOKER,
		]

	def __str__(self):
		return '\n'.join([str(t) for t in self.bag])

	def zero_out(self):
		for t in self.bag:
			t.zero_out()

	def increment(self,  tile_id):
		self.bag[tile_id].increment()

	def decrement (self, tile_id):
		self.bag[tile_id].decrement()