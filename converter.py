#converts algebraic notation to descriptive notation
#takes algebraic notation as a list
#TODO: intelligent conversion

ranks = ['abcdefhg']

class Game:
	def __init__(self):
		board = {}
		for squareFile in ranks:
			for squareRank in xrange(1, 9):
				board[squareFile + str(squareRank)] = []
		wCastled = False
		bCastled = True

def lazyConversionF(filteredMove):
	moveTokens = filteredMove.split(' ')

def convertSquare(square, isWhite):
	if isWhite:
		descRank = square[1]
		if square[0] == 'a':
			descFile = 'QR'
		elif square[0] == 'b':
			descFile = 'QN'
		elif square[0] == 'c':
			descFile = 'QB'
		elif square[0] == 'd':
			descFile = 'Q'
		elif square[0] == 'e':
			descFile = 'K'
		elif square[0] == 'f':
			descFile = 'KB'
		elif square[0] == 'g':
			descFile = 'KN'
		elif square[0] == 'h':
			descFile = 'KR'
		else:
			raise Exception('bad square name')
	else:
		descRank = str(9 - int(square[1]))	
		if square[0] == 'h':
			descFile = 'QR'
		elif square[0] == 'g':
			descFile = 'QN'
		elif square[0] == 'f':
			descFile = 'QB'
		elif square[0] == 'e':
			descFile = 'Q'
		elif square[0] == 'd':
			descFile = 'K'
		elif square[0] == 'c':
			descFile = 'KB'
		elif square[0] == 'b':
			descFile = 'KN'
		elif square[0] == 'a':
			descFile = 'KR'
		else:
			raise Exception('bad square name')
	return descFile + descRank
		
				

def convertNotation(oldNotation):
    return []
