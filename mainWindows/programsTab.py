
import sys
sys.path.append("client")
from client import Client
sys.path.append("components")
from enrolmentDialog import EnrolmentDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
import datetime
import json
import client
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

class ProgramsTab(QWidget):
    def __init__(self):
        super(ProgramsTab, self).__init__()
        

        self.programsData = Client.getPrograms()
        # *, 0, 1,2,3
        self.filterOptions = ['All','Available', 'Pending', 'Enrolled', 'Rejected']
        self.filterText = ""
        self.filerOption = 0
        

        self.horizontalLayout_2 = QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLineEdit = QLineEdit(self)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.refreshPushButton = QPushButton(self)
        self.refreshPushButton.setObjectName("refreshPushButton")
        icon_path = os.path.join(current_dir, "Refresh_icon.svg.png")
        self.refreshPushButton.setIcon(QIcon(icon_path))
        self.refreshPushButton.clicked.connect(self.handleSearchChanged)
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout.addWidget(self.refreshPushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.programsListWidget = QListWidget(self)
        self.programsListWidget.setObjectName("programsListWidget")
        self.verticalLayout_3.addWidget(self.programsListWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_2 = QScrollArea(self)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 407, 557))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.titleLabel = QLabel(self.scrollAreaWidgetContents_5)
        font = QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setWordWrap(1)
        self.verticalLayout_10.addWidget(self.titleLabel)
        self.graphicsView_3 = QLabel()
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_10.addWidget(self.graphicsView_3)
        self.subtitleLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.subtitleLabel.setWordWrap(1)
        self.verticalLayout_10.addWidget(self.subtitleLabel)
        self.dateTimeLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.dateTimeLabel.setObjectName("dateTimeLabel")
        self.dateTimeLabel.setWordWrap(1)
        self.verticalLayout_10.addWidget(self.dateTimeLabel)
        self.locationLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.locationLabel.setObjectName("locationLabel")
        self.locationLabel.setWordWrap(1)
        self.verticalLayout_10.addWidget(self.locationLabel)
        self.participantsLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.participantsLabel.setObjectName("participantsLabel")
        self.participantsLabel.setWordWrap(1)
        self.verticalLayout_10.addWidget(self.participantsLabel)
        self.frame = QFrame(self.scrollAreaWidgetContents_5)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10.addWidget(self.frame)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_9.addWidget(self.scrollArea_2)
        self.enrollPushButton = QPushButton(self)
        self.enrollPushButton.setObjectName("enrollPushButton")
        self.verticalLayout_9.addWidget(self.enrollPushButton)

        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayout_2.setStretch(1, 2)
        
        self.programsListWidget.currentRowChanged.connect(self.handleSearchReturned)
        self.searchLineEdit.textChanged.connect(self.handleSearchChanged)
        self.searchLineEdit.returnPressed.connect(self.handleSearchReturned)
        self.refreshPushButton.pressed.connect(self.handleRefresh)
        
        self.searchLineEdit.setPlaceholderText("Search")
        self.userProgramApprovements = self.getClientEnrolledPrograms()
        self.updateDisplayProgramsList(self.programsData)
        self.programsListWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.programsListWidget.setStyleSheet("QListWidget { background-color: transparent; }")
        self.comboBox.addItems(self.filterOptions)
        
        self.comboBox.currentIndexChanged.connect(self.handleComboBoxSelection)
    
    def handleRefresh(self):
        self.programsData = Client.getPrograms()
        self.userProgramApprovements = self.getClientEnrolledPrograms()
        self.handleSearchChanged()
    
    def handleSearchChanged(self):
        # self.programsData = Client.getPrograms()
        self.filterPrograms()
       
    def handleComboBoxSelection(self, index):
        self.filerOption = index
        self.filterPrograms()

    def filterPrograms(self):
        text = self.searchLineEdit.text()
        filterProgramsData = self.programsData
        if self.filerOption != 0:
            stateFilter = None
            if self.filerOption == 1:
                stateFilter = 0
                pass
            elif self.filerOption == 2:
                stateFilter = 1
                pass
            elif self.filerOption == 3:
                stateFilter = 2
                pass
            elif self.filerOption == 4:
                stateFilter = 3
                pass
            
            if stateFilter != None:
                result = []
                for program in filterProgramsData:
                    if isinstance(program, dict) and 'enrollStatusCode' in program and isinstance(program['enrollStatusCode'], int):
                        if program['enrollStatusCode'] == stateFilter:
                            result.append(program)
                            pass
                        pass
                    pass
                pass
                filterProgramsData = result
            pass
        
        if text != '':
            result = []
            for program in filterProgramsData:
                if isinstance(program, dict) and 'title' in program and isinstance(program['title'], str):
                    if text.lower() in program['title'].lower():
                        result.append(program)
                        pass
                    pass
                pass
            filterProgramsData = result
            pass
        self.updateDisplayProgramsList(filterProgramsData)
        # self.handleSearchReturned()



        
    def handleSearchReturned(self, index = 0):
        if self.programsListWidget.count() > 0 and index >= 0:
            pid = self.programsListWidget.item(index).data(Qt.UserRole)['id']
            i = -1
            for x, obj in enumerate(self.programsData):
                if isinstance(obj, dict) and 'id' in obj and obj['id'] == pid:
                    i = x
                    
            if(i>=0):
                self.programsListWidget.setCurrentRow(index)
                self.updateDisplayInformationView(i)
                
    def getClientApprovements(self):
        approvements = []
        #TODO
        userData = client.user
        self.currentUser = Client.getUser(userData["id"])
        if 'approvementIds' in self.currentUser and isinstance(self.currentUser ['approvementIds'], str) and self.currentUser ['approvementIds'] is not '':
            parsed = json.loads(self.currentUser ['approvementIds'])
            if 'approvementIds' in parsed and isinstance(parsed ['approvementIds'], list) and parsed['approvementIds'] is not None:
                approvements = parsed['approvementIds']
                    
        return approvements
    
    def getClientEnrolledPrograms(self):
        approvements = self.getClientApprovements()
        if isinstance(approvements, list):
            programs = Client.getUserApprovementByIds(approvements)
            return programs
        
                
    def updateDisplayProgramsList(self, data):
        self.programsListWidget.clear()
        self.enrollPushButton.setDisabled(True)
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                programsApprovementStat = None
                if isinstance(self.userProgramApprovements, list) and len(self.userProgramApprovements) > 0:
                    found_items = [a for a in self.userProgramApprovements if a.get('programId')== item['id']]
                    if len(found_items) > 0:
                        item["enrollStatusCode"] = found_items[0]["approveStatus"]
                        item["approvementId"] = found_items[0]["id"]
                        
                    pass
                    
                widget = self.createWidget(item)
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                listItem.setSizeHint(widget.sizeHint())
                self.programsListWidget.addItem(listItem)
                self.programsListWidget.setItemWidget(listItem, widget)
            pass
        pass
        
    def updateDisplayInformationView(self, i):
        if isinstance(self.programsData, list) and len(self.programsData) > 0:
            if(i > -1 and i <= len(self.programsData)):
                item = self.programsData[i]
                title = "Unknown"
                imageUrl = "Unknown"
                subtitle = "Unknown"
                dateTime = "Unknown"
                location = "Unknown"
                participants = ""
                
                
                if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                    title = item['title']
                pass
                if 'imageUrl' in item and isinstance(item['imageUrl'], str) and item['imageUrl'] != None:
                    imageUrl = item['imageUrl']
                pass
                if 'description' in item and isinstance(item['description'], str) and item['description'] != None:
                    subtitle = item['description']
                pass
                if 'timestamp' in item and isinstance(item['timestamp'], int) and item['timestamp'] != None:
                    timestamp = item['timestamp']
                    dateTime = f"{datetime.datetime.fromtimestamp(timestamp).strftime('%d %b %y')}"
                    
                
                        
                    
                pass
                if 'location' in item and isinstance(item['location'], str) and item['location'] != None:
                    location = item['location']
                pass
                if 'users' in item and isinstance(item['users'], str) and item['users'] != '':
                    parsed = json.loads(item['users'])
                    if 'users' in parsed and isinstance(parsed['users'], list) and parsed['users'] is not None:
                        user_ids = parsed['users']
                        users = Client.getUsersByIds(user_ids)
                        participants = ',   '.join([user.get('username', 'Unknown') for user in users])
                        # Use the 'participants' string as needed
                
                self.titleLabel.setText(title)
                image = QImage()
                try:
                    image.loadFromData(requests.get(imageUrl).content)
                except:
                    pass
                scaledImage = image.scaledToWidth(500, mode=Qt.SmoothTransformation)
                self.graphicsView_3.setPixmap(QPixmap(scaledImage))
                self.subtitleLabel.setText(subtitle)
                self.subtitleLabel.setOpenExternalLinks(True)
                self.dateTimeLabel.setText(dateTime)
                self.locationLabel.setText(location)
                self.participantsLabel.setText(participants)
                if self.enrollPushButton.receivers(self.enrollPushButton.clicked) > 0:
                    self.enrollPushButton.clicked.disconnect()

                self.enrollPushButton.clicked.connect(self.noneNoneDialog)
                if 'enrollStatusCode' in item and isinstance(item['enrollStatusCode'], int) and item['enrollStatusCode'] != None:
                    if item['enrollStatusCode'] == 0:
                        self.enrollPushButton.setText("Enroll now")
                        self.enrollPushButton.setEnabled(True)
                        self.enrollPushButton.clicked.connect(self.showEnrollmentFormDialog)
                        pass
                    elif item['enrollStatusCode'] == 1:
                        self.enrollPushButton.setText("Cancel")
                        self.enrollPushButton.setEnabled(True)
                        self.enrollPushButton.clicked.connect(self.showCancelEnrollmentFormDialog)
                        pass
                    elif item['enrollStatusCode'] == 2:
                        self.enrollPushButton.setText("Cancel")
                        self.enrollPushButton.setEnabled(True)
                        self.enrollPushButton.clicked.connect(self.showCancelEnrollmentFormDialog)
                        pass
                    elif item['enrollStatusCode'] == 3:
                        self.enrollPushButton.setText("Enroll now")
                        self.enrollPushButton.setEnabled(True)
                        self.enrollPushButton.clicked.connect(self.showEnrollmentFormDialog)
                        pass
                    elif item['enrollStatusCode'] == 4:
                        self.enrollPushButton.setText("Enrolled by department")
                        self.enrollPushButton.setEnabled(False)
                        self.enrollPushButton.clicked.connect(self.noneNoneDialog)
                        pass
                    else:
                        self.enrollPushButton.setText("Enroll now")
                        self.enrollPushButton.setEnabled(False)
                        self.enrollPushButton.clicked.connect(self.noneNoneDialog)
                        pass
                    pass
                else:
                    self.enrollPushButton.setText("Enroll now")
                    self.enrollPushButton.setEnabled(False)
                    self.enrollPushButton.clicked.connect(self.showEnrollmentFormDialog)
                    pass
                
                if 'paymentStatus' in item and isinstance(item['paymentStatus'], int) and item['paymentStatus'] != None:
                    paymentStatus = item['paymentStatus']
                    if paymentStatus == 0 or paymentStatus == 3:
                        self.enrollPushButton.setEnabled(True)
                    elif paymentStatus == 1   :
                        self.enrollPushButton.setEnabled(False)
                        self.enrollPushButton.setText("Pending for payment")
                    elif paymentStatus == 1 or paymentStatus == 2 :
                        self.enrollPushButton.setEnabled(False)
                        self.enrollPushButton.setText("Payment is done")
            pass
        pass


    
    def showCancelEnrollmentFormDialog(self):
        currentData = self.programsListWidget.currentItem().data(Qt.UserRole)
        formDialog = EnrolmentDialog(self, type = 1, programName = currentData['title'])
        if formDialog.exec_() == QDialog.Accepted:
            approveId = Client.updateApprovalStatusById({"id":currentData['approvementId'], 'approveStatus': 0})
             
            self.handleRefresh()
            
            currentIndex = self.programsListWidget.currentIndex().row()
              
                
            if(currentIndex != None):
                self.programsListWidget.setCurrentRow(currentIndex)
                self.updateDisplayInformationView(currentIndex)
            pass
            
            
        pass
    
    
    def showEnrollmentFormDialog(self):
        currentData = self.programsListWidget.currentItem().data(Qt.UserRole)
        formDialog = EnrolmentDialog(self, type = 0, programName = currentData['title'])
        if formDialog.exec_() == QDialog.Accepted:
            
            if currentData.get('approvementId'):
                approveId = Client.updateApprovalStatusById({"id":currentData['approvementId'], 'approveStatus': 1})
                result = True
            else:
                approveId = Client.addNewApproval({"userId":self.currentUser["id"], "programId":currentData['id'], 'approveStatus': 1})
                newApprovements = self.getClientApprovements()
                newApprovements.append(approveId)
                result = Client.updateUserProgramApprovements(self.currentUser['id'], newApprovements)
             
            if result == True:
                
                currentIndex = self.programsListWidget.currentIndex().row()
                self.programsData = Client.getPrograms()
                self.userPrograms = self.getClientEnrolledPrograms()
                self.updateDisplayProgramsList(self.programsData)
                #modified
                self.notifyHR(currentData["id"]) 

                self.handleRefresh()
                
                currentIndex = self.programsListWidget.currentIndex().row()
                 
                if(currentIndex != None):
                    self.programsListWidget.setCurrentRow(currentIndex)
                    self.updateDisplayInformationView(currentIndex)
                pass
           
            
        pass
           
    def noneNoneDialog(self):
        pass
    

    #todo 
    #modified
    def notifyHR(self, programId):
        hrs = Client.getUsersByDepartments([9])
        notificationData = {
            "type":0,
            "innerType":0,
            "programId": int(programId),
        }
        Client.addNewnotifications([item['id'] for item in hrs], notificationData)


    def createWidget(self, item):
        widget = QWidget()
        widget.setObjectName("widget")
        widget.setMaximumHeight(50)

        # Set the border-radius and background color
        widget.setStyleSheet("QWidget#widget { border-radius: 10px; background-color: #F5F5F5; }")

        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")

        statusLabel = QLabel(widget)
        statusLabel.setObjectName("statusLabel")
        statusText = "Unknown"
        
        if 'enrollStatusCode' in item and isinstance(item['enrollStatusCode'], int) and item['enrollStatusCode'] is not None:
            if item['enrollStatusCode'] == 0:
                statusText = "Available"
            elif item['enrollStatusCode'] == 1:
                statusText = "Pending Approve"
            elif item['enrollStatusCode'] == 2:
                statusText = "Enrolled"
            elif item['enrollStatusCode'] == 3:
                statusText = "Rejected"
            elif item['enrollStatusCode'] == 4:
                statusText = "Department Enrolled"
        elif 'enrollStatusCode' not in item :
            statusText = "Available"

        statusLabel.setText(statusText)
        statusLabel.setFixedWidth(100)
        horizontalLayout.addWidget(statusLabel)

        titleLabel = QLabel(widget)
        titleLabel.setObjectName("titleLabel")
        title = 'Unknown'
        if 'title' in item and isinstance(item['title'], str) and item['title'] is not None:
            title = item['title']
            


        # Set the word wrap and ellipsis for the titleLabel
        titleLabel.setWordWrap(True)
        fontMetrics = QFontMetrics(titleLabel.font())
        elidedTitle = fontMetrics.elidedText(title, Qt.ElideRight, titleLabel.width())
        titleLabel.setText(elidedTitle)

        horizontalLayout.addWidget(titleLabel)

        return widget