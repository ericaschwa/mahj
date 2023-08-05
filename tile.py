# Represents a type of tile in the bag (for example, flower, joker, etc.)

class Tile:

	def __init__(self, name, count, tile_id):
		self.name = name
		self.count = count
		self.tile_id = tile_id

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
