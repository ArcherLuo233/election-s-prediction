from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QWidget

from libs.enumrations import UserPermission
from libs.g import g
from libs.service import upload_file

from .pageUI import Ui_Form


class PicWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.pixmap = None
        self.path = ""
        self.ui.btn_upload.clicked.connect(self.upload_picture)

    def set_picture(self, pic_path):
        self.pixmap = QPixmap()
        if self.pixmap.load(pic_path):
            self.path = pic_path
        else:
            self.pixmap = None
            self.path = ""
        self.update()

    def get_data(self):
        return self.path

    def upload_picture(self):
        filename = QFileDialog.getOpenFileName(self, "导入文件", "./", "图片文件(*.jpg *.png)")[0]
        if filename == "":
            return
        path = upload_file(filename, True)
        self.set_picture(path)

    def paintEvent(self, e):
        if g.current_user.permission != UserPermission.Admin:
            self.ui.btn_upload.hide()
        else:
            self.ui.btn_upload.show()
        pixmap = self.pixmap
        if pixmap is None:
            self.ui.label_pic.setText("")
            return
        pixmap = pixmap.scaledToHeight(self.ui.label_pic.height(), Qt.SmoothTransformation)
        self.ui.label_pic.setPixmap(pixmap)
