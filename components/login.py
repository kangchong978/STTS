import sys
import json
import os
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append("client")
current_dir = os.path.dirname(os.path.abspath(__file__))
from client import Client
import client

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Database Settings")
        self.resize(300, 200)

        vbox = QVBoxLayout()

        t1 = QLabel()
        t1.setText("Host")
        vbox.addWidget(t1)

        self.host_field = QLineEdit()
        vbox.addWidget(self.host_field)

        t2 = QLabel()
        t2.setText("Port")
        vbox.addWidget(t2)

        self.port_field = QLineEdit()
        vbox.addWidget(self.port_field)

        t3 = QLabel()
        t3.setText("User")
        vbox.addWidget(t3)

        self.user_field = QLineEdit()
        vbox.addWidget(self.user_field)

        t4 = QLabel()
        t4.setText("Password")
        vbox.addWidget(t4)

        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)
        vbox.addWidget(self.password_field)

        t5 = QLabel()
        t5.setText("Database")
        vbox.addWidget(t5)

        self.database_field = QLineEdit()
        vbox.addWidget(self.database_field)

        save_button = QPushButton()
        save_button.setText("Save")
        vbox.addWidget(save_button)

        self.setLayout(vbox)

        save_button.clicked.connect(self.saveSettings)

        # Load settings if available
        self.loadSettings()

    def loadSettings(self):
        try:
            with open('settings.json', 'r') as f:
                settings = json.load(f)
                self.host_field.setText(settings.get('host', ''))
                self.port_field.setText(str(settings.get('port', '')))
                self.user_field.setText(settings.get('user', ''))
                self.password_field.setText(settings.get('password', ''))
                self.database_field.setText(settings.get('database', ''))
        except FileNotFoundError:
            pass

    def saveSettings(self):
        host = self.host_field.text()
        port = self.port_field.text()
        user = self.user_field.text()
        password = self.password_field.text()
        database = self.database_field.text()

        # Validate the input fields
        if len(host) == 0 or len(port) == 0 or len(user) == 0 or len(database) == 0:
            QMessageBox.warning(self, "Validation Error", "Please enter all the database settings.")
            return

        # Save the settings to a JSON file
        settings = {
            'host': host,
            'port': int(port),
            'user': user,
            'password': password,
            'database': database
        }
        
        with open('settings.json', 'w') as f:
            json.dump(settings, f)

        QMessageBox.information(self, "Settings Saved", "Database settings have been saved successfully.")
        Client.updateConfig()
        self.accept()


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

        settings_button = QPushButton()
        icon_path = os.path.join(current_dir, "data-management.png")
        settings_button.setIcon(QIcon(icon_path))
        settings_button.clicked.connect(self.openSettingsDialog)

        login_button = QPushButton()
        login_button.setText("Login")
        vbox.addWidget(login_button)
        vbox.addWidget(settings_button)

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

        if isinstance(result, int) and result != False:
            if self.remember_checkbox.isChecked():
                self.settings.setValue("username", username)
                self.settings.setValue("password", password)
                self.settings.setValue("remember_me", "true")
            else:
                self.settings.remove("username")
                self.settings.remove("password")
                self.settings.remove("remember_me")
            client.user = {"id":result, "username": username}
            self.accept()
        else:
            QMessageBox.warning(self, "Validation Error", "Username or password incorrect.")

    def openSettingsDialog(self):
        dialog = SettingsDialog(self)
        dialog.exec_()
