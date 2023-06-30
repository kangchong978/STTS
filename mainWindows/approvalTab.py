from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QLabel, QPushButton, QDialog, QDialogButtonBox, QFrame, QComboBox
from PyQt5.QtCore import Qt
from client import Client

class ApprovalTab(QtWidgets.QWidget):
    def __init__(self):
        super(ApprovalTab, self).__init__()

        self.approvalData = Client.getApproval()

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
        self.pushButton_5.setText("Decline")
        self.pushButton_4.setText("Approve")

        self.pushButton_5.clicked.connect(self.declineSelectedUser)
        self.pushButton_4.clicked.connect(self.approveSelectedUser)
        self.lineEdit_17.textChanged.connect(self.searchByProgramID)

        self.DisplayApprovalList(self.approvalData)

    def DisplayApprovalList(self, data):
        self.listWidget_4.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                widget = self.createWidget(item)
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                listItem.setSizeHint(widget.sizeHint())
                self.listWidget_4.addItem(listItem)
                self.listWidget_4.setItemWidget(listItem, widget)
                # item = QtWidgets.QListWidgetItem(self.listWidget_4)
                # self.listWidget_4.addItem(item)
                # self.listWidget_4.setItemWidget(item, widget)

    def createWidget(self, item):
        widget = QWidget()
        widget.setObjectName("widget")
        widget.setMaximumHeight(50)

        # Set the border-radius and background color
        widget.setStyleSheet("QWidget#widget { border-radius: 10px; background-color: #F5F5F5; }")

        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")

        #TODO
        id = QLabel(widget)
        id.setObjectName("id")
        IDtext = "Unknown"
        if 'id' in item and isinstance(item['id'], int) and item['id'] is not None:
            IDtext = f"{item['id']}"

        id.setText(IDtext)
        id.setFixedWidth(100)
        horizontalLayout.addWidget(id)

        #TODO
        userId = QLabel(widget)
        userId.setObjectName("userId")
        userIdtext = "Unknown"
        if 'userId' in item and isinstance(item['userId'], int) and item['userId'] is not None:
            userIdtext = f"{item['userId']}"

        userId.setText(userIdtext)
        userId.setFixedWidth(100)
        horizontalLayout.addWidget(userId)

        
        #TODO
        programId = QLabel(widget)
        programId.setObjectName("programId")
        programIdtext = "Unknown"
        if 'programId' in item and isinstance(item['programId'], int) and item['programId'] is not None:
            programIdtext = f"{item['programId']}"

        programId.setText(programIdtext)
        programId.setFixedWidth(100)
        horizontalLayout.addWidget(programId)

        #TODO 
        approveStatus = QLabel(widget)
        approveStatus.setObjectName("approveStatus")
        approveStatustext = "Unknown"
        if 'approveStatus' in item and isinstance(item['approveStatus'], int) and item['approveStatus'] is not None:
            approveStatustext = f"{item['approveStatus']}"

        approveStatus.setText(approveStatustext)
        approveStatus.setFixedWidth(100)
        horizontalLayout.addWidget(approveStatus)

        return widget

    def declineSelectedUser(self):
        selected_items = self.listWidget_4.selectedItems()
        for item in selected_items:
            user_widget = self.listWidget_4.itemWidget(item)
            approval_status_label = user_widget.layout().itemAt(3).widget()
            approval_status_label.setText("Declined")

    def approveSelectedUser(self):
        selected_items = self.listWidget_4.selectedItems()
        for item in selected_items:
            user_widget = self.listWidget_4.itemWidget(item)
            approval_status_label = user_widget.layout().itemAt(3).widget()
            approval_status_label.setText("Approved")

    def searchByProgramID(self, text):
        count = self.listWidget_4.count()
        for index in range(count):
            item = self.listWidget_4.item(index)
            user_widget = self.listWidget_4.itemWidget(item)
            programid_label = user_widget.layout().itemAt(4).widget()
            programid = programid_label.text()
            if text.lower() in programid.lower():
                item.setHidden(False)
            else:
                item.setHidden(True)
