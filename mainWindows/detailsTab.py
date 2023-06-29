import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append("client")
from client import Client

class DetailsTab(QtWidgets.QWidget):
    def __init__(self):
        super(DetailsTab, self).__init__()

        self.programsData = Client.getPrograms()

        self.setObjectName("detailsTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filterLineEdit = QtWidgets.QLineEdit(self)
        self.filterLineEdit.setObjectName("filterLineEdit")
        self.horizontalLayout_3.addWidget(self.filterLineEdit)
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.listView = QtWidgets.QListWidget(self)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.listView.setStyleSheet("QListWidget { background-color: transparent; }")

        self.populate_list()

    def populate_list(self):
        data = self.programsData

        for itemData in data:
            widget = self.createWidget(itemData)
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(widget.sizeHint())
            self.listView.addItem(item)
            self.listView.setItemWidget(item, widget)

    def createWidget(self, item):
        widget = QtWidgets.QWidget()
        widget.setObjectName("widget")
        widget.setMaximumHeight(50) 
        horizontalLayout = QtWidgets.QHBoxLayout(widget)
        horizontalLayout.setObjectName("horizontalLayout")
        statusLabel = QtWidgets.QLabel(widget)
        statusLabel.setObjectName("statusLabel")
        statusText = "Unknown"
        if 'enrollStatusCode' in item and isinstance(item['enrollStatusCode'], int) and item['enrollStatusCode'] != None:
            if(item['enrollStatusCode'] == 0):
                statusText = "Enrolled"
            elif(item['enrollStatusCode'] == 1):
                statusText = "Pending Approve"
            elif(item['enrollStatusCode'] == 2):
                statusText = "Approved"
            elif(item['enrollStatusCode'] == 3):
                statusText = "Cancelled"
                
        statusLabel.setText(statusText)
        statusLabel.setFixedWidth(100)
        horizontalLayout.addWidget(statusLabel)
        titleLabel = QtWidgets.QLabel(widget)
        titleLabel.setObjectName("titleLabel")
        title = 'Unknown'
        if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                    title = item['title']
        titleLabel.setText(title)
        titleLabel.setWordWrap(True)
        horizontalLayout.addWidget(titleLabel)
        
        button = QtWidgets.QPushButton(widget)
        button.setObjectName("button")
        button.setText("View")
        button.setFixedWidth(80)
        horizontalLayout.addWidget(button)

        return widget


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    detailsTab = DetailsTab()
    detailsTab.show()

    sys.exit(app.exec_())
