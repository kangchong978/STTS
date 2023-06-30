import json
import mysql.connector

# Connection details for the remote database
config = {
    'host': '10.3.241.47',
    'port': 3306,  # The default MySQL port is 3306
    'user': 'stts_1',
    # 'password': '',
    'database': 'stts_db',
}

# Create a connection to the remote database
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

class Client:
    @staticmethod
    def setCursor(cursor):
        Client.cursor = cursor
    
    @staticmethod
    def getPrograms():
        cursor.execute("SELECT * FROM programs")
        results = cursor.fetchall()
        return Client.parseToDict(results)
    
    @staticmethod
    def getUsers():
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        return Client.parseToDict(results)
    
    @staticmethod
    def getNotifications():
        cursor.execute("SELECT * FROM notifications")
        results = cursor.fetchall()
        return Client.parseToDict(results)

    @staticmethod
    def getAccount():
        cursor.execute("SELECT * FROM company")
        results = cursor.fetchall()
        return Client.parseToDict(results)
    @staticmethod
    def getApproval():
        cursor.execute("SELECT * FROM approval")
        results = cursor.fetchall()
        return Client.parseToDict(results)
    
    @staticmethod
    def getDepartment():
        cursor.execute("SELECT * FROM department")
        results = cursor.fetchall()
        return Client.parseToDict(results)
    
    @staticmethod
    def getFileStorage():
        cursor.execute("SELECT * FROM files_storage")
        results = cursor.fetchall()
        return Client.parseToDict(results)

    @staticmethod
    def getCompany():
        cursor.execute("SELECT * FROM company")
        results = cursor.fetchall()
        return Client.parseToDict(results)
    
    @staticmethod
    def parseToDict(data):
        result_list = []
        columns = [column[0] for column in cursor.description]  # Get the column names

        for row in data:
            result_dict = dict(zip(columns, row))
            result_list.append(result_dict)

        return result_list
