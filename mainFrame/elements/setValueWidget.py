from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDoubleSpinBox
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.Qt import QPixmap

class SetValueWidget(QGroupBox):
    
    def __init__(self, name, unit="", defaultVal = 0, minVal = 0, maxVal = 100, decimals = 2, widthLabel = 150, widthValue = 100, widthUnit = 70):
        super().__init__()
        
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet(".QGroupBox{ border: 0px solid white }")
        
        self.label = QLabel(name)
        self.mainLayout.addWidget(self.label)
        self.label.setFixedWidth(widthLabel)
    
        self.value = QDoubleSpinBox()
        self.mainLayout.addWidget(self.value)
        self.value.setFixedWidth(widthValue)
        self.value.setMaximum(maxVal)
        self.value.setMinimum(minVal)
        self.value.setValue(defaultVal)
        self.value.setDecimals(decimals)
        
        self.unit = QLabel(unit)
        self.mainLayout.addWidget(self.unit)
        self.unit.setFixedWidth(widthUnit)
        

        self.mainLayout.addStretch(1)