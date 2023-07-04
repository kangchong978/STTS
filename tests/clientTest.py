# import unittest
import sys
sys.path.append("client")
from client import Client

import unittest

class TestStringMethods(unittest.TestCase):

    #def testCheckCredentialsUser(self):
    #    result = Client.checkCredentials("admin", "admin123")
    #    self.assertEqual(result, 1)
    
    # def test_fetch_programs_SQL(self):
    #     result = Client.getPrograms()
    #     if isinstance(result, list) and len(result) > 0:
    #         firstEnableRow = result[0]
    #         self.assertEqual(firstEnableRow['id'],  2 )
            
    #def testGetUserApprovementByIds(self):
    #    result = Client.getUserApprovementByIds("84")
    #    if isinstance(result,list) and len(result):
    #        firstRow = result[0]
    #        self.assertEqual(firstRow['id'],  84 )

    def testEditUser(self):
        userData = {    
            'username': 'theboss',
            'departmentId': 4,
            'role': 0,
            'id': 36
        }
        result = Client.editUser(userData)
        self.assertTrue(result)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
    
# Run test
# python3.8 -m unittest tests.clientTest