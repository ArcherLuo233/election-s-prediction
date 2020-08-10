from PyQt5.QtWidgets import QWidget, QDialog, QCheckBox

from .dialogUI import Ui_Dialog
from .pageUI import Ui_Form


class ChoiceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.done)

    def get_choices(self, items, selected):
        layout = self.ui.layout
        while layout.count():
            w = layout.takeAt(0).widget()
            w.close()
            w.deleteLater()
        checkboxes = []
        for item in items:
            checkbox = QCheckBox(item)
            checkbox.setFont(self.font())
            checkbox.setChecked(item in selected)
            checkboxes.append(checkbox)
            layout.addWidget(checkbox)
        self.exec()
        selected = []
        for checkbox in checkboxes:
            if checkbox.isChecked():
                selected.append(checkbox.text())
        return selected


class CheckComboBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_dialog)
        self._selected = []
        self._items = []
        self.dialog = ChoiceDialog()

    def open_dialog(self):
        self.dialog.setFont(self.font())
        self._selected = self.dialog.get_choices(self._items, self._selected)
        self.ui.lineEdit.setText('|'.join(self._selected))

    def set_items(self, items):
        self._items = items
        self._selected = []

    @property
    def selected_items(self):
        return self._selected

    @selected_items.setter
    def selected_items(self, val):
        self._selected = val
