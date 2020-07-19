# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 493)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.mayor_name = QtWidgets.QLineEdit(self.widget)
        self.mayor_name.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.mayor_name.setFont(font)
        self.mayor_name.setObjectName("mayor_name")
        self.horizontalLayout_3.addWidget(self.mayor_name)
        self.btn_savemayor = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_savemayor.setFont(font)
        self.btn_savemayor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_savemayor.setObjectName("btn_savemayor")
        self.horizontalLayout_3.addWidget(self.btn_savemayor)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(40, -1, 40, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(80, 20, 0, 20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.name = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.name)
        self.vote_number = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.vote_number.setFont(font)
        self.vote_number.setObjectName("vote_number")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.vote_number)
        self.cpwl = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.cpwl.setFont(font)
        self.cpwl.setObjectName("cpwl")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cpwl)
        self.Mayor_text = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.Mayor_text.setFont(font)
        self.Mayor_text.setObjectName("Mayor_text")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Mayor_text)
        self.population = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.population.setFont(font)
        self.population.setObjectName("population")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.population)
        self.numofhouse_text = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.numofhouse_text.setFont(font)
        self.numofhouse_text.setObjectName("numofhouse_text")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.numofhouse_text)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.lab_img = QtWidgets.QLabel(self.frame_2)
        self.lab_img.setObjectName("lab_img")
        self.horizontalLayout.addWidget(self.lab_img)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.textedit_remark = QtWidgets.QPlainTextEdit(self.frame_2)
        self.textedit_remark.setObjectName("textedit_remark")
        self.verticalLayout_2.addWidget(self.textedit_remark)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_reflash = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_reflash.setFont(font)
        self.btn_reflash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reflash.setObjectName("btn_reflash")
        self.horizontalLayout_8.addWidget(self.btn_reflash)
        self.btn_findzone = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_findzone.setFont(font)
        self.btn_findzone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_findzone.setObjectName("btn_findzone")
        self.horizontalLayout_8.addWidget(self.btn_findzone)
        self.btn_election_all = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_election_all.setFont(font)
        self.btn_election_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_election_all.setObjectName("btn_election_all")
        self.horizontalLayout_8.addWidget(self.btn_election_all)
        self.btn_save = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_8.addWidget(self.btn_save)
        self.btn_savemap = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.btn_savemap.setFont(font)
        self.btn_savemap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_savemap.setObjectName("btn_savemap")
        self.horizontalLayout_8.addWidget(self.btn_savemap)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 15)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "南投县%s"))
        self.label.setText(_translate("Form", "镇长:"))
        self.btn_savemayor.setText(_translate("Form", "修改镇长"))
        self.name.setText(_translate("Form", "镇长:"))
        self.vote_number.setText(_translate("Form", "总人口:"))
        self.cpwl.setText(_translate("Form", "总户数:"))
        self.Mayor_text.setText(_translate("Form", "TextLabel"))
        self.population.setText(_translate("Form", "TextLabel"))
        self.numofhouse_text.setText(_translate("Form", "TextLabel"))
        self.lab_img.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "地区概况:"))
        self.btn_reflash.setText(_translate("Form", "刷新"))
        self.btn_findzone.setText(_translate("Form", "选区"))
        self.btn_election_all.setText(_translate("Form", "选举情况"))
        self.btn_save.setText(_translate("Form", "保存"))
        self.btn_savemap.setText(_translate("Form", "上传地图"))
