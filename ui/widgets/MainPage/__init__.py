from PyQt5.QtWidgets import QWidget
from .MainPageUI import Ui_Form
from ...page_elements.NavigateMenu import NavigateMenu


class MainPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_navigate_menu(self.ui.navigation_widget)

    @staticmethod
    def init_navigate_menu(widget) -> NavigateMenu:
        menu = [
            ("信息登记", ["来绍交流", "台商台干", "重要人士", "陆配", "陆生", "台属"]),
            ("地区统计", ["测试文本1", "测试文本2"])
        ]
        for i in menu:
            j, k = i
            widget.addField(j, [(kk, None) for kk in k])
        widget.fields[0].switch()
        widget.fields[0].menu_labels[0].linkActivated.emit("#")
        return widget
