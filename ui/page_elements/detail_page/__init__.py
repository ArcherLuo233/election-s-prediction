from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QMessageBox,
                             QTableWidget, QTableWidgetItem)

from libs.enumrations import UserPermission
from libs.fields_translater import FieldsTranslater
from libs.g import g
from model.base import Base
from ui.page_elements.modal_dialog import ModalDialog
from ui.page_elements.table_cells.file_widget import FileWidget
from ui.page_elements.table_cells.normal_widget import NormalWidget
from ui.page_elements.table_cells.pic_widget import PicWidget

from .dialogUI import Ui_Dialog


class DetailPage(ModalDialog):
    pic_item_height = 6

    def __init__(self, parent, model: Base):
        super().__init__(parent)
        self.setFixedSize(1000, 800)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.default_conditions = {}
        # model
        self.model = model
        self.need_pic = self.model.pic
        self.data_id = 0
        self.translator = FieldsTranslater(self.model)
        # tableWidget
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.ui.tableWidget.cellChanged.connect(self.ui.tableWidget.resizeRowsToContents)
        # tableWidget-header
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        hor_header.setSectionResizeMode(0, QHeaderView.Fixed)
        hor_header.setSectionResizeMode(2, QHeaderView.Fixed)
        # btn-bind
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_append.clicked.connect(self.append)
        self.ui.btn_modify.clicked.connect(self.modify)
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_export.clicked.connect(self.export)

    def set_default_conditions(self, **kwargs):
        self.default_conditions = kwargs

    def append(self):
        data = self.get_data_from_table()
        self.model.create(**data)
        self.close()

    def modify(self):
        data = self.get_data_from_table()
        item = self.model.get_by_id(self.data_id)
        item.modify(**data)
        self.close()

    def delete(self):
        res = QMessageBox.question(None, "删除", "确认删除吗？")
        if res == QMessageBox.No:
            return
        item = self.model.get_by_id(self.data_id)
        item.delete()
        self.close()

    def export(self):
        default_name = "./{model}-{id}.docx".format(model=self.model.class_name, id=self.data_id)
        filename = QFileDialog.getSaveFileName(None, "导出文档", default_name, "word文档(*.docx)")[0]
        if filename == "":
            return
        self.model.export_document(self.data_id, filename)
        QMessageBox.information(None, "导出文档", "导出完成")

    def refresh_data(self, id_: int):
        if id_ == -1:
            meta = self.model()
        else:
            meta = self.model.get_by_id(id_)
            if meta is None:
                print("Not found:", type(self.model), "id:", id_)
                return
        data_list = []
        filter_list = ['id', 'photo']
        filtered_data = {}
        for idx in meta.field:
            if idx in filter_list:
                filtered_data[idx] = getattr(meta, idx)
                continue
            comment = self.translator.to_text(idx)
            value = getattr(meta, idx)
            type_ = "normal"
            if idx in self.model.file_field:
                type_ = "file"
            data_list.append({
                'comment': comment,
                'value': value,
                'type': type_
            })
        if meta.pic:
            filtered_data['photo'] = meta.photo
        self.refresh_table(data_list, **filtered_data)

    def refresh_table(self, data_list, **kwargs):
        table_widget = self.ui.tableWidget
        pic_height = self.pic_item_height if self.need_pic else 0
        row_count = (len(data_list) - pic_height + 1) // 2 + pic_height
        column_count = 4
        table_widget.clearContents()
        table_widget.setRowCount(row_count)
        table_widget.setColumnCount(column_count)
        # pic-item
        if self.need_pic:
            table_widget.setSpan(0, 2, pic_height, 1)
            table_widget.setSpan(0, 3, pic_height, 1)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled)
            item.setText("照片")
            table_widget.setItem(0, 2, item)
            pic_widget = PicWidget()
            pic_widget.set_picture(kwargs.get('photo'))
            table_widget.setCellWidget(0, 3, pic_widget)
        # data-list-set
        for i, item in enumerate(data_list[:pic_height]):
            self.generate_item(item, i, 0)
        for i, item in enumerate(data_list[pic_height:]):
            row = pic_height + i // 2
            col = 0 if i % 2 == 0 else 2
            self.generate_item(item, row, col)
        # 奇数时不可编辑
        if (len(data_list) - pic_height) % 2 == 1:
            item = QTableWidgetItem()
            item.setFlags(Qt.NoItemFlags)
            table_widget.setItem(row_count - 1, 2, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.NoItemFlags)
            table_widget.setItem(row_count - 1, 3, item)
        table_widget.resizeColumnsToContents()
        table_widget.resizeRowsToContents()

    def generate_item(self, item, row, col):
        table_widget = self.ui.tableWidget
        comment_item = QTableWidgetItem()
        comment_item.setText(item['comment'])
        comment_item.setFlags(Qt.ItemIsEnabled)
        table_widget.setItem(row, col, comment_item)
        if item['type'] == 'normal':
            widget = NormalWidget(item['value'])
            widget.textChanged.connect(table_widget.resizeRowsToContents)
            table_widget.setCellWidget(row, col + 1, widget)
        elif item['type'] == 'file':
            description = "{model}-{id}-{comment}".format(
                model=self.model.class_name,
                id=self.data_id,
                comment=item['comment']
            )
            file_widget = FileWidget(description)
            file_widget.set_file_path(item['value'])
            table_widget.setCellWidget(row, col + 1, file_widget)

    def get_data_from_table(self) -> dict:
        table_widget = self.ui.tableWidget
        pic_height = self.pic_item_height if self.need_pic else 0
        row_cnt = table_widget.rowCount()
        data = dict()
        if self.need_pic:
            pic_widget = table_widget.cellWidget(0, 3)
            data['photo'] = pic_widget.get_data()
        for row in range(0, row_cnt):
            cols = [0] if row < pic_height else [0, 2]
            for col in cols:
                item = table_widget.item(row, col)
                if item is None or item.text() == '':
                    continue
                text = item.text()
                field = self.translator.to_field(text)
                widget = table_widget.cellWidget(row, col + 1)
                content = widget.get_data()
                data[field] = content
        for field, val in self.default_conditions.items():
            data[field] = val
        return data

    def show_(self, enable: bool, data):
        self.ui.tableWidget.setEnabled(enable)
        id_ = data['id']
        self.data_id = id_
        if id_ == -1:
            self.ui.btn_append.show()
            self.ui.btn_modify.hide()
            self.ui.btn_delete.hide()
            self.ui.btn_export.hide()
        else:
            self.ui.btn_append.hide()
            self.ui.btn_modify.show()
            self.ui.btn_delete.show()
            self.ui.btn_export.show()
        if self.model.export_docx:
            self.ui.btn_export.show()
        else:
            self.ui.btn_export.hide()
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_append.hide()
            self.ui.btn_modify.hide()
            self.ui.btn_delete.hide()
        self.refresh_data(id_)
        self.exec_()
