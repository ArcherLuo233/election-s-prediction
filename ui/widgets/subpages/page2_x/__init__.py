from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import Qt

from libs.fields_translater import FieldsTranslater
from ui.page_elements.zone_detail_page import DetailPage
from PyQt5.QtWidgets import (QDialog, QHeaderView, QTableWidget,
                             QTableWidgetItem)
from .pageUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets

class Page2_x(QWidget):
    model = None
    summary = {}
    need_pic = True
    title: str = None

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.zonedialog = DetailPage(self)
        self.id_selected = set()
        if self.model:
            self.translator = FieldsTranslater(self.model)
        self.condition_boxes = []
        # label_title
        self.ui.label_title.setText("南投县%s镇" % self.title)
        # button_findzone
        self.ui.btn_findzone.clicked.connect(self.findzone)
        # init_
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)

        table_widget = self.ui.tableWidget
        table_widget.setSelectionMode(QTableWidget.NoSelection)
        item = QTableWidgetItem()
        item.setText("基本情况")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        item.setFont(font)
        item.setTextAlignment(Qt.AlignCenter)
        table_widget.setSpan(3, 0, 1, 2)
        table_widget.setItem(3, 0, item)

        item = QTableWidgetItem()
        item.setText("  日月潭位于中国台湾省阿里山以北、能高山之南的南投县鱼池乡水社村，旧称水沙连、龙湖、水社大湖、珠潭、双潭，亦名水里社。日月潭湖面海拔748米，常态面积为7.93㎞²（满水位时10㎞²），最大水深27米，湖周长约37千米，是中国台湾外来种生物最多的淡水湖泊之一。它以光华岛为界，北半湖形状如圆日，南半湖形状如弯月。2009年，日月潭入选世界纪录协会“中国台湾最大的天然淡水湖”，在清朝时即被选为台湾八大景之一，有“海外别一洞天” [1]  之称。")
        item.setFont(font)
        table_widget.setSpan(4, 0, 1, 2)
        table_widget.setItem(4,0,item)
        table_widget.setRowHeight(4, 200)
        table_widget.setWordWrap(True)

    def findzone(self):
        self.zonedialog.show()

    def resizeEvent(self, e):
        self.zonedialog.locationDialog()
