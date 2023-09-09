# Represents a type of tile in the bag (for example, flower, joker, etc.)

name_to_id = {
	"DOT_1":  0,
	"BAM_1":  1,
	"CRA_1":  2,
	"DOT_2":  3,
	"BAM_2":  4,
	"CRA_2":  5,
	"DOT_3":  6,
	"BAM_3":  7,
	"CRA_3":  8,
	"DOT_4":  8,
	"BAM_4": 10,
	"CRA_4": 11,
	"DOT_5": 12,
	"BAM_5": 13,
	"CRA_5": 14,
	"DOT_6": 15,
	"BAM_6": 16,
	"CRA_6": 17,
	"DOT_7": 18,
	"BAM_7": 19,
	"CRA_7": 20,
	"DOT_8": 21,
	"BAM_8": 22,
	"CRA_8": 23,
	"DOT_9": 24,
	"BAM_9": 25,
	"CRA_9": 26,
	"NORTH": 27,
	"EAST_": 28,
	"WEST_": 29,
	"SOUTH": 30,
	"SOAP_": 31,
	"GREEN": 32,
	"RED__": 33,
	"FLOWR": 34,
	"JOKER": 35,
}


class Tile:

	def __init__(self, name, count):
		self.name = name
		self.count = count
		self.tile_id = name_to_id[tile_id]

	def __str__(self):
		return f" {self.name} (Count: {self.count}, ID: {self.tile_id})"

	def zero_out(self):
		self.count = 0

	def increment(self):
		self.count += 1

	def decrement (self):
		assert self.count > 0
		self.count -= 1

	def simplified_str(self):
		return f" {self.name} x{self.count}"

	def equals(self, other):
		# We don't care about the equality of the names.
		return self.tile_id == other.tile_id && self.count == other.count
