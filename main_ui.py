# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kangchong/Desktop/STTS/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1446, 943)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.searchLineEdit = QtWidgets.QLineEdit(self.tab)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.verticalLayout_5.addWidget(self.searchLineEdit)
        self.programsListWidget = QtWidgets.QListWidget(self.tab)
        self.programsListWidget.setObjectName("programsListWidget")
        self.verticalLayout_5.addWidget(self.programsListWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 916, 774))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.titleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_10.addWidget(self.titleLabel)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_10.addWidget(self.graphicsView_3)
        self.subtitleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.verticalLayout_10.addWidget(self.subtitleLabel)
        self.dateTimeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.dateTimeLabel.setObjectName("dateTimeLabel")
        self.verticalLayout_10.addWidget(self.dateTimeLabel)
        self.locationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.locationLabel.setObjectName("locationLabel")
        self.verticalLayout_10.addWidget(self.locationLabel)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10.addWidget(self.frame)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_9.addWidget(self.scrollArea_2)
        self.enrollPushButton = QtWidgets.QPushButton(self.tab)
        self.enrollPushButton.setObjectName("enrollPushButton")
        self.verticalLayout_9.addWidget(self.enrollPushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 20, 255, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(280, 20, 501, 481))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_9.setGeometry(QtCore.QRect(20, 50, 461, 192))
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(170, 440, 131, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(200, 130, 100, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 330, 191, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(20, 290, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 250, 461, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_90 = QtWidgets.QLabel(self.frame_2)
        self.label_90.setGeometry(QtCore.QRect(270, 290, 81, 16))
        self.label_90.setObjectName("label_90")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_4.setGeometry(QtCore.QRect(270, 310, 85, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_5.setGeometry(QtCore.QRect(270, 330, 85, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_91 = QtWidgets.QLabel(self.frame_2)
        self.label_91.setGeometry(QtCore.QRect(20, 370, 81, 16))
        self.label_91.setObjectName("label_91")
        self.listWidget_24 = QtWidgets.QListWidget(self.frame_2)
        self.listWidget_24.setGeometry(QtCore.QRect(20, 390, 461, 51))
        self.listWidget_24.setObjectName("listWidget_24")
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_8.setGeometry(QtCore.QRect(40, 410, 85, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_9.setGeometry(QtCore.QRect(150, 410, 85, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_10.setGeometry(QtCore.QRect(110, 370, 85, 20))
        self.checkBox_10.setObjectName("checkBox_10")
        self.pushButton_72 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_72.setGeometry(QtCore.QRect(380, 360, 100, 31))
        self.pushButton_72.setObjectName("pushButton_72")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 60, 255, 411))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 470, 100, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_12.setGeometry(QtCore.QRect(165, 470, 100, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 255, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 771, 441))
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(self.tab_2)
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
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 20, 255, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 60, 771, 441))
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_14.setGeometry(QtCore.QRect(680, 20, 100, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.widget_2 = QtWidgets.QWidget(self.tab_4)
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
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.listWidget_16 = QtWidgets.QListWidget(self.tab_5)
        self.listWidget_16.setGeometry(QtCore.QRect(10, 60, 771, 441))
        self.listWidget_16.setObjectName("listWidget_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(10, 20, 255, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.widget_9 = QtWidgets.QWidget(self.tab_5)
        self.widget_9.setGeometry(QtCore.QRect(20, 80, 741, 61))
        self.widget_9.setObjectName("widget_9")
        self.label_68 = QtWidgets.QLabel(self.widget_9)
        self.label_68.setGeometry(QtCore.QRect(30, 10, 131, 16))
        self.label_68.setObjectName("label_68")
        self.pushButton_45 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_45.setGeometry(QtCore.QRect(500, 0, 100, 41))
        self.pushButton_45.setObjectName("pushButton_45")
        self.label_70 = QtWidgets.QLabel(self.widget_9)
        self.label_70.setGeometry(QtCore.QRect(30, 30, 111, 16))
        self.label_70.setObjectName("label_70")
        self.label_69 = QtWidgets.QLabel(self.widget_9)
        self.label_69.setGeometry(QtCore.QRect(210, 30, 58, 16))
        self.label_69.setObjectName("label_69")
        self.label_67 = QtWidgets.QLabel(self.widget_9)
        self.label_67.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_67.setObjectName("label_67")
        self.pushButton_46 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_46.setGeometry(QtCore.QRect(620, 0, 100, 41))
        self.pushButton_46.setObjectName("pushButton_46")
        self.checkBox = QtWidgets.QCheckBox(self.widget_9)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 21, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_47 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_47.setGeometry(QtCore.QRect(680, 20, 100, 41))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_48.setGeometry(QtCore.QRect(570, 20, 100, 41))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_49.setGeometry(QtCore.QRect(460, 20, 100, 41))
        self.pushButton_49.setObjectName("pushButton_49")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.listWidget_22 = QtWidgets.QListWidget(self.tab_21)
        self.listWidget_22.setGeometry(QtCore.QRect(10, 130, 771, 371))
        self.listWidget_22.setObjectName("listWidget_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_21)
        self.lineEdit_23.setGeometry(QtCore.QRect(10, 80, 255, 31))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pushButton_64 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_64.setGeometry(QtCore.QRect(280, 10, 141, 41))
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_65 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_65.setGeometry(QtCore.QRect(680, 80, 100, 41))
        self.pushButton_65.setObjectName("pushButton_65")
        self.widget_13 = QtWidgets.QWidget(self.tab_21)
        self.widget_13.setGeometry(QtCore.QRect(20, 140, 741, 61))
        self.widget_13.setObjectName("widget_13")
        self.label_84 = QtWidgets.QLabel(self.widget_13)
        self.label_84.setGeometry(QtCore.QRect(30, 10, 131, 16))
        self.label_84.setObjectName("label_84")
        self.pushButton_66 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_66.setGeometry(QtCore.QRect(500, 0, 100, 41))
        self.pushButton_66.setObjectName("pushButton_66")
        self.label_85 = QtWidgets.QLabel(self.widget_13)
        self.label_85.setGeometry(QtCore.QRect(30, 30, 111, 16))
        self.label_85.setObjectName("label_85")
        self.label_87 = QtWidgets.QLabel(self.widget_13)
        self.label_87.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_87.setObjectName("label_87")
        self.pushButton_67 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_67.setGeometry(QtCore.QRect(620, 0, 100, 41))
        self.pushButton_67.setObjectName("pushButton_67")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_13)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 10, 21, 20))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_68 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_68.setGeometry(QtCore.QRect(570, 80, 100, 41))
        self.pushButton_68.setObjectName("pushButton_68")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_21)
        self.lineEdit_24.setGeometry(QtCore.QRect(10, 10, 255, 51))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.pushButton_69 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_69.setGeometry(QtCore.QRect(460, 80, 100, 41))
        self.pushButton_69.setObjectName("pushButton_69")
        self.tabWidget.addTab(self.tab_21, "")
        self.tab_28 = QtWidgets.QWidget()
        self.tab_28.setObjectName("tab_28")
        self.listWidget_23 = QtWidgets.QListWidget(self.tab_28)
        self.listWidget_23.setGeometry(QtCore.QRect(10, 40, 771, 461))
        self.listWidget_23.setObjectName("listWidget_23")
        self.widget_14 = QtWidgets.QWidget(self.tab_28)
        self.widget_14.setGeometry(QtCore.QRect(20, 50, 741, 41))
        self.widget_14.setObjectName("widget_14")
        self.label_89 = QtWidgets.QLabel(self.widget_14)
        self.label_89.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label_89.setObjectName("label_89")
        self.pushButton_71 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_71.setGeometry(QtCore.QRect(630, 0, 100, 41))
        self.pushButton_71.setObjectName("pushButton_71")
        self.tabWidget.addTab(self.tab_28, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1446, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))
        self.subtitleLabel.setText(_translate("MainWindow", "subtitle"))
        self.dateTimeLabel.setText(_translate("MainWindow", "DateTime"))
        self.locationLabel.setText(_translate("MainWindow", "Location"))
        self.enrollPushButton.setText(_translate("MainWindow", "Enroll"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
        self.pushButton_13.setText(_translate("MainWindow", "Add Image"))
        self.label_90.setText(_translate("MainWindow", "Department"))
        self.checkBox_4.setText(_translate("MainWindow", "A"))
        self.checkBox_5.setText(_translate("MainWindow", "B"))
        self.label_91.setText(_translate("MainWindow", "Participance"))
        self.checkBox_8.setText(_translate("MainWindow", "User name"))
        self.checkBox_9.setText(_translate("MainWindow", "User name"))
        self.checkBox_10.setText(_translate("MainWindow", "Select all"))
        self.pushButton_72.setText(_translate("MainWindow", "Remove"))
        self.pushButton_11.setText(_translate("MainWindow", "Add"))
        self.pushButton_12.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.label_5.setText(_translate("MainWindow", "Title"))
        self.label_6.setText(_translate("MainWindow", "Approvement status"))
        self.pushButton_2.setText(_translate("MainWindow", "show"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton_14.setText(_translate("MainWindow", "Add"))
        self.label_35.setText(_translate("MainWindow", "Username"))
        self.label_36.setText(_translate("MainWindow", "Id"))
        self.label_37.setText(_translate("MainWindow", "Department"))
        self.pushButton_15.setText(_translate("MainWindow", "Delete"))
        self.pushButton_16.setText(_translate("MainWindow", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.label_68.setText(_translate("MainWindow", "Approvement status"))
        self.pushButton_45.setText(_translate("MainWindow", "Approve"))
        self.label_70.setText(_translate("MainWindow", "Department"))
        self.label_69.setText(_translate("MainWindow", "Staff id"))
        self.label_67.setText(_translate("MainWindow", "Staff name"))
        self.pushButton_46.setText(_translate("MainWindow", "Decline"))
        self.pushButton_47.setText(_translate("MainWindow", "Approve"))
        self.pushButton_48.setText(_translate("MainWindow", "Decline"))
        self.pushButton_49.setText(_translate("MainWindow", "Select All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.pushButton_64.setText(_translate("MainWindow", "Update Amount"))
        self.pushButton_65.setText(_translate("MainWindow", "Done"))
        self.label_84.setText(_translate("MainWindow", "Payment status"))
        self.pushButton_66.setText(_translate("MainWindow", "Done"))
        self.label_85.setText(_translate("MainWindow", "Total staff"))
        self.label_87.setText(_translate("MainWindow", "Amount"))
        self.pushButton_67.setText(_translate("MainWindow", "Reject"))
        self.pushButton_68.setText(_translate("MainWindow", "Reject"))
        self.lineEdit_24.setText(_translate("MainWindow", "Company amount"))
        self.pushButton_69.setText(_translate("MainWindow", "Select All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_21), _translate("MainWindow", "Page"))
        self.label_89.setText(_translate("MainWindow", "notifications messages"))
        self.pushButton_71.setText(_translate("MainWindow", "show"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_28), _translate("MainWindow", "Page"))
