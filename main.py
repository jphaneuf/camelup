#inputs
#camel positions
#number of spaces
#camels that have already rolled
#space modifiers

#yellow,white,green,orange,blue

#inbetween
#rank camels
#evaluate every possible dice outcome

#moving rules
#move all camels on top


#outputs
#probability table for each camel

class game:
	def __init__(self):
		self.board =[[] for i in range(10)]
		self.camels = ["blue","yellow","orange","green","white"]
		self.modifiers = ["forward","backward"]
		#Test sequences
		self.insertCamels("blue",1,True)
		self.insertCamels("orange",1,True)
		self.insertCamels("yellow",1,False)
		print self.board
		self.moveCamel("blue",2)
	def insertCamels(self,camels,position,top):
		if top: #general case
			self.board[position].insert(0,camels)
		else:   #if moving back from modifier
			self.board[position].append(camels)
	def moveCamel(self,camel,nSpaces):
		#find camel
		for s in range(len(self.board)):
			for i in range(len(self.board[s])):
				if camel == self.board[s][i]:
					camelStack = [self.board[i].pop(0) for j in range(i+1)] 
					currentPosition = s
					break
		self.insertCamels(camelStack,currentPosition+nSpaces,True)
					 
		#move camel with camels on top
		#check modifier
	def getAllDiceRolls(self):
		pass
	def createProbablitySummary(self):
		pass
	def printBoard(self):
		print self.board
myGame = game()
myGame.printBoard()
