from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, Qt


class NavigateLabel(QLabel):
    checkChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.checked = False
        self.text = "测试文本"
        self.alias = ""
        font = self.parent().font()
        font.setPixelSize(20)
        self.setFont(font)
        self.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
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
