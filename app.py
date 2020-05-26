import sys

import qt_app
from ui.page_elements.NavigateMenu import NavigateMenu


def initNavigateMenu() -> NavigateMenu:
    widget = NavigateMenu()
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


def main():
    widget = initNavigateMenu()
    widget.show()
    sys.exit(qt_app.app.exec_())


if __name__ == '__main__':
    main()
