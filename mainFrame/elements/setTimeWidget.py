from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTimeEdit
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTime
from PyQt5.Qt import QPixmap

class SetTimeWidget(QGroupBox):
    
    def __init__(self, name, unit="", defaultVal = QTime(0,0,0), widthLabel = 150, widthValue = 100, widthUnit = 70):
        super().__init__()
        
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        
        self.label = QLabel(name)
        self.mainLayout.addWidget(self.label)
        self.label.setFixedWidth(widthLabel)
    
        self.value = QTimeEdit()
        self.mainLayout.addWidget(self.value)
        self.value.setFixedWidth(widthValue)
        self.value.setTime(defaultVal)
        
        self.unit = QLabel(unit)
        self.mainLayout.addWidget(self.unit)
        self.unit.setFixedWidth(widthUnit)

        self.mainLayout.addStretch(1)