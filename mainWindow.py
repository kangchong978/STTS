import sys
from mainWindows.accountTab import AccountTab
from mainWindows.addProgramTab import AddProgramTab
from mainWindows.approvalTab import ApprovalTab
from mainWindows.detailsTab import DetailsTab
from mainWindows.programsTab import ProgramsTab
from mainWindows.userTab import UserTab

from PyQt5 import QtWidgets, QtCore
 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(860, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 821, 551))
        self.tabWidget.setObjectName("tabWidget")
        
        
        self.tab1 = ProgramsTab()
        self.tab2 = AddProgramTab()
        # self.tab3 = DetailsTab()
        self.tab4 = ApprovalTab()
        self.tab5 = AccountTab()
        self.tab6 = UserTab()
        # self.tab7 = NotificationTab()
        
        self.tabWidget.addTab(self.tab1, "Programs")
        self.tabWidget.addTab(self.tab2, "Add Programs")
        # self.tabWidget.addTab(self.tab3, "Details")
        self.tabWidget.addTab(self.tab4, "Approvals")
        self.tabWidget.addTab(self.tab5, "Account")
        self.tabWidget.addTab(self.tab6, "Users")
        # self.tabWidget.addTab(self.tab3, "Notifications")


        self.setCentralWidget(self.tabWidget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
