from PyQt5.QtWidgets import QMessageBox, QWidget

from libs.link_manager import link_manager
from model.rs import RS
from ui.page_elements.detail_page import DetailPage
from ui.wrapper.dialog_like_widget import create_dialog_like_widget

from .pages import ChoicePage
from .pageUI import Ui_Form


class Page3_1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dialog = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data_id = 0
        self.ui.pushButton.clicked.connect(self.go_back)
        self.ui.label_staff.linkActivated.connect(self.detail)

    def set_data_id(self, id_):
        self.data_id = id_
        self.refresh_data()

    def refresh_data(self):
        self.set_staff_info()

    @staticmethod
    def staff_info2str(_id, name):
        return '<a href="#detail:{1}">' \
               '<span style="text-decoration: none; color:rgb(68, 126, 217);">{0}' \
               '</span></a>'.format(name, _id)

    def set_staff_info(self):
        info = {
            '理事': [
                '张三'
            ],
            '监事': [
                '李四',
                '人名3',
            ],
            '代表': [
                '人名4',
                '人名5',
                '人名6',
            ]
        }
        s = str()
        for position, infos in info.items():
            s += position + ':'
            for name in infos:
                s += ' '
                s += self.staff_info2str(name, name)
            s += '<br>'
        self.ui.label_staff.setText(s)

    def go_back(self):
        link_manager.activate("#goto:3")

    def detail(self, link):
        name = link[len("#detail:"):]
        data = RS.search(nickname=name)
        cnt = data['meta']['count']
        if cnt == 0:
            QMessageBox.critical(None, "查看详情", "查无此人")
        elif cnt == 1:
            dialog = DetailPage(self, RS)
            dialog.show_(True, {'id': data['data'][0].id})
        else:
            widget = ChoicePage()
            widget.set_default_conditions(nickname=name)
            widget.set_dialog_parent(self)
            dialog = create_dialog_like_widget(self, widget)
            dialog.setFixedSize(1500, 800)
            dialog.exec_()
