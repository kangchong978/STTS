from PyQt5 import QtCore, QtGui, QtWidgets


class UserTab(QtWidgets.QWidget):
    def __init__(self):
        super(UserTab, self).__init__()

        self.setObjectName("UserTab")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 20, 255, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.listWidget_3 = QtWidgets.QListWidget(self)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 60, 771, 441))
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_14 = QtWidgets.QPushButton(self)
        self.pushButton_14.setGeometry(QtCore.QRect(680, 20, 100, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setGeometry(QtCore.QRect(20, 80, 741, 41))
        self.widget_2.setObjectName("widget_2")
        self.label_35 = QtWidgets.QLabel(self.widget_2)
        self.label_35.setGeometry(QtCore.QRect(90, 10, 71, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.widget_2)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.widget_2)
        self.label_37.setGeometry(QtCore.QRect(190, 10, 71, 16))
        self.label_37.setObjectName("label_37")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_15.setGeometry(QtCore.QRect(640, 0, 100, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_16.setGeometry(QtCore.QRect(530, 0, 100, 41))
        self.pushButton_16.setObjectName("pushButton_16")