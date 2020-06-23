from PyQt5.Qt import Qt
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QDialog, QMessageBox,QHeaderView,QTableWidgetItem,QHBoxLayout,QCheckBox,QWidget,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from libs.g import g
from ui.page_elements.window_mask import WindowMask
from ui.page_elements.user_add import Useradd
from model.user import User


from .usermanagerUI import Ui_Dialog


class Usermanager(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setParent(parent)
        # mask
        self.mask_ = WindowMask(parent)
        self.mask_.close()
        # event-loop
        self.loop = QEventLoop()
        self.mask_.clicked.connect(self.loop.quit)
        # btn_
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_modify.clicked.connect(self.modify)
        self.ui.btn_adduser.clicked.connect(self.adduser)
        self.ui.btn_deluser.clicked.connect(self.deluser)
        self.ui.reload.clicked.connect(self.refresh)
        # widget-init
        self.user_add_dialog=Useradd(self)
        self.font=QtGui.QFont()
        self.font.setFamily("黑体")
        self.font.setPointSize(14)
        hor_header = self.ui.tableWidget.horizontalHeader()
        hor_header.setSectionResizeMode(QHeaderView.Stretch)
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')
        self.location_dialog()
        self.refresh()
        self.close()

    def show(self):
        self.mask_.show()
        super().show()
        self.raise_()
        self.loop.exec()
        self.close()
        self.mask_.close()

    def closeEvent(self, e):
        if self.loop.isRunning():
            self.loop.quit()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setBrush(self.palette().window())
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)
    def refresh(self):
        data=User.search(page_size=-1)
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.verticalHeader().hide()
        for index,i in enumerate(data["data"]):
            if (index>=self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.insertRow(index)
            item = QTableWidgetItem()
            item.setFont(self.font)
            item.setText(i.username)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(index, 0, item)
            item = QTableWidgetItem()
            item.setFont(self.font)
            item.setText(i.nickname)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(index, 1, item)

            item = QCheckBox(self)
            hLayout =QHBoxLayout()
            widget = QWidget()
            hLayout.addWidget(item)
            hLayout.setAlignment(Qt.AlignCenter)
            widget.setLayout(hLayout)
            if i.permission==1:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tableWidget.setCellWidget(index, 2, widget)

    def modify(self):
        row=self.ui.tableWidget.rowCount()
        for i in range(row):
            username=self.ui.tableWidget.item(i,0).text()
            nickname=self.ui.tableWidget.item(i,1).text()
            ckb=self.ui.tableWidget.cellWidget(i,2).children()[1]
            if ckb.isChecked() :
                permission=1
            else :
                permission=0
            targetuser=User.search(username=username,page_size=-1)["data"][0]
            if (targetuser.nickname!=nickname):
                targetuser.modify(nickname=nickname)

            if (targetuser.permission!=permission):
                targetuser.modify(permission=permission)

            QMessageBox.information(None, "管理用户", "保存成功")

    def adduser(self):
        self.user_add_dialog.ui.LineEdit.setText("")
        self.user_add_dialog.ui.LineEdit_2.setText("")
        self.user_add_dialog.ui.LineEdit_3.setText("")
        self.user_add_dialog.ui.LineEdit_4.setText("")
        self.user_add_dialog.show()
        self.refresh()

    def deluser(self):
        selectrow=self.ui.tableWidget.currentRow()
        if not selectrow:
            QMessageBox.warning(None, "删除用户失败", "未选定用户!")
        else :
            username = self.ui.tableWidget.item(selectrow, 0).text()
            targetuser = User.search(username=username, page_size=-1)["data"][0]
            targetuser.delete()
            QMessageBox.information(None, "管理用户", "删除成功")
            self.refresh()

    def resizeEvent(self, e):
        self.user_add_dialog.location_dialog()

    def location_dialog(self):

        self.mask_.resize(self.parent().size())
        geo = self.parent().geometry()
        width = 500
        left = (geo.width() - width) / 2
        geo.setLeft(left)
        geo.setRight(left + width)
        geo.setTop(geo.top()-200)
        geo.setBottom(geo.bottom()-600)
        self.setGeometry(geo)
