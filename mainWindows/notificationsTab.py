import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
sys.path.append("client")
from client import Client
import datetime


class NotificationsTab(QWidget):
    def __init__(self):
        super(NotificationsTab, self).__init__()
        
        self.notificationsData = Client.getNotifications()
        

        self.setObjectName("tab_28")
        self.verticalLayout_8 = QVBoxLayout(self)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_14 = QWidget(self)
        self.listView = QListWidget(self)
        self.listView.setObjectName("listView")
        self.verticalLayout_8.addWidget(self.listView)
        
        self.listView.setStyleSheet("QListView::item:selected { background-color: #fbfbfb; }")
        
        
        self.updateDisplayNotificationsList(Client.getNotifications())
        
        
    def updateDisplayNotificationsList(self, data):
        self.listView.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                widget = self.createWidget(item)
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                listItem.setSizeHint(widget.sizeHint())
                self.listView.addItem(listItem)
                self.listView.setItemWidget(listItem, widget)
            pass
        pass
    
            
    def createWidget(self, item):
        
        widget = CustomWidget()
        widget.setObjectName("widget")

        # Set the border-radius and background color
        widget.setStyleSheet("QWidget#widget { background-color: #F5F5F5; }")
        widget.setFixedHeight(40)
        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")
        message = QLabel(widget)
        message.setObjectName("message")
        message.setTextFormat(Qt.RichText)
        message.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        dateTimeLabel = QLabel(widget)

        dateTimeText = "Unknown"
        programTitle = "Unknown"
        messageText = "Unknown"
        badge = ""
        
        if isinstance(item, dict):
            if 'reached' in item and isinstance(item['reached'], bool) and item['reached'] != None:
                if item['reached'] == False:
                    badge = "<font color='red'>⚫ </font>"
                pass
            if 'timestamp' in item and isinstance(item['timestamp'], int) and item['timestamp'] is not None:
                timestamp = item['timestamp']
                current_date = datetime.datetime.now().date()
                item_date = datetime.datetime.fromtimestamp(timestamp).date()

                if item_date == current_date:
                    dateTimeText = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M')
                else:
                    dateTimeText = datetime.datetime.fromtimestamp(timestamp).strftime('%d %b %y')

            #TODO   
            if 'programId' in item and isinstance(item['programId'], dict) and item['programId'] != None:
                if 'title' in item['programId'] and isinstance(item['programId']['title'], str) and item['programId']['title'] != None:
                    programTitle = item['programId']['title']
            
            if 'type' in item and isinstance(item['type'], int) and item['type'] != None:
                type = item['type']
                if type == 0:
                    if 'innerType' in item and isinstance(item['innerType'], int) and item['innerType'] != None:
                        innerType = item['innerType']
                        if innerType == 0:
                            messageText = f"Your enrolment request for <b>{programTitle}</b> is <font color='blue'>Approved</font>."
                            # 
                            pass
                        elif innerType == 1:
                            messageText = f"Your enrolment request for <b>{programTitle}</b> is <font color='red'>Rejected</font>."
                            # 
                            pass
                        elif innerType == 2:
                            messageText = f"You are <font color='blue'>added</font> for joining <b>{programTitle}</b>e."
                            # 
                            pass
                        elif innerType == 3:
                            messageText = f"You are <font color='red'>removed</font> for joining <b>{programTitle}</b>e."
                            # 
                            pass
                        pass
                        # 
                    pass
                elif type == 1:
                    if 'innerType' in item and isinstance(item['innerType'], int) and item['innerType'] != None:
                        innerType = item['innerType']
                        if innerType == 0:
                            messageText = f"The payment for <b>{programTitle}</b> is <font color='green'>Done</font>."
                            # 
                            pass
                        elif innerType == 1:
                            messageText = f"The payment for <b>{programTitle}</b> is <font color='red'>Rejected</font>."
                            # 
                            pass
                        pass
                        # 
                    pass
                elif type == 2:
                    if 'innerType' in item and isinstance(item['innerType'], int) and item['innerType'] != None:
                        innerType = item['innerType']
                        if innerType == 0:
                            messageText = f"The <b>{programTitle}</b>e is <font color='grey'>Closed</font>."
                            # 
                            pass
                        elif innerType == 1:    
                            messageText = f"The <b>{programTitle}</b>e is <font color='grey'>Removed</font>."
                            # 
                            pass
                        pass
                        # 
                    pass
                pass
            pass
        
        message.setText( messageText)
        message.setWordWrap(True)
        
        dateTimeLabel.setText( badge + dateTimeText)
        
        horizontalLayout.addWidget(message)
        horizontalLayout.addWidget(dateTimeLabel)


        return widget
    
class CustomWidget(QWidget):
            def sizeHint(self):
                return QSize(self.width(), self.height())