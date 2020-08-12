from PyQt5.QtCore import Qt

from libs.enumrations import UserPermission
from libs.g import g
from ui.page_elements.check_combo_box import CheckComboBox


class CheckComboWidget(CheckComboBox):
    def __init__(self):
        super().__init__()
        self.ui.pushButton.setCursor(Qt.PointingHandCursor)
        self.ui.pushButton.setChecked(True)

    def get_data(self):
        return self.selected_items

    def paintEvent(self, e):
        if g.current_user.permission != UserPermission.Admin:
            self.ui.pushButton.hide()
        else:
            self.ui.pushButton.show()
