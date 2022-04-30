"""
Test Suite for the experimental grid.
"""
import experGrid
import experRule
import unittest

"""
test_toggle_on
Acceptance test for the cellToggle function

test_toggle_off
Acceptance test for the cellToggle function

test_new_grid_positive
Acceptance test for making a cell grid

test_new_grid_negative
Acceptance test for making a cell grid
"""
class TestSuite(unittest.TestCase):
    def test_toggle_on(self):
        offCell = experGrid.Cell(0, 0, 0)
        offCell.cellToggle()
        self.assertEqual(offCell.s, 1, "Should be 1")

    def test_toggle_off(self):
        onCell = experGrid.Cell(0, 0, 1)
        onCell.cellToggle()
        self.assertEqual(onCell.s, 0, "Should be 0")

    def test_new_grid_positive(self):
        tested = experGrid.CellGrid(4, 6)
        count = 0
        for y in range(tested.h):
            for x in range(tested.w):
                if(tested.grid[y][x].s == 0):
                    count += 1
        self.assertEqual(count, 24, "Should be 24 dead cells")

    def test_new_grid_negative(self):
        tested = experGrid.CellGrid(-4, -6)
        count = 0
        for y in range(tested.h):
            for x in range(tested.w):
                if(tested.grid[y][x].s == 0):
                    count += 1
        self.assertEqual(count, 0, "Should be 0 dead cells")

    """
    The following 4 tests provide total Path coverage of intValid2.

    def intValid2(dim):
        result = -1
        if type(dim) == int:
            result = dim
            if result < 0 or result >= 100:
                return -1
        return result

    test_int_char
    Also an acceptance test for intValid2

    test_int_low
    Also an acceptance test for intValid2

    test_int_high
    Also an acceptance test for intValid2

    test_int_valid
    Also an acceptance test for intValid2

    test_int_zero
    Acceptance test for intValid2 for equivalence partition

    test_int_hundred
    Acceptance test for intValid2 for equivalence partition
    """
    def test_int_char(self):
        result = experGrid.intValid2('a')
        self.assertEqual(result, -1, "Should be -1")

    def test_int_low(self):
        result = experGrid.intValid2(-2)
        self.assertEqual(result, -1, "Should be -1")

    def test_int_high(self):
        result = experGrid.intValid2(110)
        self.assertEqual(result, -1, "Should be -1")

    def test_int_valid(self):
        result = experGrid.intValid2(40)
        self.assertEqual(result, 40, "Should be 40")

    def test_int_zero(self):
        result = experGrid.intValid2(0)
        self.assertEqual(result, 0, "Should be 0")

    def test_int_hundred(self):
        result = experGrid.intValid2(100)
        self.assertEqual(result, -1, "Should be -1")

    """
    Acceptance test for updateGrid
    Integration test between experGrid.py and experRule.py
    This test was performed in a big-bang approach
    """
    def test_update_with_rule(self):
        testRule = experRule.Rule(1, 3, 2)
        testGrid = experGrid.CellGrid(5, 5)
        testGrid.grid[2][1].s = 1
        testGrid.grid[2][2].s = 1
        testGrid.grid[2][3].s = 1
        testGrid.updateGrid(testRule)

        correct = False
        liveCount = 0
        for y in range(testGrid.h):
            for x in range(testGrid.w):
                if (testGrid.grid[y][x].s == 1):
                    liveCount += 1

        if(testGrid.grid[1][2].s == 1 and testGrid.grid[2][2].s == 1 \
        and testGrid.grid[3][2].s == 1 and liveCount == 3):
            correct = True

        self.assertEqual(correct, True, "Should be True")

    """
    Acceptance test for updateGrid
    Integration test between experGrid.py and experRule.py
    This test was performed in a big-bang approach
    """
    def test_update_with_rule_edge(self):
        testRule = experRule.Rule(1, 3, 2)
        testGrid = experGrid.CellGrid(5, 5)
        testGrid.grid[0][1].s = 1
        testGrid.grid[0][2].s = 1
        testGrid.grid[0][3].s = 1
        testGrid.updateGrid(testRule)

        correct = False
        liveCount = 0
        for y in range(testGrid.h):
            for x in range(testGrid.w):
                if (testGrid.grid[y][x].s == 1):
                    liveCount += 1

        if(testGrid.grid[0][2].s == 1 and testGrid.grid[1][2].s == 1 \
        and liveCount == 2):
            correct = True

        self.assertEqual(correct, True, "Should be True")

if __name__ == '__main__':
    unittest.main()
