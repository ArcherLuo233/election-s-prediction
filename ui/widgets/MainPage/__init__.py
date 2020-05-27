from PyQt5.QtWidgets import QWidget, QHBoxLayout
from .MainPageUI import Ui_Form
from ...page_elements.NavigateMenu import NavigateMenu
from qt_app import PageManager


class MainPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_navigate_menu(self.ui.navigation_widget)
        self.ui.main_widget.setLayout(QHBoxLayout())

    def linkManager(self, s: str):
        print(s)
        if s.startswith("#goto:"):
            w = self.ui.main_widget
            if w.layout().count():
                w.layout().takeAt(0).widget().hide()
            page_widget = PageManager.getPage(s[6:])
            if page_widget is None:
                return
            w.layout().addWidget(page_widget)
            page_widget.show()
            return

    def init_navigate_menu(self, widget) -> NavigateMenu:
        menu = [
            ("信息登记",
             {"来绍交流": "1_1",
              "台商台干": "",
              "重要人士": "",
              "陆配": "",
              "陆生": "",
              "台属": ""}),
            ("地区统计",
             {"测试文本1": "",
              "测试文本2": ""})
        ]
        for i in menu:
            j, k = i
            widget.addField(j, [(kk, k[kk], self.linkManager) for kk in k])
        widget.fields[0].switch()
        widget.fields[0].menu_labels[0].linkActivated.emit("#")
        return widget
