from PyQt5.QtWidgets import QWidget, QHBoxLayout
from .MainPageUI import Ui_Form
from ...page_elements.NavigateMenu import NavigateMenu
from libs.PageManager import PageManager
from libs.LinkManager import link_manager


class MainPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.main_widget.setLayout(QHBoxLayout())
        with open("./static/qss/main.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
        navi_widget = self.ui.navigation_widget
        link_manager.linkActivated.connect(self.linkManager)
        self.init_navigate_menu(navi_widget)
        navi_widget.fields[0].switch()
        navi_widget.fields[0].menu_labels[0].linkActivated.emit("#goto:1_1")

    def linkManager(self, s: str):
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
            ("信息登记", "1_1",
             {"来绍交流": "1_1",
              "台商台干": "1_2",
              "重要人士": "1_3",
              "陆配": "1_4",
              "陆生": "1_5",
              "台属": "1_6",
              "公务团组": "1_7",
              "商务团组": "1_8",
              "来访团组": "1_9",
              "居住证人员": "1_10",
              }),
            ("地区统计", "2", {}),
            ("机构信息", "3", {}),
            ("人士信息", "4", {})
        ]
        for i in menu:
            title, alias, menus = i
            widget.addField(title, alias, [(menu, menus[menu]) for menu in menus])
        return widget
