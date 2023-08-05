# Represents a "bag" of tiles - either the tiles that have not yet been
# revealed, the discard pile, or someone's hand

from tile import Tile

class BagOfTiles:
	# Represents all tiles available to the game

	def __init__(self):
		self.bag = [
			Tile("DOT_1", 4,  0),
			Tile("DOT_2", 4,  1),
			Tile("DOT_3", 4,  2),
			Tile("DOT_4", 4,  3),
			Tile("DOT_5", 4,  4),
			Tile("DOT_6", 4,  5),
			Tile("DOT_7", 4,  6),
			Tile("DOT_8", 4,  7),
			Tile("DOT_9", 4,  8),
			Tile("BAM_1", 4,  9),
			Tile("BAM_2", 4, 10),
			Tile("BAM_3", 4, 11),
			Tile("BAM_4", 4, 12),
			Tile("BAM_5", 4, 13),
			Tile("BAM_6", 4, 14),
			Tile("BAM_7", 4, 15),
			Tile("BAM_8", 4, 16),
			Tile("BAM_9", 4, 17),
			Tile("CRA_1", 4, 18),
			Tile("CRA_2", 4, 19),
			Tile("CRA_3", 4, 20),
			Tile("CRA_4", 4, 21),
			Tile("CRA_5", 4, 22),
			Tile("CRA_6", 4, 23),
			Tile("CRA_7", 4, 24),
			Tile("CRA_8", 4, 25),
			Tile("CRA_9", 4, 26),
			Tile("NORTH", 4, 27),
			Tile("EAST_", 4, 28),
			Tile("WEST_", 4, 29),
			Tile("SOUTH", 4, 30),
			Tile("SOAP_", 4, 31),
			Tile("GREEN", 4, 32),
			Tile("RED__", 4, 33),
			Tile("FLOWR", 8, 34),
			Tile("JOKER", 8, 35),
		]
		self.update_ungrouped_bag()

	def __str__(self):
		return '\n'.join([str(t) for t in self.bag])

	def zero_out(self):
		for t in self.bag:
			t.zero_out()
		self.update_ungrouped_bag()

	def increment(self,  tile_id):
		self.bag[tile_id].increment()
		self.update_ungrouped_bag()

	def decrement (self, tile_id):
		self.bag[tile_id].decrement()
		self.update_ungrouped_bag()

	def simplified_str(self):
		ret = '\n'.join([t.simplified_str() for t in self.bag if t.count > 0])
		if len(ret) == 0: return "Empty"
		return ret

	def update_ungrouped_bag(self):
		self.ungrouped_bag = []
		for tile in self.bag:
			self.ungrouped_bag += [tile.tile_id] * tile.count
