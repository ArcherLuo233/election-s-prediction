from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from .boxUI import Ui_Form


class ConditionBox(QWidget):
    delete_clicked = pyqtSignal()
    field_changed = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fields = []
        self.ui.btn_delete.clicked.connect(self.delete_clicked)
        self.ui.comboBox.currentTextChanged.connect(self.field_changed)
        height = self.ui.btn_delete.size().height()
        self.ui.comboBox.setFixedHeight(height)
        self.ui.lineEdit.setFixedHeight(height)

    @property
    def current_field(self):
        return self.ui.comboBox.currentText()

    def set_fields(self, fields: list):
        #姓名字段设为默认
        if "姓名" in fields:
            temp_index = fields.index("姓名")
            temp = fields[temp_index]
            fields[temp_index] = fields[0]
            fields[0] = temp  

        self.fields = fields
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(fields)

    def add_fields(self, fields):
        if isinstance(fields, str):
            fields = [fields]
        for field in fields:
            self.fields.append(field)
            self.ui.comboBox.addItem(field)

    def del_fields(self, fields):
        if isinstance(fields, str):
            fields = [fields]
        for field in fields:
            self.ui.comboBox.removeItem(self.fields.index(field))
            self.fields.remove(field)

    def get(self):
        return {
            'field': self.ui.comboBox.currentText(),
            'val': self.ui.lineEdit.text()
        }
