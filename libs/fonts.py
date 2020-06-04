from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import QDir


def loadFonts():
    fonturl = QDir.currentPath() + "/static/fonts/"
    files = QDir(fonturl).entryList(("*.ttf", "*.ttc"))
    for file in files:
        filename = fonturl + file
        QFontDatabase.addApplicationFont(filename)
