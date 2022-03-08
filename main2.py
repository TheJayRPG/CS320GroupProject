from alg_game_of_life import *

''' global variables/ Macros '''
''' defined for simplicity in changing attributes used throughout program '''
ROWS = 20
COLUMNS = 20

''' Class holding rules for current game '''
''' Populated by API, used by all '''
''' Default rules for "square cells" set initially '''
class GameRules:
    
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
				
rules = GameRules(ROWS, COLUMNS)
		
''' Class holding cell statistics '''
''' Populated by Algorithms, used by ThoughtProcess and to print '''
''' Held in 2D array cellStats[row][column] '''
class Cell:
	# Define singleton
	neighbors = 0
	past = []          # list to hold last 30 cell states
	generations = 0
	living = 0
	dead = 0
				
cellStats = [[ Cell() for j in range(COLUMNS)] for _ in range(ROWS)]
		
''' Class to hold 2D array of currentGeneration '''
''' Initially populated by API when program in "stop state" '''
''' While running Algorithm creates nextGeneration cell state
    then updates currentGeneration with new data '''
class Status():
	# Set all cells to dead by default
	status = 0

# Two instances of class to avoid use before definition issue
currentGeneration = [[ Status() for j in range(COLUMNS)] for _ in range(ROWS)]
newGen = [[ Status() for j in range(COLUMNS)] for _ in range(ROWS)]

def main():

	'''from alg_game_of_life import generate_rand, update_generation, draw_generation'''
	
	flag = 0                        # Flag to track if first time through function
	UpdateFunction.generate_rand(update, currentGeneration, floor(ROWS/2), floor(COLUMNS/2))
	UpdateFunction.draw_generation(update, currentGeneration, ROWS, COLUMNS)
	
	user_action = ''
	
	while user_action != 'q':
		user_action = input("Press enter to add generation or q to quit:")
	
		if user_action == '':

			if flag == 0:
				newGen = update.update_generation(currentGeneration, rules, cellStats)
			else:
				newGen = UpdateFunction.update_generation(update, newGen, rules, cellStats)
	
			UpdateFunction.draw_generation(update, newGen, ROWS, COLUMNS)
			flag = 1

if __name__ == '__main__':
	main()
	
