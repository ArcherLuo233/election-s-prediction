from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget,QHeaderView, QMessageBox, QTableWidgetItem,QCheckBox,QHBoxLayout

from model.user import User
from ui.page_elements.modal_dialog import ModalDialog
from ui.page_elements.user_add import UserAdd

from .usermanagerUI import Ui_Dialog


class UserManager(ModalDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(800, 800)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_modify.clicked.connect(self.modify)
        self.ui.btn_adduser.clicked.connect(self.add_user)
        self.ui.btn_deluser.clicked.connect(self.del_user)
        self.ui.reload.clicked.connect(self.refresh)
        # widget-init
        self.user_add_dialog = UserAdd(self)
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setFixedHeight(25)
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        hor_header.setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.tableWidget.resizeColumnToContents(2)
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        self.refresh()

    def refresh(self):
        data = User.search(page_size=-1)
        table_widget = self.ui.tableWidget
        table_widget.clearContents()
        for index, i in enumerate(data["data"]):
            if index >= self.ui.tableWidget.rowCount():
                table_widget.insertRow(index)
            item = QTableWidgetItem()
            item.setFont(self.font())
            item.setText(i.username)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(Qt.ItemIsEnabled)
            table_widget.setItem(index, 0, item)
            item = QTableWidgetItem()
            item.setFont(self.font())
            item.setText(i.nickname)
            item.setTextAlignment(Qt.AlignCenter)
            table_widget.setItem(index, 1, item)

            item = QCheckBox()
            hLayout = QHBoxLayout()
            widget = QWidget()
            hLayout.addWidget(item)
            hLayout.setContentsMargins(0,0,0,0)
            hLayout.setAlignment(Qt.AlignCenter)
            widget.setLayout(hLayout)
            if i.permission == 1:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            table_widget.setCellWidget(index, 2, widget)
        self.ui.tableWidget.horizontalHeader().setFont(self.font())

    def modify(self):
        row = self.ui.tableWidget.rowCount()
        for i in range(row):
            username = self.ui.tableWidget.item(i, 0).text()
            nickname = self.ui.tableWidget.item(i, 1).text()
            ckb = self.ui.tableWidget.item(i, 2)
            if ckb.checkState() == Qt.Checked:
                permission = 1
            else:
                permission = 0
            target_user = User.search(username=username, page_size=-1)["data"][0]
            if target_user.nickname != nickname:
                target_user.modify(nickname=nickname)

            if target_user.permission != permission:
                target_user.modify(permission=permission)

            QMessageBox.information(None, "管理用户", "保存成功")

    def add_user(self):
        self.user_add_dialog.ui.LineEdit.setText("")
        self.user_add_dialog.ui.LineEdit_2.setText("")
        self.user_add_dialog.ui.LineEdit_3.setText("")
        self.user_add_dialog.ui.LineEdit_4.setText("")
        self.user_add_dialog.show()
        self.refresh()

    def del_user(self):
        select_row = self.ui.tableWidget.currentRow()
        if select_row == -1:
            QMessageBox.warning(None, "删除用户失败", "未选定用户!")
        else:
            username = self.ui.tableWidget.item(select_row, 0).text()
            target_user = User.search(username=username, page_size=-1)["data"][0]
            target_user.delete()
            QMessageBox.information(None, "管理用户", "删除成功")
            self.refresh()
