from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPalette, QColor


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
        self.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        self.setCursor(Qt.PointingHandCursor)
        self.setAutoFillBackground(True)

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
        color = "black" if self.checked else "white"
        s = '<a href="#goto:{2}" style="text-decoration: none; color:{0};">' \
            '{1}</a>'.format(color, self.text, self.alias)
        super().setText(s)
        bgcolor = QColor("white") if self.checked else QColor(51, 51, 51)
        palette: QPalette = self.palette()
        palette.setColor(QPalette.Background, bgcolor)
        self.setPalette(palette)
        self.update()
