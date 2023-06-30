from PyQt5 import QtCore, QtGui, QtWidgets

class ApprovalTab(QtWidgets.QWidget):
    def __init__(self):
        super(ApprovalTab, self).__init__()

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

        self.DisplayUsersList()

    def DisplayUsersList(self):
        # Dummy data for demonstration
        users = [
            {"userID": "001", "username": "John Doe", "department": "Finance", "approvalstatus": "Approved", "programid": "P001"},
            {"userID": "002", "username": "Jane Smith", "department": "HR", "approvalstatus": "Pending", "programid": "P002"},
            {"userID": "003", "username": "Bob Johnson", "department": "IT", "approvalstatus": "Declined", "programid": "P003"}
        ]

        for user in users:
            userWidget = self.createWidget(user["userID"], user["username"], user["department"], user["approvalstatus"], user["programid"])
            item = QtWidgets.QListWidgetItem(self.listWidget_4)
            self.listWidget_4.addItem(item)
            self.listWidget_4.setItemWidget(item, userWidget)

    def createWidget(self, userID, username, department, approvalstatus, programid):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        label_userID = QtWidgets.QLabel(userID)
        label_username = QtWidgets.QLabel(username)
        label_department = QtWidgets.QLabel(department)
        label_approvalstatus = QtWidgets.QLabel(approvalstatus)
        label_programid = QtWidgets.QLabel(programid)

        layout.addWidget(label_userID)
        layout.addWidget(label_username)
        layout.addWidget(label_department)
        layout.addWidget(label_approvalstatus)
        layout.addWidget(label_programid)

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
