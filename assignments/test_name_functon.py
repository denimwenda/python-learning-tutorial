#Unit Test and Test Cases
#Unit test verifies that a specific function's behavior is correct.
#Test case is a collection of unit test that together prove that a function behaves as it is supposed
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')

unittest.main()