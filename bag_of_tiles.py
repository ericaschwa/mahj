# Represents a "bag" of tiles - either the tiles that have not yet been
# revealed, the discard pile, or someone's hand

from tile import Tile

class BagOfTiles:
	# Represents all tiles available to the game

	def __init__(self):
		self.bag = [
			Tile("DOT_1", 4),
			Tile("BAM_1", 4),
			Tile("CRA_1", 4),
			Tile("DOT_2", 4),
			Tile("BAM_2", 4),
			Tile("CRA_2", 4),
			Tile("DOT_3", 4),
			Tile("BAM_3", 4),
			Tile("CRA_3", 4),
			Tile("DOT_4", 4),
			Tile("BAM_4", 4),
			Tile("CRA_4", 4),
			Tile("DOT_5", 4),
			Tile("BAM_5", 4),
			Tile("CRA_5", 4),
			Tile("DOT_6", 4),
			Tile("BAM_6", 4),
			Tile("CRA_6", 4),
			Tile("DOT_7", 4),
			Tile("BAM_7", 4),
			Tile("CRA_7", 4),
			Tile("DOT_8", 4),
			Tile("BAM_8", 4),
			Tile("CRA_8", 4),
			Tile("DOT_9", 4),
			Tile("BAM_9", 4),
			Tile("CRA_9", 4),
			Tile("NORTH", 4),
			Tile("EAST_", 4),
			Tile("WEST_", 4),
			Tile("SOUTH", 4),
			Tile("SOAP_", 4),
			Tile("GREEN", 4),
			Tile("RED__", 4),
			Tile("FLOWR", 8),
			Tile("JOKER", 8),
		]
		self.update_ungrouped_bag()

	def __init__(self, tiles):
		self.bag = tiles
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

	def simplified_str(self, delimiter='\n'):
		ret = delimiter.join([t.simplified_str() for t in self.bag if t.count > 0])
		if len(ret) == 0: return "Empty"
		return ret

	def update_ungrouped_bag(self):
		self.ungrouped_bag = []
		for tile in self.bag:
			self.ungrouped_bag += [tile.tile_id] * tile.count
