from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QFrame

from customWidgets.components.customLineEdit import CustomLineEdit

windowStyle = """
QDialog {
    background-color: #30363F;
}
QLabel {
    text-align: center;
    border-style: none;
    color: rgb(181, 181, 181);
}
"""


class SpeedWindow(QDialog):
    def __init__(self, parent=None):
        super(SpeedWindow, self).__init__(parent)
        self.windowName = QLabel(self)
        self.horizontalLine = QFrame(self)
        self.motorSpeed = QLabel(self)
        self.lineEditSpeed = CustomLineEdit(self)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("Speed")
        self.setWindowTitle("Speed")
        self.resize(278, 193)
        self.setMinimumSize(278, 193)
        self.setMaximumSize(278, 193)
        self.setStyleSheet(windowStyle)

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.windowName.setGeometry(QRect(110, 5, 220, 25))
        self.windowName.setObjectName("windowName")
        self.windowName.setFont(font)
        self.windowName.setText("Speed")

        font.setPointSize(10)
        self.horizontalLine.setGeometry(QRect(0, 30, 291, 16))
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")

        self.lineEditSpeed.setGeometry(QRect(98, 100, 80, 30))
        self.lineEditSpeed.setObjectName("lineEditSpeed")
        self.lineEditSpeed.setReadOnly(True)
        self.lineEditSpeed.setLineEditStyle()

        self.motorSpeed.setGeometry(QRect(100, 70, 110, 20))
        self.motorSpeed.setObjectName("motorSpeed")
        self.motorSpeed.setFont(font)
        self.motorSpeed.setText("Motor Speed")
