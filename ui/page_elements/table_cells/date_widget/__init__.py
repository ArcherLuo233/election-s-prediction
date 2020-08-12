import datetime

from PyQt5.QtWidgets import QDateEdit


class DateWidget(QDateEdit):
    def __init__(self):
        super().__init__()
        self.setDisplayFormat("yyyy/MM/dd")

    def set_date(self, date):
        if date is None:
            return
        date = datetime.datetime.strptime(date, '%Y/%m/%d')
        self.setDate(date)

    def get_data(self):
        return self.text()
