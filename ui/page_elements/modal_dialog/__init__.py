from PyQt5.QtCore import QEvent, QSize, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog

from ui.page_elements.window_mask import WindowMask


class ModalDialog(QDialog):
    def __init__(self, parent, size=(1000, 800)):
        super().__init__()
        self.setParent(parent)
        self.mask_ = WindowMask(parent)
        self.mask_.close()
        self.hide()
        self.size_ = QSize(size[0], size[1])
        self.mask_.clicked.connect(self.close)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.parent().installEventFilter(self)
        self.location_dialog()

    def showEvent(self, e):
        self.mask_.show()
        self.mask_.raise_()
        self.raise_()

    def eventFilter(self, o, e: QEvent):
        if e.type() == QEvent.Resize:
            self.location_dialog()
        return False

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
        width = self.size_.width()
        height = self.size_.height()
        pw = self.parent().width()
        ph = self.parent().height()
        width = min(width, pw - 20)
        height = min(height, ph - 40)
        self.setFixedSize(width, height)
        left = (geo.width() - width) / 2
        top = (geo.height() - height) / 2
        geo.setWidth(width)
        geo.setHeight(height)
        geo.setLeft(left)
        geo.setTop(top)
        self.setGeometry(geo)
