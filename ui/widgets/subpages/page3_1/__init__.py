from PyQt5.QtWidgets import QMessageBox, QWidget

from libs.enumrations import UserPermission
from libs.g import g
from libs.link_manager import link_manager
from model.jg import JG
from model.zyrs import ZYRS
from ui.page_elements.detail_page import DetailPage
from ui.wrapper.dialog_like_widget import create_dialog_like_widget

from .append_dialog import AppendDialog
from .modify_dialog import ModifyDialog
from .pages import ChoicePage
from .pageUI import Ui_Form


class Page3_1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dialog = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data_id = 0
        self.del_mode = False
        self.name = ''
        self.summary = "测试文本" * 20
        self.staff_info = {
            '理事': [],
            '监事': [],
            '代表': []
        }
        self.ui.pushButton.clicked.connect(self.go_back)
        self.ui.label_staff.linkActivated.connect(self.handle_link)
        self.ui.btn_modify_name.clicked.connect(self.modify_name)
        self.ui.btn_modify_summary.clicked.connect(self.modify_summary)
        self.ui.btn_append.clicked.connect(self.append)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_del_mode.clicked.connect(self.switch_del_mode)

    @property
    def remark(self):
        return self.ui.textedit_remark.toPlainText()

    @remark.setter
    def remark(self, text):
        self.ui.textedit_remark.setPlainText(text)

    def paintEvent(self, e):
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_save.hide()
            self.ui.btn_del_mode.hide()
            self.ui.btn_modify_name.hide()
            self.ui.btn_modify_summary.hide()
            self.ui.btn_append.hide()
        else:
            self.ui.btn_save.show()
            self.ui.btn_del_mode.show()
            self.ui.btn_modify_name.show()
            self.ui.btn_modify_summary.show()
            self.ui.btn_append.show()

    def switch_del_mode(self):
        self.del_mode = not self.del_mode
        self.refresh()

    def delete(self, type_, name):
        self.staff_info[type_].remove(name)
        self.refresh()

    def set_data_id(self, id_):
        self.data_id = id_
        self.refresh_data()

    def refresh_data(self):
        if self.data_id == -1:
            data = JG()
        else:
            data = JG.search(id=self.data_id)['data'][0]
        self.name = data.name
        self.summary = data.introduction
        self.staff_info = {
            '理事': data.director,
            '监事': data.supervisor,
            '代表': data.representative
        }
        self.remark = data.remark
        self.refresh()

    def modify_name(self):
        dialog = ModifyDialog(self, self.name)
        res = dialog.show_()
        if res is None:
            return
        self.name = res
        self.refresh()

    def modify_summary(self):
        dialog = ModifyDialog(self, self.summary)
        res = dialog.show_()
        if res is None:
            return
        self.summary = res
        self.refresh()

    def append(self):
        dialog = AppendDialog(self, self.staff_info.keys())
        res = dialog.show_()
        if res is None:
            return
        self.staff_info[res[0]].append(res[1])
        self.refresh()

    def save(self):
        data = {
            'name': self.name,
            'introduction': self.summary,
            'director': self.staff_info['理事'],
            'supervisor': self.staff_info['监事'],
            'representative': self.staff_info['代表'],
            'remark': self.remark
        }
        if self.data_id == -1:
            JG.create(**data)
        else:
            model = JG.search(id=self.data_id)['data'][0]
            model.modify(**data)
        QMessageBox.information(None, "保存", "已保存")

    def refresh(self):
        self.ui.label_name.setText(self.name)
        self.ui.label_summary.setText(self.summary)
        self.set_staff_info(self.staff_info)
        self.ui.textedit_remark.setPlainText(self.remark)

    def staff_info2str(self, type_, name):
        s = '<a href="#detail:{0}">' \
            '<span style="text-decoration: none; color:rgb(68, 126, 217);">{0}' \
            '</span></a>'.format(name)
        if self.del_mode:
            s += '  <a href="#del:{type}-{name}">' \
                 '<span style="text-decoration: none; color:rgb(68, 126, 217);">删除' \
                 '</span></a>'.format(type=type_, name=name)
        return s

    def set_staff_info(self, info):
        s = str()
        for position, infos in info.items():
            s += position + ':'
            ss = ''
            for name in infos:
                if name == '':
                    continue
                ss += ' '
                ss += self.staff_info2str(position, name)
            if ss == '':
                ss = ' 无'
            s += ss
            s += '<br>'
        self.ui.label_staff.setText(s)

    def go_back(self):
        link_manager.activate("#goto:3")

    def handle_link(self, link: str):
        if link.startswith("#detail:"):
            self.detail(link[len("#detail:"):])
        elif link.startswith("#del:"):
            type_, name = link[len("#del:"):].split('-', 1)
            self.delete(type_, name)

    def detail(self, name):
        data = ZYRS.search(nickname=name)
        cnt = data['meta']['count']
        if cnt == 0:
            QMessageBox.critical(None, "查看详情", "查无此人")
        elif cnt == 1:
            dialog = DetailPage(self, ZYRS)
            dialog.show_(True, {'id': data['data'][0].id})
        else:
            widget = ChoicePage()
            widget.set_default_conditions(nickname=name)
            widget.set_dialog_parent(self)
            dialog = create_dialog_like_widget(self, widget)
            dialog.setFixedSize(1500, 800)
            dialog.exec_()
