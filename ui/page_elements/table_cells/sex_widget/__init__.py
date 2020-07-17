from PyQt5.QtWidgets import QWidget

from .pageUI import Ui_Form


class SexWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def set_sex(self, sex):
        if sex == '男':
            self.ui.btn_male.setChecked(True)
        elif sex == '女':
            self.ui.btn_female.setChecked(True)

    def get_data(self):
        return self.ui.buttonGroup.checkedButton().text()
