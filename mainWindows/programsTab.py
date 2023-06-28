
import sys
sys.path.append("client")
from client import Client
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
import datetime

class ProgramsTab(QWidget):
    def __init__(self):
        super(ProgramsTab, self).__init__()
        self.programsData = Client.getPrograms()

        self.verticalLayout_7 = QVBoxLayout(self)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.searchLineEdit = QLineEdit(self)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.verticalLayout_5.addWidget(self.searchLineEdit)
        self.programsListWidget = QListWidget(self)
        self.programsListWidget.setObjectName("programsListWidget")
        self.verticalLayout_5.addWidget(self.programsListWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_2 = QScrollArea(self)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 455, 411))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.titleLabel = QLabel(self.scrollAreaWidgetContents_5)
        font = QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setWordWrap(1)
        self.verticalLayout_10.addWidget(self.titleLabel)
        self.graphicsView_3 = QLabel(self.scrollAreaWidgetContents_5) 
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
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        
        self.programsListWidget.currentRowChanged.connect(self.handleSearchReturned)
        self.searchLineEdit.textChanged.connect(self.handleSearchChanged)
        self.searchLineEdit.returnPressed.connect(self.handleSearchReturned)
        
        self.searchLineEdit.setPlaceholderText("Search")
        self.updateDisplayProgramsList(self.programsData)
    
    
    
    def handleSearchChanged(self,text):
       self.filterPrograms(text)
    
    def filterPrograms(self, text):
        result = []
        if text != '':
            for program in self.programsData:
                if isinstance(program, dict) and 'title' in program and isinstance(program['title'], str):
                    if text.lower() in program['title'].lower():
                        result.append(program)
                        pass
                    pass
                pass
            
            self.updateDisplayProgramsList(result)
            pass
        else:
            self.updateDisplayProgramsList(self.programsData)
            pass
        
    def handleSearchReturned(self, index = 0):
        if self.programsListWidget.count() > 0 and index >= 0:
            pid = self.programsListWidget.item(index).data(Qt.UserRole)['pid']
            i = -1
            for x, obj in enumerate(self.programsData):
                if isinstance(obj, dict) and 'pid' in obj and obj['pid'] == pid:
                    i = x
                    
            if(i>=0):
                self.programsListWidget.setCurrentRow(index)
                self.updateDisplayInformationView(i)
                
    def updateDisplayProgramsList(self, data):
        self.programsListWidget.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                title = "Unknown"
                if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                  title = item['title']
                  pass
                listItem.setText(title)
                self.programsListWidget.addItem(listItem)
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
                self.titleLabel.setText(title)
                image = QImage()
                image.loadFromData(requests.get(imageUrl).content)
                scaledImage = image.scaledToWidth(500, mode=Qt.SmoothTransformation)
                self.graphicsView_3.setPixmap(QPixmap(scaledImage))
                self.subtitleLabel.setText(subtitle)
                self.dateTimeLabel.setText(dateTime)
                self.locationLabel.setText(location)
                
                if 'enrollStatusCode' in item and isinstance(item['enrollStatusCode'], int) and item['enrollStatusCode'] != None:
                    if item['enrollStatusCode'] == 0:
                        self.enrollPushButton.setText("Enroll now")
                        self.enrollPushButton.setEnabled(True)
                        pass
                    elif item['enrollStatusCode'] == 1:
                        self.enrollPushButton.setText("Cancel")
                        self.enrollPushButton.setEnabled(True)
                        pass
                    elif item['enrollStatusCode'] == 2:
                        self.enrollPushButton.setText("Cancel")
                        self.enrollPushButton.setEnabled(True)
                        pass
                    else:
                        self.enrollPushButton.setText("Enroll now")
                        self.enrollPushButton.setEnabled(False)
                        pass
                    pass
                else:
                    self.enrollPushButton.setText("Enroll now")
                    self.enrollPushButton.setEnabled(False)
                    pass
            pass
        pass
        