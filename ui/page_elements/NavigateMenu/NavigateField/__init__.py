from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPalette, QPixmap

from ui.page_elements.NavigateMenu.NavigateLabel import NavigateLabel

from .NavigateFieldUI import Ui_Form
from libs.LinkManager import link_manager


class NavigateField(QWidget):
    def __init__(self, title: str, alias: str = ""):
        QWidget.__init__(self)
        self.menu_labels: [NavigateLabel] = []
        self.is_hide: bool = True
        self.title = title
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label_title.setTitle(title, alias)
        self.ui.label_title.checkChanged.connect(self.refreshUI)

        self.ui.label_icon.setPixmap(QPixmap("./static/svg/list.svg").scaled(30, 30))
        self.ui.label_icon.setAutoFillBackground(True)

        self.ui.label_switch.setAutoFillBackground(True)
        self.ui.label_switch.linkActivated.connect(self.switch)
        self.ui.label_switch.close()

        self.refreshUI(False)

        self.adjustSize()

    def switch(self):
        self.is_hide = not self.is_hide
        s = '<a href="#" style="text-decoration: none;' \
            'color: white;">{0}</a>'.format("展开" if self.is_hide else "隐藏")
        self.ui.label_switch.setText(s)
        for i in self.menu_labels:
            if self.is_hide:
                i.hide()
            else:
                i.show()

    def appendMenu(self, text: str, alias=""):
        label = NavigateLabel(self)
        label.setTitle(text, alias)
        label.setParent(self)
        label.setStyleSheet("QLabel{margin-left: 10px;}")
        if self.is_hide:
            label.hide()
        label.linkActivated.connect(link_manager.activate)
        label.checkChanged.connect(self.ui.label_title.setChecked)
        self.ui.layout_menu.addWidget(label)
        self.menu_labels.append(label)
        self.ui.label_switch.show()
        return label

    def refreshUI(self, checked):
        bgcolor = QColor(230, 182, 102) if checked else QColor(122, 122, 122)
        pal = self.ui.label_switch.palette()
        pal.setColor(QPalette.Background, bgcolor)
        self.ui.label_switch.setPalette(pal)
        self.ui.label_icon.setPalette(pal)
