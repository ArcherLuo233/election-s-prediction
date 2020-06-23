from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog

from ui.page_elements.window_mask import WindowMask


class ModalDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.mask_ = WindowMask(parent)
        self.mask_.close()
        self.hide()
        self.mask_.clicked.connect(self.close)
        self.setAttribute(Qt.WA_DeleteOnClose)

    def showEvent(self, e):
        self.mask_.show()
        self.raise_()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setBrush(self.palette().window())
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

    def resizeEvent(self, e):
        self.location_dialog()

    def closeEvent(self, e):
        self.mask_.close()

    def location_dialog(self):
        self.mask_.resize(self.parent().size())
        geo = self.parent().geometry()
        width = self.width()
        height = self.height()
        left = (geo.width() - width) / 2
        top = (geo.height() - height) / 2
        geo.setWidth(width)
        geo.setHeight(height)
        geo.setLeft(left)
        geo.setTop(top)
        self.setGeometry(geo)
