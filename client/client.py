import json
import mysql.connector
from tqdm import tqdm
from PyQt5.QtWidgets import QApplication, QProgressDialog
import json

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
        cursor.execute("SELECT * FROM programs")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Programs')

    @staticmethod
    def getUsers():
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Users')
    
    @staticmethod
    def getUser(username):
        cursor.execute(f'SELECT * FROM users WHERE username = "{username}"')
        results = cursor.fetchall()
        parsed = Client.parseToDictWithProgress(results, 'Fetching Users')
        if len(parsed) > 0:
            return parsed[0]
        else: 
            return None

    @staticmethod
    def getNotifications():
        cursor.execute("SELECT * FROM notifications")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Notifications')

    @staticmethod
    def getAccount():
        # latest 1 only
        cursor.execute("SELECT * FROM company ORDER BY updatedTimestamp DESC LIMIT 1")
        results = cursor.fetchall()
        parsed = Client.parseToDictWithProgress(results, 'Fetching Account')
        if len(parsed) > 0:
            return parsed[0]
        return None

    @staticmethod
    def getApproval():
        cursor.execute("SELECT * FROM approval")
        results = cursor.fetchall()
        return Client.parseToDictWithProgress(results, 'Fetching Approval')

    @staticmethod
    def getDepartment():
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
        result_list = []
        columns = [column[0] for column in cursor.description]  # Get the column names

        progress_dialog = QProgressDialog(desc, None, 0, len(data))
        progress_dialog.setWindowModality(1)  # Set the dialog to modal
        progress_dialog.setWindowTitle("Progress")
        progress_dialog.show()

        for i, row in enumerate(data):
            result_dict = dict(zip(columns, row))
            result_list.append(result_dict)
            progress_dialog.setValue(i + 1)
            QApplication.processEvents()  # Process events to keep GUI responsive


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
        query = "UPDATE users SET programs = %s WHERE id = %s"
        values = (f'{{"programs":{json.dumps(programsData)}}}', id)

        Client.executeWithProgress(query, values, 'Updating User Program Approvements')

        if cursor.rowcount > 0:
            return True
        else:
            return False

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
        query = "INSERT INTO users (id, username, departmentId) VALUES (%s, %s, %s)"
        values = (userData['id'], userData['username'], userData['departmentId'])

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

        if result is None:
            return False

        # Assuming the password is stored in the database as a hash, compare it with the provided password
        # You may need to adapt this part based on how passwords are stored and hashed in your database
        # Assuming the password is stored in the second column (index 1) of the query result
        stored_password = result[1]

        if stored_password == password:
            return True
        else:
            return False