from ui.page import Ui_Form
from Page1 import page1_window
from Page2 import page2_window
from Page3 import page3_window
from Page4 import page4_window
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class page_window(QtWidgets.QWidget):
    current_widget: QtWidgets.QWidget = None

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_page1.linkActivated.connect(self.linkManager)
        self.ui.label_page2.linkActivated.connect(self.linkManager)
        self.ui.label_page3.linkActivated.connect(self.linkManager)
        self.ui.label_page4.linkActivated.connect(self.linkManager)
        self.ui.label_page5.linkActivated.connect(self.linkManager)
        self.linkManager("#page1")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawRect(self.ui.widget_2.geometry())
        painter.setBrush(QColor(122, 122, 122, 50))
        geo = self.ui.widget_3.geometry()
        tl = self.ui.widget_3.mapTo(self, geo.topLeft())
        painter.drawRect(QRect(tl, geo.size()))
        super().paintEvent(a0)

    def linkManager(self, link: str):
        if "#page" in link:
            if self.current_widget:
                self.current_widget.deleteLater()
            try:
                window_class = globals()[link[1:] + '_window']
            except:
                self.current_widget = None
                return ""
            widget = window_class()
            self.ui.widget.layout().addWidget(widget)
            self.current_widget = widget
            widget.show()
        pass
