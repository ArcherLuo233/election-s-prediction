from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import (QFileDialog, QLabel, QMessageBox, QSizePolicy,
                             QSpacerItem, QWidget)

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


class Pagejgxq(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dialog = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data_id = 0
        self.del_mode = False
        self.name = ''
        self.summary = "测试文本" * 20
        self.back_page = 'jg'
        self.staff_names = JG.staff_names
        self.staff_info = {i: [] for i in self.staff_names.keys()}
        self.type = None
        self.ui.pushButton.clicked.connect(self.go_back)
        self.ui.btn_modify_name.clicked.connect(self.modify_name)
        self.ui.btn_modify_summary.clicked.connect(self.modify_summary)
        self.ui.btn_append.clicked.connect(self.append)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_export.clicked.connect(self.export_word)
        self.ui.btn_del_mode.clicked.connect(self.switch_del_mode)
        self.ui.widget.exclude = JG.combo_field['type']['exclude']
        self.ui.widget.set_items(JG.combo_field['type']['items'])

    @property
    def remark(self):
        return self.ui.textedit_remark.toPlainText()

    @remark.setter
    def remark(self, text):
        self.ui.textedit_remark.setPlainText(text)

    @property
    def type(self):
        return self.ui.widget.selected_items

    @type.setter
    def type(self, val):
        self.ui.widget.selected_items = val

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

    def set_back_page(self, pagename):
        self.back_page = pagename

    def refresh_data(self):
        if self.data_id == -1:
            data = JG()
        else:
            data = JG.search(id=self.data_id)['data'][0]
        self.name = data.name
        self.summary = data.introduction
        self.staff_info = {
            i: getattr(data, j)
            for i, j in self.staff_names.items()
        }
        self.remark = data.remark
        self.type = data.type
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
            **{
                j: self.staff_info[i]
                for i, j in self.staff_names.items()
            },
            'remark': self.remark,
            'type': self.type
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
        while self.ui.staff_layout.count():
            w = self.ui.staff_layout.takeAt(0)
            if w.widget():
                w.widget().deleteLater()
        for i, (position, infos) in enumerate(info.items()):
            label1 = QLabel(position)
            label1.setFont(self.font())
            label1.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            pal = label1.palette()
            pal.setBrush(QPalette.WindowText, QColor(122, 122, 122))
            label1.setPalette(pal)
            self.ui.staff_layout.addWidget(label1, i, 0)
            ss = ''
            for name in infos:
                if name == '':
                    continue
                ss += ' '
                ss += self.staff_info2str(position, name)
            if ss == '':
                ss = '无'
            label2 = QLabel(ss)
            label2.setFont(self.font())
            label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            label2.setWordWrap(True)
            label2.linkActivated.connect(self.handle_link)
            self.ui.staff_layout.addWidget(label2, i, 1)

    def go_back(self):
        link_manager.activate("#goto:" + self.back_page)

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
            # dialog.setFixedSize(1500, 800)
            dialog.exec_()

    def export_word(self):
        default_name = "./机构-{id}.docx".format(model=JG, id=self.data_id)
        filename = QFileDialog.getSaveFileName(None, "导出文档", default_name, "word文档(*.docx)")[0]
        if filename == "":
            return

        try:
            JG.export_document(self.data_id, filename)
        except Exception as e:
            # QMessageBox.warning(None, "导出数据", "导出失败,请关闭目标文件!")
            QMessageBox.warning(None, "导出数据", str(e))
            return
        QMessageBox.information(None, "导出文档", "导出完成")
