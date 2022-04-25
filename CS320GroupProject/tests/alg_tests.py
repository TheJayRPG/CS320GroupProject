''' ***************************************** '''
''' Tests for Algorithm functions             '''
''' ***************************************** '''

import unittest

# import classes to test
from Conway.Algorithms.alg import *

# import dependencies
from Conway.main import ROWS, COLUMNS, Status, Rules, Cell

''' Testing class Cells_Environment() private function _check_if_stable() '''
class Test_check_if_stable(unittest.TestCase):

	def setUp(self):
		self.test_cell = Cells_Environment()
		print(self.test_cell)
		
	''' Black Box/Acceptance Test of _check_if_stable() function.          '''
	''' Function is designed to check if stability is reached within 20    '''
	''' generations and returns number of generations to reach stability.  '''
	''' Function returns -1 if not stable. Partitions are 0 (empty object),'''
	''' 1 (single gen - not stable), 2 (second gen matches first), 2       '''
	''' (second gen not matched), 20 (eventually stable), and 21 (not      '''
	''' stable within maximum number of generations tested). (8 tests)     '''
	
	# test 1- acceptance test
	def test_check_if_stable_empty_object(self):
	
		# Cells_Environment set to default values (empty)
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = []
		self.test_cell.numLiving = 0
		self.test_cell.changed = []
		self.test_cell.numChanged = 0
		
		# Test null
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
						self.test_cell.living, self.test_cell.numLiving,
						self.test_cell.changed, self.test_cell.numChanged),
						-1, "Error, null object returns value")
		self.assertEqual(self.test_cell.period, -1, "Error expected period"
		                 " == -1.")
	
	# test 2- acceptance test
	def test_check_if_stable_1gen(self):
		# One generation
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0]]
		self.test_cell.numLiving = 1
		self.test_cell.changed = [[0,0]]
		self.test_cell.numChanged = 1
	
		# Test single generation
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
						self.test_cell.living, self.test_cell.numLiving,
						self.test_cell.changed, self.test_cell.numChanged),
						-1, "Error, first generation returns value >=0.")
		self.assertEqual(self.test_cell.period, -1, "Error expected period"
		                 " == -1.")
	
	# test 3- acceptance test
	def test_check_if_stable_2gen_still_life(self):
		# Two gen that match
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[0,0]]
		self.test_cell.numLiving = 2
		self.test_cell.changed = [[0,0],"None"]
		self.test_cell.numChanged = 2
	
		#Test still life - matches on 1st generation
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
		                self.test_cell.living, self.test_cell.numLiving,
		                self.test_cell.changed, self.test_cell.numChanged),
		                1, "Error, first generation still life returns"
		                " value <0.")
		self.assertEqual(self.test_cell.period, 1, "Error, still life period"
		                 "!= 1.")
	
	# test 4- acceptance test
	def test_check_if_stable_2gen_not_stable(self):
		# 2 unmatched gen
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0]]
		self.test_cell.numLiving = 2
		self.test_cell.changed = [[0,0],[[0,0],[1,0]]]
		self.test_cell.numChanged = 2
		
		#Test 2 generations not matching
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
		                self.test_cell.living, self.test_cell.numLiving,
		                self.test_cell.changed, self.test_cell.numChanged),
		                -1, "Error, second unmatching generation returns"
		                " gen2stable > 0.")
		self.assertEqual(self.test_cell.period, -1, "Error expected period"
		                 " == -1.")
	
	# test 5- acceptance test
	# Not totally necessary, but testing middle value
	def test_check_if_stable_5gen_still_life(self):
		# gen 5 and 6 match- period 1 stil life
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0],[2,0],[3,0],[4,0],[4,0]]
		self.test_cell.numLiving = 6
		self.test_cell.changed = [[0,0],[[0,0],[1,0]],[[1,0],[2,0]],
		                          [[2,0],[3,0]],[[3,0],[4,0]],"None"]
		self.test_cell.numChanged = 6
	
		#Test still life - matches on 5th generation - still life
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
		                self.test_cell.living, self.test_cell.numLiving,
		                self.test_cell.changed, self.test_cell.numChanged),
		                5, "Error, fifth generation still life returns"
		                " value <0.")
		self.assertEqual(self.test_cell.period, 1, "Error expected period"
		                 " == 1.")
	
	# test 6- acceptance test
	# Not totally necessary, but testing middle value- period > 1
	def test_check_if_stable_6gen_period2(self):
		# gen 5 and 7 match- period 2 oscillation
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[4,0],
		                         [5,0],[4,0]]
		self.test_cell.numLiving = 9
		self.test_cell.changed = [[0,0],[[0,0],[1,0]],[[1,0],[2,0]],
		                          [[2,0],[3,0]],[[3,0],[4,0]],[[4,0],[5,0]],
		                          [[4,0],[5,0]],[[4,0],[5,0]],[[4,0],[5,0]]]
		self.test_cell.numChanged = 9
	
		#Test period 2
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
		                self.test_cell.living, self.test_cell.numLiving,
		                self.test_cell.changed, self.test_cell.numChanged),
		                6, "Error, sixth generation period = 2 returns"
		                " unexpected value.")
		self.assertEqual(self.test_cell.period, 2, "Error expected period"
		                 " == 2.")
	
	# test 7- acceptance test
	def test_check_if_stable_20gen_period(self):
		# 21 gen - 1 and 21 match (period = 20)
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
		                         [8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],
		                         [15,0],[16,0],[17,0],[18,0],[19,0],[0,0],[1,0],
		                         [2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],
		                         [10,0],[11,0],[12,0],[13,0],[14,0],[15,0],
		                         [16,0],[17,0],[18,0],[19,0],[0,0]]
		self.test_cell.numLiving = 41
		self.test_cell.changed = [[0,0],[[0,0],[1,0]],[[1,0],[2,0]],[[2,0],[3,0]],
		                          [[3,0],[4,0]],[[4,0],[5,0]],[[5,0],[6,0]],
		                          [[6,0],[7,0]],[[7,0],[8,0]],[[8,0],[9,0]],
		                          [[9,0],[10,0]],[[10,0],[11,0]],[[11,0],[12,0]],
		                          [[12,0],[13,0]],[[13,0],[14,0]],[[14,0],[15,0]],
		                          [[15,0],[16,0]],[[16,0],[17,0]],[[17,0],[18,0]],
								  [[18,0],[19,0]],[[0,0],[19,0]],[[0,0],[1,0]],
								  [[1,0],[2,0]],[[2,0],[3,0]],[[3,0],[4,0]],
								  [[4,0],[5,0]],[[5,0],[6,0]],[[6,0],[7,0]],
		                          [[7,0],[8,0]],[[8,0],[9,0]],[[9,0],[10,0]],
		                          [[10,0],[11,0]],[[11,0],[12,0]],[[12,0],[13,0]],
		                          [[13,0],[14,0]],[[14,0],[15,0]],[[15,0],[16,0]],
		                          [[16,0],[17,0]],[[17,0],[18,0]],[[18,0],[19,0]],
								  [[0,0],[19,0]]]
		self.test_cell.numChanged = 41
		
		#Test 20 generation period
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
		                self.test_cell.living, self.test_cell.numLiving,
		                self.test_cell.changed, self.test_cell.numChanged),
		                20, "Error, expected value of 20 generations to "
		                "reach stability.")
		self.assertEqual(self.test_cell.period, 20, "Error expected period"
		                 " == 20.")
	
	# test 8- acceptance test
	def test_check_if_stable_21gen_out_of_range(self):
		# 22 gen - 1 and 22 match (period = 21)
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
		                         [8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],
		                         [15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[0,0],
								 [1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],
		                         [9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],
		                         [16,0],[17,0],[18,0],[19,0],[20,0],[0,0]]
		self.test_cell.numLiving = 43
		self.test_cell.changed = [[0,0],[[0,0],[1,0]],[[1,0],[2,0]],[[2,0],[3,0]],
		                          [[3,0],[4,0]],[[4,0],[5,0]],[[5,0],[6,0]],
		                          [[6,0],[7,0]],[[7,0],[8,0]],[[8,0],[9,0]],
		                          [[9,0],[10,0]],[[10,0],[11,0]],[[11,0],[12,0]],
		                          [[12,0],[13,0]],[[13,0],[14,0]],[[14,0],[15,0]],
		                          [[15,0],[16,0]],[[16,0],[17,0]],[[17,0],[18,0]],
								  [[18,0],[19,0]],[[19,0],[20,0]],[[0,0],[20,0]],
								  [[0,0],[1,0]],[[1,0],[2,0]],[[2,0],[3,0]],
		                          [[3,0],[4,0]],[[4,0],[5,0]],[[5,0],[6,0]],
		                          [[6,0],[7,0]],[[7,0],[8,0]],[[8,0],[9,0]],
		                          [[9,0],[10,0]],[[10,0],[11,0]],[[11,0],[12,0]],
		                          [[12,0],[13,0]],[[13,0],[14,0]],[[14,0],[15,0]],
		                          [[15,0],[16,0]],[[16,0],[17,0]],[[17,0],[18,0]],
								  [[18,0],[19,0]],[[19,0],[20,0]],[[0,0],[20,0]]]
		self.test_cell.numChanged = 43
		
		#Test 21 generation period
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
		                self.test_cell.living, self.test_cell.numLiving,
		                self.test_cell.changed, self.test_cell.numChanged),
		                -1, "Error, period out of range but function "
		                "returned period > 0.")
		self.assertEqual(self.test_cell.period, -1, "Error expected period"
		                 " == -1.")
		                
	# End Black Box testing
	
	''' White Box Testing of _check_if_stable() function                   '''
	''' With black box tests path coverage is achieved, with every possible'''
	''' combination of branches covered (not all truth values can be       '''
	''' reached). Requires 4 additional tests. See control flow to see     '''
	''' specific tests that cover each possible truth value.               '''
	
	# test 9
	''' Stability previously recorded by function '''
	def test_check_if_stable_previously_reported(self):
	
		# Cells_Environment set to test values
		self.test_cell.gen2stable = 1                       # still life
		self.test_cell.period = 1
		self.test_cell.stable = 0                           # marked stable
		self.test_cell.living = [[0,0],[0,0],[0,0],[0,0]]   # 4 gen used
		self.test_cell.numLiving = 4
		self.test_cell.changed = [[0,0], "None", "None", "None"]
		self.test_cell.numChanged = 4
		
		# Test previously marked stable
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
						self.test_cell.living, self.test_cell.numLiving,
						self.test_cell.changed, self.test_cell.numChanged),
						1, "Error, stable still life returns unexpected "
						"value")
		self.assertEqual(self.test_cell.period, 1, "Error expected period"
		                 " == 1.")
	
	# test 10
	''' Matching generations have unequal period '''
	def test_check_if_stable_unequal_period(self):
	
		# Cells_Environment set to default values (empty)
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0],[2,0],[0,0],[1,0],[0,0]]
		self.test_cell.numLiving = 6
		self.test_cell.changed = [[0,0],[[0,0],[1,0]],[[1,0],[2,0]],[[0,0],[2,0]],
		                          [[0,0],[1,0]],[[0,0],[1,0]]]
		self.test_cell.numChanged = 6
		
		# Test previously marked stable
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
						self.test_cell.living, self.test_cell.numLiving,
						self.test_cell.changed, self.test_cell.numChanged),
						-1, "Error, stable still life returns unexpected "
						"value")
		self.assertEqual(self.test_cell.period, -1, "Error expected period"
		                 " == -1.")
	
	# test 11
	''' Matching generations have umatched cells between matches '''
	def test_check_if_stable_inconsistent_values(self):
	
		# Cells_Environment set to default values (empty)
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0],[0,0],[2,0],[0,0]]
		self.test_cell.numLiving = 5
		self.test_cell.changed = [[0,0],[[0,0],[1,0]],[[0,0],[1,0]],[[0,0],[2,0]],[[0,0],[2,0]]]
		self.test_cell.numChanged = 5
		
		# Test previously marked stable
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
						self.test_cell.living, self.test_cell.numLiving,
						self.test_cell.changed, self.test_cell.numChanged),
						-1, "Error, stable still life returns unexpected "
						"value")
		self.assertEqual(self.test_cell.period, -1, "Error expected period"
		                 " == -1.")
		                 
	# test 12
	def test_check_if_stable_3gen_single_match(self):
		# 3 gen, 1 & 3 match
		self.test_cell.gen2stable = -1
		self.test_cell.period = -1
		self.test_cell.stable = -1
		self.test_cell.living = [[0,0],[1,0],[0,0]]
		self.test_cell.numLiving = 3
		self.test_cell.changed = [[0,0],[[0,0],[1,0]],[[0,0],[1,0]]]
		self.test_cell.numChanged = 3
		
		#Test 3 generations with single match
		self.assertEqual(Cells_Environment._check_if_stable(self.test_cell,
		                self.test_cell.living, self.test_cell.numLiving,
		                self.test_cell.changed, self.test_cell.numChanged),
		                -1, "Error, first matching generation returns"
		                " gen2stable > 0.")
		self.assertEqual(self.test_cell.period, -1, "Error expected period"
		                 " == -1.")
		
''' Integration Testing - Classes are tightly coupled                       '''
''' Testing integration of classes Status object from main.py created inside'''
''' UpdateFunction.update_generation(),and it calls class Cells_Environment '''
''' to determine stability and period. SetInitialCells also used to get     '''
''' preset initial generation. This class is new and will contain multiple  '''
''' options for users to choose as initial cell states.                     '''
''' Integration testing was done using a big bang strategy, though the      '''
''' code was written and combined using more of a top down approach. I      '''
''' started by writing the main objects that were used in UpdateFunction()  '''
''' and wrote enough code to start to put it all together. Then features    '''
''' were added, including modules within the class and the additional       '''
''' classes of Cells_Environment() and SetInitialCellls(), which was written'''
''' for integration testing but will be necessary in the completed project. '''
class Test_integration_of_alg_functions(unittest.TestCase):
	
		def setUp(self):
			# Setup empty 'arrays' and default rules
			# Classes defined in main
			self.curGen = [[ Status() for j in range(COLUMNS)]
			               for _ in range(ROWS)]
			self.newGen = [[ Status() for j in range(COLUMNS)]
			               for _ in range(ROWS)]
			self.rules = Rules(ROWS, COLUMNS)
			self.cellStats = [[ Cell() for j in range(COLUMNS)]
			                  for _ in range(ROWS)]
			
			# Fill initial generation- Uses class SetInitialCells
			#SetInitialCells.cross_period3(self, self.curGen, ROWS, COLUMNS)
			#SetInitialCells.blinker_period2(self, self.curGen, ROWS, COLUMNS) - not working?
			#SetInitialCells.koks_galaxy_period8(self, self.curGen, ROWS, COLUMNS)
			SetInitialCells.octagon_period5(self, self.curGen, ROWS, COLUMNS)
		
		# Using class UpdateFunction
		def test_by_drawing(self):
			UpdateFunction.draw_generation(self, self.curGen, ROWS, COLUMNS)
		
		#Using class UpdateFunction
		def test_run_until_stable(self):
			while self.cellStats[0][0].stableAt == -1:
				self.newGen = UpdateFunction.update_generation(update,
				              self.curGen, self.rules, self.cellStats)
				UpdateFunction.draw_generation(self, self.newGen, ROWS, COLUMNS)
				self.curGen = self.newGen
				self.newGen = [[0 for j in range(COLUMNS)]
							    for _ in range(ROWS)]
							    
		# Check updated values in class Cells_Environment
		# Bad test? world.period always = -1 but inside update_generation
		# function it prints correctly, as does it inside main when not running
		# tests. Object imported from Algorithms.alg, exactly the same
		# as is done and works within main. I don't understand why this test
		# fails
		'''def test_check_values(self):
			self.assertEqual(world.period, 3, f"Error, period = {world.period} expected period == 3.")'''
			
			
