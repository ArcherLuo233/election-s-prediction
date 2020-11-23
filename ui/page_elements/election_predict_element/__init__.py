import pickle

import pandas as pd
from pandas.core.frame import DataFrame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
from sklearn.preprocessing import StandardScaler

from model.area import Area

from .predict_elementUI import Ui_Dialog


class Prediction(QDialog):
    def __init__(self, parent, title, year, pro, name):
        self.title = title
        self.year = year
        self.pro = pro
        self.name = name
        super().__init__(parent)
        self.setWindowFlags(Qt.Window)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # btn_
        self.ui.btn_begin.clicked.connect(self.startpredict)
        self.ui.btn_in.clicked.connect(self.addin)
        # widget-init
        self.message = QMessageBox()
        self.message.setStandardButtons(QMessageBox.Yes)
        self.message.button(QMessageBox.Yes).setText('确认')

    def is_number(self, str):
        flag = 0
        for i in str:
            if i == '.':
                flag += 1
                if flag == 2: return False
                continue
            if i < '0' or i > '9': return False
        return True

    def getpolitical(self, type):
        if type == '民主进步党':
            lv = 1
            wu = 0
            lan = 0
        elif type == '其他':
            lv = 0
            wu = 1
            lan = 0
        elif type == '中国国民党':
            lv = 0
            wu = 0
            lan = 1
        return lv, wu, lan

    def startpredict(self):

        ruling_party = self.ui.cob_ruling.currentText()
        political_area = self.ui.cob_political_area.currentText()
        party = self.ui.cob_party.currentText()

        political_area_lv, political_area_wu, political_area_lan = self.getpolitical(political_area)
        ruling_party_lv, ruling_party_wu, ruling_party_lan = self.getpolitical(ruling_party)
        party_lv, party_wu, party_lan = self.getpolitical(party)

        times = self.ui.lineEdit.text()
        last_rate = self.ui.LineEdit_2.text()
        last_last_rate = self.ui.LineEdit_3.text()
        if not times or not self.is_number(times):
            QMessageBox.warning(None, "预测", "请检查候选人历史当选次数是否有误!")
            return
        if not last_rate or not self.is_number(last_rate):
            QMessageBox.warning(None, "预测", "请检查上届选举支持率是否有误!")
            return
        if not last_last_rate or not self.is_number(last_rate):
            QMessageBox.warning(None, "预测", "请检查上上届选举支持率是否有误!")
            return
        times = float(times)
        last_rate = float(last_rate)
        last_last_rate = float(last_last_rate)
        if self.ui.cob_whether_reselected.currentText() == '是':
            whether_reselected = 1
        else:
            whether_reselected = 0
        if self.ui.cob_gender.currentText() == '女':
            gender = 0
        else:
            gender = 1

        item = []
        item.append(political_area_lv)
        item.append(political_area_wu)
        item.append(political_area_lan)
        item.append(party_lv)
        item.append(party_wu)
        item.append(party_lan)
        item.append(ruling_party_lv)
        item.append(ruling_party_lan)
        item.append(ruling_party_wu)
        item.append(last_rate)
        item.append(last_last_rate)
        item.append(whether_reselected)
        item.append(gender)
        item.append(times)
        target = []
        target.append(item)
        df = pd.read_csv('./static/prediction/X_train.csv')
        X_train = df.values
        df = DataFrame(target)
        X_test = df.values
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_test = scaler.transform(X_test)

        with open('./static/prediction/xgb_model_isselected.pickle', 'rb') as fr:
            xgb_model = pickle.load(fr)
        y_pred_isselected = xgb_model.predict(X_test)
        with open('./static/prediction/xgb_model_rate.pickle', 'rb') as fr:
            xgb_model = pickle.load(fr)
        y_pred_rate = xgb_model.predict(X_test)

        self.ui.label_3.setText(str(round(y_pred_rate[0], 4)))

        if y_pred_isselected[0] == 1:
            self.ui.label_5.setText("当选")
        else:
            self.ui.label_5.setText("未当选")

    def addin(self):
        if (self.ui.label_3.text() == "Null"):
            QMessageBox.warning(None, "预测", "请先预测!")
            return
        rate = float(self.ui.label_3.text())
        source = Area.search(name=self.title)['data'][0]
        data = Area.search(name=self.title)['data'][0].extra
        for i in data:
            fg = 1
            if str(i["year"]) == self.year:
                allnumber = i["valid_number"]
                for j in i["projects"]:
                    if str(j["name"]) == self.pro:
                        for k in j["people"]:
                            if str(k["nickname"]) == self.name:
                                fg = 0
                                k['YoY'] = round(allnumber * rate)
                                break
                    if fg == 0: break
            if fg == 0: break
        # source.extra=data #待修改
        source.modify(extra=data)
        QMessageBox.warning(None, "预测", "填入成功!")
