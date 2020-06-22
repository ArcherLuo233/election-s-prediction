from PyQt5.QtWidgets import QWidget

from libs.fields_translater import FieldsTranslater
from ui.page_elements.zone_detail_page import DetailPage

from .pageUI import Ui_Form


class Page2_x(QWidget):
    model = None
    summary = {}
    need_pic = True
    title: str = None

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.zonedialog = DetailPage(self)
        self.id_selected = set()
        if self.model:
            self.translator = FieldsTranslater(self.model)
        self.condition_boxes = []
        # label_title
        self.ui.label_title.setText("南投县%s镇" % self.title)
        # button_findzone
        self.ui.btn_findzone.clicked.connect(self.findzone)

    def findzone(self):
        self.zonedialog.show()

    def resizeEvent(self, e):
        self.zonedialog.locationDialog()
