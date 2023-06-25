import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
import datetime
import json
 
class MainWindow(QMainWindow):
    programs = json.load(open('dummpyData.json')) ['programs']
    client = json.load(open('dummpyClientData.json')) ['client']
    mode = 0 # [0=view, 1=edit] 
    
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(800,500)
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab_widget.addTab(self.tab1, "Programs")
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.tab_widget.addTab(self.tab3, "Tab 3")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("tab demo")
        
        self.createMenuBar()

    def createMenuBar(self):
        bar = self.menuBar()
        edit = bar.addMenu("Edit") 
        activities = edit.addMenu("Activities")
        editMode = QAction("Edit mode",self)
        editMode.setData({'action':'editMode'})
        activities.addAction(editMode)
        saveEdit = QAction("Save",self)
        saveEdit.setShortcut("Ctrl+S")
        saveEdit.setData({'action':'saveEdit'})
        activities.addAction(saveEdit)
        edit.triggered[QAction].connect(self.processtrigger)
        
        
        if(self.client['rolePrivilege'] > 0):
            edit.setDisabled(False)
        else:
            edit.setDisabled(True)
            
    def processtrigger(self,q):
        data = q.data()
        if data['action'] == 'editMode':
            self.edit = True

        elif data['action'] == 'saveEdit':
            self.edit = False    
        self.handleFlagChange(self.edit)
        
        # if flag:
        #     # Recreate Tab 1 UI in edit mode
        #     self.tab_widget.removeTab(0)
        #     self.tab1UI(edit_mode=True)
        # else:
        #     # Recreate Tab 1 UI in view mode
        #     self.tab_widget.removeTab(0)
        #     self.tab1UI(edit_mode=False)
         
        

    def tab1UI(self):
        mainVbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.searchLineEdit = QLineEdit()
        self.searchLineEdit.setPlaceholderText("🔎 Search programs")
        self.searchLineEdit.textChanged.connect(self.handleSearchChanged)
        self.searchLineEdit.returnPressed.connect(self.handleSearchReturned)
        
        mainVbox.addWidget(self.searchLineEdit)
        
        self.leftlist = QListWidget()
        for index, item in enumerate(self.programs):
            listItem = QListWidgetItem()
            listItem.setData(Qt.UserRole, item)
            listItem.setText(f"{datetime.datetime.fromtimestamp(item['timestamp']).strftime('%d %b %y')} | {item['title']}")
            self.leftlist.addItem(listItem)
        self.leftlist.currentRowChanged.connect(self.display)
        topright = QFrame()
        topright.setFrameShape(QFrame.StyledPanel)
        layout = QVBoxLayout(topright)
        self.label = QLabel(topright)
        self.label.setWordWrap(True)
        self.label.setStyleSheet('QLabel{font-size:24px;font-weight:bold;}')
        self.label2 = QLabel(topright) 
        self.label2.setWordWrap(True)
        self.label3 = QLabel(topright) 

        self.label4 = QLabel(topright) 
        self.label5 = QLabel(topright) 
        self.label6 = QLabel(topright) 
        self.label7 = QLabel(topright) 
        
        self.b1 = QPushButton(topright)
        
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        layout.addWidget(self.label6)
        layout.addWidget(self.label7)
        layout.addStretch()
        
        layout.addWidget(self.b1)
        
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.leftlist)
        splitter1.addWidget(topright)
        splitter1.setSizes([150, 500])
        hbox.addWidget(splitter1)
        mainVbox.addLayout(hbox)
        self.tab1.setLayout(mainVbox)
        

        
    def handleSearchChanged(self,text):
       self.filterPrograms(text)
        
    def filterPrograms(self, text):
        if text != '':
            self.leftlist.clear()

            for program in self.programs:
                if isinstance(program, dict) and 'title' in program and isinstance(program['title'], str):
                    if text.lower() in program['title'].lower():
                        listItem = QListWidgetItem()
                        listItem.setData(Qt.UserRole, program)
                        listItem.setText(f"{datetime.datetime.fromtimestamp(program['timestamp']).strftime('%d %b %y')} | {program['title']}")
                        self.leftlist.addItem(listItem)


        else:
            self.leftlist.clear()
            for index, item in enumerate(self.programs):
                listItem = QListWidgetItem()
                listItem.setData(Qt.UserRole, item)
                listItem.setText(f"{datetime.datetime.fromtimestamp(item['timestamp']).strftime('%d %b %y')} | {item['title']}")
                self.leftlist.addItem(listItem)
            
            
    def handleSearchReturned(self):
        if self.leftlist.count() > 0:
            pid = self.leftlist.item(0).data(Qt.UserRole)['pid']
            i = -1
            for index, obj in enumerate(self.programs):
                if isinstance(obj, dict) and 'pid' in obj and obj['pid'] == pid:
                    i = index
                    
            if(i>=0):
                self.display(i)

         
        
    def display(self, i):
        self.label.setText(f"{self.programs[i]['title']}")
        self.label2.setText(f"{self.programs[i]['description']}")
        image = QImage()
        image.loadFromData(requests.get(self.programs[i]['imageUrl']).content)
        scaledImage = image.scaledToWidth(500, mode=Qt.SmoothTransformation)
        self.label3.setPixmap(QPixmap(scaledImage))
        self.label4.setText(f"📍 {self.programs[i]['venue']}")
        self.label5.setText(f"🕒 {datetime.datetime.fromtimestamp(self.programs[i]['timestamp']).strftime('%d %B %Y %H:%M')}")
        enrolStatus ='⚫️ Unknown'
        enrolButton = {'text':'Unvailable', 'style':''}
        
        if self.programs[i]['enrollStatusCode'] == 0:
            enrolStatus = '🟩 Available'
            enrolButton ={'text':'Enroll now', 'style':'color: white; background-color: #047DD9'} 
        elif self.programs[i]['enrollStatusCode'] == 1:
            enrolStatus = '🟨 Pending verification'
            enrolButton ={'text':'Cancel enrollment', 'style':'color: white; background-color: #D9D8D4'} 
        elif self.programs[i]['enrollStatusCode'] == 2:
            enrolStatus = '🟦 Enrolled'
            enrolButton ={'text':'Cancel enrollment', 'style':'color: white; background-color: #D9D8D4'} 

          
        else:
          pass 
        self.label6.setText(enrolStatus)
        self.label7.setText(f"🫂 {len(self.programs[i]['participances'])}")
        self.b1.setText(f"{enrolButton['text']}") 
        self.b1.setStyleSheet(f"{enrolButton['style']}")

        
    def tab2UI(self):
       layout = QFormLayout()
       sex = QHBoxLayout()
       sex.addWidget(QRadioButton("Male"))
       sex.addWidget(QRadioButton("Female"))
       layout.addRow(QLabel("Sex"),sex)
       layout.addRow("Date of Birth",QLineEdit())
       self.tab2.setLayout(layout)
    def tab3UI(self):
       layout = QHBoxLayout()
       layout.addWidget(QLabel("subjects"))
       layout.addWidget(QCheckBox("Physics"))
       layout.addWidget(QCheckBox("Maths"))
       self.tab3.setLayout(layout)
def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()