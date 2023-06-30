
import sys
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
        self.searchLineEdit.setPlaceholderText("Search")
        self.updateAccountDetails()
        self.updateDisplayApprovementList(self.progaramsData)
        self.searchLineEdit.textChanged.connect(self.searchPrograms)  # Connect Search bar signal to function
        self.pushButton_64.clicked.connect(self.showUpdateAmountDialog)  # Connect button signal to dialog function
        
    def updateAccountDetails(self):
        data =  self.accountData
        totalAmount = "$ "
        if(isinstance(data, dict) and "amount" in data and isinstance(data["amount"], float)):
            totalAmount += f'{data["amount"]}'
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
        
        paymentDoneButton.setText("Done")
        paymentRejectButton.setText("Reject")
        
      
        
        programTitle = "Unknown"
        programTotalCost = "0.00"
       
        
        if isinstance(item, dict):
            if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                    programTitle = item['title']
            if 'cost' in item and isinstance(item['cost'], float) and item['cost'] != None:
                    programTotalCost = "{:.2f}".format(item['cost'])
    
        
        programNameLabel.setText( programTitle)
        programCostLabel.setText( "<font color = 'red'> - $" +programTotalCost+ "</font>")
        
        horizontalLayout.addWidget(programCostLabel)
        horizontalLayout.addWidget(programNameLabel)
        horizontalLayout.addWidget(paymentDoneButton)
        horizontalLayout.addWidget(paymentRejectButton)
        horizontalLayout.setStretch(1,2)
        
        return widget
    
    def showUpdateAmountDialog(self):
        currentAmount = self.accountData.get("amount", 0.0)
        newAmount, ok = QInputDialog.getDouble(self, "Update Amount", "Enter new amount:", currentAmount, decimals=2)
        if ok:
            #TODO
            # Save the new amount
            self.accountData["amount"] = newAmount
            # self.updateAccountDetails()
            # Update the account data on the server
            result =  Client.updateAccount(self.accountData)
            # print(result)
            if result == True:
                self.accountData = Client.getAccount()
                self.updateAccountDetails()
                
            
            
class CustomWidget(QWidget):
    def sizeHint(self):
        return QSize(self.width(), self.height())
        
    