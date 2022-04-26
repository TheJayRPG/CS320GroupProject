''' *********************************************************************** '''
''' Custom Conway's Game of Life                                            '''
''' Algorithms                                                              '''
''' *********************************************************************** '''
import sys
sys.path.append("/Users/kristinehess/Desktop/CS_320/Project_code/CS320GroupProject")

from Conway.main import ROWS, COLUMNS, Status, Cell, Rules
from math import floor
from random import randint

# Class to manage Calculations about the cellular environment
class Cells_Environment(Status):
	# Singleton
	gen2stable = -1
	period = -1
	stable = -1
	living = []
	numLiving = 0
	changed = []
	numChanged = 0


	# Internal function to check if stability has been reached and if there is
	# a period of oscillation returns -1, -1 if not stable and generations to
	# reach stability and period if stable. A period of 1 is a still life
	def _check_if_stable(self, living, numLiving, changed, numChanged):
	
		# Stability has already been obtained and reported
		# return same values so no updates are made
		# This allows program to keep running to show stable pattern
		# but for main to terminate if it chooses
		if self.stable == 0:
			return self.gen2stable;
			
		# IF EMPTY RETURN (PREVENT INDEX OUT OF BOUNDS ERROR)
		if numLiving <= 0:
			return self.gen2stable;
	
		# Finds Still lifes - no changes between generations
		if changed[numChanged - 1] == "None":
			self.gen2stable = numChanged - 1
			self.stable = 0
			self.period = 1
			# print(f"Still life has been reached in {self.gen2stable} generations.")
			return self.gen2stable;
			
		matched = [0]
		last = numLiving - 1
		gen2check = min(41, numLiving)    # Check for period of up to 20
		                                  
		minVal = numLiving - gen2check - 1
		period = 1
		
		#print(f"minVal = {minVal}, gen2check = {gen2check}")
		#print(f"index {last} = {living[last]}")
		
		for i in range((last - 1), minVal, -1):
			x = all(elem in living[last] for elem in living[i])
			#print(f"index {i} matches? {x}")
			if x:
				matched[0] += 1
				matched.append(i)
			
		#print(f"last index = {last}, matches found at {matched}")
		
		if matched[0] >= 2:
			if last - matched[1] == matched[1] - matched[2]:
				period = last - matched[1]
				a = last                  # index of last matched element
				b = matched[1]            # index of previous occurrance
				#print(f" a = {a} b = {b}")
				
				# Checks for matches between already found matched elements
				for gen in range(1,period):
				
					#print(f"Living[a] cells = {living[a-gen]}")
					#print(f"Living[b] cells = {living[b-gen]}")
					y = all(elem in living[a - gen] for elem in living[b-gen])
					#print(f" a matches b = {y}")
					if not y:
						#print("Not Stable between matches.")
						return -1;
			else:
				# Not stable
				#print("Period not equal.")
				return -1
			
			# print(f"Period of oscillation = {period}")
			self.gen2stable = last - period
			self.stable = 0
			self.period = period
			
			#print(f"Gen2stable = {self.gen2stable}")
			#print(f"period = {self.period}")
			
			return self.gen2stable;
						
		return -1;


	# Function called from UpdateFunction. Used to update the cell's
	# environment object. Calls on _check_if_stable for stability and period
	# of oscillation and passes return value onto its caller. Return value
	# stability is a tuple containing the number of generations to reach
	# stability (-1 if not stable) and the period of oscillation (1 if still
	# life, -1 if not stable)
	def update_environment(self, currentGeneration, nextGen):
	
		alive = []
		delta = []
			
		for i in range(ROWS):
			for j in range(COLUMNS):
				
				#New list to hold temp variables
				temp = []
				temp.insert(0, '')
				temp.insert(1, '')
								
				past = currentGeneration[i][j].status
				new = nextGen[i][j].status
				
				# If cell is alive, add to alive list
				if new == 1:
					temp[0] = i
					temp[1] = j
					alive.append(temp)
						
				# If cell changed, add to delta list
				if past != new:
					temp[0] = i
					temp[1] = j
					delta.append(temp)
									
		if len(alive) != 0:
			self.living.append(alive)
			self.numLiving += 1
			
		if len(delta) != 0:
			self.changed.append(delta)
			self.numChanged += 1
		else:
			self.changed.append("None")
			self.numChanged += 1
		
		stability = world._check_if_stable(self.living, self.numLiving,
		    self.changed, self.numChanged)
		    
		return stability;
			

world = Cells_Environment()


# Return nextGen of cells and update cellStats array with info abour the
# new generation
class UpdateFunction(Status, Cell, Rules):
	def __init__(self, ROWS, COLUMNS):
		self.ROWS = ROWS
		self.COLUMNS = COLUMNS
		#self.new = [[ Status() for j in range(COLUMNS)] for _ in range(ROWS)]
		#self.returnVal = -1
		
	# Get list of a cells neighbors (coefficients of (i,j)) by rule being
	#followed
	def _get_neighbor_type(self, i, j, shape, pattern):

		# Triangle Shape
		if shape == 3:
			
			# Immediate neighbors (1 layer) = 12
			if pattern == 1:
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
			elif pattern == 2:
				neighborhood = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),
					(-1,-3), (-1,-2), (-1,-1), (-1,0), (-1,1), (-1,2), (-1,3),
					(0,-4), (0,-3), (0,-2), (0,-1), (0,1), (0,2), (0,3), (0,4),
					(1,-3), (1,-2), (1,-1), (1,0), (1,1), (1,2), (1,3), (2,-2),
					(2,-1), (2,0), (2,1), (2,2)]
				# Downward/Even Triangle
				if i + j % 2 == 0:
					more = [(-2,-3), (-2, 3), (-1,-4), (-1,4)]
				# Upward/Odd Triangle
				else:
					more = [(2,-3), (2, 3), (1,-4), (1,4)]
				neighborhood += more
				
			# Knights move neighbors = 11
			elif pattern == 3:
				neighborhood =[(-2,-1), (-2,1), (-1,-2), (-1,2), (0,-2), (0,2),
					(1,-2), (1,2), (2,-1), (2,1)]
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
		if shape == 4:
			
			# Immediate neighbors (1 layer) = 8
			if pattern == 1:
				neighborhood = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1),
					(1,0), (1,1)]
				
			# Double layer of neighbors = 24
			elif pattern == 2:
				neighborhood = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),
					(-1,-2), (-1,-1), (-1,0), (-1,1), (-1,2), (0,-2), (0,-1),
					(0,1), (0,2), (1,-2), (1,-1), (1,0), (1,1), (1,2), (2,-2),
					(2,-1), (2,0), (2,1), (2,2)]
				
			# Knights move neighbors = 8
			elif pattern == 3:
				print("Square Knights move")
				neighborhood = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2),
					(1,2), (2,-1), (2,1)]
				
			# Error
			else:
				print("Error: undefined pattern type.\n")
				return -1

		# Pentagon Shape
		if shape == 5:
				
			# Immediate neighbors (1 layer) = 7
			if pattern == 1:
				print("Pentagon 1 layer")
				# Even Row
				if i % 2 == 0:
					neighborhood = [(-1,-1), (-1,0), (0,-1), (0,1), (1,-1),
						(1,0)]
					# Pointing up (house)
					if ((i % 4 == 0 and j % 2 == 1) or
						(i % 4 == 2 and j % 2 == 0)):
						more = [(2,0)]
					# Upside down (house)
					else:
						more = [(-2,0)]
					neighborhood += more
				# Odd Row
				if i % 2 == 1:
					neighborhood = [(-2,-0), (-1,0), (-1,1), (1,0), (1,1),
					    (2,0)]
					# House pointing right
					if ((i % 4 == 0 and j % 2 == 1) or
						(i % 4 == 2 and j % 2 == 0)):
						more = [(0,-1)]
					# House pointing left
					else:
						more = [(0,1)]
					neighborhood += more

			# Double layer of neighbors = 22
			elif pattern == 2:
				print("Pentagon 2 layer")
				neighborhood = [(-3,0), (-2,-1), (-2,0), (-2,1), (-1,-1),
					(-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1),
					(2,-1), (2,0), (2,1), (3,0)]
				# Even Row
				if i + j % 2 == 0:
					more = [(-3,-1), (-1, -2), (0,-2), (0,2), (1,-2), (3,-1)]
				# Odd Row
				else:
					more = [(-4,0), (-3, 1), (-1,2), (1,2), (3,1), (4,0)]
				neighborhood += more

			# Knights move (sort of) of neighbors = 15
			elif pattern == 3:
				print("pentagon - knights move")
				neighborhood =[(-3,0), (-2,1), (-2,1), (2,-1), (2,1), (3,0)]
				# Even Row
				if i % 2 == 0:
					neighborhood = [(-3,-1), (-1,-2), (-1,1), (0,-2), (0,2),
						(1,-2), (1,1), (3,-1)]
					# Pointing up (house)
					if ((i % 4 == 0 and j % 2 == 1) or
						(i % 4 == 2 and j % 2 == 0)):
						more = [(-2,0)]
					# Upside down (house)
					else:
						more = [(2,0)]
					neighborhood += more
				# Odd Row
				if i % 2 == 1:
					neighborhood = [(-4,0), (-3,1), (-1,-1), (-1,2), (1,-1),
						(1,2), (3,1), (4,0)]
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
		if shape == 6:
				
			# Immediate neighbors (1 layer) = 6
			if pattern == 1:
				neighborhood = [(0,-1), (0,1)]
				#Even Hexagon
				if (i + j) %2 == 0:
					more = [(-1,-1), (-1,0), (-1,1), (1,0)]
				# Odd Hexagon
				else:
					more = [(-1,0), (1,-1), (1,0), (1,1)]
				neighborhood += more
				
			# Double layer of neighbors = 18
			elif pattern == 2:
				neighborhood = [(-1,-2), (-1,-1), (-1,0), (-1,1), (-1,2),
					(0,-2), (0,-1), (0,1), (0,2), (1,-2), (1,-1), (1,0), (1,1),
					(1,2)]
				#Even Hexagon
				if (i + j) % 2 == 0:
					more = [(-2,-1), (-2,0), (-2,1), (2,0)]
				# Odd Hexagon
				else:
					more = [(-2,0), (2,-1), (2,0), (2,1)]
				neighborhood += more
				
			# Knights move neighbors = 18
			elif pattern == 3:
				neighborhood = [(-2,-2), (-2,-1), (-2,1), (-2,2),(0,-3),
					(0,-2), (0,2), (0,3), (2,-2), (2,-1), (2,1), (2,2)]
				#Even Hexagon
				if (i + j) % 2 == 0:
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
		neighborhood = self._get_neighbor_type(i, j, rules.shape,
			rules.pattern)

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
				neighbors = self._count_neighbors(currentGeneration, x, y,
					rules)

				cellStats[x][y].neighbors = neighbors

				life = 0

				# Test if cell stays alive
				if currentGeneration[x][y].status == 1:
					if (neighbors >= rules.min2live and
						neighbors <= rules.max2live):
						life = 1
						cellStats[x][y].living += 1
					else:
						cellStats[x][y].dead += 1
				# Test if cell spawns
				else:
					if (neighbors >= rules.min2spawn and
						neighbors <= rules.max2spawn):
						life = 1
						cellStats[x][y].living += 1
					else:
						cellStats[x][y].dead += 1

				nextGen[x][y].status = life
				cellStats[x][y].past.append(life)
				cellStats[x][y].generations += 1
				
		stable = Cells_Environment.update_environment(world, currentGeneration,
		    nextGen)
		    
		if stable > 0:
		    cellStats[0][0].stableAt = stable    # set flag- stability reached
		    #print(f"stable. period is {world.period}")
		    
		return nextGen;
	

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
			
	# Method to show the neighbors of a cell (visualization)
	def show_neighbors(self, row, column, shape, pattern):
	
		width = height = 16
		i = floor(width / 2)
		j = floor(height / 2)
		flag = 0
		
		# Call with row and column so that even/odd shapes can be tested
		neighborhood = self._get_neighbor_type(row, column, shape, pattern)
		
		pattern_type = ''
		if pattern == 1:
			pattern_type = "Single layer"
		elif pattern == 2:
			pattern_type = "Double layer"
		elif pattern == 3:
			pattern_type = "Knights-move"
		else:
			print("Error pattern {pattern} is not recognized.")
			return -1
		
		# Triangle
		if shape == 3:
		
			print("")
			print("Triangle: Columns should be squished horizontally")
			print("Pattern: " + pattern_type)
			print(neighborhood)
			print("")
			
			# Iterate through fields in our display
			for x in range(height):
				for y in range(width):
					#1st level of list comprehension
					for n in neighborhood:
						# Find list that matches cell coordinates
						# Shift so target cell prints at center of field
						if n[0] == x - i and n[1] == y - j:
						
							if (x + y) % 2 == 1:
								print("V", end = ' ')
							else:
								print("^", end = ' ')
							flag = 1
					
					# Print * for cell or error if cell is its own neighbor
					if x == i and y == j:
						if flag == 1:
							print("Error, cell can't be a neighbor of itself")
						else:
							print("*", end = ' ')
							flag = 1
					
					# Print blank if nothing printed
					if flag == 0:
						print("_", end = ' ')
					
					flag = 0
					
				print(" ")
		
		# Square
		if shape == 4:
		
			print("")
			print("Square")
			print(f"Pattern: {pattern_type}")
			print(neighborhood)
			print("")
		
			# Iterate through fields in our display
			for x in range(height):
				for y in range(width):
				
					#1st level of list comprehension
					for n in neighborhood:
						# Find list that matches cell coordinates
						# Shift so target cell prints at center of field
						if n[0] == x - i and n[1] == y - j:
							print("X", end = ' ')
							flag = 1
					
					# Print * for cell or error if cell is its own neighbor
					if x == i and y == j:
						if flag == 1:
							print("Error, cell can't be a neighbor of itself")
						else:
							print("*", end = ' ')
							flag = 1
					
					# Print blank if nothing printed
					if flag == 0:
						print("_", end = ' ')
					
					flag = 0
					
				print(" ")
				
		# Pentagon
		if shape == 5:
			
			print("")
			print("Pentagon")
			print(f"Pattern: {pattern_type}")
			print(neighborhood)
			print("")
						
			# Iterate through fields in our display
			for x in range(height):
				for y in range(width):
				
					#1st level of list comprehension
					for n in neighborhood:
						# Find list that matches cell coordinates
						# Shift so target cell prints at center of field
						if n[0] == x - i and n[1] == y - j:
						
							if x  % 2 == 0:
								if ((x % 4 == 0 and j % 2 == 1) or
									(x % 4 == 2 and j % 2 == 0)):
									print("/\\ ", end = ' ')
								else:
									print("\/ ", end = ' ')
							else:
								if((x % 4 == 1 and j % 2 == 0) or
									(x % 4 == 2 and j % 2 == 1)):
									print("> ", end = ' ')
								else:
									print("<  ", end = ' ')
							flag = 1
						
					#  Print * for cell or error if cell is its own neighbor
					if x == i and y == j:
						if flag == 1:
							print("Error, cell can't be a neighbor of itself")
						else:
							print("*", end = ' ')
							flag = 1
					
					#Print blank if nothing printed
					if flag == 0:
						print("_", end = ' ')
					
					flag = 0
					
				print(" ")
		
		# Hexagon (Columns should be vertically staggered)
		if shape == 6:
			
			print("")
			print("Hexagon: Columns should be vertically staggered")
			print(f"Pattern: {pattern_type}")
			print(neighborhood)
			print("")
			
			# Iterate through fields in our display
			for x in range(height):
				for y in range(width):
				
					#1st level of list comprehension
					for n in neighborhood:
						# Find list that matches cell coordinates
						# Shift so target cell prints at center of field
						if n[0] == x - i and n[1] == y - j:
							print("O", end = ' ')
							flag = 1
					
					# Print * for cell and error if cell is its own neighbor
					if x == i and y == j:
						if flag == 1:
							print("Error, cell can't be a neighbor of itself")
						else:
							print("*", end = ' ')
							flag = 1
						
					#If nothing printed, print blank
					if flag == 0:
						print("_", end = ' ')
					
					flag = 0
					
				print(" ")
				
update = UpdateFunction(ROWS, COLUMNS)

class SetInitialCells(Status):
	def __init__(self, ROWS, COLUMNS):
		self.ROWS = ROWS
		self.COLUMNS = COLUMNS
	
	''' Not working in test?? '''
	def blinker_period2(self, currentGeneration, ROWS, COLUMNS):
		x = floor((COLUMNS - 1) / 2)
		y = floor((ROWS - 2) / 2)
		
		currentGeneration[y][x].status = 1
		currentGeneration[y+1][x].status = 1
				
	def cross_period3(self, currentGeneration, ROWS, COLUMNS):
		x = floor((COLUMNS - 8) / 2)
		y = floor((ROWS - 8) / 2)
		
		for a in range(4):
			currentGeneration[y][x+2+a].status = 1
			currentGeneration[y+7][x+2+a].status = 1
			
		for b in range(3):
			currentGeneration[y+2][x+b].status = 1
			currentGeneration[y+2][x+b+5].status = 1
			currentGeneration[y+5][x+b].status = 1
			currentGeneration[y+5][x+b+5].status = 1
			
		currentGeneration[y+1][x+2].status = 1
		currentGeneration[y+1][x+5].status = 1
		currentGeneration[y+3][x].status = 1
		currentGeneration[y+3][x+7].status = 1
		currentGeneration[y+4][x].status = 1
		currentGeneration[y+4][x+7].status = 1
		currentGeneration[y+6][x+2].status = 1
		currentGeneration[y+6][x+5].status = 1
		
	def octagon_period5(self, currentGeneration, ROWS, COLUMNS):
		x = floor((COLUMNS - 8) / 2)
		y = floor((ROWS - 8) / 2)
		
		for a in range(8):
			currentGeneration[y+2][x+a].status = 1
			currentGeneration[y+5][x+a].status = 1
			currentGeneration[y+a][x+2].status = 1
			currentGeneration[y+a][x+5].status = 1
			
		currentGeneration[y+2][x+2].status = 0
		currentGeneration[y+2][x+5].status = 0
		currentGeneration[y+5][x+2].status = 0
		currentGeneration[y+5][x+5].status = 0
			
	def koks_galaxy_period8(self, currentGeneration, ROWS, COLUMNS):
		x = floor((COLUMNS - 9) / 2)
		y = floor((ROWS - 9) / 2)
		
		for a in range(6):
			currentGeneration[y][x+3+a].status = 1
			currentGeneration[y+1][x+3+a].status = 1
			currentGeneration[y+a][x].status = 1
			currentGeneration[y+a][x+1].status = 1
			currentGeneration[y+7][x+a].status = 1
			currentGeneration[y+8][x+a].status = 1
			currentGeneration[y+3+a][x+7].status = 1
			currentGeneration[y+3+a][x+8].status = 1
			
initial_cells = SetInitialCells(ROWS, COLUMNS)
