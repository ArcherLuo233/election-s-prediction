from PyQt5.QtCore import pyqtSignal, QObject


class LinkManager(QObject):
    linkActivated = pyqtSignal(str)

    def activate(self, link):
        self.linkActivated.emit(link)


link_manager = LinkManager()
