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
		self.remainingMoves = ["orange","yellow","blue","green","white"]
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
					self.stats[i].append(rank[i])		
		for cml in self.camels:
			print cml
			for st in self.stats:
				print float(st.count(cml))/len(st)
	def printBoard(self):
		print "forward modifiers",self.forwardMods
		print "backwards modifiers",self.backwardMods
		print self.baseBoard
	def copyBaseBoard(self):
		self.baseBoard = copy.deepcopy(self.board)
	def clearBoard(self):
		self.baseBoard = [[] for i in range(20)]
		self.board = [[] for i in range(20)]
		self.forwardMods = []
		self.backwardMods = []
myGame = game()
while(1):
	x = raw_input(">>>:").split()
	for i in range(len(x)):
		if x[i] == "o": x[i] = "orange"
		if x[i] == "g": x[i] = "green"
		if x[i] == "b": x[i] = "blue"
		if x[i] == "w": x[i] = "white"
		if x[i] == "y": x[i] = "yellow"
	if x[0] == "board" and len(x)==11:
		myGame.clearBoard()
		for c,s in zip(x[1::2],x[2::2]):
			if not c in myGame.camels:
				print "fuck you"
				break
			myGame.insertCamels(c,int(s),True)
		myGame.copyBaseBoard()
		myGame.printBoard()
	if x[0] == "run":
		myGame.getAllDiceRolls()	
	if x[0] == "remaining":
		for c in x[1::]:
			if not c in myGame.camels:
				print "fuck you"
				break
		myGame.remainingMoves = x[1::]		
		print myGame.remainingMoves
	if x[0] == "print":
		myGame.printBoard()
	if x[0] == "forward":
		myGame.forwardMods = [int(i) for i in x[1::]]
	if x[0] == "back":
		myGame.backwardMods = [int(i) for i in x[1::]]
	

#set board
#update remaining Moves
