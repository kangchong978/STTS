import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append("client")

from client import Client

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(200, 200)

        vbox = QVBoxLayout()

        t1 = QLabel()
        t1.setText("Username")
        vbox.addWidget(t1)

        self.username_field = QLineEdit()
        vbox.addWidget(self.username_field)

        t2 = QLabel()
        t2.setText("Password")
        vbox.addWidget(t2)

        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)
        vbox.addWidget(self.password_field)

        self.remember_checkbox = QCheckBox("Remember me")
        vbox.addWidget(self.remember_checkbox)

        login_button = QPushButton()
        login_button.setText("Login")
        vbox.addWidget(login_button)

        self.setLayout(vbox)

        self.settings = QSettings("MyApp", "LoginWindow")
        self.loadSavedCredentials()

        login_button.clicked.connect(self.openMainWindow)

    def loadSavedCredentials(self):
        username = self.settings.value("username")
        password = self.settings.value("password")
        remember_me = self.settings.value("remember_me")

        if remember_me == "true" and username is not None and password is not None:
            self.username_field.setText(username)
            self.password_field.setText(password)
            self.remember_checkbox.setChecked(True)

    def openMainWindow(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if len(username) == 0 or len(password) == 0:
            QMessageBox.warning(self, "Validation Error", "Please enter both username and password.")
            return

        if len(password) < 6:
            QMessageBox.warning(self, "Validation Error", "Password should be at least 6 characters long.")
            return
        
        result = Client.checkCredentials(username, password)
        
        if result:
            if self.remember_checkbox.isChecked():
                self.settings.setValue("username", username)
                self.settings.setValue("password", password)
                self.settings.setValue("remember_me", "true")
            else:
                self.settings.remove("username")
                self.settings.remove("password")
                self.settings.remove("remember_me")

            self.accept()
        else:
            QMessageBox.warning(self, "Validation Error", "Username or password incorrect.")
