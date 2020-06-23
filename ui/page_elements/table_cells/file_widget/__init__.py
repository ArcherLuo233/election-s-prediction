import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget

from libs.service import download_file, upload_file

from .pageUI import Ui_Form


class FileWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.path = None
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_upload.clicked.connect(self.upload)

    def set_file_path(self, path):
        self.path = path
        self.update()

    def delete(self):
        self.set_file_path(None)
        QMessageBox.information(None, "删除文件", "已删除，保存后生效")

    def upload(self):
        filename = QFileDialog.getOpenFileName(self, "上传文件", "./", "文件(*.*)")[0]
        if filename == "":
            return
        path = upload_file(filename)
        self.set_file_path(path)
        QMessageBox.information(None, "上传文件", "上传完成，保存后生效")

    def download(self):
        suffix = os.path.splitext(self.path)[1]
        default_name = "download" + suffix
        filename = QFileDialog.getSaveFileName(self, "下载文件", default_name)[0]
        if filename == "":
            return
        download_file(self.path, filename)
        QMessageBox.information(None, "下载文件", "下载完成")

    def get_data(self):
        return self.path

    def paintEvent(self, e):
        if self.path:
            self.ui.btn_delete.show()
            self.ui.btn_download.show()
        else:
            self.ui.btn_delete.hide()
            self.ui.btn_download.hide()