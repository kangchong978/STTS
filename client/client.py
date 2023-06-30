import json

class Client:
    def __init__(self):
        pass
    
    def getPrograms():
        return json.load(open('dummyData.json'))['programs']
    
    def getNotifications():
        return json.load(open('dummyNotifications.json'))['notifications']
