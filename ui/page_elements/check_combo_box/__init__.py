from PyQt5.QtWidgets import QButtonGroup, QCheckBox, QDialog, QWidget

from .dialogUI import Ui_Dialog
from .pageUI import Ui_Form


class ChoiceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.done)
        self.setWindowTitle("请选择")
        self.button_group = QButtonGroup()

    def get_choices(self, items, selected):
        layout = self.ui.layout
        while layout.count():
            w = layout.takeAt(0).widget()
            self.button_group.removeButton(w)
            w.close()
            w.deleteLater()
        checkboxes = []
        for item in items:
            checkbox = QCheckBox(item)
            self.button_group.addButton(checkbox)
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
        self.exclude = False
        self.dialog = ChoiceDialog()

    def open_dialog(self):
        self.dialog.button_group.setExclusive(self.exclude)
        self._selected = self.dialog.get_choices(self._items, self._selected)
        if self.exclude and self._selected:
            self._selected = [self._selected[0]]
        self.ui.lineEdit.setText('|'.join(self._selected))

    def set_items(self, items):
        self._items = items
        self._selected = []

    @property
    def selected_items(self):
        if self.exclude:
            if self._selected:
                return self._selected[0]
            return None
        return self._selected

    @selected_items.setter
    def selected_items(self, val):
        if val is None:
            if self.exclude:
                val = ''
            else:
                val = []
        if isinstance(val, str):
            val = [val]
        self._selected = val
        self.ui.lineEdit.setText('|'.join(val))
