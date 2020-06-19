from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from config.uicolor import UIColor as color
from libs.g import g
from libs.LinkManager import link_manager
from libs.PageManager import PageManager
from ui.page_elements.NavigateMenu import NavigateMenu

from .MainPageUI import Ui_Form


class MainPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_logout.linkActivated.connect(self.logout)
        self.ui.main_widget.setLayout(QHBoxLayout())
        with open("./static/qss/main.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
        navi_widget = self.ui.navigation_widget
        link_manager.linkActivated.connect(self.linkManager)
        self.init_navigate_menu(navi_widget)
        navi_widget.fields[0].switch()
        navi_widget.fields[0].menu_labels[0].linkActivated.emit("#goto:1_1")
        navi_widget.fields[1].switch()
        # header-palette
        self.ui.widget_header.setAutoFillBackground(True)
        pal: QPalette = self.ui.widget_header.palette()
        pal.setColor(QPalette.WindowText, color.HeaderText)
        pal.setColor(QPalette.Background, color.HeaderBackground)
        self.ui.widget_header.setPalette(pal)
        self.ui.label.setPalette(pal)
        self.ui.label_username.setPalette(pal)
        self.ui.label_logo.setPalette(pal)
        self.ui.label_logout.setStyleSheet("padding-top: 2px")
        self.ui.label_logout.setText('<a href="#logout"'
                                     'style="text-decoration:none;'
                                     'color:%s;">登出</a>' % color.HeaderText.name())

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
            ("地区统计", "2_1",
             {"炎峰里": "2_1",
              "中正里": "2_2",
              "玉峰里": "2_3",
              "明正里": "2_4",
              "和平里": "2_5",
              "中山里": "2_6",
              "敦和里": "2_7",
              "山脚里": "2_8",
              "新厝里": "2_9",
              "上林里": "2_10",
              "碧峰里": "2_11",
              "碧洲里": "2_12",
              "复兴里": "2_13",
              "北投里": "2_14",
              "石川里": "2_15",
              "加老里": "2_16",
              "新庄里": "2_17",
              "新丰里": "2_18",
              "御史里": "2_19",
              "北势里": "2_20",
              "中原里": "2_21",
              "富寮里": "2_22",
              "南埔里": "2_23",
              "坪顶里": "2_24",
              "土城里": "2_25",
              "平林里": "2_26",
              "双冬里": "2_27",
              }),
            ("机构信息", "3", {}),
            ("人士信息", "4", {})
        ]
        for i in menu:
            title, alias, menus = i
            widget.addField(title, alias, [(menu, menus[menu]) for menu in menus])
        return widget

    def refreshUser(self):
        self.ui.label_username.setText(g.current_user.nickname)

    def logout(self):
        PageManager.getPage("Login", False).show()
        self.close()
