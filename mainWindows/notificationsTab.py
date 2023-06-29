from PyQt5 import QtCore, QtGui, QtWidgets

class NotificationsTab(QtWidgets.QWidget):
    def __init__(self):
        super(NotificationsTab, self).__init__()

        self.setObjectName("tab_28")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_14 = QtWidgets.QWidget(self)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_89 = QtWidgets.QLabel(self.widget_14)
        self.label_89.setObjectName("label_89")
        self.horizontalLayout_8.addWidget(self.label_89)
        self.frame_7 = QtWidgets.QFrame(self.widget_14)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.pushButton_71 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_71.setObjectName("pushButton_71")
        self.horizontalLayout_8.addWidget(self.pushButton_71)
        self.horizontalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.addWidget(self.widget_14)
        self.listView = QtWidgets.QListView(self)
        self.listView.setObjectName("listView")
        self.verticalLayout_8.addWidget(self.listView)
