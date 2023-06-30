import json

class Client:
    def __init__(self):
        pass
    
    def getPrograms():
        return json.load(open('dummyData.json'))['programs']
    
    def getUsers():
        return json.load(open('dummyDataUser.json'))['users']
