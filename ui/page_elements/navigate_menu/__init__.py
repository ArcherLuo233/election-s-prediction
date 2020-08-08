from typing import Union

from PyQt5.QtWidgets import QVBoxLayout, QWidget

from libs.link_manager import link_manager

from .NavigateField import NavigateField
from .NavigateLabel import NavigateLabel


class NavigateMenu(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 20, 0, 0)
        layout.setSpacing(20)
        self.setLayout(layout)
        self.fields: [NavigateField] = []
        self.checked_label: Union[None, NavigateLabel] = None

    def add_field(self, title: str, alias: str, menu: [tuple]):
        field = NavigateField(title, alias)
        field.ui.label_title.linkActivated.connect(link_manager.activate)
        field.ui.label_title.linkActivated.connect(self.labelClicked)
        for text, alias in menu:
            label = field.append_menu(text, alias)
            label.linkActivated.connect(self.labelClicked)
        self.fields.append(field)
        self.layout().addWidget(field)

    def clear_fields(self):
        self.checked_label = None
        for i in self.fields:
            i.deleteLater()
        self.fields = []

    def labelClicked(self):
        if self.checked_label:
            self.checked_label.setChecked(False)
        self.sender().setChecked(True)
        self.checked_label = self.sender()
