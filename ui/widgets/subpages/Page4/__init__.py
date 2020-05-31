from PyQt5.QtWidgets import QWidget, QLabel

from .pageUI import Ui_Form
from libs.LinkManager import link_manager


class Page4(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setInsInfo()

    def setInsInfo(self):
        info = {}
        for i in range(1, 11):
            info["机构%d" % i] = "4_%d" % i
        for text in info.keys():
            label = QLabel()
            label.setText(self.info2Str(text, info[text]))
            label.linkActivated.connect(link_manager.activate)
            self.ui.layout_ins.addWidget(label)

    @staticmethod
    def info2Str(text, page) -> str:
        return '<a href="#goto:{1}">' \
               '<span style="text-decoration: none; color:rgb(68, 126, 217);">{0}' \
               '</span></a>'.format(text, page)
