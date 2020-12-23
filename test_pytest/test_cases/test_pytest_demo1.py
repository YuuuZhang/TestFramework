import pytest
import unittest
import pytest_html
from my_pkg.app import app

class test_demo1(unittest.TestCase):

    @pytest.mark.cat_a
    def test_1(self):
        self.assertEqual(1, 2)

    def test_2(self):
        self.assertEqual(2, 2)

    def test_3(self):
        self.assertEqual(3, 3)
    
if __name__ == "__main__":
    
    app.print_sth()

    # Run tests in category 'cat_a'
    # generate a report in root path.
    # plugin objects to be auto-registered during initialization.
    cmd_list = ['-v', '-m', 'cat_a', '--html=report.html']
    pytest.main(cmd_list)