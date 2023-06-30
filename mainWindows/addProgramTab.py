from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDateTime
import requests
import sys
sys.path.append("client")
import json

from client import Client
class AddProgramTab(QWidget):
    def __init__(self):
        super(AddProgramTab, self).__init__()

        self.programsData = Client.getPrograms()
        self.suggestionFontSizes = ["8", "10", "13", "16", "24", "32"]
        self.departments = Client.getDepartment()
        

        self.setObjectName("AddProgramTab")
        self.horizontalLayout_19 = QHBoxLayout(self)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
    

        self.widget_8 = QWidget(self)
        self.widget_8.setObjectName("widget_8")
        self.widget_8.setMaximumWidth(250)
        self.verticalLayout_32 = QVBoxLayout(self.widget_8)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.searchLineEdit = QLineEdit(self.widget_8)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.verticalLayout_32.addWidget(self.searchLineEdit)
        self.programsListWidget = QListWidget(self.widget_8)
        self.programsListWidget.setObjectName("programsListWidget")
        self.verticalLayout_32.addWidget(self.programsListWidget)
        self.horizontalLayout_32 = QHBoxLayout(self.widget_8)
        self.removeProgramsButton = QPushButton(self.widget_8)
        self.removeProgramsButton.setObjectName("removeProgramsButton")
        self.horizontalLayout_32.addWidget(self.removeProgramsButton)
        self.addProgramsButton = QPushButton(self.widget_8)
        self.addProgramsButton.setObjectName("addProgramsButton")
        self.horizontalLayout_32.addWidget(self.addProgramsButton)
        self.verticalLayout_32.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_19.addWidget(self.widget_8)
        self.widget_11 = QWidget(self)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_33 = QVBoxLayout(self.widget_11)
        self.verticalLayout_33.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.gridLayout_2 = QVBoxLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.titleLineText = QLineEdit(self.widget_11)
        self.titleLineText.setObjectName("titleLineText")
        self.gridLayout_2.addWidget(self.titleLineText)
        self.graphicsView_12 =QLabel(self.widget_11)
        self.graphicsView_12.setObjectName("graphicsView_12")
        # self.graphicsView_12.setFixedHeight(250)
        self.gridLayout_2.addWidget(self.graphicsView_12 )
        self.uploadPushButton = QPushButton(self.widget_11)
        self.uploadPushButton.setObjectName("uploadPushButton")
        self.uploadPushButton.setFixedWidth(150)
        self.gridLayout_2.addWidget(self.uploadPushButton )
        
        self.verticalLayout_34 = QVBoxLayout()
        self.toolbar = QToolBar()
        self.fontComboBox = QFontComboBox()
        self.toolbar.addWidget(self.fontComboBox)

        self.fontSizeComboBox = QComboBox()
        self.fontSizeComboBox.setEditable(True)
        self.toolbar.addWidget(self.fontSizeComboBox)

        self.boldAction = QAction("Bold", self)
        self.toolbar.addAction(self.boldAction)

        self.italicAction = QAction("Italic", self)
        self.toolbar.addAction(self.italicAction)
        
        self.underlineAction = QAction("Underline", self)
        self.toolbar.addAction(self.underlineAction)
        self.bulletAction = QAction("Bullets", self)
        self.toolbar.addAction(self.bulletAction)
        self.linkAction = QAction("Link", self)
        self.toolbar.addAction(self.linkAction)
        self.leftAlignAction = QAction("Left Align", self)
        self.toolbar.addAction(self.leftAlignAction)
        self.centerAlignAction = QAction("Center Align", self)
        self.toolbar.addAction(self.centerAlignAction)
        self.rightAlignAction = QAction("Right Align", self)
        self.toolbar.addAction(self.rightAlignAction)       
        self.colorAction = QAction("Text Color", self)
        self.toolbar.addAction(self.colorAction)

        self.verticalLayout_34.addWidget(self.toolbar)
        self.subtitleLineText = QTextEdit(self.widget_11)
        self.subtitleLineText.setObjectName("subtitleLineText")
        self.subtitleLineText.setFixedHeight(250)
        self.verticalLayout_34.addWidget(self.subtitleLineText)
        self.verticalLayout_34.setSpacing(0)
        self.gridLayout_2.addLayout(self.verticalLayout_34 )
        self.dateTimeEdit = QDateTimeEdit(self.widget_11)
        self.dateTimeEdit.setObjectName("dateTimeEdit_4")
        self.gridLayout_2.addWidget(self.dateTimeEdit )
        self.locationLineText = QLineEdit(self.widget_11)
        self.locationLineText.setObjectName("locationLineText")
        self.gridLayout_2.addWidget(self.locationLineText )
        # Create a QScrollArea
        scrollArea = QScrollArea(self.widget_11)
        scrollArea.setWidgetResizable(True)
        scrollContent = QWidget(scrollArea)
        scrollArea.setWidget(scrollContent)
        scrollLayout = QVBoxLayout(scrollContent)
        scrollLayout.setObjectName("scrollLayout")
        scrollLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_33.addWidget(scrollArea)
        self.horizontalLayout_19.addWidget(self.widget_11)
        self.pushButton_10 = QPushButton(self.widget_11)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_33.addWidget(self.pushButton_10)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        # participants
        self.verticalLayout_113 = QVBoxLayout()
        self.verticalLayout_113.setObjectName("verticalLayout_113")
        self.label_103 = QLabel(self.widget_11)
        self.label_103.setObjectName("label_103")
        self.verticalLayout_113.addWidget(self.label_103)
        self.listWidget_24 = QListView(self.widget_11)
        self.listWidget_24.setObjectName("listWidget_24")
        self.verticalLayout_113.addWidget(self.listWidget_24)
        self.horizontalLayout_23.addLayout(self.verticalLayout_113)
        # # department
        self.verticalLayout_114 = QVBoxLayout()
        self.verticalLayout_114.setObjectName("verticalLayout_114")
        self.label_102 = QLabel(self.widget_11)
        self.label_102.setObjectName("label_103")
        self.verticalLayout_114.addWidget(self.label_102)
        self.listView_5 = QListView(self.widget_11)
        self.listView_5.setObjectName("listView_5")
        self.verticalLayout_114.addWidget(self.listView_5)
        self.horizontalLayout_23.addLayout(self.verticalLayout_114)
        self.gridLayout_2.addLayout(self.horizontalLayout_23 )
        # self.gridLayout_2.setStretch(3, 1)
        
        self.uploadPushButton.setText("Upload Image")
        self.removeProgramsButton.setText("Remove")
        self.addProgramsButton.setText("Add")
        self.label_102.setText("Department")
        self.label_103.setText("Participants")
        self.pushButton_10.setText("Save")
        self.searchLineEdit.setPlaceholderText("Search")
        self.titleLineText.setPlaceholderText("Input program`s title here ...")
        self.subtitleLineText.setPlaceholderText("Input program`s discription here ...")
        self.subtitleLineText.setAcceptRichText(True) 
        self.locationLineText.setPlaceholderText("Input program`s location here ...")
        self.fontSizeComboBox.addItems(self.suggestionFontSizes)
        self.fontSizeComboBox.setCurrentText("13")

        self.updateDisplayProgramsList(self.programsData)
        self.searchLineEdit.textChanged.connect(self.handleSearchChanged)
        self.programsListWidget.currentRowChanged.connect(self.handleSearchReturned)
        self.fontComboBox.currentFontChanged.connect(self.handleFontChanged)
        self.fontSizeComboBox.currentTextChanged.connect(self.handleFontSizeChanged)
        self.boldAction.triggered.connect(self.handleBoldAction)
        self.italicAction.triggered.connect(self.handleItalicAction)
        self.underlineAction.triggered.connect(self.handleUnderlineAction)
        self.bulletAction.triggered.connect(self.handleBulletClicked)
        self.linkAction.triggered.connect(self.handleLinkClicked)
        self.leftAlignAction.triggered.connect(self.handleLeftAlignClicked)
        self.centerAlignAction.triggered.connect(self.handleCenterAlignClicked)
        self.rightAlignAction.triggered.connect(self.handleRightAlignClicked)
        self.colorAction.triggered.connect(self.handleTextColorClicked)
        self.uploadPushButton.pressed.connect(self.handleUploadImageClicked)
        
        
       
        
    def handleSearchChanged(self,text):
        self.filterPrograms(text)
        
    def filterPrograms(self, filterText):
        text = filterText
        filterProgramsData = self.programsData
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
        self.handleSearchReturned()
        
    def updateDepartmentsList(self, data):
        model = QStandardItemModel(self.listView_5)
        for department in data:
            item = QStandardItem(department)
            item.setCheckable(True)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            model.appendRow(item)
        self.listView_5.setModel(model)
        delegate = CheckBoxDelegate(self.listView_5)
        self.listView_5.setItemDelegate(delegate)
        
    def updateParticipantsList(self, data):
        model = QStandardItemModel(self.listWidget_24)
        for user in data:
            # TODO
            item = QStandardItem(f"{user}")
            item.setCheckable(True)
            item.setCheckState(2)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            model.appendRow(item)
        self.listWidget_24.setModel(model)
        delegate = CheckBoxDelegate(self.listWidget_24)
        self.listWidget_24.setItemDelegate(delegate)
    
    def handleTextColorClicked(self):
        color = QColorDialog.getColor()
        if color.isValid():
            charFormat = self.subtitleLineText.currentCharFormat()
            charFormat.setForeground(color)
            self.subtitleLineText.mergeCurrentCharFormat(charFormat)
            
    def handleBulletClicked(self):
        cursor = self.subtitleLineText.textCursor()
        listFormat = QTextListFormat()

        if cursor.currentList():
            listFormat.setStyle(Qt.NoPen)
        else:
            listFormat.setStyle(QTextListFormat.ListDisc)

        cursor.beginEditBlock()
        blockFormat = cursor.blockFormat()
        blockFormat.setIndent(0)
        cursor.setBlockFormat(blockFormat)
        cursor.createList(listFormat)
        cursor.endEditBlock()

    def handleLinkClicked(self):
        link, ok = QInputDialog.getText(self, "Insert Link", "Enter URL:")

        if ok and link:
            cursor = self.subtitleLineText.textCursor()
            url = QUrl(link)
            cursor.insertHtml(f'<a href="{url.toString()}">{url.toString()}</a>')

    def handleLeftAlignClicked(self):
        self.subtitleLineText.setAlignment(Qt.AlignLeft)

    def handleCenterAlignClicked(self):
        self.subtitleLineText.setAlignment(Qt.AlignCenter)

    def handleRightAlignClicked(self):
        self.subtitleLineText.setAlignment(Qt.AlignRight)

    
    def handleFontChanged(self, font):
        self.subtitleLineText.setCurrentFont(font)

    def handleFontSizeChanged(self, fontSize):
        try:
            pointSize = float(fontSize)
            if pointSize > 0:
                self.subtitleLineText.setFontPointSize(pointSize)
        except ValueError:
            pass

    def handleBoldAction(self):
        font = self.subtitleLineText.currentFont()
        font.setBold(not font.bold())
        
        format = QTextCharFormat()
        format.setFont(font)
        
        cursor = self.subtitleLineText.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
            
        cursor.mergeCharFormat(format)
        self.subtitleLineText.mergeCurrentCharFormat(format)

    def handleItalicAction(self):
        italic = self.subtitleLineText.fontItalic()
        self.subtitleLineText.setFontItalic(not italic)

    def handleUnderlineAction(self):
        underline = self.subtitleLineText.fontUnderline()
        self.subtitleLineText.setFontUnderline(not underline)
        
    def handleUploadImageClicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.gif)")
        if filename:
            image = QPixmap(filename)
            scaledImage = image.scaledToWidth(500, mode=Qt.SmoothTransformation)
            self.graphicsView_12.setPixmap(scaledImage)

    
    def updateDisplayProgramsList(self, data):
        self.programsListWidget.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                title = "Unknown"
                if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                    title = item['title']
                listItem = QListWidgetItem(title)
                listItem.setData(Qt.UserRole, item)
                self.programsListWidget.addItem(listItem)
            pass
        pass
        
        
    def handleSearchReturned(self, index = 0):
        if self.programsListWidget.count() > 0 and index >= 0:
            data = self.programsListWidget.item(index).data(Qt.UserRole)
            if(isinstance(data, object)):
                self.programsListWidget.setCurrentRow(index)
                self.updateDisplayInformationView(data)
    
    def updateDisplayInformationView(self, data):
        
        title = ""
        imageUrl = ""
        subtitle = ""
        dateTime = QDate.currentDate()
        location = ""
        enrolledUsers = []
        
        
        if isinstance(data, object) and data != None:
            item = data
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
                datetime_obj = datetime.datetime.fromtimestamp(timestamp)
                dateTime = QDateTime(datetime_obj.date(), datetime_obj.time())
            if 'location' in item and isinstance(item['location'], str) and item['location'] != None:
                location = item['location']
                pass
            if 'users' in item and isinstance(item['users'], str) and item['users'] != None:
                parsed_json = json.loads(item['users'])
                if 'users' in parsed_json and isinstance(parsed_json['users'], list) and parsed_json['users'] != None:
                    enrolledUsers = parsed_json['users']
                pass
                
            self.titleLineText.setText(title)
            self.subtitleLineText.setText(subtitle)
            scene = QGraphicsScene()
            image = QImage()
            try:
                image.loadFromData(requests.get(imageUrl).content)
            except:
                pass    
            
            scaledImage = image.scaledToWidth(500, mode=Qt.SmoothTransformation)
            self.graphicsView_12.setPixmap(QPixmap(scaledImage))
            self.subtitleLineText.setText(subtitle)
            self.locationLineText.setText(location)
            self.updateParticipantsList(enrolledUsers)
            # TODO
            #self.updateDepartmentsList()
            
            try:
                self.dateTimeEdit.setDateTime(dateTime)
            except:
                pass
            pass
        pass
    
    
class CheckBoxDelegate(QStyledItemDelegate):
        def initStyleOption(self, option, index):
            super().initStyleOption(option, index)
            option.features |= QStyleOptionViewItem.HasCheckIndicator