from PyQt5.QtCore import QObject, pyqtSignal


class LinkManager(QObject):
    linkActivated = pyqtSignal(str)

    def activate(self, link):
        self.linkActivated.emit(link)


link_manager = LinkManager()
