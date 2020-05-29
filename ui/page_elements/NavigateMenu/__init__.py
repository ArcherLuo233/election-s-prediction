from PyQt5.QtWidgets import *
from typing import Union

from .NavigateField import NavigateField
from .NavigateLabel import NavigateLabel


class NavigateMenu(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.setLayout(QVBoxLayout())
        self.fields: [NavigateField] = []
        self.checked_label: Union[None, NavigateLabel] = None

    def addField(self, title: str, alias: str, menu: [tuple], callback):
        field = NavigateField(title, alias)
        field.ui.label_title.linkActivated.connect(callback)
        field.ui.label_title.linkActivated.connect(self.labelClicked)
        for text, alias in menu:
            label = field.appendMenu(text, alias, callback)
            label.linkActivated.connect(self.labelClicked)
        self.fields.append(field)
        self.layout().addWidget(field)

    def labelClicked(self):
        if self.checked_label:
            self.checked_label.setChecked(False)
        self.sender().setChecked(True)
        self.checked_label = self.sender()
        self.adjustSize()
