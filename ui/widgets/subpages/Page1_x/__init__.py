import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QLabel, QMessageBox,
                             QTableWidget, QTableWidgetItem, QWidget)

from config.settings import DEFAULT_PAGE_SIZE
from libs.exception import AppException
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
        # label_title
        self.ui.label_title.setText("%s人员信息查询/登记" % title)
        # button_search
        icon = QIcon("./static/svg/search.svg")
        self.ui.button_search.setIcon(icon)
        # button_add
        self.ui.button_add.clicked.connect(self.action_add)

        # tableWidget
        cols = len(self.summary) + 2
        table_widget = self.ui.tableWidget
        table_widget.clear()
        table_widget.setColumnCount(cols)
        table_widget.setSortingEnabled(True)
        table_widget.setSelectionMode(QTableWidget.NoSelection)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget.horizontalHeader().setFixedHeight(30)
        table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # set-header
        item = QTableWidgetItem()
        item.setText("编号")
        table_widget.setHorizontalHeaderItem(0, item)
        for i, text in enumerate(self.summary.keys(), 1):
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
        if self.model is None:
            count = 0
        else:
            count = self.model.search()['meta']['count']
        page_size = DEFAULT_PAGE_SIZE
        max_page = math.ceil(count / page_size)
        self.ui.page_controller.setMaxPage(max_page)
        self.ui.page_controller.pageChanged.connect(self.refresh_page)
        # refresh-table
        self.refresh_page()

    def refresh_page(self, page: int = 1):
        # todo:custom search
        self.refresh_table(page)

    def refresh_table(self, page=1, page_size=DEFAULT_PAGE_SIZE, data=None):
        if data is None:
            data = dict()
        if self.model is None:
            return
        cols = len(self.summary) + 2
        table_widget = self.ui.tableWidget
        table_widget.clearContents()
        table_widget.setRowCount(page_size)
        # load data
        data = self.model.search(page=page, page_size=page_size, **data)
        for i, info in enumerate(data['data']):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled)
            item.setData(Qt.DisplayRole, info.id)
            table_widget.setItem(i, 0, item)
            for j, k in enumerate(self.summary.keys(), 1):
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled)
                item.setText(getattr(info, self.summary[k]))
                table_widget.setItem(i, j, item)
            # detail_label
            detail_label = QLabel(self)
            detail_label.setText('<a href="#detail:{}">详细信息</a>'.format(info.id))
            detail_label.setFont(self.font())
            detail_label.linkActivated.connect(self.detail)
            detail_label.show()
            table_widget.setCellWidget(i, cols - 1, detail_label)

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
