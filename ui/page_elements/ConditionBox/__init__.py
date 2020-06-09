from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from .boxUI import Ui_Form


class ConditionBox(QWidget):
    delete_clicked = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_delete.clicked.connect(self.delete_clicked)
        height = self.ui.btn_delete.size().height()
        self.ui.comboBox.setFixedHeight(height)
        self.ui.lineEdit.setFixedHeight(height)

    def set_fields(self, fields: list):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(fields)

    def get(self):
        return {
            'field': self.ui.comboBox.currentText(),
            'val': self.ui.lineEdit.text()
        }
