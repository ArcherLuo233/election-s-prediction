from model.jzz import JZZ
from ui.widgets.subpages.Page1_x import Page1_x


class Page1_10(Page1_x):
    def __init__(self):
        Page1_x.__init__(self, "居住证人员", "jzz")
        self.model = JZZ
