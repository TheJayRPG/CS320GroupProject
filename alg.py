''' *********************************************************************** '''
''' Custom Conway's Game of Life                                            '''
''' Algorithms                                                              '''
''' *********************************************************************** '''

from .main import ROWS, COLUMNS, rules, cellStats, currentGeneration, Status

def updateStatus(currentGeneration, cellStats, rules):

	# New array to hold status of next generation cells
	nextGen = Status()

	for y in range COLUMNS: x in range ROWS:

			# Adjust row and column values to take advantage of negative
			# indexing to prevent range out of bounds error
			if x > ROWS - 3: i = x - ROWS else i = x

			if y > COLUMNS - 3: j = y - COLUMNS else j = y

			if rules.shape == 3: 
				neighbor = _triangle(currentGeneration, i, j, rules.pattern) 
			else if rules.shape == 4: 
				neighbor = _square(currentGeneration, i, j, rules.pattern) 
			else if rules.shape == 5: 
				neighbor = _pentagon(currentGeneration, i, j, rules.pattern)
			else if rules.shape == 6: 
				neighbor = _hexagon(currentGeneration, i, j, rules.pattern) 
			else: 
				print("Error, unrecognized shape.\n")

			# Determine if cells should remain alive or should regenerate based
			# on rules, copy into new array, and update cell statistics
			if currentGeneration[x][y] == 1 and neighbor >= rules.min2live 
			                                and neighbor <= rules.max2live: 
				nextGen[x][y] = 1 
				cellStats[x][y].living += 1 
			else if currentGeneration[x][y] == 0 and neighbor >= 
			                rules.min2spawn and neighbor <= rules.max2spawn:
				nextGen[x][y] = 1 
				cellStats[x][y].living += 1 
			else: 
				cellStats[x][y].dead += 1

			# Update cell statistics with new generation's info
			cellStats[x][y].neighbors = neighbor 
			cellStats[x][y].generations += 1 
			cellStats[x][y].past.append(nextGen[x][y])

	return nextGen

def _triangle(currentGeneration, i, j, rules.pattern):

	# Single layer of neighbors - total neighbors = 12
	if rules.pattern == 1: 
		count = sum(currentGeneration[i][j-2:j+3]) - currentGeneration[i][j]
		# Downward/Even Triangle
		if i + j % 2 == 0: 
			count += sum(currentGeneration[i-1][j-2:j+3]) + 
					 sum(currentGeneration[i+1][j-1:j+2]) 
		# Upward/Odd Triagle
		else: 
			count += sum(currentGeneration[i-1][j-1:j+2]) + 
					 sum(currentGeneration[i+1][j-2:

	# Double layer of neighbors - total neighbors = 36
	else if rules.pattern == 2: 
		count = sum(currentGeneration[i][j-4:j+5]) - currentGeneration[i][j]
	    # Downward/Even Triangle
		if i + j % 2 == 0: 
			count += sum(currentGeneration[i-2][j-3:j+4]) + 
			         sum(currentGeneration[i-1][j-4:j+5]) + 
			         sum(currentGeneration[i+1][j-3:j+4]) + 
			         sum(currentGeneration[i+2][j-2:j+3])
		# Upward/Odd Triagle
		else: 
			count += sum(currentGeneration[i-2][j-2:j+3]) +
					 sum(currentGeneration[i-1][j-3:j+4]) + 
					 sum(currentGeneration[i+1][j-4:j+5]) + 
					 sum(currentGeneration[i+2][j-3:j+4])

	# Knights move neighbors - total neighbors = 11
	else if rules.pattern == 3: 
		count = currentGeneration[i-2][j-1] + currentGeneration[i-2][j+1] + 
	            currentGeneration[i-1][j-2] + currentGeneration[i-1][j+2] + 
	            currentGeneration[i][j-2]   + currentGeneration[i][j+2]   + 
	            currentGeneration[i+1][j-2] + currentGeneration[i+1][j+2] + 
	            currentGeneration[i+2][j-1] + currentGeneration[i+2][j+1] 
		#Downward/Even Triangle
		if i + j % 2 == 0: 
			count += currentGeneration[i+1][j] 
		#Upward/Odd Triangle
		else: 
			count += currentGeneration[i-1][j]

	#Undefined pattern
	else: 
		print("Error: undefined pattern type.\n")
		count = -1

	return count

def _square(currentGeneration, i, j, rules.pattern):
	
	# Single layer of neighbors - total neighbors = 8
	if rules.pattern == 1: 
		count = sum(currentGeneration[i-1][j-1:j+2]) + 
				sum(currentGeneration[i][j-1:j+2])   + 
				sum(currentGeneration[i+1][j-1:j+2]) - 
				currentGeneration[i][j]

	# Double layer of neighbors - total neighbors = 24
	else if rules.pattern == 2: 
		count = sum(currentGeneration[i-2][j-2:j+3]) + 
		        sum(currentGeneration[i-1][j-2:j+3]) + 
		        sum(currentGeneration[i][j-2:j+3])   + 
	            sum(currentGeneration[i+1][j-2:j+3]) + 
	            sum(currentGeneration[i+2][j-2:j+3]) - 
	            currentGeneration[i][j]

	# Knights move neighbors - total neighbors = 8
	else if rules.pattern == 3: 
		count = currentGeneration[i-2][j-1] + currentGeneration[i-2][j+1] + 
		        currentGeneration[i-1][j-2] + currentGeneration[i-1][j+2] + 
		        currentGeneration[i+1][j-2] + currentGeneration[i+1][j+2] + 
		        currentGeneration[i+2][j-1] + currentGeneration[i+2][j+1] 

    #Undefined pattern
	else: 
		print("Error: undefined pattern type.\n")
		count = -1

	return count

def _pentagon(currentGeneration, i, j, rules.pattern):

	# Single layer of neighbors - total neighbors = 7
	if rules.pattern == 1:
		# Even Row
		if i % 2 == 0: 
			count = sum(currentGeneration[i-1][j-1:j+1]) + 
			        sum(currentGeneration[i][j-1:j+2])   + 
			        sum(currentGeneration[i+1][j-1:j+1]) - 
			        currentGeneration[i][j] 
			 if (i % 4 == 0 and j % 2 == 1) or (i % 4 == 2 and j % 2 == 0): 
			 	count += currentGeneration[i+2][j] 
			 else: 
			 	count += currentGeneration[i-2][j]
		# Odd Row
		else: 
			count = sum(currentGeneration[i-2:i+3][j]) + 
			        sum(currentGeneration[i-1:i+2][j+1]) - 
			        sum(currentGeneration[i][j:j+2]) 
			if (i % 4 ==1 and j % 2 == 0) or (i % 4 == 3 and j % 2 == 1): 
				count += currentGeneration[i][j-1] 
			else: 
				count += currentGeneration[i][j+1]

	# Double layer of neighbors - total neighbors = 36
	else if rules.pattern == 2: 
		# Even Row 
		if i % 2 == 0: 
			count = sum(currentGeneration[i-3][j-1:j+1]) + 
					sum(currentGeneration[i-2][j-1:j+2]) + 
					sum(currentGeneration[i-1][j-2:j+2]) + 
			        sum(currentGeneration[i][j-2:j+3])   + 
			        sum(currentGeneration[i+1][j-2:j+2]) + 
			        sum(currentGeneration[i+2][j-1:j+2]) + 
			        sum(currentGeneration[i+3][j-1:j+1]) - 
			        currentGeneration[i][j] 
		# Odd Row 
		else: 
			count = currentGeneration[i-4][j]            +
					sum(currentGeneration[i-3][j:j+2])   + 
					sum(currentGeneration[i-2][j-1:j+2]) + 
					sum(currentGeneration[i-1][j-1:j+3]) + 
			        sum(currentGeneration[i][j-1:j+2])   + 
			        sum(currentGeneration[i+1][j-1:j+3]) + 
			        sum(currentGeneration[i+2][j-1:j+2]) + 
			        sum(currentGeneration[i+3][j:j+2])   +
			        currentGeneration[i+4][j]            - 
			        currentGeneration[i][j] 
	

	# Knights move neighbors (sort of) - total neighbors = 15
	else if rules.pattern == 3:
		# Even Row 
		if i % 2 == 0: 
			count = sum(currentGeneration[i-3][j-1:j+1]) + 
					sum(currentGeneration[i-2][j-1:j+2]) + 
					currentGeneration[i-1][j-2] + currentGeneration[i-1][j+1] +
			        currentGeneration[i][j-2]   + currentGeneration[i][j+2]   + 
			        currentGeneration[i+1][j-2] + currentGeneration[i+1][j+1] +
			        sum(currentGeneration[i+2][j-1:j+2]) + 
			        sum(currentGeneration[i+3][j-1:j+1])
			if (i % 4 == 0 and j % 2 == 1) or (i % 4 == 2 and j % 2 == 0): 
			 	count = count - currentGeneration[i-2][j] 
			else: 
			 	count = count - currentGeneration[i+2][j]
		# Odd Row 
		else: 
			count = currentGeneration[i-4][j]            +
					sum(currentGeneration[i-3][j:j+2])   + 
					currentGeneration[i-2][j-1] + currentGeneration[i-2][j+1] + 
					currentGeneration[i-1][j-1] + currentGeneration[i-1][j+2] +
			        currentGeneration[i+1][j-1] + currentGeneration[i+1][j+2] +
			        currentGeneration[i+2][j-1] + currentGeneration[i+2][j+1] + 
			        sum(currentGeneration[i+3][j:j+2])   +
			        currentGeneration[i+4][j]            - 
			if (i % 4 ==1 and j % 2 == 0) or (i % 4 == 3 and j % 2 == 1): 
				count += currentGeneration[i][j+1] 
			else: 
				count += currentGeneration[i][j-1] 

	#Undefined pattern
	else: 
		print("Error: undefined pattern type.\n")
		count = -1
		
	return count

def _hexagon(currentGeneration, i, j, rules.pattern):

	# Single layer of neighbors - total neighbors = 6
	if rules.pattern == 1: 
		count = currentGeneration[i][j-1] + currentGeneration[i][j+1]
		# Even Hexagon
		if (i + j) % 2 == 0: 
			count += sum(currentGeneration[i-1][j-1:j+2]) + 
			         currentGeneration[i+1][j]
		# Odd Hexagon
		else: 
			count += sum(currentGeneration[i+1][j-1:j+2]) + 
			         currentGeneration[i-1][j]

	# Double layer of neighbors - total neighbors = 18
	else if rules.pattern == 2: 
		count = sum(currentGeneration[i-1][j-2:j+3]) + 
			    sum(currentGeneration[i][j-2:j+3])   + 
			    sum(currentGeneration[i+1][j-2:j+3]) -
			    currentGeneration[i][j] 
		# Even Hexagon
		if (i + j) % 2 == 0: 
			count += sum(currentGeneration[i-2][j-1:j+2]) + 
			         currentGeneration[i+2][j]
		# Odd Hexagon
		else: 
			count += sum(currentGeneration[i+2][j-1:j+2]) + 
			         currentGeneration[i-2][j]

	# Knights move neighbors - total neighbors = 18
	else if rules.pattern == 3: 
		count = sum(currentGeneration[i-2][j-2:j])   + 
				sum(currentGeneration[i-2][j+1:j+3]) + 
			    sum(currentGeneration[i][j-3:j+1])   + 
			    sum(currentGeneration[i][j+2:j+4])   + 
			    sum(currentGeneration[i+2][j-2:j])   + 
			    sum(currentGeneration[i+2][j+1:j+3]) + 
		# Even Hexagon
		if (i + j) % 2 == 0: 
			count += currentGeneration[i-3][j-1] + 
					 currentGeneration[i+3][j+1] + 
					 currentGeneration[i-1][j-3] + 
					 currentGeneration[i-1][j+3] + 
			         currentGeneration[i+1][j-1] + 
			         currentGeneration[i+1][j+1] 
		# Odd Hexagon
		else: 
			count += currentGeneration[i-2][j-1] + 
			         currentGeneration[i-1][j+1] + 
					 currentGeneration[i+1][j-3] + 
					 currentGeneration[i+1][j+3] + 
			         currentGeneration[i+3][j-1] + 
			         currentGeneration[i+3][j+1] 

	#Undefined pattern
	else: 
		print("Error: undefined pattern type.\n")
		count = -1

	return count



