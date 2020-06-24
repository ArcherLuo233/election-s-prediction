import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QLabel, QMessageBox,
                             QTableWidgetItem, QWidget)

from config.settings import DEFAULT_PAGE_SIZE
from libs.exception import AppException
from libs.fields_translater import FieldsTranslater
from ui.page_elements.condition_box import ConditionBox
from ui.page_elements.condition_group import ConditionGroup
from ui.page_elements.detail_page import DetailPage
from ui.wrapper.dialog_like_widget import create_dialog_like_widget

from .pageUI import Ui_Form


class Page1_x(QWidget):
    model = None
    members_model = None
    summary = {}
    need_pic = False
    title: str = None

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_selected = set()
        self.sort_field = 'id'
        self.sort_order = 'asc'
        self.default_conditions = {}
        self.dialog_parent = self
        if self.model:
            self.translator = FieldsTranslater(self.model)
            self.condition_group = ConditionGroup(self.translator.to_text(self.model.field))
            self.condition_boxes = []
        # label_title
        self.ui.label_title.setText("%s人员信息查询/登记" % self.title)
        # button_search
        icon = QIcon("./static/svg/search.svg")
        self.ui.button_search.setIcon(icon)
        # btn_add_condition
        self.ui.btn_add_condition.clicked.connect(self.add_condition)
        # button_search
        self.ui.button_search.clicked.connect(self.refresh_page)
        # button_add
        self.ui.button_add.clicked.connect(self.action_add)
        # btn_select_all
        self.ui.btn_select_all.clicked.connect(self.select_all)
        # btn_select_null
        self.ui.btn_select_null.clicked.connect(self.select_null)
        # btn_mul_delete
        self.ui.btn_mul_delete.clicked.connect(self.mul_delete)

        # tableWidget
        cols = self.cols
        table_widget = self.ui.tableWidget
        table_widget.clear()
        table_widget.setColumnCount(cols)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        table_widget.horizontalHeader().setFixedHeight(30)
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
        if self.model is None:
            count = 0
        else:
            count = self.model.search()['meta']['count']
        max_page = math.ceil(count / page_size)
        self.ui.page_controller.set_max_page(max_page)
        if self.model is None:
            return
        conditions = self.get_conditions()
        data = self.model.search(page=page,
                                 page_size=page_size,
                                 order={self.sort_field: self.sort_order},
                                 **conditions)
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
                item.setText(getattr(info, self.summary[k]))
                table_widget.setItem(i, j, item)
            # detail_label
            detail_label = QLabel(self)
            detail_text = '<a href="#detail:{}">详细信息</a>'.format(info.id)
            if self.members_model:
                detail_text += '   <a href="#members:{}">团员信息</a>'.format(info.id)
            detail_label.setText(detail_text)
            detail_label.setFont(self.font())
            detail_label.linkActivated.connect(self.detail)
            detail_label.show()
            table_widget.setCellWidget(i, cols - 1, detail_label)
        table_widget.resizeColumnToContents(0)
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
        if link.startswith("#detail:"):
            self.open_detail(True, data={'id': int(link[len("#detail:"):])})
        else:
            self.open_members({'id': int(link[len("#members:"):])})

    def action_add(self):
        self.open_detail(True, data={'id': -1})
        self.refresh_page()

    def open_members(self, data):
        page_name = self.members_model.__name__
        dialog = create_dialog_like_widget(self.dialog_parent, page_name.lower())
        dialog.setFixedSize(1500, 800)
        field = self.model.__name__.lower() + '_id'
        dialog.wrapped_widget.set_default_conditions(**{field: data['id']})
        dialog.wrapped_widget.set_dialog_parent(self)
        dialog.exec_()

    def open_detail(self, enable: bool, data):
        if self.model is None:
            print("jiubei: 没有设置Model: ", self.title)
            return
        dialog = DetailPage(self.dialog_parent, self.model, self.need_pic)
        dialog.set_default_conditions(**self.default_conditions)
        dialog.show_(enable, data)
        self.refresh_page(self.ui.page_controller.page)

    def resizeEvent(self, e):
        self.refresh_conditions()

    def download_template(self):
        filename = QFileDialog.getSaveFileName(self, "选择保存地址", "./", "excel文件(*.xlsx *.xls)")[0]
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
        filename = QFileDialog.getOpenFileName(self, "导入文件", "./", "excel文件(*.xls *.xlsx)")[0]
        if filename == "":
            return
        try:
            if self.model is None:
                raise AppException("Undefined Import: %s" % self.title)
            self.model.import_(filename)
        except AppException as e:
            QMessageBox.warning(None, "导入数据", e.msg)
            return
        QMessageBox.information(None, "导入数据", "导入完毕")
        self.refresh_page()

    def export_to_file(self):
        filename = QFileDialog.getSaveFileName(self, "选择保存地址", "./", "excel文件(*.xlsx *.xls)")[0]
        if filename == "":
            return
        try:
            if self.model is None:
                raise AppException("Undefined Export: %s" % self.title)
            conditions = self.get_conditions()
            self.model.export(filename, **conditions)
        except AppException as e:
            QMessageBox.warning(None, "导入数据", e.msg)
            return
        QMessageBox.information(None, "导出数据", "导出完毕")
