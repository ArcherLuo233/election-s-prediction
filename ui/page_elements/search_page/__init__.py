import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QLabel, QMessageBox,
                             QTableWidgetItem, QWidget)

from config.settings import DEFAULT_PAGE_SIZE
from libs.enumrations import UserPermission
from libs.exception import AppException
from libs.fields_translater import FieldsTranslater
from libs.g import g
from model.zyrs import ZYRS
from ui.page_elements.condition_box import ConditionBox
from ui.page_elements.condition_group import ConditionGroup
from ui.page_elements.detail_page import DetailPage
from ui.wrapper.dialog_like_widget import create_dialog_like_widget

from .pageUI import Ui_Form


class SearchPage(QWidget):
    model = None
    summary = {}
    title = None
    default_conditions = {}
    member_page_name = ''
    cant_add = False
    table_header_height = 30

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_selected = set()
        self.sort_field = 'id'
        self.sort_order = 'desc'
        self.dialog_parent = self
        self.show_close_btn = False
        if self.model:
            self.members_model = self.model.ty
            self.translator = FieldsTranslater(self.model)
            dic = dict()
            if isinstance(self.summary, dict):
                for i, j in self.summary.items():
                    if not hasattr(self.model, j):
                        print(self.model.class_name, '找不到 {} 的对应字段 {}'.format(i, j))
                    dic[i] = j
            elif isinstance(self.summary, list):
                for i in self.summary:
                    field = self.translator.to_field(i)
                    if field == '翻译缺失':
                        print(self.model.class_name, '缺少字段', i)
                        continue
                    dic[i] = field
            self.summary = dic
            self.condition_group = ConditionGroup(self.translator.to_text(self.model.field))
            self.condition_boxes = []
        # label_title
        self.ui.label_title.setText(self.title)
        # button_search
        icon = QIcon("./static/svg/search.svg")
        self.ui.button_search.setIcon(icon)
        # btn_add_condition
        self.ui.btn_add_condition.clicked.connect(self.add_condition)
        # button_search
        self.ui.button_search.clicked.connect(self.refresh_page)
        # button_add
        self.ui.button_add.clicked.connect(self.action_add)
        if self.cant_add:
            self.ui.button_add.hide()
        # btn_select_all
        self.ui.btn_select_all.clicked.connect(self.select_all)
        # btn_select_null
        self.ui.btn_select_null.clicked.connect(self.select_null)
        # btn_mul_delete
        self.ui.btn_mul_delete.clicked.connect(self.mul_delete)
        # btn_mul_export
        self.ui.btn_mul_export.clicked.connect(self.mul_export)
        # tableWidget
        cols = self.cols
        table_widget = self.ui.tableWidget
        table_widget.clear()
        table_widget.setColumnCount(cols)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.horizontalHeader().setFixedHeight(self.table_header_height)
        table_widget.horizontalHeader().sectionClicked.connect(self.section_clicked)
        table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget.cellChanged.connect(self.cell_changed)

        # set-header
        item = QTableWidgetItem()
        item.setText("")
        table_widget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setText("编号")
        table_widget.setHorizontalHeaderItem(1, item)
        for i, text in enumerate(self.summary.keys(), 2):
            item = QTableWidgetItem()
            item.setText(text)
            table_widget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()
        item.setText("详情")
        table_widget.setHorizontalHeaderItem(cols - 1, item)

        # download-template
        self.ui.btn_downloadTemplate.clicked.connect(self.download_template)
        # import
        self.ui.button_import.clicked.connect(self.import_from_file)
        # export
        self.ui.button_export.clicked.connect(self.export_to_file)
        # page_controller
        self.ui.page_controller.pageChanged.connect(self.refresh_page)
        # refresh-table
        self.refresh_page()

    def add_condition(self):
        if not self.model:
            return
        if len(self.condition_boxes) == len(self.model.field):
            QMessageBox.information(None, "添加筛选器", "没有其他的字段了")
            return
        box = ConditionBox()
        box.delete_clicked.connect(self.del_condition)
        self.condition_boxes.append(box)
        self.condition_group.add_box(box)
        self.refresh_conditions()

    def del_condition(self):
        box = self.sender()
        self.condition_boxes.remove(box)
        self.condition_group.del_box(box)
        self.refresh_conditions()
        box.deleteLater()

    def set_default_conditions(self, **kwargs):
        self.default_conditions = kwargs
        self.refresh_page()

    def refresh_conditions(self):
        if not self.model:
            return
        if not self.condition_boxes:
            return
        col = (self.width() - 100) // 400
        layout = self.ui.layout_conditions
        cnt = layout.count()
        for i in range(0, cnt):
            layout.takeAt(i)
        for i, w in enumerate(self.condition_boxes):
            layout.addWidget(w, i // col, i % col)

    @property
    def cols(self):
        return len(self.summary) + 3

    def set_dialog_parent(self, parent):
        self.dialog_parent = parent

    def set_wrapper(self, wrapper):
        self.show_close_btn = True
        self.ui.btn_close.clicked.connect(wrapper.close)

    def section_clicked(self, id_):
        table_widget = self.ui.tableWidget
        hor_header = table_widget.horizontalHeader()
        if id_ == 0 or id_ == hor_header.count() - 1:
            hor_header.setSortIndicatorShown(False)
            return
        else:
            hor_header.setSortIndicatorShown(True)
        order = hor_header.sortIndicatorOrder()
        if self.model:
            text = table_widget.horizontalHeaderItem(id_).text()
            self.sort_field = self.translator.to_field(text)
            self.sort_order = 'asc' if order == Qt.AscendingOrder else 'desc'
        self.refresh_page()

    def refresh_page(self, page: int = 1, page_size=DEFAULT_PAGE_SIZE):
        conditions = self.get_conditions()
        try:
            data = self.model.search(page=page,
                                     page_size=page_size,
                                     order={self.sort_field: self.sort_order},
                                     **conditions)
        except AppException as e:
            QMessageBox.warning(None, "导出数据", e.msg)
        if self.model is None:
            count = 0
        else:
            count = data['meta']['count']
        max_page = math.ceil(count / page_size)
        self.ui.page_controller.set_max_page(max_page)
        if self.model is None:
            return
        self.ui.sum.setText(str(data['meta']['count']))
        self.refresh_table(data['data'], page_size)

    def get_conditions(self):
        data = {}
        for w in self.condition_boxes:
            c = w.get()
            field = self.translator.to_field(c['field'])
            data[field] = c['val']
        for field, val in self.default_conditions.items():
            data[field] = val
        return data

    def refresh_table(self, records: list, page_size=DEFAULT_PAGE_SIZE):
        self.id_selected = set()
        cols = self.cols
        table_widget = self.ui.tableWidget
        table_widget.setSortingEnabled(False)
        table_widget.clearContents()
        table_widget.setRowCount(page_size)
        # load data
        for i, info in enumerate(records):
            # checkbox
            item = QTableWidgetItem()
            item.setCheckState(Qt.Unchecked)
            item.setData(Qt.UserRole, info.id)
            table_widget.setItem(i, 0, item)
            # id-column
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, info.id)
            table_widget.setItem(i, 1, item)
            # summarys
            for j, k in enumerate(self.summary.keys(), 2):
                item = QTableWidgetItem()
                data = getattr(info, self.summary[k])
                if data is None:
                    data = ''
                if isinstance(data, list):
                    while '' in data:
                        data.remove('')
                    data = ','.join(data)
                if self.model != ZYRS and k == '姓名':
                    res = ZYRS.get_by_name(data)
                    if res:
                        label = QLabel(self)
                        text = '<a href="#zyrs:{}">{}</a>'.format(res.id, data)
                        label.setText(text)
                        label.setFont(table_widget.font())
                        label.linkActivated.connect(self.detail)
                        label.show()
                        table_widget.setCellWidget(i, j, label)
                        continue
                item.setText(str(data))
                table_widget.setItem(i, j, item)
            # detail_label
            detail_label = QLabel(self)
            detail_text = '<a href="#detail:{}">详细信息</a>'.format(info.id)
            if self.model and self.members_model:
                detail_text += '   <a href="#members:{}">人员信息</a>'.format(info.id)
            if self.model.class_name == '在绍台企':
                detail_text += '   <a href="#jyb:{}">经营情况</a>'.format(info.id)
            detail_label.setText(detail_text)
            detail_label.setFont(table_widget.font())
            detail_label.linkActivated.connect(self.detail)
            detail_label.show()
            table_widget.setCellWidget(i, cols - 1, detail_label)
        table_widget.resizeColumnsToContents()
        if table_widget.columnWidth(1) < 50:
            table_widget.setColumnWidth(1, 50)
        for i in range(2, table_widget.horizontalHeader().count()):
            if table_widget.columnWidth(i) < 130:
                table_widget.setColumnWidth(i, 130)
        table_widget.setSortingEnabled(True)

    def cell_changed(self, row, col):
        if col != 0:
            return
        table_widget = self.ui.tableWidget
        item = table_widget.item(row, col)
        checked = item.checkState()
        id_ = item.data(Qt.UserRole)
        if checked == Qt.Checked:
            self.id_selected.add(id_)
        elif id_ in self.id_selected:
            self.id_selected.remove(id_)

    def mul_delete(self):
        if len(self.id_selected) == 0:
            return
        res = QMessageBox.question(None, "删除", "确认删除吗？")
        if res == QMessageBox.No:
            return
        for id_ in self.id_selected:
            rec = self.model.get_by_id(id_)
            rec.delete()
        self.refresh_page()

    def mul_export(self):
        if len(self.id_selected) == 0:
            return
        filedir = QFileDialog.getExistingDirectory(None, "请选择存放文件夹", "./")
        if filedir == '':
            return
        for id_ in self.id_selected:
            try:
                name = self.model.get_by_id(id_).nickname
            except:
                name = id_
            filename = '/{model}-{name}.docx'.format(model=self.model.class_name, name=name)
            filename = filedir + filename
            self.model.export_document(id_, filename)
        QMessageBox.information(None, "批量导出", "批量导出完成")

    def select_all(self):
        table_widget = self.ui.tableWidget
        rows = table_widget.rowCount()
        for row in range(0, rows):
            item = table_widget.item(row, 0)
            if item is None:
                break
            item.setCheckState(Qt.Checked)

    def select_null(self):
        table_widget = self.ui.tableWidget
        rows = table_widget.rowCount()
        for row in range(0, rows):
            item = table_widget.item(row, 0)
            if item is None:
                break
            item.setCheckState(Qt.Unchecked)

    def detail(self, link: str):
        if link.startswith('#detail:'):
            self.open_detail(True, data={'id': int(link[len("#detail:"):])})
        elif link.startswith('#members:'):
            self.open_members({'id': int(link[len("#members:"):])})
        elif link.startswith('#zyrs:'):
            self.open_zyrs(True, data={'id': int(link[len("#zyrs:"):])})
        elif link.startswith('#jyb:'):
            self.open_jyb({'id': int(link[len("#jyb:"):])})

    def action_add(self):
        self.open_detail(True, data={'id': -1})
        self.refresh_page()

    def open_members(self, data):
        page_name = self.member_page_name
        dialog = create_dialog_like_widget(self.dialog_parent, page_name)
        field = self.model.__name__.lower() + '_id'
        dialog.wrapped_widget.set_default_conditions(**{field: data['id']})
        # dialog.setFixedSize(1500, 800)
        dialog.wrapped_widget.set_dialog_parent(self)
        dialog.exec_()
        self.refresh_page(self.ui.page_controller.page)

    def open_detail(self, enable: bool, data):
        if self.model is None:
            print("页面没有设置Model: ", self.title)
            return
        dialog = DetailPage(self.dialog_parent, self.model)
        dialog.set_default_conditions(**self.default_conditions)
        dialog.show_(enable, data)
        self.refresh_page(self.ui.page_controller.page)

    def open_zyrs(self, enable: bool, data):
        dialog = DetailPage(self.dialog_parent, ZYRS)
        dialog.set_default_conditions(**self.default_conditions)
        dialog.show_(enable, data)
        self.refresh_page(self.ui.page_controller.page)

    def open_jyb(self, data):
        page_name = 'zstq_jyb'
        dialog = create_dialog_like_widget(self.dialog_parent, page_name.lower())
        # dialog.setFixedSize(1500, 800)
        field = self.model.__name__.lower() + '_id'
        dialog.wrapped_widget.set_default_conditions(**{field: data['id']})
        dialog.wrapped_widget.set_dialog_parent(self)
        dialog.exec_()
        self.refresh_page(self.ui.page_controller.page)

    def resizeEvent(self, e):
        self.refresh_conditions()

    def paintEvent(self, e):
        if not self.model.export_docx:
            self.ui.btn_mul_export.hide()
        else:
            self.ui.btn_mul_export.show()
        if self.show_close_btn:
            self.ui.btn_close.show()
        else:
            self.ui.btn_close.hide()
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_mul_delete.hide()
            self.ui.button_add.hide()
        else:
            self.ui.btn_mul_delete.show()
            if not self.cant_add:
                self.ui.button_add.show()

    def download_template(self):
        default_name = './{model}-模板.xlsx'.format(model=self.model.class_name)
        filename = QFileDialog.getSaveFileName(self, "选择保存地址", default_name, "excel文件(*.xlsx)")[0]
        if filename == "":
            return
        try:
            if self.model is None:
                QMessageBox.warning(None, "错误", "找不到该模型")
                return
            self.model.export_template(filename)
        except AppException as e:
            QMessageBox.warning(None, "错误", e.msg)
            return
        QMessageBox.information(None, "下载模板", "下载完毕")

    def import_from_file(self):
        filename = QFileDialog.getOpenFileName(self, "导入文件", "./", "excel文件(*.xlsx)")[0]
        if filename == "":
            return
        try:
            if self.model is None:
                raise AppException("Undefined Import: %s" % self.title)
            self.model.import_(filename, **self.default_conditions)
        except BaseException as e:
            QMessageBox.warning(None, "导入数据", e.msg)
            return
        QMessageBox.information(None, "导入数据", "导入完毕")
        self.refresh_page()

    def export_to_file(self):
        default_name = './{model}.xlsx'.format(model=self.model.class_name)
        if len(self.default_conditions) != 0:
            default_name = default_name[:-5]
        for i, j in self.default_conditions.items():
            default_name += '-{data}'.format(data=j)
        filename = QFileDialog.getSaveFileName(self, "选择保存地址", default_name, "excel文件(*.xlsx)")[0]
        if filename == "":
            return
        try:
            if self.model is None:
                raise AppException("Undefined Export: %s" % self.title)
            conditions = self.get_conditions()
            self.model.export(filename, **conditions)
        except Exception as e:
            QMessageBox.warning(None, "导出数据", "导出失败,请关闭目标文件!")
            return
        # if self.model is None:
        #     raise AppException("Undefined Export: %s" % self.title)
        # conditions = self.get_conditions()
        # self.model.export(filename, **conditions)
        QMessageBox.information(None, "导出数据", "导出完毕")
