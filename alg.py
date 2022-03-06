''' *********************************************************************** '''
''' Custom Conway's Game of Life                                            '''
''' Algorithms                                                              '''
''' *********************************************************************** '''

from .main2 import ROWS, COLUMNS, rules, cellStats, currentGeneration, Status
from random import randint

Class UpdateCurrentGeneration(currentGeneration, rules, cellStats):

	

	Class UpdateFunctions:
	
		# Using a list chosen by the shape, pattern, and position (even/odd)
		# of neighbors for cell (i,j) and a for loop to protect against
		# index out of range values. Using negative indexing on the min values
		def _countNeighbors(currentGeneration, i, j, rules):

			count = 0
			
			# Lists of the coefficients for neighbors to include by shape and pattern (i,j)

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
				else if rules.pattern == 2:
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
				else if rules.pattern == 3:
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
				else if rules.type == 2:
					neighborhood = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),
					    (-1,-2), (-1,-1), (-1,0), (-1,1), (-1,2), (0,-2), 
					    (0,-1), (0,1), (0,2), (1,-2), (1,-1), (1,0), (1,1), 
					    (1,2), (2,-2), (2,-1), (2,0), (2,1), (2,2)]
				
				# Knights move neighbors = 8
				else if rules.pattern == 3:
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
						if (i % 4 == 0 and j % 2 == 1) or 
						    (i % 4 == 2 and j % 2 == 0):
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
						if (i % 4 == 0 and j % 2 == 1) or 
						    (i % 4 == 2 and j % 2 == 0):
							more = [(0,-1)]
						# House pointing left
						else:
							more = [(0,1)]
						neighborhood += more

				# Double layer of neighbors = 22
				if rules.pattern == 2:
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
				if rules.pattern == 3:
					neighborhood =[(-3,0), (-2,1), (-2,1), (2,-1), (2,1),
					    (3,0)]
					# Even Row
					if i % 2 == 0: 
						neighborhood = [(-3,-1), (-1,-2), (-1,1), (0,-2), 
						    (0,2), (1,-2), (1,1), (3,-1)]
						# Pointing up (house)
						if (i % 4 == 0 and j % 2 == 1) or 
						    (i % 4 == 2 and j % 2 == 0):
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
					if (i % 4 == 1 and j % 2 == 0) or
					    (i % 4 == 3 and j % 2 == 1): 
					    more = [(0,1)] 
					# House pointing to left
					else: 
						more = [(0,-1)] neighborhood += more

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
				else if rules.type == 2:
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
				else if rules.pattern == 3:
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

			# Calculate status of neighbors
			for rows in neighborhood:
				
				h = i + row[0]
				# Wrap around to top if fall off of bottom of field
				if(h > ROWS):
					h -= ROWS

				w = j + row[1]
				# Wrap around to left edge if fall off of right one
				if(w > COLUMNS)
					w -= COLUMNS

				count+= currentGeneration[h][w]

			return count

		def updateGeneration(currentGeneration, rules, cellStats):

			# New array to hold status of next generation cells
			nextGen = Status()

			for y in range COLUMNS: x in range ROWS:
				neighbors = _countNeighbors(currentGeneration, x, y, rules)

				cellStatus[x][y].neighbors = neighbors

				life = 0

				# Test if cell stays alive
				if currentGeneration[x][y] == 1:
					if neighbors >= rules.min2live and neighbors <= rules.max2live:
						life = 1
						cellStats[x][y].living++
					else:
						cellStats[x][y].dead++
				# Test if cell spawns
				else:
					if neighbors >= rule.min2spawn and neighbors <= rule.max2spawn:
						life = 1
						cellStats[x][y].living++
					else:
						cellStats[x][y].dead++

				nextGen[x][y] = life
				cellStats[x][y].past.append(life)
				cellStats[x][y].generations++

		# Method to randomly generate initial cell population
		def generateRand(currentGeneration, height, width):
		
			corner_i = (ROWS - height) / 2
			corner_j = (COLUMNS - width) / 2
			
			for j in range width: i in range height:
				# 25% chance of cell starting as alive
				rand = randint(0,3)
				if rand == 1:
					currentGeneration[i][j] = 1
					
		# Method to draw currentGeneration for testing
		def drawGeneration(currentGeneration, ROWS, COLUMNS):
			
			for i in range ROWS: j in range COLUMNS:
				if currentGeneration[i][j] == 1:
					print("X")
				else:
					print("_")
					
	
	'''Class Universe

		def __init__(self):
			self.livingHistory = []           # list of "alive" lists for calculations
			self.alive = []                   # List of all cells alive n a given generation
			self.changedHistory = []          # list of "changed" lists for calculation
			self.changed = []                 # List of all cells that changed from the last generation
			self.genetations
			
			
	'''
			
			
		def livingCells(self):
			for i in range ROWS: j in range COLUMNS:
				if currentGeneration[i][j] == 1:
					thisCell = [i,j]
					cell.livingHistory += thisCell
					
		
					
			
			
			



