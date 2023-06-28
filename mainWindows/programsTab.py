
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

        self.setObjectName("programsTab")
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(QRect(10, 60, 255, 441))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(10, 20, 255, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(280, 20, 501, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QRect(20, 50, 461, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(20, 20, 61, 21))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.frame)
        self.label_2.setGeometry(QRect(20, 250, 100, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setGeometry(QRect(20, 270, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setGeometry(QRect(20, 290, 58, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(170, 440, 131, 32))
        self.pushButton.setObjectName("pushButton")
        
        self.listWidget.currentRowChanged.connect(self.updateDisplayInformationView)
        
        self.lineEdit.setPlaceholderText("Search")
        self.updateDisplayProgramsList()
        
    def updateDisplayProgramsList(self):
        if isinstance(self.programsData, list) and len(self.programsData) > 0:
            for item in self.programsData:
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                title = "Unknown"
                if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                  title = item['title']
                  pass
                listItem.setText(title)
                self.listWidget.addItem(listItem)
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
                enrolStateCode = -1
                
                
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
                self.label.setText(title)
                image = QImage()
                image.loadFromData(requests.get(imageUrl).content)
                pixmap_item = QGraphicsPixmapItem(QPixmap(image))
                scene = QGraphicsScene()
                scene.addItem(pixmap_item)
                self.graphicsView.setScene(scene)
                self.label_2.setText(subtitle)
                self.label_3.setText(dateTime)
                self.label_4.setText(location)
                
                if 'enrollStatusCode' in item and isinstance(item['enrollStatusCode'], int) and item['enrollStatusCode'] != None:
                    if item['enrollStatusCode'] == 0:
                        self.pushButton.setText("Enroll now")
                        self.pushButton.setEnabled(True)
                        pass
                    elif item['enrollStatusCode'] == 1:
                        self.pushButton.setText("Cancel")
                        self.pushButton.setEnabled(True)
                        pass
                    elif item['enrollStatusCode'] == 2:
                        self.pushButton.setText("Cancel")
                        self.pushButton.setEnabled(True)
                        pass
                    else:
                        self.pushButton.setText("Enroll now")
                        self.pushButton.setEnabled(False)
                        pass
                    pass
                else:
                    self.pushButton.setText("Enroll now")
                    self.pushButton.setEnabled(False)
                    pass
            pass
        pass
        