from PyQt5.QtWidgets import QHBoxLayout

from ui.page_elements.modal_dialog import ModalDialog


class DialogLikeWidgetWrapper(ModalDialog):
    def __init__(self, parent, w):
        super().__init__(parent)
        self.wrapped_widget = w
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(w)
        self.setLayout(layout)


def create_dialog_like_widget(parent, widget):
    if isinstance(widget, str):
        from libs.page_magager import PageManager
        widget = PageManager.get_page(widget, True)
    return DialogLikeWidgetWrapper(parent, widget)
