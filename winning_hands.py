# Represents all possible winning hands in mahjong
# For now, we're excluding closed hands and hands that have pairs or other
# joker-ineligible groupings.

from tile import Tile

WINNING_HANDS = [
	# 222 0000 222 3333
	[Tile("BAM_2", 3), Tile("SOAP_", 4), Tile("CRA_2", 3), Tile("CRA_3", 4)],
	[Tile("BAM_2", 3), Tile("SOAP_", 4), Tile("DOT_2", 3), Tile("DOT_3", 4)],
	[Tile("CRA_2", 3), Tile("SOAP_", 4), Tile("BAM_2", 3), Tile("BAM_3", 4)],
	[Tile("CRA_2", 3), Tile("SOAP_", 4), Tile("DOT_2", 3), Tile("DOT_3", 4)],
	[Tile("DOT_2", 3), Tile("SOAP_", 4), Tile("BAM_2", 3), Tile("BAM_3", 4)],
	[Tile("DOT_2", 3), Tile("SOAP_", 4), Tile("CRA_2", 3), Tile("CRA_3", 4)],

	# 
]