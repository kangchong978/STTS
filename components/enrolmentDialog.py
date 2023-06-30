import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class EnrolmentDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, type= 0, programName= ""):
        super(EnrolmentDialog, self).__init__(parent)
        
        if type == 0:
            self.setWindowTitle("Enroll comfirmation")
        elif type == 1:
            self.setWindowTitle("Cancel comfirmation")
            
        self.resize(242, 114)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label")
        self.verticalLayout.addWidget(self.label2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        
        if type == 0:
            self.label.setText("Are you want to enroll to:")
        elif type == 1:
            self.label.setText("Are you want to cancel to:")
            
        self.label2.setText(f"{programName}")
        
        self.buttonBox.accepted.connect(self.accept) # type: ignore
        self.buttonBox.rejected.connect(self.reject) # type: ignore
        
        
    