from PyQt5.QtWidgets import *
from typing import Union

from .NavigateField import NavigateField
from .NavigateLabel import NavigateLabel
from libs.LinkManager import link_manager


class NavigateMenu(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 20, 0, 0)
        layout.setSpacing(20)
        self.setLayout(layout)
        self.fields: [NavigateField] = []
        self.checked_label: Union[None, NavigateLabel] = None

    def addField(self, title: str, alias: str, menu: [tuple]):
        field = NavigateField(title, alias)
        field.ui.label_title.linkActivated.connect(link_manager.activate)
        field.ui.label_title.linkActivated.connect(self.labelClicked)
        for text, alias in menu:
            label = field.appendMenu(text, alias)
            label.linkActivated.connect(self.labelClicked)
        self.fields.append(field)
        self.layout().addWidget(field)

    def labelClicked(self):
        if self.checked_label:
            self.checked_label.setChecked(False)
        self.sender().setChecked(True)
        self.checked_label = self.sender()
