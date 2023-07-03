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
import dropboxFunc


from client import Client
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class AddProgramTab(QWidget):
    def __init__(self):
        super(AddProgramTab, self).__init__()

        self.programsData = Client.getPrograms()
        self.suggestionFontSizes = ["8", "10", "13", "16", "24", "32"]
        self.departments = Client.getDepartments()
        

        self.setObjectName("AddProgramTab")
        self.horizontalLayout_19 = QHBoxLayout(self)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
    

        self.widget_8 = QWidget(self)
        self.widget_8.setObjectName("widget_8")
        self.widget_8.setMaximumWidth(250)
        self.verticalLayout_32 = QVBoxLayout(self.widget_8)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_8)
        
        self.searchLineEdit = QLineEdit(self.widget_8)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_32.addWidget(self.searchLineEdit)
        self.refreshPushButton = QPushButton(self)
        self.refreshPushButton.setObjectName("refreshPushButton")
        icon_path = os.path.join(current_dir, "Refresh_icon.svg.png")
        self.refreshPushButton.setIcon(QIcon(icon_path))
        self.horizontalLayout_32.addWidget(self.refreshPushButton)
        self.verticalLayout_32.addLayout(self.horizontalLayout_32)
        self.refreshPushButton.clicked.connect(self.refresh)
        
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
        self.gridLayout_2.addWidget(self.graphicsView_12 )
        self.graphicsView_12_url =QLabel(self.widget_11)
        self.graphicsView_12_url.setObjectName("graphicsView_12_url")
        self.gridLayout_2.addWidget(self.graphicsView_12_url )
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
        # self.pushButton_10.setEnabled(True)
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
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.listView_5.setSizePolicy(size_policy)

        # Set a minimum height for the listView_5
        self.listView_5.setMinimumHeight(200) 
        
        self.verticalLayout_114.addWidget(self.listView_5)
        self.horizontalLayout_23.addLayout(self.verticalLayout_114)
        self.gridLayout_2.addLayout(self.horizontalLayout_23 )
        self.amountLineEdit = QLineEdit(self.widget_11)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.gridLayout_2.addWidget(self.amountLineEdit)
        self.totalCost = QLabel(self.widget_11)
        self.totalCost.setObjectName("totalCost")
        self.gridLayout_2.addWidget(self.totalCost)
        self.requestForPayment = QPushButton(self.widget_11)
        self.requestForPayment.setObjectName("requestForPayment")
        self.gridLayout_2.addWidget(self.requestForPayment)
        # self.gridLayout_2.setStretch(3, 1)
        
        self.uploadPushButton.setText("Upload Image")
        self.removeProgramsButton.setText("Remove")
        self.addProgramsButton.setText("Add")
        self.label_102.setText("Department")
        self.label_103.setText("Participants")
        self.pushButton_10.setText("Save")
        # self.pushButton_10.setEnabled(False)
        
        self.searchLineEdit.setPlaceholderText("Search")
        self.titleLineText.setPlaceholderText("Input program`s title here ...")
        self.subtitleLineText.setPlaceholderText("Input program`s discription here ...")
        self.subtitleLineText.setAcceptRichText(True) 
        self.locationLineText.setPlaceholderText("Input program`s location here ...")
        self.fontSizeComboBox.addItems(self.suggestionFontSizes)
        self.fontSizeComboBox.setCurrentText("13")
        self.amountLineEdit.setPlaceholderText("Insert cost per participants")
        self.totalCost.setText("Amount total: $")
        self.requestForPayment.setText("Request Payment")
        
        double_validator = QDoubleValidator()
        double_validator.setNotation(QDoubleValidator.StandardNotation)  # Allow standard floating-point notation
        double_validator.setDecimals(2)  # Specify the number of decimal places allowed

        # Set the validator for the amountLineEdit
        self.amountLineEdit.setValidator(double_validator)

        self.updateDisplayProgramsList(self.programsData)
        self.searchLineEdit.textChanged.connect(self.handleSearchChanged)
        self.searchLineEdit.returnPressed.connect(self.handleSearchReturned)
        
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
        self.pushButton_10.pressed.connect(self.saveChangeCurrentProgram)
        self.addProgramsButton.pressed.connect(self.addNewProgramHandler)
        self.removeProgramsButton.pressed.connect(self.removeProgramHandler)
        self.amountLineEdit.textChanged.connect(self.onAmountChanged)
        
    def refresh(self):
        self.programsData = Client.getPrograms()
        self.updateDisplayProgramsList( self.programsData)
        self.filterPrograms(self.searchLineEdit.text())
        
    def onAmountChanged(self):
        # Retrieve the new amount value from the line edit
        text = self.amountLineEdit.text()
        amount = 0
        if text != "":
            amount = float(text)
            
        new_amount = amount

        # Calculate the total cost
        total_cost = new_amount * len(self.getCheckedItemsId(self.listWidget_24))  # Assuming enrolledUsers is a list of enrolled users

        self.totalCost.setText(str(total_cost))
        
    def saveChangeCurrentProgram(self):
        title = self.titleLineText.text()
        imageUrl = self.graphicsView_12_url.text()
        description = self.subtitleLineText.toHtml()
        datetimeValue = self.dateTimeEdit.dateTime()
        timestamp = datetimeValue.toSecsSinceEpoch()
        location = self.locationLineText.text()
        id = self.programsListWidget.currentItem().data(Qt.UserRole)['id']
        departments = {"departments": self.getCheckedItemsId(self.listView_5) }
        json_departments = json.dumps(departments)
        originalUsers = self.programsListWidget.currentItem().data(Qt.UserRole).get('parsedUsers', [])
        users = {"users": self.getCheckedItemsId(self.listWidget_24)}
        json_users = json.dumps(users)
        
        originalUserSet = set(originalUsers)
        addedUsersSet = set(users["users"])
        missingUsersSet = originalUserSet - addedUsersSet
        addedUsersSet = addedUsersSet - originalUserSet

        missingUsers = list(missingUsersSet)
        addedUsers = list(addedUsersSet)
        
        amount = float(self.amountLineEdit.text() or 0)
        
        if imageUrl != "":
            imageUrl = dropboxFunc.uploadImage(imageUrl)

        formData = {
            "title": title,
            "imageUrl": imageUrl,
            "description": description,
            "timestamp": timestamp,
            "location": location,
            "departments": json_departments,
            "users": json_users,
            "cost": amount
        }
        result =  Client.updateProgram(id,formData)
        if result == True:
            if len(missingUsers) > 0:
                self.updateUsersApprovement({"id":id ,"approveStatus":0}, missingUsers)
            if len(addedUsers) > 0:
                self.updateUsersApprovement({"id":id ,"approveStatus":4}, addedUsers)
            previousIndex = self.programsListWidget.currentRow()
            self.updateDisplayProgramsList(Client.getPrograms())
            self.programsListWidget.setCurrentRow(previousIndex)
            #changes 
            self.notifyUser(id) 
            self.notifyFinance(id)


            
    def updateUsersApprovement(self, data, usersIds):
        users = Client.getUsersByIds(usersIds)
        for user in users:
            userNewApprovements = self.getClientApprovements(user)
            newApprovements = Client.getUserApprovementByIds(   userNewApprovements)
            found_items = [a for a in newApprovements if a["programId"]== data['id']]
            if len(found_items) > 0:
                approval_data = {
                    "id": int(found_items[0]["id"]),
                    "approveStatus": data["approveStatus"]  # Set the status to 2 for Approved
                }
                Client.updateApproval(approval_data)
                pass
            else:
                approveId = Client.addNewApproval({"userId":user["id"], "programId":data['id'], 'approveStatus': 4})
                newApprovements.append(approveId)
                result = Client.updateUserProgramApprovements(self.currentUser['id'], newApprovements)
        
    def getClientApprovements(self, userData):
        approvements = []
        #TODO
        userData = userData
        self.currentUser = Client.getUser(userData["id"])
        if 'approvementIds' in self.currentUser and isinstance(self.currentUser ['approvementIds'], str) and self.currentUser ['approvementIds'] != '':
            parsed = json.loads(self.currentUser ['approvementIds'])
            if 'approvementIds' in parsed and isinstance(parsed ['approvementIds'], list) and parsed['approvementIds'] is not None:
                approvements = parsed['approvementIds']
                    
        return approvements
        
    def addNewProgramHandler(self):
        result = self.addNewProgramDialog()
        if result != None:
            newId = Client.addNewProgram(result)
            self.updateDisplayProgramsList(Client.getPrograms())
            self.pushButton_10.setEnabled(False)
            
            pass
        
    def removeProgramHandler(self):
        item = None
        try:
            item = self.programsListWidget.currentItem().data(Qt.UserRole)
        except:
            print('An exception occurred')
        if item != None:
            result = self.removeProgramDialog(f'{item["title"]}')
            if result == True:
                result =  Client.removeProgram(item["id"],{"enable":0})
                self.updateDisplayProgramsList(Client.getPrograms())
                self.pushButton_10.setEnabled(False)
                pass
        
    def removeProgramDialog(self, title):
        # Show a confirmation dialog
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirm Removal")
        confirm_dialog.setText("Are you sure you want to remove this program?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)
        
        # Execute the dialog and check the user's response
        response = confirm_dialog.exec()
        
        if response == QMessageBox.Yes:
            # User confirmed the removal
            # Add your removal logic here
            return True
        
        return False
       
        
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
        self.pushButton_10.setEnabled(False)
        
    def updateDepartmentsList(self, departmentData, enrolledUsers, enable = True):
        data = self.departments
        model = QStandardItemModel(self.listView_5)
        if data is None:
            return
        for index, department in enumerate(data):
            department_name = department.get('name')
            if department_name:
                item = QStandardItem(department_name)
                if enable:
                    item.setCheckable(True)
                    item.setEnabled(True)
                else :
                    item.setCheckable(False)
                    item.setEnabled(False)
                    
                    
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                item.setData(department, Qt.UserRole)
                model.appendRow(item)
                # Check if department['id'] is in departmentData
                if department['id'] in departmentData:
                    item.setCheckState(Qt.Checked)
        self.listView_5.setModel(model)
        delegate = CheckBoxDelegate(self.listView_5)
        self.listView_5.setItemDelegate(delegate)
        model.itemChanged.connect(lambda item: self.handleDepartmentItemChecked(item, enrolledUsers))

    
    # def getEnrolledUsers(self, item):
    #     enrolledUsers = []
    #     if 'users' in item and isinstance( item ['users'], str) and item ['users'] is not '':
    #         parsed = json.loads( item ['users'])
    #         if 'users' in parsed and isinstance(parsed ['users'], list) and parsed['users'] is not None:
    #             enrolledUsers = parsed['users']
                

    def updateEnrolledUsersList(self, enrolledUsers, oriUsers):
        
        self.updateParticipantsList( usersIds=oriUsers, usersWithDetails=enrolledUsers,)



                
    def handleDepartmentItemChecked(self, item, enrolledUsers):
         
        users = Client.getUsersByDepartments(self.getCheckedItemsId(self.listView_5))
        if isinstance(users, list):
            self.updateEnrolledUsersList(users, enrolledUsers)    
            self.onAmountChanged()
          
        pass

    def getCheckedItemsId(self, listview):
        # Retrieve the index of the checked item
        checked_items = []
        model = listview.model()
        for index in range(model.rowCount()):
            model_item = model.item(index)
            if model_item.checkState() == Qt.Checked:
                checked_items.append(model_item.data(Qt.UserRole)['id'])
                # checked_items.append(index)
        print(checked_items)
        return checked_items

        # Call your desired function with the checked item indices
        # your_function(checked_items)
        
    def updateParticipantsList(self, usersIds=None, usersWithDetails=None, enable =True):
            data = []

            # Add users from usersIds
            if usersIds is not None and isinstance(usersIds, list):
                data.extend(Client.getUsersByIds(usersIds))

            # Add remaining users from usersWithDetails
            if usersWithDetails is not None and isinstance(usersWithDetails, list):
                for user in usersWithDetails:
                    userId = user.get('id')
                    if userId not in [dataUser.get('id') for dataUser in data]:
                        data.append(user)

            model = QStandardItemModel(self.listWidget_24)
            model.itemChanged.connect(self.onAmountChanged)

            for user in data:
                username = user.get('username', 'Unknown')
                departmentId = user.get('departmentId')

                departmentName = 'Unknown'
                if departmentId is not None:
                    department = next((dept for dept in self.departments if dept['id'] == departmentId), None)
                    if department:
                        departmentName = department['name']

                item = QStandardItem(f"{username} - {departmentName}")
                if enable:
                    item.setEnabled(True)
                    item.setCheckable(True)
                else :
                    item.setEnabled(False)
                    item.setCheckable(False)
                item.setCheckState(Qt.Checked)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                if departmentId is not None:
                    item.setData(user, Qt.UserRole)
                    


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
            self.graphicsView_12_url.setText(filename)

    
    def updateDisplayProgramsList(self, data):
        self.programsListWidget.clear()
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                title = "Unknown"
                if 'title' in item and isinstance(item['title'], str) and item['title'] != None:
                    title = item['title']
                
                if 'users' in item and isinstance(item ['users'], str) and item['users'] != '':
                    parsed = json.loads(item ['users'])
                    if 'users' in parsed and isinstance(parsed ['users'], list) and parsed['users'] != None:
                        parsedUsers = parsed['users']
                        
                        item['parsedUsers'] = parsedUsers
                
                listItem = QListWidgetItem(title)
                listItem.setData(Qt.UserRole, item)
                self.programsListWidget.addItem(listItem)
            pass
        pass
        
        
    def handleSearchReturned(self, index = None):
        if index != None:
            self.pushButton_10.setEnabled(True)
        else:
            index = 0
        if self.programsListWidget.count() > 0 and index >= 0:
            data = self.programsListWidget.item(index).data(Qt.UserRole)
            if(isinstance(data, object)):
                self.programsListWidget.setCurrentRow(index)
                self.updateDisplayInformationView(data)
    
    def updateDisplayInformationView(self, data):
        
        title = ""
        imageUrl = ""
        subtitle = ""
        dateTime = QDateTime.currentDateTime()
        location = ""
        enrolledUsers = []
        departments = []
        cost = ""
        digitCost = 0
        enableEditUserDept = True
        
        
        
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
            if 'timestamp' in item and isinstance(item['timestamp'], int) and item['timestamp'] != 0:
                timestamp = item['timestamp']
                datetime_obj = datetime.datetime.fromtimestamp(timestamp)
                dateTime = QDateTime(datetime_obj.date(), datetime_obj.time())
            if 'location' in item and isinstance(item['location'], str) and item['location'] != None:
                location = item['location']
                pass
            if 'cost' in item and isinstance(item['cost'], float) and item['cost'] != None:
                digitCost = item['cost']
                cost = "{:.2f}".format(item['cost'])
                pass
            if 'users' in item and isinstance(item['users'], str) and item['users'] != None:
                parsed_json = {}
                try:
                    parsed_json = json.loads(item['users'])
                except:
                    pass
                if 'users' in parsed_json and isinstance(parsed_json['users'], list) and parsed_json['users'] != None:
                    enrolledUsers = parsed_json['users']
                pass
            if 'departments' in item and isinstance(item['departments'], str) and item['departments'] != None:
                parsed_json = {}
                try:
                    parsed_json = json.loads(item['departments'])
                except:
                    pass
                if 'departments' in parsed_json and isinstance(parsed_json['departments'], list) and parsed_json['departments'] != None:
                    departments = parsed_json['departments']
                pass
            if 'paymentStatus' in item and isinstance(item['paymentStatus'], int) :
                if  item['paymentStatus']  == 0:
                    enableEditUserDept = True
                    self.requestForPayment.setEnabled(True)
                    self.requestForPayment.setText("Request Payment")
                    self.amountLineEdit.setDisabled(False)
                    pass
                elif  item['paymentStatus']  == 1:
                    enableEditUserDept = False
                    self.requestForPayment.setEnabled(False)
                    self.requestForPayment.setText("Program payment is pending")
                    self.amountLineEdit.setDisabled(True)
                    pass
                elif  item['paymentStatus']  == 2:
                    enableEditUserDept = False
                    self.requestForPayment.setEnabled(False)
                    self.requestForPayment.setText("Program payment is approved")
                    self.amountLineEdit.setDisabled(True)
                    pass
                elif  item['paymentStatus']  == 3:
                    enableEditUserDept = True
                    self.requestForPayment.setEnabled(True)
                    self.requestForPayment.setText("Program payment is denied, retry")
                    self.amountLineEdit.setDisabled(False)
                    pass
                pass

                
            self.titleLineText.setText(title)
            self.subtitleLineText.setText(subtitle)
            image = QImage()
            try:
                image.loadFromData(requests.get(imageUrl).content)
            except:
                pass    
            
            scaledImage = image.scaledToWidth(500, mode=Qt.SmoothTransformation)
            self.graphicsView_12.setPixmap(QPixmap(scaledImage))
            self.graphicsView_12_url.setText(imageUrl)
            self.subtitleLineText.setText(subtitle)
            self.locationLineText.setText(location)
            self.updateParticipantsList(usersIds= enrolledUsers ,enable = enableEditUserDept )
            self.updateDepartmentsList(departments, enrolledUsers,enable =enableEditUserDept)
            self.label_103.setText(f"Participants ({len(enrolledUsers)})")
            self.amountLineEdit.setText(f"{cost}")
            self.totalCost.setText( f"{( digitCost * len(enrolledUsers))}")
            self.requestForPayment.pressed.connect(self.handleRequestForPayment)
            
            
            
            try:
                self.dateTimeEdit.setDateTime(dateTime)
            except:
                pass
            pass
        pass
    def handleRequestForPayment(self):
        self.requestForPayment.setEnabled(False)
        current_item = self.programsListWidget.currentItem()
    
        # Check if there is a current item
        if current_item is not None:
            # Retrieve the data stored in the UserRole role
            data = current_item.data(Qt.UserRole)
            
            users = {"users": self.getCheckedItemsId(self.listWidget_24)}
            departments = {"departments": self.getCheckedItemsId(self.listView_5) }
            json_departments = json.dumps(departments)
            json_users = json.dumps(users)
            result = Client.updateProgramPayment(data["id"], {"paymentStatus": 1, "cost": float(self.amountLineEdit.text() or 0), "users": json_users, "departments":json_departments})
            if result == True:
                self.programsData = Client.getPrograms()
                # self.updateDisplayProgramsList()
                # self.handleSearchReturned()
                previousIndex = self.programsListWidget.currentRow()
                self.updateDisplayProgramsList( self.programsData)
                self.programsListWidget.setCurrentRow(previousIndex)
            

    def notifyUser(self, programId):

        notificationData = {
            "type": 0,
            "innerType": 0,
            "programId": int(programId),
        }
        
        Client.addNewnotifications(self.getCheckedItemsId(self.listWidget_24), notificationData)

    def notifyFinance(self, programId):
        finance = Client.getUsersByDepartments([8])
        notificationData = {
            "type":0,
            "innerType":0,
            "programId": int(programId),
        }
        Client.addNewnotifications([item['id'] for item in finance], notificationData)
    
    def addNewProgramDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Add New Program")
        
        # Create layout
        layout = QVBoxLayout()
        
        # Create title label and input field
        titleLabel = QLabel("Title:")
        titleLineEdit = QLineEdit()
        
        # Add title label and input field to the layout
        layout.addWidget(titleLabel)
        layout.addWidget(titleLineEdit)
        
        # Create OK and Cancel buttons
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(dialog.accept)
        buttonBox.rejected.connect(dialog.reject)
        
        # Add button box to the layout
        layout.addWidget(buttonBox)
        
        # Set the layout for the dialog
        dialog.setLayout(layout)
        
        # Show the dialog and wait for user input
        while True:
            if dialog.exec() == QDialog.Accepted:
                # Retrieve the title value from the input field
                title = titleLineEdit.text()
                
                data = {"title": title}
                
                # Check if the title is empty
                if title.strip() == "":
                    # Show an error message and continue the loop
                    QMessageBox.warning(dialog, "Error", "Title is required. Please enter a title.")
                    continue
                
                # Perform any further processing or validation here
                
                return data
            
            return None
    
    
class CheckBoxDelegate(QStyledItemDelegate):
        def initStyleOption(self, option, index):
            super().initStyleOption(option, index)
            option.features |= QStyleOptionViewItem.HasCheckIndicator
            