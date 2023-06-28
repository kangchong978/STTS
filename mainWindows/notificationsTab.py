from PyQt5 import QtCore, QtGui, QtWidgets

class notificationsTab(QtWidgets.QWidget):
    def __init__(self):
        super(notificationsTab, self).__init__()

        self.setObjectName("notificationsTab")
        self.listWidget_23 = QtWidgets.QListWidget(self)
        self.listWidget_23.setGeometry(QtCore.QRect(10, 40, 771, 461))
        self.listWidget_23.setObjectName("listWidget_23")
        self.widget_14 = QtWidgets.QWidget(self)
        self.widget_14.setGeometry(QtCore.QRect(20, 50, 741, 41))
        self.widget_14.setObjectName("widget_14")
        self.label_89 = QtWidgets.QLabel(self.widget_14)
        self.label_89.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label_89.setObjectName("label_89")
        self.pushButton_71 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_71.setGeometry(QtCore.QRect(630, 0, 100, 41))
        self.pushButton_71.setObjectName("pushButton_71")
        self.tabWidget.addTab(self, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1446, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
