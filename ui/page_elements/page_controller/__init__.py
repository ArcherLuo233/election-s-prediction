from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QWidget

from .PageControllerUI import Ui_Form


class PageController(QWidget):
    pageChanged = pyqtSignal(int)

    def __init__(self, parent=None, page: int = 1, maxpage: int = 1):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_goto.clicked.connect(self.goto_clicked)
        self.ui.buttonGroup.buttonClicked.connect(self.page_change)
        self.ui.button_prev.clicked.connect(self.prev_page)
        self.ui.button_next.clicked.connect(self.next_page)
        self.page = page
        self.maxpage = maxpage
        self.set_max_page(maxpage)

    def refresh(self):  # noqa: C901
        self.ui.label_leftdot.hide()
        self.ui.label_rightdot.hide()
        while self.ui.layout_middle.count():
            but = self.ui.layout_middle.takeAt(0).widget()
            self.ui.buttonGroup.removeButton(but)
            self.ui.layout_middle.removeWidget(but)
            but.close()
            but.deleteLater()
        if self.maxpage == 1:
            self.ui.button_right.hide()
        else:
            self.ui.button_right.show()
        left: int = self.page - 2
        right: int = self.page + 2
        if left <= 2:
            right = min(5, self.maxpage)
        if right >= self.maxpage - 1:
            left = max(1, self.maxpage - 4)
        if left <= 1:
            left = 2
        if right >= self.maxpage:
            right = self.maxpage - 1
        if left <= right:
            for i in range(left, right + 1):
                but = QPushButton(self)
                but.setText(str(i))
                but.setCheckable(True)
                but.setFont(self.font())
                but.setCursor(Qt.PointingHandCursor)
                if i == self.page:
                    but.setChecked(True)
                self.ui.layout_middle.addWidget(but)
                self.ui.buttonGroup.addButton(but)
        if self.page == 1:
            self.ui.button_left.setChecked(True)
        elif self.page == self.maxpage:
            self.ui.button_right.setChecked(True)
        if left >= 3:
            self.ui.label_leftdot.show()
        if right <= self.maxpage - 2:
            self.ui.label_rightdot.show()

    def page_change(self, x):
        if isinstance(x, int):
            page = x
        elif isinstance(x, str):
            page = int(x)
        else:
            page = int(x.text())
        page = max(1, page)
        page = min(self.maxpage, page)
        if self.page != page:
            self.page = page
            self.ui.spinBox.setValue(page)
            self.refresh()
            self.pageChanged.emit(page)

    def set_page(self, page):
        self.page_change(page)

    def next_page(self):
        self.set_page(self.page + 1)

    def prev_page(self):
        self.set_page(self.page - 1)

    def set_max_page(self, maxpage: int):
        maxpage = max(1, maxpage)
        self.maxpage = maxpage
        self.ui.label.setText("共 %d 页" % maxpage)
        self.ui.button_right.setText(str(maxpage))
        if maxpage < self.page:
            self.page_change(1)
        self.ui.spinBox.setRange(1, maxpage)
        self.refresh()

    def goto_clicked(self):
        self.set_page(self.ui.spinBox.value())
