import itertools
class game:
	def __init__(self):
		self.board =[[] for i in range(10)]
		self.camels = ["blue","yellow","orange","green","white"]
		self.modifiers = ["forward","backward"]
		self.forwardMods = [5]
		self.backwardMods = [3]
		self.remainingMoves = self.camels
		#Test sequences
		self.insertCamels("blue",1,True)
		self.insertCamels("orange",1,True)
		self.insertCamels("yellow",1,False)
		self.insertCamels("white",2,True)
		self.insertCamels("green",4,True)
		print self.board
		self.moveCamel("blue",2)
	def insertCamels(self,camels,position,top):
		if type(camels) == type("a"):#string
			camels = [camels]
		if top: #general case
			self.board[position] = camels +self.board[position]
		else:   #if moving back from modifier
			self.board[position] = self.board[position]+camels
	def moveCamel(self,camel,nSpaces):
		#find camel
		for s in range(len(self.board)):
			for i in range(len(self.board[s])):
				if camel == self.board[s][i]:
					camelStack = [self.board[i].pop(0) for j in range(i+1)]
					currentPosition = s
					break
		if (currentPosition+nSpaces) in self.forwardMods:
			self.insertCamels(camelStack,currentPosition+nSpaces+1,True)
		elif (currentPosition+nSpaces) in self.backwardMods:
			self.insertCamels(camelStack,currentPosition+nSpaces-1,False)
		else:
			self.insertCamels(camelStack,currentPosition+nSpaces,True)
	def rankBoard(self):
		rank = []
		for space in self.board[::-1]:
			for cml in space:
				rank = rank+[cml]
		return rank
	def getAllDiceRolls(self):
		colors = list(itertools.permutations(self.remainingMoves))
		l = len(self.remainingMoves)
		v = [1]*l+[2]*l+[3]*l
		numberRolls =list(set(list(itertools.permutations(v,l))))
		print colors[0]
		print numberRolls[0]
				
		#[color,space(1-3)]
		
	def createProbablitySummary(self):
		pass
	def printBoard(self):
		print self.board
myGame = game()
myGame.printBoard()
myGame.rankBoard()
myGame.getAllDiceRolls()
