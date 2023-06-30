import json

class Client:
    def __init__(self):
        pass
    
    def getPrograms():
        return json.load(open('dummyData.json'))['programs']
    
    def getUsers():
        return json.load(open('dummyDataUser.json'))['users']
    
    def getNotifications():
        return json.load(open('dummyNotifications.json'))['notifications']

    def getAccount():
        return json.load(open('dummyAccounts.json'))['account']
    