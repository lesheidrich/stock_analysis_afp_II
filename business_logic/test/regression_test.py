import unittest
import os

if __name__ == '__main__':
    test_dir = os.path.dirname(__file__)
    test_suite = unittest.TestLoader().discover(test_dir, pattern='*.py')

    unittest.TextTestRunner().run(test_suite)

