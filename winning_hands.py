# Represents all possible winning hands in mahjong
# For now, we're excluding closed hands and hands that have pairs or other
# joker-ineligible groupings.

from bag_of_tiles import BagOfTiles
from tile import Tile, ID_TO_NAME

def populate_winning_hands():
	winning_hands = [
		# 222 0000 222 3333 (any 2 suits)
		[Tile("BAM_2", 3), Tile("SOAP_", 4), Tile("CRA_2", 3), Tile("CRA_3", 4)],
		[Tile("BAM_2", 3), Tile("SOAP_", 4), Tile("DOT_2", 3), Tile("DOT_3", 4)],
		[Tile("CRA_2", 3), Tile("SOAP_", 4), Tile("BAM_2", 3), Tile("BAM_3", 4)],
		[Tile("CRA_2", 3), Tile("SOAP_", 4), Tile("DOT_2", 3), Tile("DOT_3", 4)],
		[Tile("DOT_2", 3), Tile("SOAP_", 4), Tile("BAM_2", 3), Tile("BAM_3", 4)],
		[Tile("DOT_2", 3), Tile("SOAP_", 4), Tile("CRA_2", 3), Tile("CRA_3", 4)],

		# 222 4444 666 8888 (any 1 or 2 suits)
		[Tile("BAM_2", 3), Tile("BAM_4", 4), Tile("BAM_6", 3), Tile("BAM_8", 4)],
		[Tile("CRA_2", 3), Tile("CRA_4", 4), Tile("CRA_6", 3), Tile("CRA_8", 4)],
		[Tile("DOT_2", 3), Tile("DOT_4", 4), Tile("DOT_6", 3), Tile("DOT_8", 4)],
		[Tile("BAM_2", 3), Tile("BAM_4", 4), Tile("CRA_6", 3), Tile("CRA_8", 4)],
		[Tile("BAM_2", 3), Tile("BAM_4", 4), Tile("DOT_6", 3), Tile("DOT_8", 4)],
		[Tile("CRA_2", 3), Tile("CRA_4", 4), Tile("BAM_6", 3), Tile("BAM_8", 4)],
		[Tile("CRA_2", 3), Tile("CRA_4", 4), Tile("DOT_6", 3), Tile("DOT_8", 4)],
		[Tile("DOT_2", 3), Tile("DOT_4", 4), Tile("BAM_6", 3), Tile("BAM_8", 4)],
		[Tile("DOT_2", 3), Tile("DOT_4", 4), Tile("CRA_6", 3), Tile("CRA_8", 4)],

		# 222 888 DDDD DDDD (any 3 suits, 2s and 8s only)
		[Tile("BAM_2", 3), Tile("BAM_8", 3), Tile("SOAP_", 4), Tile("RED__", 4)],
		[Tile("CRA_2", 3), Tile("CRA_8", 3), Tile("SOAP_", 4), Tile("GREEN", 4)],
		[Tile("DOT_2", 3), Tile("DOT_8", 3), Tile("GREEN", 4), Tile("RED__", 4)],

	]
	# 11111 NNNN 11111 (any 2 suits, any like nos, any wind)
	for i in range(0, 9):
		# +0 is DOT, +1 is BAM, +2 is CRA
		winning_hands.append([Tile(ID_TO_NAME[i * 3], 5),     Tile("RED__", 4), Tile(ID_TO_NAME[i * 3 + 1], 5)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3], 5),     Tile("GREEN", 4), Tile(ID_TO_NAME[i * 3 + 2], 5)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 1], 5), Tile("SOAP_", 4), Tile(ID_TO_NAME[i * 3 + 2], 5)])

	# FFFF 11111 22222 (any 2 suits, any 2 consec. nos.)
	for i in range(0, 8):
		winning_hands.append([Tile("FLOWR", 4), Tile(ID_TO_NAME[i * 3], 5),     Tile(ID_TO_NAME[(i+1) * 3 + 1], 5)])
		winning_hands.append([Tile("FLOWR", 4), Tile(ID_TO_NAME[i * 3], 5),     Tile(ID_TO_NAME[(i+1) * 3 + 2], 5)])
		winning_hands.append([Tile("FLOWR", 4), Tile(ID_TO_NAME[i * 3 + 1], 5), Tile(ID_TO_NAME[(i+1) * 3]    , 5)])
		winning_hands.append([Tile("FLOWR", 4), Tile(ID_TO_NAME[i * 3 + 1], 5), Tile(ID_TO_NAME[(i+1) * 3 + 2], 5)])
		winning_hands.append([Tile("FLOWR", 4), Tile(ID_TO_NAME[i * 3 + 2], 5), Tile(ID_TO_NAME[(i+1) * 3]    , 5)])
		winning_hands.append([Tile("FLOWR", 4), Tile(ID_TO_NAME[i * 3 + 2], 5), Tile(ID_TO_NAME[(i+1) * 3 + 1], 5)])

	# 111 2222 333 4444 (any run, 1 or 2 suits)
	for i in range(0, 6):
		winning_hands.append([Tile(ID_TO_NAME[i * 3    ], 3), Tile(ID_TO_NAME[(i+1) * 3    ], 4), Tile(ID_TO_NAME[(i+2) * 3    ], 3), Tile(ID_TO_NAME[(i+3) * 3    ], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 1], 3), Tile(ID_TO_NAME[(i+1) * 3 + 1], 4), Tile(ID_TO_NAME[(i+2) * 3 + 1], 3), Tile(ID_TO_NAME[(i+3) * 3 + 1], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 2], 3), Tile(ID_TO_NAME[(i+1) * 3 + 2], 4), Tile(ID_TO_NAME[(i+2) * 3 + 2], 3), Tile(ID_TO_NAME[(i+3) * 3 + 2], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3    ], 3), Tile(ID_TO_NAME[(i+1) * 3    ], 4), Tile(ID_TO_NAME[(i+2) * 3 + 1], 3), Tile(ID_TO_NAME[(i+3) * 3 + 1], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3    ], 3), Tile(ID_TO_NAME[(i+1) * 3    ], 4), Tile(ID_TO_NAME[(i+2) * 3 + 2], 3), Tile(ID_TO_NAME[(i+3) * 3 + 2], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 1], 3), Tile(ID_TO_NAME[(i+1) * 3 + 1], 4), Tile(ID_TO_NAME[(i+2) * 3    ], 3), Tile(ID_TO_NAME[(i+3) * 3    ], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 1], 3), Tile(ID_TO_NAME[(i+1) * 3 + 1], 4), Tile(ID_TO_NAME[(i+2) * 3 + 2], 3), Tile(ID_TO_NAME[(i+3) * 3 + 2], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 2], 3), Tile(ID_TO_NAME[(i+1) * 3 + 2], 4), Tile(ID_TO_NAME[(i+2) * 3 + 1], 3), Tile(ID_TO_NAME[(i+3) * 3 + 1], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 2], 3), Tile(ID_TO_NAME[(i+1) * 3 + 2], 4), Tile(ID_TO_NAME[(i+2) * 3    ], 3), Tile(ID_TO_NAME[(i+3) * 3    ], 4)])

	# 111 2222 111 2222 (any 2 suits, any any 2 consec nos)
	for i in range(0, 8):
		winning_hands.append([Tile(ID_TO_NAME[i * 3    ], 3), Tile(ID_TO_NAME[(i+1) * 3    ], 4), Tile(ID_TO_NAME[i * 3 + 1], 3), Tile(ID_TO_NAME[(i+1) * 3 + 1], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3    ], 3), Tile(ID_TO_NAME[(i+1) * 3    ], 4), Tile(ID_TO_NAME[i * 3 + 2], 3), Tile(ID_TO_NAME[(i+1) * 3 + 2], 4)])
		winning_hands.append([Tile(ID_TO_NAME[i * 3 + 1], 3), Tile(ID_TO_NAME[(i+1) * 3 + 1], 4), Tile(ID_TO_NAME[i * 3 + 2], 3), Tile(ID_TO_NAME[(i+1) * 3 + 2], 4)])

	return winning_hands

winning_hands = populate_winning_hands()
for hand in winning_hands:
	bag = BagOfTiles(hand)
	print(bag.simplified_str(delimiter=" "))