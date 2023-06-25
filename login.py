import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
    app = QApplication(sys.argv)
    win = QDialog()
    vbox = QVBoxLayout()
    t1 = QLabel()
    t1.setText("Username")    
    vbox.addWidget(t1)
    nm = QLineEdit()
    vbox.addWidget(nm)
    t2 = QLabel()
    t2.setText("Password")    
    vbox.addWidget(t2)
    pw = QLineEdit()
    vbox.addWidget(pw)
    c1 = QCheckBox("Remember me")
    vbox.addWidget(c1)
    b1 = QPushButton()
    b1.setText("Login")
    b1.clicked.connect(b1_clicked)
    vbox.addWidget(b1)
    win.setLayout(vbox)
    win.setGeometry(100,100,200,100)
    win.setWindowTitle("STTS")
    win.show()
    sys.exit(app.exec_())
def b1_clicked():
    print ("Button 1 clicked")
if __name__ == '__main__':
    window()
    
 