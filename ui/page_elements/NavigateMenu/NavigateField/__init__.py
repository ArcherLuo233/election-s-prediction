from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import pyqtSignal, Qt
from .NavigateFieldUI import Ui_Form


class NavigateLabel(QLabel):
    checkChanged = pyqtSignal(bool)

    def __init__(self):
        QLabel.__init__(self)
        self.checked = False
        self.text = "测试文本"
        font = QFont("黑体", 14)
        self.setFont(font)
        self.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

    def setChecked(self, check):
        if self.checked == check:
            return
        self.checked = check
        self.setText(self.text)
        self.checkChanged.emit(check)

    def setText(self, p_str):
        self.text = p_str
        if self.checked:
            str = '<a href="#{0}"><span style="text-decoration: none; color:rgb(68, 126, 217);">{0}</span></a>'
        else:
            str = '<a href="#{0}"><span style="text-decoration: none; color:rgb(0, 0, 0);">{0}</span></a>'
        str = str.format(self.text)
        super().setText(str)


class NavigateField(QWidget):
    def __init__(self, title: str):
        QWidget.__init__(self)
        self.menu_labels: [NavigateLabel] = []
        self.is_hide: bool = True
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_title.setText(title)
        self.ui.label_switch.linkActivated.connect(self.switch)
        self.adjustSize()

    def switch(self):
        self.is_hide = not self.is_hide
        s = '<a href="#"><span style="text-decoration: none; color:rgb(68, 126, 217);">{0}</span></a>'.format(
            "展开" if self.is_hide else "隐藏")
        self.ui.label_switch.setText(s)
        for i in self.menu_labels:
            if self.is_hide:
                i.hide()
            else:
                i.show()
        self.adjustSize()
        self.parent().adjustSize()

    def appendMenu(self, text: str, callback=None):
        label = NavigateLabel()
        label.setText(text)
        label.setParent(self)
        if self.is_hide:
            label.hide()
        if callback:
            label.linkActivated.connect(callback)
        label.checkChanged.connect(self.checkChange)
        self.ui.layout_menu.addWidget(label)
        self.menu_labels.append(label)
        self.adjustSize()
        return label

    def checkChange(self, check):
        text_color = QColor(68, 126, 217) if check else QColor(0, 0, 0)
        palette = self.ui.label_title.palette()
        palette.setBrush(QPalette.WindowText, text_color)
        self.ui.label_title.setPalette(palette)
