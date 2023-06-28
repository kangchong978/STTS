from PyQt5 import QtCore, QtGui, QtWidgets

class ApprovalTab(QtWidgets.QWidget):
    def __init__(self):
        super(ApprovalTab, self).__init__()
 
        self.setObjectName("tab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 255, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listWidget1 = QtWidgets.QListWidget(self)
        self.listWidget1.setGeometry(QtCore.QRect(10, 60, 771, 441))
        self.listWidget1.setObjectName("listWidget1")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 80, 741, 41))
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(140, 10, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 0, 100, 41))
        self.pushButton_2.setObjectName("pushButton_2")
