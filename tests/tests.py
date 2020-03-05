import unittest
from pyavtech import PyAvr


class TestAvrOpen(unittest.TestCase):
    def setUp(self):
        self.avr = PyAvr()


if __name__ == '__main__':
    unittest.main(exit=False)
