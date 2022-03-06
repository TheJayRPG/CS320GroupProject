''' global variables/ Macros '''
''' defined for simplicity in changing attributes used throughout program '''
ROWS = 20
COLUMNS = 20

''' Class holding rules for current game '''
''' Populated by API, used by all '''
''' Default rules for "square cells" set initially '''
class Rules():
	def __init__(self):
		self.shape = 4          # options are 3,4,5,6 sides
		self.pattern = 1        # 1= single layer, 2= double, 3= knight's move
		self.min2live = 2
		selfmax2live = 3
		self.min2spawn = 3
		self.max2spawn = 3
		self.rows = ROWS
		self.columns = COLUMNS
		
	#rules = Rules()
		
''' Class holding cell statistics '''
''' Populated by Algorithms, used by ThoughtProcess and to print '''
''' Held in 2D array cellStats[row][column] '''
class Cell:
	def __init__(self):
		self.neighbors = 0
		self.past = []          # list to hold last 30 cell states
		self.generations = 0
		self.living = 0
		self.dead = 0
		
	cellStats = [ [Cell()] * COLUMNS for _ in range(ROWS)]
		
''' Class to hold 2D array of currentGeneration '''
''' Initially populated by API when program in "stop state" '''
''' While running Algorithm creates nextGeneration cell state
    then updates currentGeneration with new data '''
class Status:
	def __init__(self, ROWS, COLUMNS):
		self.i = ROWS
		self.j = COLUMNS
		
		currentGeneration = [ [0] * COLUMNS for _ in range(ROWS)]  # All cells initially dead

def main():
	
	game = UpdateFunctions()
	rules = Rules()
	game.generateRand(currentGeneration, 10, 10)
	gamedrawGeneration(currentGeneration(ROWS, COLUMNS))
	
	user_action = ''
	
	while user_action != 'q':
		user_action = input("Press enter to add generation or q to quit:")
	
		if user_action == '':
			game.updateGeneration(currentGeneration, rules, cellStats)
			game.drawGeneration(currentGeneration(ROWS, COLUMNS))
				
	main()
	
