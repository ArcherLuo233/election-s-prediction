from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPalette
from PyQt5.QtWidgets import QLabel

from config.uicolor import UIColor as color


class NavigateLabel(QLabel):
    checkChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.checked = False
        self.text = "测试文本"
        self.alias = ""
        font = self.parent().font()
        font.setBold(50)
        font.setPixelSize(20)
        self.setFont(font)
        self.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.setAutoFillBackground(True)
        self.setContentsMargins(0, 10, 0, 10)
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
        s = self.text
        self.setText(s)
        textcolor = color.NavigateTextHighlight if self.checked else color.NavigateText
        bgcolor = color.NavigateBackgroundHighlight if self.checked else color.NavigateBackground
        palette: QPalette = self.palette()
        palette.setColor(QPalette.WindowText, textcolor)
        palette.setColor(QPalette.Background, bgcolor)
        self.setPalette(palette)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() != Qt.LeftButton:
            return
        link = "#goto:{}".format(self.alias)
        self.linkActivated.emit(link)
