
import json
import sys
import time
sys.path.append("client")
from client import Client
sys.path.append("components")
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
import datetime

class AccountTab(QWidget):
    def __init__(self):
        super(AccountTab, self).__init__()
        self.accountData = Client.getAccount()
        self.progaramsData = Client.getPrograms()
 
        self.setObjectName("tab_5")
        self.verticalLayout_7 = QVBoxLayout(self)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_4 = QWidget(self)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_1 = QLabel(self.widget_4)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_5.addWidget(self.label_1)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName("label_1")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.frame_6 = QFrame(self.widget_4)

        self.pushButton_64 = QPushButton(self.widget_4)
        self.pushButton_64.setObjectName("pushButton_64")
        self.horizontalLayout_5.addWidget(self.pushButton_64)
        self.pushButton_65 = QPushButton(self.widget_4)
        self.pushButton_65.setObjectName("pushButton_65")
        self.horizontalLayout_5.addWidget(self.pushButton_65)
        self.horizontalLayout_5.addWidget(self.frame_6)

        self.verticalLayout_7.addWidget(self.widget_4)
        self.widget_5 = QWidget(self)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.searchLineEdit = QLineEdit(self.widget_5)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_6.addWidget(self.searchLineEdit)
        self.verticalLayout_7.addWidget(self.widget_5)
        self.widget_13 = QWidget(self)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_7.addWidget(self.widget_13)
        self.listView = QListWidget(self)
        self.listView.setObjectName("listView")
        self.verticalLayout_7.addWidget(self.listView)
        self.label_1.setText("Company Amount")
        self.pushButton_64.setText("Update Amount")
        self.pushButton_65.setText("Refresh")
        
        self.searchLineEdit.setPlaceholderText("Search")
        self.updateAccountDetails()
        self.updateDisplayApprovementList(self.progaramsData)
        self.searchLineEdit.textChanged.connect(self.searchPrograms)  # Connect Search bar signal to function
        self.pushButton_64.clicked.connect(self.showUpdateAmountDialog)  # Connect button signal to dialog function
        self.pushButton_65.clicked.connect(self.refreshListAndAccount)  # Connect button signal to dialog function
        
    def refreshListAndAccount(self):
        self.accountData = Client.getAccount()
        self.updateAccountDetails()
        self.progaramsData = Client.getPrograms()
        self.updateDisplayApprovementList(self.progaramsData)
        
    def updateAccountDetails(self):
        data =  self.accountData
        totalAmount = "$ "
        if(isinstance(data, dict) and "amount" in data and isinstance(data["amount"], float)):
            totalAmount += "{:.2f}".format(data['amount'])
            pass
        self.label_2.setText(totalAmount)
        
    def updateDisplayApprovementList(self, data):
        self.listView.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                widget = self.createWidget(item)
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                listItem.setSizeHint(widget.sizeHint())
                self.listView.addItem(listItem)
                self.listView.setItemWidget(listItem, widget)
            pass
        pass
    
            
    def searchPrograms(self):
        searchValue = self.searchLineEdit.text().strip().lower()
        matchedItems = []
        for i in range(self.listView.count()):
            listItem = self.listView.item(i)
            #TODO
            department = listItem.data(Qt.UserRole)
            if department:
                if (
                    searchValue in str(department.get("title")).lower()
                ):
                    matchedItems.append(listItem)

        for i in range(self.listView.count()):
            listItem = self.listView.item(i)
            listItem.setHidden(listItem not in matchedItems)
        pass
    def createWidget(self, item):
        
        widget = CustomWidget()
        widget.setObjectName("widget")

        # Set the border-radius and background color
        widget.setStyleSheet("QWidget#widget { background-color: #F5F5F5; }")
        widget.setFixedHeight(40)
        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")
        programNameLabel = QLabel(widget)
        programNameLabel.setObjectName("programNameLabel")
        programCostLabel = QLabel(widget)
        programCostLabel.setObjectName("programCostLabel")
        programCostLabel.setMinimumWidth(100)
        paymentDoneButton = QPushButton(widget)
        paymentDoneButton.setObjectName("paymentDoneButton")
        paymentDoneButton.setFixedWidth(100)
        paymentRejectButton = QPushButton(widget)
        paymentRejectButton.setObjectName("paymentRejectButton")
        paymentRejectButton.setFixedWidth(100)
        status = QLabel(widget)
        paymentDoneButton.setText("Done")
        paymentRejectButton.setText("Reject")
        
        programTitle = "Unknown"
        programTotalCost = "0.00"
        totalUsers = 0
       
        
        if isinstance(item, dict):
            if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                    programTitle = item['title']
            if 'users' in item and isinstance(item['users'], str) and item['users'] != '':
                    parsed = json.loads(item['users'])
                    if 'users' in parsed and isinstance(parsed['users'], list) and parsed['users'] is not None:
                        totalUsers = len(parsed['users'])
                        # participants = ',   '.join([user.get('username', 'Unknown') for user in users])
            if 'cost' in item and isinstance(item['cost'], float) and item['cost'] != None:
                    programTotalCost = "{:.2f}".format(item['cost'] * totalUsers)
    
        
        programNameLabel.setText( programTitle)
        programCostLabel.setText( "<font color = 'red'> - $ " +programTotalCost+ "</font>")
        
        horizontalLayout.addWidget(programCostLabel)
        horizontalLayout.addWidget(programNameLabel)
        if item['paymentStatus'] == 0: 
            status.setHidden(False)
            status.setText("No Request")
            paymentDoneButton.setHidden(True)
            paymentRejectButton.setHidden(True)
            horizontalLayout.addWidget(status)
            pass
        elif item['paymentStatus'] == 1:
            status.setHidden(True)
            horizontalLayout.addWidget(paymentDoneButton)
            horizontalLayout.addWidget(paymentRejectButton)
        elif item['paymentStatus'] == 2: 
            status.setHidden(False)
            status.setText("Payment Done")
            paymentDoneButton.setHidden(True)
            paymentRejectButton.setHidden(True)
            horizontalLayout.addWidget(status)
        elif item['paymentStatus'] == 3: 
            status.setHidden(False)
            status.setText("Payment Rejected")
            paymentDoneButton.setHidden(True)
            paymentRejectButton.setHidden(True)
            horizontalLayout.addWidget(status)
        horizontalLayout.setStretch(1,2)
        
        paymentDoneButton.pressed.connect(lambda: self.updatePaymentDone(item))
        paymentRejectButton.pressed.connect(lambda: self.updatePaymentDenied(item))
        
        return widget
    


    def updatePaymentDone(self, item):
        self.showPaymentDoneDialog(item)
        self.updateDisplayApprovementList(Client.getPrograms())
        if 'users' in item and isinstance(item ['users'], str) and item['users'] != '':
                    parsed = json.loads(item ['users'])
                    if 'users' in parsed and isinstance(parsed ['users'], list) and parsed['users'] != None:
                        parsedUsers = parsed['users']
                        
                        self.notifyUserApproved(parsedUsers,item['id'])  
        pass
    
    def updatePaymentDenied(self, item):
        Client.updateProgramPayment(item["id"],{"paymentStatus":3})
        self.updateDisplayApprovementList(Client.getPrograms())
        if 'users' in item and isinstance(item ['users'], str) and item['users'] != '':
            parsed = json.loads(item ['users'])
            if 'users' in parsed and isinstance(parsed ['users'], list) and parsed['users'] != None:
                parsedUsers = parsed['users']
                
                self.notifyUserDeclined(parsedUsers,item['id'])  
        pass
    
    def showUpdateAmountDialog(self):
        currentAmount = self.accountData.get("amount", 0.0)
        newAmount, ok = QInputDialog.getDouble(self, "Update Amount", "Enter new amount:", currentAmount, decimals=2)
        if ok:
            self.accountData["amount"] = newAmount
            result =  Client.updateAccount(self.accountData)
            if result == True:
                self.accountData = Client.getAccount()
                self.updateAccountDetails()
    
    def showPaymentDoneDialog(self, item):
        currentAmount = self.accountData.get("amount", 0.0)
        programCost = item.get("cost", 0.0)
        totalUsers = 0
        if 'users' in item and isinstance(item['users'], str) and item['users'] != '':
                    parsed = json.loads(item['users'])
                    if 'users' in parsed and isinstance(parsed['users'], list) and parsed['users'] is not None:
                        totalUsers = len(parsed['users'])
        totalCost=  (programCost*totalUsers)
        remainingAmount = currentAmount - totalCost

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Payment Confirmation")
        msgBox.setText(f"The cost of the program is: ${totalCost:.2f}")
        msgBox.setInformativeText(f"The remaining amount will be: ${remainingAmount:.2f}")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        if remainingAmount < 0:
            msgBox.setDisabled(True)
            msgBox.setInformativeText("Insufficient funds. Cannot proceed with the payment.")
        else:
            msgBox.setDefaultButton(QMessageBox.Ok)

        response = msgBox.exec_()
        if response == QMessageBox.Ok and remainingAmount >= 0:
            # Proceed with the payment
            newAmount = remainingAmount
            previousAmount = currentAmount
            programId = item.get("id")
            timestamp =  int(time.time() * 1000)

            accountData = {
                "amount": newAmount,
                "previousAmount": previousAmount,
                "programId": programId,
                "updatedTimestamp": timestamp,
            }
            result = Client.updateAccount(accountData)
            Client.updateProgramPayment(item['id'],{"paymentStatus":2})
            if result:
                
                self.accountData = Client.getAccount()
                self.updateAccountDetails()
            


    def notifyUserApproved(self,users,programId):

        notificationData = {
            "type": 3,
            "innerType": 0,
            "programId": int(programId),
        }

        Client.addNewnotifications(users, notificationData)

        
    def notifyUserDeclined(self,users,programId):
    
        notificationData = {
            "type": 3,
            "innerType": 1,
            "programId": int(programId),
        }

        Client.addNewnotifications(users, notificationData)


class CustomWidget(QWidget):
    def sizeHint(self):
        return QSize(self.width(), self.height())
        
    