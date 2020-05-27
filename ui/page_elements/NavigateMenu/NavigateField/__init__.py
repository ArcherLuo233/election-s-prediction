from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import pyqtSignal, Qt
from .NavigateFieldUI import Ui_Form


class NavigateLabel(QLabel):
    checkChanged = pyqtSignal(bool)

    def __init__(self):
        QLabel.__init__(self)
        self.checked = False
        self.text = "测试文本"
        self.alias = ""
        font = QFont("黑体", 14)
        self.setFont(font)
        self.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.setCursor(Qt.PointingHandCursor)

    def setChecked(self, check):
        if self.checked == check:
            return
        self.checked = check
        self.updateText()
        self.checkChanged.emit(check)

    def setTitle(self, title: str, alias: str = ""):
        self.text = title
        self.alias = alias if alias != "" else title
        self.updateText()

    def updateText(self):
        color = "rgb(68, 126, 217)" if self.checked else "rgb(0, 0, 0)"
        s = '<a href="#goto:{2}"><span style="text-decoration: none; color:{0};">\
            {1}</span></a>'.format(color, self.text, self.alias)
        super().setText(s)


class NavigateField(QWidget):
    def __init__(self, title: str):
        QWidget.__init__(self)
        self.menu_labels: [NavigateLabel] = []
        self.is_hide: bool = True
        self.title = title
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_title.setText(self.getLinkHtml(QColor(0, 0, 0)).format(title))
        self.ui.label_title.linkActivated.connect(self.switch)
        self.ui.label_switch.linkActivated.connect(self.switch)
        self.ui.label_switch.hide()
        self.adjustSize()

    @staticmethod
    def getLinkHtml(color: QColor = QColor(68, 126, 217)):
        col = "rgb({0}, {1}, {2})".format(color.red(), color.green(), color.blue())
        return '<a href="#">' \
               '<div>' \
               '<span style="width:100%%; height:100%%; text-decoration: none; color:%s;">{0}</span>' \
               '</div></a>' % col

    def switch(self):
        self.is_hide = not self.is_hide
        s = self.getLinkHtml().format("展开" if self.is_hide else "隐藏")
        self.ui.label_switch.setText(s)
        for i in self.menu_labels:
            if self.is_hide:
                i.hide()
            else:
                i.show()

    def appendMenu(self, text: str, alias="", callback=None):
        label = NavigateLabel()
        label.setTitle(text, alias)
        label.setParent(self)
        if self.is_hide:
            label.hide()
        if callback:
            label.linkActivated.connect(callback)
        label.checkChanged.connect(self.checkChange)
        self.ui.layout_menu.addWidget(label)
        self.menu_labels.append(label)
        self.ui.label_switch.show()
        return label

    def checkChange(self, check):
        text_color = QColor(68, 126, 217) if check else QColor(0, 0, 0)
        self.ui.label_title.setText(self.getLinkHtml(text_color).format(self.title))
