from model.ts import TS
from ui.widgets.subpages.Page1_x import Page1_x


class Page1_6(Page1_x):
    def __init__(self):
        Page1_x.__init__(self, "台属", "ts")

    def importDataFromFile(self, filename):
        TS.import_(filename)

    def exportDataToFile(self, filename):
        TS.export(filename)
