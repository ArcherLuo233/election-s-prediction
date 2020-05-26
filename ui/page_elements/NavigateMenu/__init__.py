from PyQt5.QtWidgets import *
from typing import Union

from .NavigateField import NavigateField, NavigateLabel


class NavigateMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout(QVBoxLayout())
        self.fields: [NavigateField] = []
        self.checked_label: Union[None, NavigateLabel] = None

    def addField(self, title: str, menu: [tuple]):
        field = NavigateField(title)
        for i, j in menu:
            label = field.appendMenu(i, j)
            label.linkActivated.connect(self.labelClicked)
        self.fields.append(field)
        self.layout().addWidget(field)

    def labelClicked(self):
        if self.checked_label:
            self.checked_label.setChecked(False)
        self.sender().setChecked(True)
        self.checked_label = self.sender()
        self.adjustSize()
