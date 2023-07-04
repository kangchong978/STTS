import json
import mysql.connector
from tqdm import tqdm
# from PyQt5.QtWidgets import QApplication, QProgressDialog
import json
import time
from utils import parseToDictWithProgress
user = None

# Load settings from settings.json
with open('settings.json', 'r') as f:
    config = json.load(f)
    if config != {}:
        # Create a connection to the remote database using the loaded settings
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()


class Client:
    @staticmethod
    def updateConfig( ):
        # Load settings from settings.json
        with open('settings.json', 'r') as f:
          config = json.load(f)
        Client.config = {
            'host': config['host'],
            'port': config['port'],
            'user': config['user'],
            'password': config['password'],
            'database': config['database']
        }
        
        # Re-establish the connection
        Client.connection = mysql.connector.connect(**Client.config)
        Client.cursor = Client.connection.cursor()
    
    @staticmethod
    def setCursor(cursor):
        Client.cursor = cursor

    @staticmethod
    def getPrograms():
        cursor.execute("SELECT * FROM programs WHERE enable = 1")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Programs')
    
    @staticmethod
    def getProgramById(id):
        cursor.execute(f'SELECT * FROM programs WHERE enable = 1 and id = {id}')
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Program')

    @staticmethod
    def getUsers():
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Users')
    
    @staticmethod
    def getUsersByDepartments(departments):
        if isinstance(departments, list) and len(departments) > 0:
            cursor.execute("SELECT * FROM users WHERE departmentId IN (%s)" % ','.join(['%s'] * len(departments)), tuple(departments))
            results = cursor.fetchall()
            return Client.parseToDictWithProgress(results, 'Fetching Users')
        return []
    
    @staticmethod
    def getUsersByIds(user_ids):
        if isinstance(user_ids, list) and len(user_ids) > 0:
            cursor.execute("SELECT * FROM users WHERE id IN (%s)" % ','.join(['%s'] * len(user_ids)), tuple(user_ids))
            results = cursor.fetchall()
            return Client.parseToDictWithProgress(results, 'Fetching Users')
        return []

    @staticmethod
    def getUser(id):
        cursor.execute(f'SELECT * FROM users WHERE id = "{id}"')
        results = cursor.fetchall()
        parsed = Client.parseToDictWithProgress(results, 'Fetching Users')
        if len(parsed) > 0:
            return parsed[0]
        else: 
            return None

    @staticmethod
    def getNotifications():
        cursor.execute(f'SELECT * FROM notifications WHERE userId = "{user["id"]}" ORDER BY timestamp DESC')
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Notifications')
 

    @staticmethod
    def getAccount():
        # latest 1 only
        cursor.execute("SELECT * FROM company ORDER BY id DESC LIMIT 1")
        results = cursor.fetchall()
        parsed = Client.parseToDictWithProgress(results, 'Fetching Account')
        if len(parsed) > 0:
            return parsed[0]
        return None

    @staticmethod
    def getApproval():
        cursor.execute("SELECT * FROM approval ORDER BY programId DESC")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Approval')

    @staticmethod
    def getDepartments():
        cursor.execute("SELECT * FROM department")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Departments')

    @staticmethod
    def getFileStorage():
        cursor.execute("SELECT * FROM files_storage")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching File Storage')

    @staticmethod
    def getCompany():
        cursor.execute("SELECT * FROM company")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Company')

    @staticmethod
    def parseToDict(data):
        result_list = []
        columns = [column[0] for column in cursor.description]  # Get the column names

        for row in data:
            result_dict = dict(zip(columns, row))
            result_list.append(result_dict)

        return result_list

    @staticmethod
    def parseToDictWithProgress(data, desc):
        result_list =  parseToDictWithProgress(data, 'Fetching Programs', cursor)
        return result_list

    @staticmethod
    def executeWithProgress(query, values, desc):
        with tqdm(total=1, desc=desc) as pbar:
            cursor.execute(query, values)
            connection.commit()
            pbar.update(1)

    @staticmethod
    def updateAccount(accountData):
        print(f"{accountData}")
        query = "INSERT INTO company (amount, updatedTimestamp) VALUES (%s, %s)"
        values = (accountData['amount'], accountData['updatedTimestamp'])

        Client.executeWithProgress(query, values, 'Updating Account')

        if cursor.rowcount > 0:
            return True
        else:
            return False

    @staticmethod
    def updateUserProgramApprovements(id, programsData):
        query = "UPDATE users SET approvementIds = %s WHERE id = %s"
        values = (f'{{"approvementIds":{json.dumps(programsData)}}}', id)

        Client.executeWithProgress(query, values, 'Updating User Program Approvements')

        if cursor.rowcount > 0:
            return True
        else:
            return False
        
        
        
    @staticmethod
    def getUserApprovementByIds(ids):
        if isinstance(ids,list) and len(ids):
            query = "SELECT * FROM approval WHERE id IN (%s)"
            id_placeholders = ','.join(['%s'] * len(ids))
            query = query % id_placeholders
            values = tuple(ids)

            cursor.execute(query, values)
            results = cursor.fetchall()
            return Client.parseToDictWithProgress(results, 'Fetching Company')
        else:
            return []


    @staticmethod
    def updateApproval(approvalData):
        print(f"{approvalData}")
        query = "UPDATE approval SET approveStatus = %s WHERE id = %s"
        values = (approvalData['approveStatus'], approvalData['id'])

        Client.executeWithProgress(query, values, 'Updating Approval')

        if cursor.rowcount > 0:
            return True
        else:
            return False

    @staticmethod
    def insertUser(userData):
        query = "INSERT INTO users ( username, departmentId) VALUES ( %s, %s)"
        values = ( userData['username'], userData['departmentId'])

        Client.executeWithProgress(query, values, 'Inserting User')

        if cursor.rowcount > 0:
            return True
        else:
            return False

    @staticmethod
    def checkCredentials(username, password):
        query = "SELECT * FROM users WHERE username = %s"
        values = [username]  # Make sure to pass values as a tuple

        cursor.execute(query, values)
        result = cursor.fetchone()
        stored_password = result[2]

        if stored_password == password:
            info = {
                "id": result[0],
                "departmentId": result[6],
                "role": result[9]
                }
            return info
        else:
            return False
        
    @staticmethod
    def updateProgram(id, data):
         
        query = "UPDATE programs SET title = %s, imageUrl = %s, description = %s, timestamp = %s, location = %s, departments = %s, users = %s, cost = %s"\
            "WHERE id = %s"
        values = (data['title'], data['imageUrl'], data['description'], data['timestamp'], data['location'], data['departments'], data['users'], data['cost'], id)
        
        Client.executeWithProgress(query, values, 'Updating program')
        
        if cursor.rowcount > 0:
            return True
        else:
            return False
    @staticmethod
    def updateProgramUsers(id, data):
         
        query = "UPDATE programs SET users = %s "\
            "WHERE id = %s"
        values = (  data['users'] , id)
        
        Client.executeWithProgress(query, values, 'Updating program')
        
        if cursor.rowcount > 0:
            return True
        else:
            return False
        
    @staticmethod
    def removeProgram(id, data):
         
        query = "UPDATE programs SET enable = %s " \
            "WHERE id = %s"
        values = (data['enable'], id)
        
        Client.executeWithProgress(query, values, 'Removing program')
        

        if cursor.rowcount > 0:
            return True
        else:
            return False
        
        
    @staticmethod
    def addNewProgram(data):
        query = "INSERT INTO programs (title) " \
            "VALUES (%s)"
        values = [data['title']]
    
        Client.executeWithProgress(query, values, 'Adding new program')
         
        if cursor.rowcount > 0:
            return cursor.lastrowid
        else:
            return None
        

    @staticmethod
    def deleteUser(userData):
        query = "DELETE FROM users WHERE id = %s"
        values = (userData['id'],)

        Client.executeWithProgress(query, values, 'Deleting User')

        if cursor.rowcount > 0:
            return True
        else:
            return False


    @staticmethod
    def editUser(userData):
        query = "UPDATE users SET username = %s, departmentId = %s WHERE id = %s"
        values = (userData['username'], userData['departmentId'], userData['id'])

        Client.executeWithProgress(query, values, 'Editing User')  


        if cursor.rowcount > 0:
            return True
        else:
            return False
        
    
    def updateProgramPayment(id, data):
        # 0(pending), 1(approved), 2(rejected)
        query = "UPDATE programs SET paymentStatus = %s"
        values = [data['paymentStatus']]

        if data.get('cost') is not None:
            query += ", cost = %s"
            values.append(data['cost'])

        if data.get('users') is not None:
            query += ", users = %s"
            values.append(data['users'])

        if data.get('departments') is not None:
            query += ", departments = %s"
            values.append(data['departments'])

        query += " WHERE id = %s"
        values.append(id)

        Client.executeWithProgress(query, tuple(values), 'Editing User')

        if cursor.rowcount > 0:
            return True
        else:
            return False
        
    def addNewnotification(userid, data):
        query = "INSERT INTO notifications (userid, type, innerType, timestamp, programId) VALUES (%s, %s, %s, %s, %s)"
        values = (userid, data['type'], data['innerType'],   int(time.time() * 1000), data['programId'])

        Client.executeWithProgress(query, values, 'Editing User')  
        if cursor.rowcount > 0:
            return True
        else:
            return False
        
    def addNewnotifications(user_ids, data):
        query = "INSERT INTO notifications (userid, type, innerType, timestamp, programId) VALUES (%s, %s, %s, %s, %s)"
        current_timestamp = int(time.time() * 1000)
        success_count = 0

        for user_id in user_ids:
            values = (user_id, data['type'], data['innerType'], current_timestamp, data['programId'])
            success = Client.executeWithProgress(query, values, 'Editing User')
            if success:
                success_count += 1

        return success_count == len(user_ids)
    
         
    def updatenotifications(id):
        query = f"UPDATE notifications SET reached = 1 WHERE id = %s"
        values = (id,)
        Client.executeWithProgress(query, values, 'Updating notifications status')
        # connection.commit()

        if cursor.rowcount > 0:
            return True
        else:
            return False
         
    
    def addNewApproval(data):
        query = "INSERT INTO approval (userid, programId, approveStatus) VALUES (%s, %s, %s)"
        values = (data['userId'], data['programId'], data['approveStatus'])

        Client.executeWithProgress(query, values, 'Adding approvement request')  
        result = cursor.fetchone()

        if cursor.lastrowid:
            return cursor.lastrowid
        else:
            return False
        
    def updateApprovalStatusById(data):
        query = "UPDATE approval SET approveStatus = %s WHERE id = %s"
        values = (data["approveStatus"], data["id"])

        Client.executeWithProgress(query, values, 'Updating approval status')
        connection.commit()

        if cursor.rowcount > 0:
            return True
        else:
            return False