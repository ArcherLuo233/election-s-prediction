from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QLabel, QMessageBox,
                             QTableWidget, QWidget)

from libs.exception import AppException
from ui.page_elements.detailPage import DetailPage

from .pageUI import Ui_Form


class Page1_x(QWidget):
    def __init__(self, title: str, alias: str = None):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.title = title
        self.alias = alias
        self.model = None
        # label_title
        self.ui.label_title.setText("%s人员信息查询/登记" % title)
        # button_search
        icon = QIcon("./static/svg/search.svg")
        self.ui.button_search.setIcon(icon)
        # page_controller
        self.ui.page_controller.setMaxPage(10)
        # button_add
        self.ui.button_add.clicked.connect(self.action_add)
        # tableWidget
        self.ui.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        # tableWidget-header
        hor_header: QHeaderView = self.ui.tableWidget.horizontalHeader()
        hor_header.setFixedHeight(30)
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # detail_label
        detail_label = QLabel(self)
        detail_label.setText('<a href="#detail:%d">详细信息</a>' % 1)
        detail_label.linkActivated.connect(self.detail)
        detail_label.show()
        self.ui.tableWidget.setCellWidget(0, 5, detail_label)
        # detail_page
        self.dialog = DetailPage(self)
        # downloadTemplate
        self.ui.btn_downloadTemplate.clicked.connect(self.downloadTemplate)
        # import
        self.ui.button_import.clicked.connect(self.importFromFile)
        # export
        self.ui.button_export.clicked.connect(self.exportToFile)

    def detail(self, link):
        self.openDialog(True, data={'id': link[len("#detail:"):]})

    def action_add(self):
        self.openDialog(True, data={'id': -1})

    def openDialog(self, enable: bool, data):
        if self.model is None:
            print("jiubei: 没有设置Model: ", self.title)
            return
        data['model'] = self.model
        self.dialog.setData(data)
        self.dialog.setEnabled(enable)
        self.dialog.show()

    def resizeEvent(self, QResizeEvent):
        self.dialog.locationDialog()

    def closeEvent(self, QCloseEvent):
        self.dialog.close()

    def downloadTemplate(self):
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

    def importDataFromFile(self, filename):
        if self.model is None:
            raise Exception("Undefined Import: %s" % self.title)
        self.model.import_(filename)

    def importFromFile(self):
        filename = QFileDialog.getOpenFileName(self, "导入文件", "./", "excel文件(*.xls *.xlsx)")[0]
        if filename == "":
            return
        try:
            self.importDataFromFile(filename)
        except AppException as e:
            QMessageBox.warning(None, "导入数据", e.msg)
            return
        QMessageBox.information(None, "导入数据", "导入完毕")

    def exportDataToFile(self, filename):
        if self.model is None:
            raise Exception("Undefined Export: %s" % self.title)
        self.model.export(filename)

    def exportToFile(self):
        filename = QFileDialog.getSaveFileName(self, "选择保存地址", "./", "excel文件(*.xlsx *.xls)")[0]
        if filename == "":
            return
        try:
            self.exportDataToFile(filename)
        except AppException as e:
            QMessageBox.warning(None, "导入数据", e.msg)
            return
        QMessageBox.information(None, "导出数据", "导出完毕")
