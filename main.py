import itertools
import copy
class game:
	def __init__(self):
		self.board =[[] for i in range(20)]
		self.camels = ["blue","yellow","orange","green","white"]
		self.modifiers = ["forward","backward"]
		self.forwardMods = []
		self.backwardMods = []
		self.remainingMoves = self.camels
		self.remainingMoves = ["orange","yellow"]
		#Test sequences
		self.insertCamels("blue",1,True)
		self.insertCamels("orange",5,True)
		self.insertCamels("yellow",5,False)
		self.insertCamels("white",5,True)
		self.insertCamels("green",5,True)
		###
		self.baseBoard = copy.deepcopy(self.board)
		
		####Stats:
		self.stats = [[] for i in range(len(self.camels))]
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
					camelStack = [self.board[s].pop(0) for j in range(i+1)]
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
		self.stats = [[] for i in range(len(self.camels))]
		colors = list(itertools.permutations(self.remainingMoves))
		l = len(self.remainingMoves)
		v = [1]*l+[2]*l+[3]*l
		numberRolls =list(set(list(itertools.permutations(v,l))))
		for c in colors:
			for nv in numberRolls:
				self.board = copy.deepcopy(self.baseBoard)#reset
				for i,j in zip(c,nv):
					self.moveCamel(i,j)
				rank = self.rankBoard()
				for i in range(len(rank)):
					print "#",i,self.stats[i],rank[i]
					self.stats[i].append(rank[i])		
		for cml in self.camels:
			print cml
			for st in self.stats:
				print float(st.count(cml))/len(st)
	def createProbablitySummary(self):
		pass
	def printBoard(self):
		print self.board
myGame = game()
myGame.getAllDiceRolls()
