import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
from inventory_client import inventoryclient
import get_book_titles

class UnitTestMockServer(unittest.TestCase):
    
    def testsUnitTestMockServer(self):
        mock_client = inventoryclient()

        #Mocking the return value of the function call
        mock_client.getBookTitles = MagicMock(return_value = ["Divergent","Insurgent"])
        mock_client.getBookTitles(["abcd-1000", "abcd-1001"], key = "value")
        
        #Running the Mock function call as server is not running
        result = mock_client.getBookTitles()
        expected_title = ["Divergent","Insurgent"]
        self.assertEqual(result, expected_title)

class UnitTestRealServer(unittest.TestCase):
    def testsUnitTestRealServer(self):
        real_client = inventoryclient()

        #Running the real server to get the answer
        result = get_book_titles.getBookTitles(["abcd-1002"],real_client)
        expected_title = ["Allegiant"]
        self.assertEqual(result, expected_title)

if __name__ == '__main__':
    unittest.main()