from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPalette, QPixmap
from PyQt5.QtWidgets import QMessageBox, QWidget

from libs.enumrations import UserPermission
from libs.exception import AppException
from libs.g import g
from libs.page_magager import PageManager
from model.user import User

from .pageUI import Ui_Form


class LoginPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.icon_un.setPixmap(QPixmap("./static/svg/un.svg"))
        self.ui.icon_psd.setPixmap(QPixmap("./static/svg/psd.svg"))
        self.ui.lineEdit_un.returnPressed.connect(self.ui.lineEdit_psd.setFocus)
        self.ui.lineEdit_psd.returnPressed.connect(self.login)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.btn_jg.clicked.connect(self.open_jg)
        self.ui.btn_ry.clicked.connect(self.open_ry)
        self.ui.btn_dq.clicked.connect(self.open_dq)
        self.ui.btn_logout.clicked.connect(self.logout)
        self.ui.widget_main.hide()
        self.setFixedWidth(1100)
        self.ui.cb_target.currentTextChanged.connect(self.search_method_changed)
        self.search_method_changed(self.ui.cb_target.currentText())
        self.ui.xiangxi_sf.set_items([
            '基层', '青年', '商界', '学界', '政界'
        ])
        self.ui.xiangxi_sf.ui.pushButton.setCursor(Qt.PointingHandCursor)
        self.ui.xiangxi_sf.setFont(self.font())
        with open("./static/qss/login.qss") as f:
            s = f.read()
            self.setStyleSheet(s)
        try:
            debug = g.debug
            if debug:
                self.ui.lineEdit_un.setText("admin")
                self.ui.lineEdit_psd.setText("admin")
        except AttributeError:
            pass

    def paintEvent(self, e):
        pal = self.palette()
        pixmap = QPixmap("./static/assets/login.jpeg").scaled(self.size())
        pal.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(pal)
        if not g.current_user:
            self.ui.widget_main.hide()
            self.ui.loginWidget.show()
        else:
            self.ui.loginWidget.hide()
            self.ui.widget_main.show()

    def login(self):
        un = self.ui.lineEdit_un.text()
        psd = self.ui.lineEdit_psd.text()
        try:
            user = User.login(un, psd)
        except AppException as e:
            QMessageBox.warning(None, "登录失败", e.msg)
            return
        g.current_user = user
        self.update()

    def open_jg(self):
        menu = [("机构信息", "3", {})]
        self.open_main(menu)

    def open_ry(self):
        menu = [
            (
                "在绍台胞", "tstg", {
                    "台商台干": "tstg",
                    "就业创业": "jycy",
                    "其他": "qt"
                }
            ),
            ("重要人士", "zyrs", {}),
            ("陆配", "lp", {}),
            ("陆生", "ls", {}),
            ("台属", "ts", {}),
            ("居住证人员", "jzz", {}),
            (
                "来访台胞", "lftz", {
                    "基层": "lftz_jc",
                    "青年": "lftz_qn",
                    "商界": "lftz_sj",
                    "学界": "lftz_xj",
                    "政界": "lftz_zj"
                }
            ),
            ("公务团组", "gwtz", {}),
            ("商务团组", "swtz", {}),
        ]
        self.open_main(menu)

    def open_dq(self):
        menu = [
            ("地区信息", "2_0",
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
              })
        ]
        self.open_main(menu)

    def open_main(self, menu):
        main_widget = PageManager.get_page("Main")
        main_widget.refresh_user()
        main_widget.set_menu(menu)
        main_widget.showMaximized()
        self.close()

    def logout(self):
        g.current_user = None
        self.update()

    def search_method_changed(self, s):
        if s == '模糊搜索':
            self.ui.frame_xiangxi.hide()
            self.ui.frame_mohu.show()
        else:
            self.ui.frame_mohu.hide()
            self.ui.frame_xiangxi.show()
