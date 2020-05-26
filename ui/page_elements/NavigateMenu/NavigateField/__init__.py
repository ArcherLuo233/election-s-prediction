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
        self.setCursor(Qt.PointingHandCursor)

    def setChecked(self, check):
        if self.checked == check:
            return
        self.checked = check
        self.setText(self.text)
        self.checkChanged.emit(check)

    def setText(self, p_str):
        self.text = p_str
        color = "rgb(68, 126, 217)" if self.checked else "rgb(0, 0, 0)"
        s = '<a href="#goto:{1}"><span style="text-decoration: none; color:{0};">{1}</span></a>'.format(color, self.text)
        super().setText(s)


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
        s = '<a href="#">' \
            '<div>' \
            '<span style="width:100%; height:100%; text-decoration: none; color:rgb(68, 126, 217);">{0}</span>' \
            '</div></a>'.format("展开" if self.is_hide else "隐藏")
        self.ui.label_switch.setText(s)
        for i in self.menu_labels:
            if self.is_hide:
                i.hide()
            else:
                i.show()

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
        return label

    def checkChange(self, check):
        text_color = QColor(68, 126, 217) if check else QColor(0, 0, 0)
        palette = self.ui.label_title.palette()
        palette.setBrush(QPalette.WindowText, text_color)
        self.ui.label_title.setPalette(palette)
