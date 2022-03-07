from math import floor
from random import randint

''' global variables/ Macros '''
''' defined for simplicity in changing attributes used throughout program '''
ROWS = 5
COLUMNS = 5

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
	#def __init__(self, neighbors, past, generations, living, dea):
	neighbors = 0
	past = []          # list to hold last 30 cell states
	generations = 0
	living = 0
	dead = 0
				
cellStats = [ [Cell()] * COLUMNS for _ in range(ROWS)]
		
''' Class to hold 2D array of currentGeneration '''
''' Initially populated by API when program in "stop state" '''
''' While running Algorithm creates nextGeneration cell state
    then updates currentGeneration with new data '''
class Status():
	#def __init__(self, i, j):
	#i = ROWS
	#j = COLUMNS
	status = 0
	
# All cells initially dead
currentGeneration = [ [Status()] * COLUMNS for _ in range(ROWS)]

# Return nextGen of cells and update cellStats array with info abour the
# new generation
class UpdateFunction():

	def __init__(self):
	
	update = UpdateFunction()
	
	# Get list of a cells neighbors (coefficients of (i,j)) by rule being
	#followed
	def _get_neighbor_type(self, rules):

		# Triangle Shape
		if rules.shape == 3:
			
			# Immediate neighbors (1 layer) = 12
			if rules.pattern == 1:
				neighborhood = [(0,-2), (0,-1), (0,1), (0,2), (-1,-1),
				    (-1,0), (-1,1), (1,-1), (1,0), (1,1)]
				# Downward/Even Triangle
				if i + j % 2 == 0:
					more = [(-1,-2), (-1,2)]
				# Upward/Odd Triangle
				else:
					more = [(1,-2), (1,2)]
				neighborhood += more
				
			# Double layer of neighbors = 36
			elif rules.pattern == 2:
				neighborhood = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),
				    (-1,-3), (-1,-2), (-1,-1), (-1,0), (-1,1), (-1,2),
				    (-1,3), (0,-4), (0,-3), (0,-2), (0,-1), (0,1), (0,2),
				    (0,3), (0,4), (1,-3), (1,-2), (1,-1), (1,0), (1,1),
				    (1,2), (1,3), (2,-2), (2,-1), (2,0), (2,1), (2,2)]
				# Downward/Even Triangle
				if i + j % 2 == 0:
					more = [(-2,-3), (-2, 3), (-1,-4), (-1,4)]
				# Upward/Odd Triangle
				else:
					more = [(2,-3), (2, 3), (1,-4), (1,4)]
				neighborhood += more
				
			# Knights move neighbors = 11
			elif rules.pattern == 3:
				neighborhood =[(-2,-1), (-2,1), (-1,-2), (-1,2), (0,-2),
				    (0,2), (1,-2), (1,2), (2,-1), (2,1)]
				# Downward/Even Triangle
				if i + j % 2 == 0:
					more = [(1,0)]
				# Upward/Odd Triangle
				else:
					more = [(-1,0)]
				neighborhood += more
				
			# Error
			else:
				print("Error: undefined pattern type.\n")
				return -1

		# Square Shape
		if rules.shape == 4:
			
			# Immediate neighbors (1 layer) = 8
			if rules.type == 1:
				neighborhood = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1),
				    (1,-1),  (1,0), (1,1)]
				
			# Double layer of neighbors = 24
			elif rules.type == 2:
				neighborhood = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),
				    (-1,-2), (-1,-1), (-1,0), (-1,1), (-1,2), (0,-2),
				    (0,-1), (0,1), (0,2), (1,-2), (1,-1), (1,0), (1,1),
				    (1,2), (2,-2), (2,-1), (2,0), (2,1), (2,2)]
				
			# Knights move neighbors = 8
			elif rules.pattern == 3:
				neighbors = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2),
				    (1,2), (2,-1), (2+1)]
				
			# Error
			else:
				print("Error: undefined pattern type.\n")
				return -1

		# Pentagon Shape
		if rules.shape == 5:
				
			# Immediate neighbors (1 layer) = 7
			if rules.pattern == 1:
				# Even Row
				if i % 2 == 0:
					neighborhood = [(-1,-1), (-1,0), (0,-1), (0,1), (1,-1), (1,0)]
					# Pointing up (house)
					if (i % 4 == 0 and j % 2 == 1) or (i % 4 == 2 and j % 2 == 0):
						more = [(2,0)]
					# Upside down (house)
					else:
						more = [(-2,0)]
					neighborhood += more
				# Odd Row
				if i % 2 == 0:
					neighborhood = [(-2,-0), (-1,0), (-1,1), (1,0), (1,1),
					    (2,0)]
					# House pointing right
					if (i % 4 == 0 and j % 2 == 1) or (i % 4 == 2 and j % 2 == 0):
						more = [(0,-1)]
					# House pointing left
					else:
						more = [(0,1)]
					neighborhood += more

			# Double layer of neighbors = 22
			elif rules.pattern == 2:
				neighborhood = [(-3,0), (-2,-1), (-2,0), (-2,1), (-1,-1),
				    (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1),
				    (2,-1), (2,0), (2,1), (3,0)]
				# Even Row
				if i + j % 2 == 0:
					more = [(-3,-1), (-1, -2), (0,-2), (0,2), (1,-2),
					    (3,-1)]
				# Odd Row
				else:
					more = [(-4,0), (-3, 1), (-1,2), (1,2), (3,1), (4,0)]
				neighborhood += more

			# Knights move (sort of) of neighbors = 15
			elif rules.pattern == 3:
				neighborhood =[(-3,0), (-2,1), (-2,1), (2,-1), (2,1),
				    (3,0)]
				# Even Row
				if i % 2 == 0:
					neighborhood = [(-3,-1), (-1,-2), (-1,1), (0,-2),
					    (0,2), (1,-2), (1,1), (3,-1)]
					# Pointing up (house)
					if (i % 4 == 0 and j % 2 == 1) or (i % 4 == 2 and j % 2 == 0):
						more = [(-2,0)]
					# Upside down (house)
					else:
						more = [(2,0)]
					neighborhood += more
				# Odd Row
				if i % 2 == 0:
					neighborhood = [(-4,0), (-3,1), (-1,-1), (-1,2),
					    (1,-1), (1,2), (3,1), (4,0)]
				# House pointing to right
				if (i % 4 == 1 and j % 2 == 0) or (i % 4 == 3 and j % 2 == 1):
				    more = [(0,1)]
				# House pointing to left
				else:
					more = [(0,-1)]
				neighborhood += more
			
			# Error
			else:
				print("Error: undefined pattern type.\n")
				return -1
				
		# Hexagon Shape
		if rules.shape == 6:
				
			# Immediate neighbors (1 layer) = 6
			if rules.type == 1:
				neighborhood = [(0,-1), (0,1)]
				#Even Hexagon
				if (i + j) %2 == 0:
					more = [(-1,-1), (-1,0), (-1,1), (1,0)]
				# Odd Hexagon
				else:
					more = [(-1,0), (1,-1), (1,0), (1,1)]
				neighborhood += more
				
			# Double layer of neighbors = 18
			elif rules.type == 2:
				neighborhood = [(-1,-2), (-1,-1), (-1,0), (-1,1), (-1,2),
				    (0,-2), (0,-1), (0,1), (0,2), (1,-2), (1,-1), (1,0),
				    (1,1), (1,2)]
				#Even Hexagon
				if (i + j) %2 == 0:
					more = [(-2,-1), (-2,0), (-2,1), (2,0)]
				# Odd Hexagon
				else:
					more = [(-2,0), (2,-1), (2,0), (2,1)]
				neighborhood += more
				
			# Knights move neighbors = 18
			elif rules.pattern == 3:
				neighbors = [(-2,-2), (-2,-1), (-2,1), (-2,2),(0,-3),
				    (0,-2), (0,2), (0,3), (2,-2), (2,-1), (2,1), (2,2)]
				#Even Hexagon
				if (i + j) %2 == 0:
					more = [(-3,-1), (3,1), (-1,-3), (-1,3), (1,-1), (1,1)]
				# Odd Hexagon
				else:
					more = [(-2,-1), (-1,1), (1,-3), (1,3), (3,-1), (3,1)]
				neighborhood += more
			
			# Error
			else:
				print("Error: undefined pattern type.\n")
				return -1
					
		return neighborhood
					
	def _count_neighbors(self, currentGeneration, i, j, rules):

		count = 0
		neighborhood = self._get_neighbor_type(self, rules)

		# Calculate status of neighbors
		for rows in neighborhood:
				
			h = i + row[0]
			# Wrap around to top if fall off of bottom of field
			if(h > ROWS):
				h -= ROWS

			w = j + row[1]
			# Wrap around to left edge if fall off of right one
			if(w > COLUMNS):
				w -= COLUMNS

			count+= currentGeneration[h][w].status

		return count

	# Use rules to determine if each cell in currentGeneration has enough
	# neighbors to live. Create and return new array for nextGen
	def update_generation(currentGeneration, rules, cellStats):

		# New array to hold status of next generation cells
		nextGen = [ [Status()] * COLUMNS for _ in range(ROWS)]

		for y in range(COLUMNS):
			for x in range(ROWS):
				neighbors = self._count_neighbors(self, currentGeneration, x, y, rules)

				cellStatus[x][y].neighbors = neighbors

				life = 0

				# Test if cell stays alive
				if currentGeneration[x][y].status == 1:
					if neighbors >= rules.min2live and neighbors <= rules.max2live:
						life = 1
						cellStats[x][y].living += 1
					else:
						cellStats[x][y].dead += 1
				# Test if cell spawns
				else:
					if neighbors >= rule.min2spawn and neighbors <= rule.max2spawn:
						life = 1
						cellStats[x][y].living += 1
					else:
						cellStats[x][y].dead += 1

				nextGen[x][y].status = life
				cellStats[x][y].past.append(life)
				cellStats[x][y].generations += 1

	# Method to randomly generate initial cell population
	def generate_rand(currentGeneration, height, width):
		
		corner_i = floor((ROWS - height) / 2)
		corner_j = floor((COLUMNS - width) / 2)
			
		for j in range(width):
			for i in range(height):
				# 25% chance of cell starting as alive
				rand_num = randint(0,3)
				if rand_num == 1:
					currentGeneration[i][j].status = 1
					
	# Method to draw currentGeneration for testing
	def draw_generation(currentGeneration, ROWS, COLUMNS):
			
		for i in range(ROWS):
			for j in range(COLUMNS):
				if currentGeneration[i][j].status == 1:
					print("X")
				else:
					print("_")
				
	def test_method():
		print("Test works")
					
def main():

	'''from alg_game_of_life import generate_rand, update_generation, draw_generation'''

	#rules = GameRules()
	game = UpdateFunction.generate_rand(currentGeneration, floor(ROWS/2), floor(COLUMNS/2))
	UpdateFunction.draw_generation(currentGeneration, ROWS, COLUMNS)
	
	user_action = ''
	
	while user_action != 'q':
		user_action = input("Press enter to add generation or q to quit:")
	
		if user_action == '':
			UpdateFunction.update_generation(currentGeneration, rules, cellStats)
			UpdateFunction.draw_generation(currentGeneration, ROWS, COLUMNS)
			
main()
	

