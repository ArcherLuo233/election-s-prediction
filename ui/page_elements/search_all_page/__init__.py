from PyQt5.QtWidgets import QDialog, QLabel, QTableWidgetItem

from ui.page_elements.detail_page import DetailPage
from ui.wrapper.dialog_like_widget import create_dialog_like_widget

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
        self.showMaximized()
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
                elif 'company_name' in obj.field:
                    item.setText(obj.company_name)
                elif 'nickname' in obj.field:
                    item.setText(obj.nickname)
                widget.setItem(row, 2, item)
                detail_label = QLabel(self)
                detail_text = '<a href="#detail:{}\">详细信息</a>'.format(row)
                if obj.ty:
                    detail_text += '   <a href="#members:{}">人员信息</a>'.format(row)
                detail_label.setText(detail_text)
                detail_label.setFont(widget.font())
                detail_label.linkActivated.connect(self.handle_link)
                detail_label.show()
                widget.setCellWidget(row, 3, detail_label)
                row += 1
                self.data.append(obj)
        widget.resizeColumnsToContents()

    def handle_link(self, link):
        if link.startswith("#detail:"):
            self.open_detail(True, int(link[len("#detail:"):]))
        else:
            self.open_members(int(link[len("#members:"):]))

    def open_members(self, id_):
        data = self.data[id_]
        page_name = data.__class__.__name__ + "_ty"
        dialog = create_dialog_like_widget(self, page_name.lower())
        dialog.setFixedSize(1500, 800)
        field = data.__class__.__name__.lower() + '_id'
        dialog.wrapped_widget.set_default_conditions(**{field: data.id})
        dialog.wrapped_widget.set_dialog_parent(self)
        dialog.exec_()

    def open_detail(self, enable: bool, id_):
        data = self.data[id_]
        dialog = DetailPage(self, data.__class__)
        dialog.show_(enable, {'id': data.id})
