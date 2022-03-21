from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.components.customButton import CustomButton
from customWidgets.components.customCheckBox import CustomCheckBox
from customWidgets.components.customLineEdit import CustomLineEdit
from customWidgets.components.customProgressBar import CustomProgressBar
from customWidgets.windows.speedWindow import SpeedWindow
from customWidgets.windows.temperatureWindow import TemperatureWindow
from customWidgets.windows.voltageWindow import VoltageWindow


class TestCasesFrame(QFrame):

    def __init__(self, parent):
        super(TestCasesFrame, self).__init__(parent)

        # labels
        self.frameName = QLabel(self)
        self.temperatureName = QLabel(self)
        self.testcasesName = QLabel(self)
        self.voltageName = QLabel(self)
        self.speedName = QLabel(self)
        self.maxTemperatureName = QLabel(self)
        self.minTemperatureName = QLabel(self)
        self.maxVoltageName = QLabel(self)
        self.minVoltageName = QLabel(self)

        # line edits
        self.maxTemperatureLineEdit = CustomLineEdit(self)
        self.minTemperatureLineEdit = CustomLineEdit(self)
        self.maxVoltageLineEdit = CustomLineEdit(self)
        self.minVoltageLineEdit = CustomLineEdit(self)

        # buttons and progress  bar
        self.progressBar = CustomProgressBar(self)
        self.startButton = CustomButton(self, "Start")
        self.stopButton = CustomButton(self, "Stop")

        # checkboxes
        self.temperatureCheckBox = CustomCheckBox(self)
        self.voltageCheckBox = CustomCheckBox(self)
        self.speedCheckBox = CustomCheckBox(self)

        # flags
        self.temperatureWindowOn = False
        self.voltageWindowOn = False
        self.speedWindowOn = False

        # windows
        self.temperatureWindow = TemperatureWindow(parent)
        self.voltageWindow = VoltageWindow(parent)
        self.speedWindow = SpeedWindow(parent)

        # test parameters
        self.testingTime = 30  # 30 seconds

        self.setupUi()

    def setupUi(self):
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setGeometry(QRect(640, -2, 642, 500))
        self.setMinimumSize(QSize(642, 500))
        self.setMaximumSize(QSize(642, 500))
        self.setStyleSheet("""
                            QFrame {
                            background-color: #30363F;
                            border-width: 2px;
                            border-style: solid;
                            border-color: #E47900;
                            }
                           """
                           )

        # frame label name
        self.frameName.setGeometry(QRect(262, 30, 120, 30))
        self.frameName.setStyleSheet("text-align: center;"
                                     "border-style: none;"
                                     "color: rgb(181, 181, 181)")
        self.frameName.setFont(font)
        self.frameName.setText("Test control")

        # testcases label name
        self.testcasesName.setGeometry(QRect(80, 120, 100, 30))
        self.testcasesName.setStyleSheet("text-align: center;"
                                         "border-style: none;"
                                         "color: rgb(181, 181, 181)")
        self.testcasesName.setFont(font)
        self.testcasesName.setText("Test cases")

        # temperature label name
        self.temperatureName.setGeometry(QRect(110, 160, 180, 30))
        self.temperatureName.setStyleSheet("text-align: center;"
                                           "border-style: none;"
                                           "color: rgb(181, 181, 181)")
        self.temperatureName.setFont(font)
        self.temperatureName.setText("Temperature test case")

        # voltage label name
        self.voltageName.setGeometry(QRect(110, 200, 180, 30))
        self.voltageName.setStyleSheet("text-align: center;"
                                       "border-style: none;"
                                       "color: rgb(181, 181, 181)")
        self.voltageName.setFont(font)
        self.voltageName.setText("Voltage test case")

        # speed label name
        self.speedName.setGeometry(QRect(110, 240, 180, 30))
        self.speedName.setStyleSheet("text-align: center;"
                                     "border-style: none;"
                                     "color: rgb(181, 181, 181)")
        self.speedName.setFont(font)
        self.speedName.setText("Speed test case")

        # max temperature label name
        self.maxTemperatureName.setGeometry(QRect(80, 280, 80, 30))
        self.maxTemperatureName.setStyleSheet("text-align: center;"
                                              "border-style: none;"
                                              "color: rgb(181, 181, 181)")
        self.maxTemperatureName.setFont(font)
        self.maxTemperatureName.setText("Max temp")

        # min temperature label name
        self.minTemperatureName.setGeometry(QRect(180, 280, 80, 30))
        self.minTemperatureName.setStyleSheet("text-align: center;"
                                              "border-style: none;"
                                              "color: rgb(181, 181, 181)")
        self.minTemperatureName.setFont(font)
        self.minTemperatureName.setText("Min temp")

        # max voltage label name
        self.maxVoltageName.setGeometry(QRect(280, 280, 100, 30))
        self.maxVoltageName.setStyleSheet("text-align: center;"
                                          "border-style: none;"
                                          "color: rgb(181, 181, 181)")
        self.maxVoltageName.setFont(font)
        self.maxVoltageName.setText("Max voltage")

        # min voltage label name
        self.minVoltageName.setGeometry(QRect(400, 280, 100, 30))
        self.minVoltageName.setStyleSheet("text-align: center;"
                                          "border-style: none;"
                                          "color: rgb(181, 181, 181)")
        self.minVoltageName.setFont(font)
        self.minVoltageName.setText("Min voltage")

        # horizontalLine edit max temperature
        font.setPointSize(10)
        self.maxTemperatureLineEdit.setGeometry(80, 320, 80, 35)
        self.maxTemperatureLineEdit.setLineEditStyle()
        self.maxTemperatureLineEdit.setFont(font)
        self.maxTemperatureLineEdit.setText("28.0")
        font.setPointSize(14)

        # horizontalLine edit min temperature
        font.setPointSize(10)
        self.minTemperatureLineEdit.setGeometry(180, 320, 80, 35)
        self.minTemperatureLineEdit.setLineEditStyle()
        self.minTemperatureLineEdit.setFont(font)
        self.minTemperatureLineEdit.setText("5.0")
        font.setPointSize(14)

        # horizontalLine edit max voltage
        font.setPointSize(10)
        self.maxVoltageLineEdit.setGeometry(280, 320, 80, 35)
        self.maxVoltageLineEdit.setLineEditStyle()
        self.maxVoltageLineEdit.setFont(font)
        self.maxVoltageLineEdit.setText("18.0")
        font.setPointSize(14)

        # horizontalLine edit min voltage
        font.setPointSize(10)
        self.minVoltageLineEdit.setGeometry(400, 320, 80, 35)
        self.minVoltageLineEdit.setLineEditStyle()
        self.minVoltageLineEdit.setFont(font)
        self.minVoltageLineEdit.setText("8.0")
        font.setPointSize(14)

        # progress bar
        self.progressBar.setGeometry(QRect(80, 380, 480, 30))
        self.progressBar.setProgressBarStyle()
        self.progressBar.setFont(font)
        self.progressBar.updateBar(1)

        # start button
        font.setPointSize(12)
        self.startButton.setGeometry(QRect(120, 420, 150, 35))
        self.startButton.setButtonStyle(bgColor="#01BF21", borderColor="#349E45", bgColorHover="#1FEC1F",
                                        bgColorPressed="#1FEC1F")
        self.startButton.setFont(font)
        font.setPointSize(14)

        # stop button
        font.setPointSize(12)
        self.stopButton.setGeometry(QRect(370, 420, 150, 35))
        self.stopButton.setButtonStyle(bgColor="#E51616", borderColor="#903131", bgColorHover="#FF0000",
                                       bgColorPressed="#FF0000")
        self.stopButton.setFont(font)
        font.setPointSize(14)

        # temperature check box
        self.temperatureCheckBox.setGeometry(QRect(80, 160, 32, 32))
        self.temperatureCheckBox.setCheckBoxStyle()

        # voltage check box
        self.voltageCheckBox.setGeometry(QRect(80, 200, 32, 32))
        self.voltageCheckBox.setCheckBoxStyle()

        # speed check box
        self.speedCheckBox.setGeometry(QRect(80, 240, 32, 32))
        self.speedCheckBox.setCheckBoxStyle()

        # checkbox callbacks
        self.temperatureCheckBox.stateChanged.connect(lambda state: self.updateWindowFlag(state, "temperature"))
        self.voltageCheckBox.stateChanged.connect(lambda state: self.updateWindowFlag(state, "voltage"))
        self.speedCheckBox.stateChanged.connect(lambda state: self.updateWindowFlag(state, "speed"))

        # buttons callbacks
        self.startButton.clicked.connect(lambda: self.startTestButton())

    def updateWindowFlag(self, state, flagName):
        if flagName == "temperature":
            if state == 2:
                self.temperatureWindowOn = True
            else:
                self.temperatureWindowOn = False
        if flagName == "voltage":
            if state == 2:
                self.voltageWindowOn = True
            else:
                self.voltageWindowOn = False
        if flagName == "speed":
            if state == 2:
                self.speedWindowOn = True
            else:
                self.speedWindowOn = False

    def startTestButton(self):
        if self.temperatureWindowOn:
            self.temperatureWindow.show()
        if self.voltageWindowOn:
            self.voltageWindow.show()
        if self.speedWindowOn:
            self.speedWindow.show()
