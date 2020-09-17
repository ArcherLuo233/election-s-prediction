from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout


class DialogLikeWidgetWrapper(QDialog):
    def __init__(self, parent, w):
        super().__init__(parent)
        try:
            w.set_wrapper(self)
        except:
            pass
        flags = self.windowFlags()
        flags |= Qt.WindowMinMaxButtonsHint
        self.setWindowFlags(flags)
        self.wrapped_widget = w
        self.setWindowTitle(w.windowTitle())
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(w)
        self.setLayout(layout)


def create_dialog_like_widget(parent, widget):
    if isinstance(widget, str):
        from libs.page_magager import PageManager
        widget = PageManager.get_page(widget, True)
    return DialogLikeWidgetWrapper(parent, widget)
