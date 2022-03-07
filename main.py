''' ********************************************************* '''
''' Custom Conway's Game of Life                              '''
'''                                                           '''
''' Python version 3.9??                                      '''
''' Designed using State Pattern                              '''
''' ********************************************************* '''

''' global variables/ Macros '''
''' defined for simplicity in changing attributes used throughout program '''
ROWS = 700
COLUMNS = 1000

''' Class holding rules for current game '''
''' Populated by API, used by all '''
''' Default rules for "square cells" set initially '''
class Rules:
	def __init__(self, ROWS, COLUMNS, shape = 4, pattern = 1, min2live = 2,
	    max2live = 3, min2spawn = 3, max2spawn = 3):
	    	# If no values given default values will be used
		self.rows = ROWS
		self.columns = COLUMNS
		self.shape = shape            # options are 3,4,5,6 sides
		self.pattern = pattern        # 1= single layer, 2= double, 3= knight's move
		self.min2live = min2live
		self.max2live = max2live
		self.min2spawn = min2spawn
		self.max2spawn = max2spawn
				
rules = Rules(ROWS, COLUMNS)
		
''' Class holding cell statistics '''
''' Populated by Algorithms, used by ThoughtProcess and to print '''
''' Held in 2D array cellStats[row][column] '''
class Cell:
	#def_init_(self):
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
	#def_init_(self, ROWS, COLUMNS):
		#self.i = ROWS
		#self.j = COLUMNS
	status = 0
		
# All cells initially dead
currentGeneration = [ [Status()] * COLUMNS for _ in range(ROWS)]

''' Structur to hold cell thoughts '''
class Thoughts:
	def_init_(self):
		self. =
		self. =
		
cellThoughts = [ [Thoughts()] * COLUMNS for _ in range(ROWS)]
		
''' Main loop for Game of Life '''
def main():
	while 1:
	
		''' Get rules and beginning currentGenerationm cell Status from API '''
		rules = Rules
		zoom = 0
		start = 0
		''' should be defined in API '''
		start = getAPIinfo(rules, currentGeneration)
	
		while start == 1:
	
			''' Get current zoom level from API for rendering '''
			zoom = getZoom()
		
			''' Update cell thought process '''
			if (err = updateThoughtProcess(rules, currentGeneration[i][j], cellStats[i][j], cellThoughts[i][j])) != 0:
				''' Handle error with thought process '''
				print("Error with thought process. Error code {err}\n")
	
			''' Render image '''
			if (err = renderImage(rules.shape, ROWS, COLUMNS, zoom, currentGeneration)) != 0:
				''' Handle error with image rendering '''
				print("Error with image rendering. Error code {err}\n")
			
			''' Update currentGeneration Status using Algorithms '''
			if (algorithmErr = updateStatus(rules, currentGeneration, cellStats)) != 0:
				''' Handle error with status update '''
				print("Error with updating cell status. Error code {algorithmErr}\n")
			
			start = getAPIinfo(rules, currentGeneration)
		
			''' if start == 2 pause until "game" is resumeed '''
			while start == 2:
				time.sleep(0.5)          # pause 500 miliseconds
	
		''' Exited program before stability was reached. Report error. '''
		''' Save current game status '''
		if algorithmErr == 1:
			print("Program exited prior to reaching stability\n")
			print("Saving curent program status.\n")
		
		if (err = saveProgram(rules, currentGeneration, cellStats, cellThoughts)) != 0:
			''' Handle error saving game status '''
			print("Error saving game. Error code {err}\n")
	
			
		
