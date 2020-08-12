from PyQt5.QtWidgets import QDialog, QLabel, QTableWidgetItem

from ui.page_elements.detail_page import DetailPage

from .pageUI import Ui_Dialog


class SearchAllPage(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data = []

        with open("./static/qss/main.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
        self.setFixedSize(800, 600)
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setStretchLastSection(True)
        hor_header.setMinimumSectionSize(100)
        hor_header.setFixedHeight(30)
        self.ui.pushButton.clicked.connect(self.done)

    def refresh_data(self, data: dict):
        self.data = []
        widget = self.ui.tableWidget
        widget.clearContents()
        row = 0
        for model_name, objects in data.items():
            for obj in objects:
                widget.insertRow(row)
                item = QTableWidgetItem()
                item.setText(model_name)
                widget.setItem(row, 0, item)
                item = QTableWidgetItem()
                item.setText(str(obj.id))
                widget.setItem(row, 1, item)
                item = QTableWidgetItem()
                if 'name' in obj.field:
                    item.setText(obj.name)
                elif 'nickname' in obj.field:
                    item.setText(obj.nickname)
                widget.setItem(row, 2, item)
                detail_label = QLabel(self)
                detail_text = '<a href="#detail:{}\">详细信息</a>'.format(row)
                if obj.ty:
                    detail_text += '   <a href="#members:{}">团员信息</a>'.format(row)
                detail_label.setText(detail_text)
                detail_label.setFont(self.font())
                detail_label.linkActivated.connect(self.link_manager)
                detail_label.show()
                widget.setCellWidget(row, 3, detail_label)
                row += 1
                self.data.append(obj)
        widget.resizeColumnsToContents()

    def link_manager(self, link):
        print(link)
        return
