from PyQt5.QtCore import QObject, pyqtSignal

from ui.page_elements.condition_box import ConditionBox


class ConditionGroup(QObject):
    boxes_changed = pyqtSignal()

    def __init__(self, fields):
        QObject.__init__(self)
        self.fields = set(fields)
        self.used_fields = set()
        self._boxes = []
        self.box_field = {}

    @property
    def available_fields(self):
        return self.fields - self.used_fields

    def add_box(self, box: ConditionBox):
        box.set_fields([i for i in self.available_fields])
        field = box.current_field
        self.used_fields.add(field)
        self.box_field[box] = field
        for i in self._boxes:
            i.del_fields(field)
        self._boxes.append(box)
        box.field_changed.connect(self.field_change)
        self.boxes_changed.emit()

    def del_box(self, box: ConditionBox):
        self._boxes.remove(box)
        field = box.current_field
        self.used_fields.remove(field)
        for i in self._boxes:
            i.add_fields(field)
        self.box_field.pop(box)
        box.deleteLater()
        self.boxes_changed.emit()

    def field_change(self):
        sender = self.sender()
        old_field = self.box_field[sender]
        new_field = sender.current_field
        self.used_fields.remove(old_field)
        self.used_fields.add(new_field)
        self.box_field[sender] = new_field
        for i in self._boxes:
            if sender == i:
                continue
            i.add_fields(old_field)
            i.del_fields(new_field)
