from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QLabel, QPushButton, QDialog, QDialogButtonBox, QFrame, QComboBox
from PyQt5.QtCore import Qt
from client import Client
import json
class ApprovalTab(QtWidgets.QWidget):
    def __init__(self):
        super(ApprovalTab, self).__init__()

        self.approvalData = Client.getApproval()
        self.users = Client.getUsers()
        self.programs = Client.getPrograms()
        
        

        self.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.lineEdit_17 = QtWidgets.QLineEdit(self)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_2.addWidget(self.lineEdit_17)

        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2.addWidget(self.frame_4)

        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_2.addWidget(self.pushButton_1)
        
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.listWidget_4 = QtWidgets.QListWidget(self)
        self.listWidget_4.setObjectName("listWidget_4")
        self.verticalLayout_5.addWidget(self.listWidget_4)

        self.lineEdit_17.setPlaceholderText("Search")
        self.pushButton_1.setText("Refresh")
        self.pushButton_5.setText("Decline")
        self.pushButton_4.setText("Approve")

        self.pushButton_1.clicked.connect(self.handleRefresh)
        self.pushButton_5.clicked.connect(self.declineSelectedUser)
        self.pushButton_4.clicked.connect(self.approveSelectedUser)
        self.lineEdit_17.textChanged.connect(self.searchByProgramID)

        self.displayApprovalList(self.approvalData)

    def handleRefresh(self):
        self.approvalData = Client.getApproval()
        self.displayApprovalList(self.approvalData)        
        pass 
    def displayApprovalList(self, data):
        self.listWidget_4.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                widget = self.createWidget(item)
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                listItem.setSizeHint(widget.sizeHint())
                self.listWidget_4.addItem(listItem)
                self.listWidget_4.setItemWidget(listItem, widget)
                
    def getUserUsername(self, userId):
        for user in self.users:
            if user.get('id') == userId and 'username' in user:
                return user['username']
        return None
    
    def getProgramName(self, programId):
        for program in self.programs:
            if program.get('id') == programId and 'title' in program:
                return program['title']
        return None

    def createWidget(self, item):
        widget = QWidget()
        widget.setObjectName("widget")
        widget.setMaximumHeight(50)

        # Set the border-radius and background color
        widget.setStyleSheet("QWidget#widget { border-radius: 10px; background-color: #F5F5F5; }")

        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")

        id = QLabel(widget)
        id.setObjectName("id")
        IDtext = "Unknown"
        if 'id' in item and isinstance(item['id'], int) and item['id'] is not None:
            IDtext = f"{item['id']}"

        id.setText(IDtext)
        id.setHidden(True)
        id.setFixedWidth(100)
        horizontalLayout.addWidget(id)

        userId = QLabel(widget)
        userId.setObjectName("userId")
        userIdText = "Unknown"
        if 'userId' in item and isinstance(item['userId'], int) and item['userId'] is not None:
            a = item['userId']
            username = self.getUserUsername(a)
            if username:
                userIdText = f"{username}"
            else:
                userIdText = str(a)

        userId.setText(userIdText)
        userId.setFixedWidth(100)
        horizontalLayout.addWidget(userId)

        programId = QLabel(widget)
        programId.setObjectName("programId")
        programIdtext = "Unknown"
        if 'programId' in item and isinstance(item['programId'], int) and item['programId'] is not None:
            a = item['programId']
            programName = self.getProgramName(a)
            if programName:
                programIdtext = f"{programName}"
            else:
                programIdtext = str(a)

        programId.setText(programIdtext)
        horizontalLayout.addWidget(programId)

        approveStatus = QLabel(widget)
        approveStatus.setObjectName("approveStatus")
        approveStatustext = "Unknown"
        if 'approveStatus' in item and isinstance(item['approveStatus'], int) and item['approveStatus'] is not None:
            if item['approveStatus'] == 0:
                approveStatustext = "Cancelled"
            elif item['approveStatus'] == 1:
                approveStatustext = "Pending"
            elif item['approveStatus'] == 2:
                approveStatustext = "Approved"
            elif item['approveStatus'] == 3:
                approveStatustext = "Declined"
            elif item['approveStatus'] == 4:
                approveStatustext = "Department"
            else:
                approveStatustext = "Unknown"

        approveStatus.setText(approveStatustext)
        approveStatus.setFixedWidth(100)
        horizontalLayout.addWidget(approveStatus)
        horizontalLayout.setStretch(1,2)

        return widget

    def declineSelectedUser(self):
        selected_items = self.listWidget_4.selectedItems()
        for item in selected_items:
            id = self.listWidget_4.currentItem().data(Qt.UserRole)['id']

            
            approval_data = {
                "id": int(id),
                "approveStatus": 3  # Set the status to 3 for Declined
            }
            Client.updateApproval(approval_data)
            self.handleRefresh()
            
    def approveSelectedUser(self):
        selected_items = self.listWidget_4.selectedItems()
        for item in selected_items:
            id = self.listWidget_4.currentItem().data(Qt.UserRole)['id']
            user_id = self.listWidget_4.currentItem().data(Qt.UserRole)['userId']
            programId = self.listWidget_4.currentItem().data(Qt.UserRole)['programId']
            approval_data = {
                "id": int(id),
                "approveStatus": 2  # Set the status to 2 for Approved
            }
            Client.updateApproval(approval_data)
            result = Client.getProgramById(programId)
            newUsers = []
            if isinstance(result, list) and len(result)>0 :
                if 'users' in result[0] and isinstance(result[0]  ['users'], str) and result[0]  ['users'] != '':
                    parsed = json.loads(result[0]  ['users'])
                    if 'users' in parsed and isinstance(parsed ['users'], list) and parsed['users'] is not None:
                        users = parsed['users']
                        newUsers = users
            newUsers.append(int(user_id))
            Client.updateProgramUsers(int(programId), {"users":json.dumps({"users":newUsers})})
            notificationData = {
                "userid":int(user_id),
                "type":0,
                "innerType":0,
                "programId": int(programId),
            }
            Client.addNewnotification(int(user_id), notificationData)
            self.handleRefresh()
            

    def searchByProgramID(self, text):
        count = self.listWidget_4.count()
        for index in range(count):
            item = self.listWidget_4.item(index)
            user_widget = self.listWidget_4.itemWidget(item)
            program_label = user_widget.layout().itemAt(2).widget()
            programName = program_label.text()
            if text.lower() in programName.lower():
                item.setHidden(False)
            else:
                item.setHidden(True)
