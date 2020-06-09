import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QLabel, QMessageBox,
                             QTableWidgetItem, QWidget)

from config.settings import DEFAULT_PAGE_SIZE
from libs.exception import AppException
from libs.FieldsTranslater import FieldsTranslater
from ui.page_elements.ConditionBox import ConditionBox
from ui.page_elements.detailPage import DetailPage

from .pageUI import Ui_Form


class Page1_x(QWidget):
    model = None
    summary = {}
    need_pic = True

    def __init__(self, title: str, alias: str = None):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.title = title
        self.alias = alias
        self.id_selected = set()
        if self.model:
            self.translator = FieldsTranslater(self.model)
        self.condition_boxes = []
        # label_title
        self.ui.label_title.setText("%s人员信息查询/登记" % title)
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

        # detail_page
        if self.model is not None:
            self.dialog = DetailPage(self, self.model, self.need_pic)
        else:
            self.dialog = None

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
        box = ConditionBox()
        if self.model:
            box.set_fields(self.translator.to_text(self.model.field))
        box.delete_clicked.connect(self.del_condition)
        self.condition_boxes.append(box)
        self.refresh_conditions()

    def del_condition(self):
        sender = self.sender()
        self.condition_boxes.remove(sender)
        self.refresh_conditions()
        sender.delete_clicked.disconnect(self.del_condition)
        sender.deleteLater()

    def refresh_conditions(self):
        if not self.condition_boxes:
            return
        col = (self.width() - 100) // 400
        layout = self.ui.layout_conditions
        cnt = layout.count()
        for i in range(0, cnt):
            layout.takeAt(i)
        for i, w in enumerate(self.condition_boxes):
            layout.addWidget(w, i // col, i % col)
        print(self.condition_boxes[0].width())

    @property
    def cols(self):
        return len(self.summary) + 3

    def refresh_page(self, page: int = 1, page_size=DEFAULT_PAGE_SIZE):
        if self.model is None:
            count = 0
        else:
            count = self.model.search()['meta']['count']
        max_page = math.ceil(count / page_size)
        self.ui.page_controller.setMaxPage(max_page)
        data = {}
        for w in self.condition_boxes:
            c = w.get()
            field = self.translator.to_field(c['field'])
            data[field] = c['val']
        if self.model is None:
            return
        data = self.model.search(page=page, page_size=page_size, **data)
        self.refresh_table(data['data'], page_size)

    def refresh_table(self, records: list, page_size=DEFAULT_PAGE_SIZE):
        self.id_selected = set()
        cols = self.cols
        table_widget = self.ui.tableWidget
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
            detail_label.setText('<a href="#detail:{}">详细信息</a>'.format(info.id))
            detail_label.setFont(self.font())
            detail_label.linkActivated.connect(self.detail)
            detail_label.show()
            table_widget.setCellWidget(i, cols - 1, detail_label)
        table_widget.resizeColumnToContents(0)

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

    def detail(self, link):
        self.open_dialog(True, data={'id': int(link[len("#detail:"):])})

    def action_add(self):
        self.open_dialog(True, data={'id': -1})
        self.refresh_page()

    def open_dialog(self, enable: bool, data):
        if self.model is None:
            print("jiubei: 没有设置Model: ", self.title)
            return
        self.dialog.show_(enable, data)
        self.refresh_page(self.ui.page_controller.page)

    def resizeEvent(self, e):
        if self.dialog:
            self.dialog.locationDialog()
        self.refresh_conditions()

    def closeEvent(self, e):
        if self.dialog:
            self.dialog.close()

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
                raise Exception("Undefined Import: %s" % self.title)
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
                raise Exception("Undefined Export: %s" % self.title)
            self.model.export(filename)
        except AppException as e:
            QMessageBox.warning(None, "导入数据", e.msg)
            return
        QMessageBox.information(None, "导出数据", "导出完毕")
