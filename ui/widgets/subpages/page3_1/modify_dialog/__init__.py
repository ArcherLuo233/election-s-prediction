from .dialogUI import Ui_Dialog
from ui.page_elements.modal_dialog import ModalDialog


class ModifyDialog(ModalDialog):
    def __init__(self, parent, name=''):
        super().__init__(parent)
        self.setFixedSize(300, 300)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        if name is None:
            name = ''
        self.data = name
        self.ui.lineEdit.setText(name)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_modify.clicked.connect(self.handle_modify)

    def handle_modify(self):
        self.data = self.ui.lineEdit.text()
        self.close()

    def show_(self):
        self.exec_()
        return self.data
