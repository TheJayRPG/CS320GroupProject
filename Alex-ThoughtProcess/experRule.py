"""
Rule

Class used to store data on a rule.
Range indicates how far a cell detects other cells around it during updates.
Most is the maximum number of nearby cells required for being alive.
Least is the minimum number of nearby cell required for being alive.
"""
class Rule():
    def __init__(self, range, most, least):
        self.r = range #1
        self.m = most #3
        self.l = least #2
