from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget


class WindowMask(QWidget):
    clicked = pyqtSignal()

    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.resize(parent.size())

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(QColor(10, 10, 10, 100))
        painter.drawRect(self.rect())

    def mouseReleaseEvent(self, QMouseEvent):
        self.clicked.emit()
