''' *********************************************************************** '''
''' Custom Conway's Game of Life                                            '''
''' Algorithms                                                              '''
''' *********************************************************************** '''

from main2 import ROWS, COLUMNS, Status, Cell, GameRules
from math import floor
from random import randint

# Return nextGen of cells and update cellStats array with info abour the
# new generation
class UpdateFunction(Status, Cell, GameRules):
	def __init__(self, ROWS, COLUMNS):
		self.ROWS = ROWS
		self.COLUMNS = COLUMNS
		
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
			if rules.pattern == 1:
				neighborhood = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1),
				    (1,-1),  (1,0), (1,1)]
				
			# Double layer of neighbors = 24
			elif rules.pattern == 2:
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
			if rules.pattern == 1:
				neighborhood = [(0,-1), (0,1)]
				#Even Hexagon
				if (i + j) %2 == 0:
					more = [(-1,-1), (-1,0), (-1,1), (1,0)]
				# Odd Hexagon
				else:
					more = [(-1,0), (1,-1), (1,0), (1,1)]
				neighborhood += more
				
			# Double layer of neighbors = 18
			elif rules.pattern == 2:
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
		neighborhood = self._get_neighbor_type(rules)

		# Calculate status of neighbors
		for x in neighborhood:
				
			h = i + x[0]
			# Wrap around to top if fall off of bottom of field
			if(h >= ROWS):
				h -= ROWS

			w = j + x[1]
			# Wrap around to left edge if fall off of right one
			if(w >= COLUMNS):
				w -= COLUMNS

			count+= currentGeneration[h][w].status

		return count

	# Use rules to determine if each cell in currentGeneration has enough
	# neighbors to live. Create and return new array for nextGen
	def update_generation(self, currentGeneration, rules, cellStats):

		# New array to hold status of next generation cells
		nextGen = [[ Status() for j in range(COLUMNS)] for _ in range(ROWS)]

		for x in range(ROWS):
			for y in range(COLUMNS):
				neighbors = self._count_neighbors(currentGeneration, x, y, rules)

				cellStats[x][y].neighbors = neighbors

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
					if neighbors >= rules.min2spawn and neighbors <= rules.max2spawn:
						life = 1
						cellStats[x][y].living += 1
					else:
						cellStats[x][y].dead += 1

				nextGen[x][y].status = life
				cellStats[x][y].past.append(life)
				cellStats[x][y].generations += 1
			
		return nextGen

	# Method to randomly generate initial cell population
	def generate_rand(self, currentGeneration, height, width):
		
		corner_i = floor((ROWS - height) / 2)
		corner_j = floor((COLUMNS - width) / 2)
			
		for j in range(width):
			for i in range(height):
				# 33% chance of cell starting as alive
				rand_num = randint(0,2)
				if rand_num == 1:
					currentGeneration[corner_i + i][corner_j + j].status = 1
					
	# Method to draw currentGeneration for testing
	def draw_generation(self, currentGeneration, ROWS, COLUMNS):
			
		for i in range(ROWS):
			for j in range(COLUMNS):
				if currentGeneration[i][j].status == 1:
					print("X", end = ' ')
				else:
					print("_", end = ' ')
			print("")
				
update = UpdateFunction(ROWS, COLUMNS)
					
	
