import pytest
import unittest

class test_demo2(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, 2)
    
    @pytest.mark.cat_a
    def test_2(self):
        self.assertEqual(2, 2)
