from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QLabel, QPushButton, QDialog, QDialogButtonBox, QFrame, QComboBox
from PyQt5.QtCore import Qt
import sys

sys.path.append("client")
from client import Client


class AddUserDataWindow(QDialog):
    def __init__(self, parent=None):
        super(AddUserDataWindow, self).__init__(parent)

        self.setWindowTitle("Add User Data")
        self.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout(self)

        self.lineEditUserID = QLineEdit(self)
        self.lineEditUserID.setObjectName("lineEditUserID")
        self.lineEditUserID.setPlaceholderText("User ID")
        layout.addWidget(self.lineEditUserID)

        self.lineEditUsername = QLineEdit(self)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditUsername.setPlaceholderText("Username")
        layout.addWidget(self.lineEditUsername)

        self.comboBoxDepartment = QComboBox(self)
        self.comboBoxDepartment.setObjectName("comboBoxDepartment")
        self.comboBoxDepartment.addItem("Finance")
        self.comboBoxDepartment.addItem("Marketing")
        self.comboBoxDepartment.addItem("Accounting")
        self.comboBoxDepartment.addItem("Sales")
        self.comboBoxDepartment.addItem("Human Resources")
        self.comboBoxDepartment.addItem("Admin")
        layout.addWidget(self.comboBoxDepartment)

        buttonBox = QDialogButtonBox(self)
        buttonBox.setOrientation(Qt.Horizontal)
        buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)

    def getUserData(self):
        userID = self.lineEditUserID.text()
        username = self.lineEditUsername.text()
        department = self.comboBoxDepartment.currentText()

        return {
            'id': int(userID),
            'username': username,
            'department': department
        }


class UserTab(QWidget):
    def __init__(self):
        super(UserTab, self).__init__()

        self.usersData = Client.getUsers()

        self.setObjectName("UserTab")
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.frame_3 = QFrame(self)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_9 = QPushButton(self)  # Added QPushButton for editing users
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_14 = QPushButton(self)  # Added QPushButton for deleting users
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget_3 = QWidget(self)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.pushButton_9.setText("Edit")  # Set text for Edit button
        self.pushButton_14.setText("Delete")  # Set text for Delete button
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ListWidget = QListWidget(self)
        self.ListWidget.setObjectName("ListWidget")
        self.verticalLayout.addWidget(self.ListWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.lineEdit_4.setPlaceholderText("Search")
        self.pushButton_3.setText("Add")
        self.updateDisplayUsersList(self.usersData)

        self.pushButton_3.clicked.connect(self.addButtonClicked)
        self.pushButton_9.clicked.connect(self.editButtonClicked)  # Connect Edit button signal to function
        self.pushButton_14.clicked.connect(self.deleteButtonClicked)  # Connect Delete button signal to function
        self.lineEdit_4.textChanged.connect(self.searchUsers)  # Connect Search bar signal to function

    def updateDisplayUsersList(self, data):
        self.ListWidget.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                widget = self.createWidget(item)
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                listItem.setSizeHint(widget.sizeHint())
                self.ListWidget.addItem(listItem)
                self.ListWidget.setItemWidget(listItem, widget)

    def createWidget(self, item):
        widget = QWidget()
        widget.setObjectName("widget")
        widget.setMaximumHeight(50)

        # Set the border-radius and background color
        widget.setStyleSheet("QWidget#widget { border-radius: 10px; background-color: #F5F5F5; }")

        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")
        
        #TODO
        userID = QLabel(widget)
        userID.setObjectName("userID")
        userIDtext = "Unknown"
        if 'id' in item and isinstance(item['id'], int) and item['id'] is not None:
            userIDtext = f"{item['id']}"

        userID.setText(userIDtext)
        userID.setFixedWidth(100)
        horizontalLayout.addWidget(userID)

        username = QLabel(widget)
        username.setObjectName("username")
        usernametext = "Unknown"
        if 'username' in item and isinstance(item['username'], str) and item['username'] is not None:
            usernametext = item['username']

        username.setText(usernametext)
        username.setFixedWidth(100)
        horizontalLayout.addWidget(username)

        #TODO
        department = QLabel(widget)
        department.setObjectName("department")
        departmenttext = "Unknown"
        if 'departmentId' in item and isinstance(item['departmentId'], int) and item['departmentId'] is not None:
            departmenttext = f"{item['departmentId']}"

        department.setText(departmenttext)
        department.setFixedWidth(100) 
        horizontalLayout.addWidget(department)

        return widget

    def addButtonClicked(self):
        addUserWindow = AddUserDataWindow(self)
        if addUserWindow.exec_() == QDialog.Accepted:
            newUserData = addUserWindow.getUserData()
            widget = self.createWidget(newUserData)
            listItem = QListWidgetItem()
            listItem.setData(Qt.UserRole, newUserData)
            listItem.setSizeHint(widget.sizeHint())
            self.ListWidget.addItem(listItem)
            self.ListWidget.setItemWidget(listItem, widget)

    def editButtonClicked(self):
        selectedItem = self.ListWidget.currentItem()
        if selectedItem is not None:
            userData = selectedItem.data(Qt.UserRole)
            if userData is not None:
                userID = userData.get('id')
                if userID is not None:
                    # Prompt user for the updated information
                    editUserWindow = AddUserDataWindow(self)
                    editUserWindow.setWindowTitle("Edit User Data")
                    editUserWindow.lineEditUserID.setEnabled(False)  # Disable editing of User ID
                    editUserWindow.lineEditUserID.setText(str(userID))
                    editUserWindow.lineEditUsername.setText(userData.get('username'))
                    editUserWindow.comboBoxDepartment.setCurrentText(userData.get('department'))

                    if editUserWindow.exec_() == QDialog.Accepted:
                        updatedUserData = editUserWindow.getUserData()
                        updatedUserData['id'] = userID  # Ensure the User ID remains the same
                        updatedWidget = self.createWidget(updatedUserData)
                        selectedItem.setData(Qt.UserRole, updatedUserData)
                        selectedItem.setSizeHint(updatedWidget.sizeHint())
                        self.ListWidget.setItemWidget(selectedItem, updatedWidget)

    def deleteButtonClicked(self):
        selectedItem = self.ListWidget.currentItem()
        if selectedItem is not None:
            self.ListWidget.takeItem(self.ListWidget.row(selectedItem))

    def searchUsers(self):
        searchValue = self.lineEdit_4.text().strip().lower()
        matchedItems = []
        for i in range(self.ListWidget.count()):
            listItem = self.ListWidget.item(i)
            userData = listItem.data(Qt.UserRole)
            if userData:
                if (
                    searchValue in str(userData.get("id")).lower()
                    or searchValue in userData.get("username", "").lower()
                    #TODO
                    or searchValue in userData.get("departmentId", "").lower()
                ):
                    matchedItems.append(listItem)

        for i in range(self.ListWidget.count()):
            listItem = self.ListWidget.item(i)
            listItem.setHidden(listItem not in matchedItems)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("User Management System")
        self.resize(500, 400)

        layout = QVBoxLayout(self)
        self.userTab = UserTab()
        layout.addWidget(self.userTab)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
