# Constants for use in mahj

# Note that East has one more, and one more is needed for the final hands
TILES_PER_PERSON = 13

class Tile:
	# Represents one tile

	def __init__(self, name, count, tile_id):
		self.name = name
		self.count = count
		self.tile_id = tile_id

	def __str__(self):
		return f" {self.name} (Count: {self.count}, ID: {self.tile_id})"

	def increment(self):
		self.count += 1

	def decrement (self):
		assert self.count > 0
		self.count -= 1

	def zero_out(self):
		self.count = 0

DOTS_1   = Tile("DOT_1", 4,  0)
DOTS_2   = Tile("DOT_2", 4,  1)
DOTS_3   = Tile("DOT_3", 4,  2)
DOTS_4   = Tile("DOT_4", 4,  3)
DOTS_5   = Tile("DOT_5", 4,  4)
DOTS_6   = Tile("DOT_6", 4,  5)
DOTS_7   = Tile("DOT_7", 4,  6)
DOTS_8   = Tile("DOT_8", 4,  7)
DOTS_9   = Tile("DOT_9", 4,  8)
BAMS_1   = Tile("BAM_1", 4,  9)
BAMS_2   = Tile("BAM_2", 4, 10)
BAMS_3   = Tile("BAM_3", 4, 12)
BAMS_4   = Tile("BAM_4", 4, 13)
BAMS_5   = Tile("BAM_5", 4, 14)
BAMS_6   = Tile("BAM_6", 4, 15)
BAMS_7   = Tile("BAM_7", 4, 16)
BAMS_8   = Tile("BAM_8", 4, 17)
BAMS_9   = Tile("BAM_9", 4, 18)
CRACKS_1 = Tile("CRA_1", 4, 19)
CRACKS_2 = Tile("CRA_2", 4, 20)
CRACKS_3 = Tile("CRA_3", 4, 21)
CRACKS_4 = Tile("CRA_4", 4, 22)
CRACKS_5 = Tile("CRA_5", 4, 23)
CRACKS_6 = Tile("CRA_6", 4, 24)
CRACKS_7 = Tile("CRA_7", 4, 25)
CRACKS_8 = Tile("CRA_8", 4, 26)
CRACKS_9 = Tile("CRA_9", 4, 27)
NORTH    = Tile("NORTH", 4, 28)
EAST     = Tile("EAST_", 4, 29)
WEST     = Tile("WEST_", 4, 30)
SOUTH    = Tile("SOUTH", 4, 31)
SOAP     = Tile("SOAP_", 4, 32)
GREEN    = Tile("GREEN", 4, 33)
RED      = Tile("RED__", 4, 34)
FLOWER   = Tile("FLOWR", 8, 35)
JOKER    = Tile("JOKER", 8, 36)
