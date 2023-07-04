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
    #    userData2 = {    
    #        'username': 'theboss',
    #        'departmentId': 4,
    #        'role': 0,
    #        'id': 36
    #    }
    #    Client.editUser(userData2)
    #    self.assertTrue(result)

    #def testRemoveProgram(self):
    #    data = {'enable': 0}
    #    result = Client.removeProgram(40, data) 
    #    data2 = {'enable': 1}
    #    Client.removeProgram(40, data2) 
    #    self.assertTrue(result)
    
    #def testRemoveProgram(self):
    #    data = {'enable': 0}
    #    result = Client.removeProgram(40, data) 
    #    data2 = {'enable': 1}
    #    Client.removeProgram(40, data2) 
    #    self.assertTrue(result)

    def testUpdateApprovalStatusById(self):
        data = {'approveStatus': 0,
                'id': 84}
        result = Client.updateApprovalStatusById(data)
        data2 = {'approveStatus': 4,
                'id': 84}
        Client.updateApprovalStatusById(data2)
        self.assertTrue(result)
        


if __name__ == '__main__':
    unittest.main()
    
# Run test
# python3.8 -m unittest tests.clientTest