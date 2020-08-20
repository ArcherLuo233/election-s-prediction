from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QDialog, QFileDialog, QHeaderView, QMessageBox,
                             QTableWidget, QTableWidgetItem)

from libs.enumrations import UserPermission
from libs.fields_translater import FieldsTranslater
from libs.g import g
from model.base import Base
from model.zyrs import ZYRS
from ui.page_elements.table_cells.check_combo_widget import CheckComboWidget
from ui.page_elements.table_cells.date_widget import DateWidget
from ui.page_elements.table_cells.file_widget import FileWidget
from ui.page_elements.table_cells.normal_widget import NormalWidget
from ui.page_elements.table_cells.pic_widget import PicWidget
from ui.page_elements.table_cells.sex_widget import SexWidget
from ui.wrapper.dialog_like_widget import create_dialog_like_widget

from .dialogUI import Ui_Dialog


class DetailPage(QDialog):
    pic_item_height = 4

    def __init__(self, parent, model: Base):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setMinimumSize(800, 400)
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
        if 'nickname' in data:
            zyrs = ZYRS.search(nickname=data['nickname'])['data']
            if zyrs:
                box = QMessageBox(QMessageBox.Question, "添加人物信息", "已存在该人")
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                box.setDefaultButton(QMessageBox.Yes)
                box.button(QMessageBox.Yes).setText("显示详情")
                box.button(QMessageBox.No).setText("直接添加")
                res = box.exec_()
                if res == QMessageBox.Yes:
                    if zyrs:
                        if len(zyrs) == 1:
                            dialog = DetailPage(self.parent(), ZYRS)
                            dialog.show_(True, {'id': zyrs[0].id})
                        else:
                            from .pages import ZYRSChoicePage
                            dialog = create_dialog_like_widget(self.parent(), ZYRSChoicePage())
                            dialog.setFixedSize(1500, 800)
                            dialog.wrapped_widget.set_default_conditions(nickname=data['nickname'])
                            dialog.exec_()
                    return
        self.model.create(**data)
        self.close()

    def modify(self):
        data = self.get_data_from_table()
        item = self.model.get_by_id(self.data_id)
        for file in item.read_field:
            data.pop(file)
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

        try:
            self.model.export_document(self.data_id, filename)
        except Exception as e:
            QMessageBox.warning(None, "导出数据", "导出失败,请关闭目标文件!")

            return

        QMessageBox.information(None, "导出文档", "导出完成")

    def refresh_data(self, id_: int):
        if id_ == -1:
            meta = self.model()
        else:
            meta = self.model.get_by_id(id_)
            if meta is None:
                print("Not found:", self.model.class_name, "id:", id_)
                QMessageBox.critical(None, "显示详情", "找不到该人员")
                return False
        data_list = []
        filter_list = ['id', 'photo']
        filtered_data = {}
        for idx in meta.field:
            if idx in filter_list:
                filtered_data[idx] = getattr(meta, idx)
                continue
            comment = self.translator.to_text(idx)
            value = getattr(meta, idx)
            type_ = 'normal'
            if idx in self.model.file_field:
                type_ = 'file'
            if idx in self.model.combo_field:
                type_ = 'combo'
            if idx in self.model.date_field:
                type_ = 'date'
            if idx == 'sex':
                type_ = "sex"
            read_only = True if idx in self.model.read_field else False
            data_list.append({
                'idx': idx,
                'comment': comment,
                'value': value,
                'type': type_,
                'readonly': read_only
            })
        if meta.pic:
            filtered_data['photo'] = meta.photo
        self.refresh_table(data_list, **filtered_data)
        return True

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
        widget = None
        if item['type'] == 'normal':
            widget = NormalWidget(item['value'])
            widget.textChanged.connect(table_widget.resizeRowsToContents)
        elif item['type'] == 'file':
            description = "{model}-{id}-{comment}".format(
                model=self.model.class_name,
                id=self.data_id,
                comment=item['comment']
            )
            widget = FileWidget(description)
            widget.set_file_path(item['value'])
        elif item['type'] == 'sex':
            widget = SexWidget()
            widget.set_sex(item['value'])
        elif item['type'] == 'combo':
            widget = CheckComboWidget()
            widget.exclude = self.model.combo_field[item['idx']]['exclude']
            widget.set_items(self.model.combo_field[item['idx']]['items'])
            widget.selected_items = item['value']
            widget.setFont(self.font())
        elif item['type'] == 'date':
            widget = DateWidget()
            widget.set_date(item['value'])
        if widget:
            if item['readonly']:
                widget.setEnabled(False)
            table_widget.setCellWidget(row, col + 1, widget)

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
            if field in data:
                continue
            data[field] = val
        return data

    def show_(self, enable: bool, data):
        self.ui.tableWidget.setEnabled(enable)
        id_ = data['id']
        self.data_id = id_
        if self.model.export_docx:
            self.ui.btn_export.show()
        else:
            self.ui.btn_export.hide()
        if self.refresh_data(id_):
            self.exec_()
        else:
            self.close()

    def paintEvent(self, e):
        if self.data_id == -1:
            self.ui.btn_append.show()
            self.ui.btn_modify.hide()
            self.ui.btn_delete.hide()
            self.ui.btn_export.hide()
        else:
            self.ui.btn_append.hide()
            self.ui.btn_export.show()
            self.ui.btn_modify.show()
            self.ui.btn_delete.show()
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_append.hide()
            self.ui.btn_modify.hide()
            self.ui.btn_delete.hide()
