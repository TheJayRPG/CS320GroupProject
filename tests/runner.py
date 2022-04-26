''' *********************************************************************** '''
''' Program to automate running tests                                       '''
''' Code from https://www.internalpointers.com/post/                        '''
'''           run-painless-test-suites-python-unittest                      '''
''' *********************************************************************** '''

import unittest

# import test modules
import tests.alg_tests

# initialize test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to test suite
suite.addTests(loader.loadTestsFromModule(tests.alg_tests))

# initialize runner, pass it the test suite, and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
