from ui.page_elements.modal_dialog import ModalDialog

from .append_pageUI import Ui_Dialog


class AppendDialog(ModalDialog):
    def __init__(self, parent, keys=None):
        super().__init__(parent, size=(500, 300))
        if keys is None:
            keys = ['理事', '监事', '代表']
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data = None
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(keys)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_append.clicked.connect(self.handle_append)

    def handle_append(self):
        self.data = self.ui.comboBox.currentText(), self.ui.lineEdit.text()
        self.close()

    def show_(self):
        self.exec_()
        return self.data
