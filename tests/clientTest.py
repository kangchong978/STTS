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

    #def testEditUser(self):
    #    userData = {    
    #        'username': 'thebossu',
    #        'departmentId': 4,
    #        'role': 0,
    #        'id': 36
    #    }
    #    result = Client.editUser(userData)
    #    self.assertTrue(result)

    #def testRemoveProgram(self):
    #    data = {'enable': 0}
    #    result = Client.removeProgram(data, 40) 
    #    self.assertTrue(result)

    def testDeleteUser(self):
        userData = {'id': 26}
        result = Client.deleteUser(userData)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
    
# Run test
# python3.8 -m unittest tests.clientTest