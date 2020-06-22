from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QWidget

from libs.exception import AppException
from libs.service import upload_file

from .pageUI import Ui_Form


class PicWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.pixmap = None
        self.raw_data = b""
        self.ui.btn_upload.clicked.connect(self.upload_picture)

    def set_picture_path(self, pic_path):
        raw = upload_file(pic_path)
        self.set_picture(raw)

    def set_picture(self, raw_data):
        self.pixmap = QPixmap()
        if self.pixmap.loadFromData(raw_data):
            self.raw_data = raw_data
            self.update()
        else:
            self.pixmap = None
            self.raw_data = b""

    def get_data(self):
        return self.raw_data

    def upload_picture(self):
        filename = QFileDialog.getOpenFileName(self, "导入文件", "./", "图片文件(*.jpg *.png)")[0]
        if filename == "":
            return
        raw = upload_file(filename)
        self.set_picture(raw)

    def paintEvent(self, e):
        pixmap = self.pixmap
        if pixmap is None:
            self.ui.label_pic.setText("")
            return
        pixmap = pixmap.scaledToHeight(self.ui.label_pic.height(), Qt.SmoothTransformation)
        self.ui.label_pic.setPixmap(pixmap)
