from PyQt5 import QtWidgets
import Login
import Page
import sys

app = QtWidgets.QApplication(sys.argv)
login_window = Login.login_window()
page_window = Page.page_window()