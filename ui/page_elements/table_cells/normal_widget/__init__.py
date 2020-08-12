from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QPlainTextEdit


class NormalWidget(QPlainTextEdit):
    def __init__(self, text):
        super().__init__(text)
        self.setFrameShape(self.NoFrame)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textChanged.connect(self.refresh)
        self.refresh()

    def refresh(self):
        self.adjustSize()
        self.verticalScrollBar().setValue(self.verticalScrollBar().minimum())

    def sizeHint(self):
        return QSize(self.width(), self.document().size().height() * 20 + 20)

    def get_data(self):
        return self.toPlainText()
