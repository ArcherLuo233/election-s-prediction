# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1607, 578)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        Form.setFont(font)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.loginWidget = QtWidgets.QWidget(Form)
        self.loginWidget.setObjectName("loginWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.loginWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.loginWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.loginWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 239, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.frame.setFont(font)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_login_form = QtWidgets.QWidget(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widget_login_form.setPalette(palette)
        self.widget_login_form.setObjectName("widget_login_form")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_login_form)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_un = QtWidgets.QWidget(self.widget_login_form)
        self.widget_un.setObjectName("widget_un")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_un)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon_un = QtWidgets.QLabel(self.widget_un)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_un.sizePolicy().hasHeightForWidth())
        self.icon_un.setSizePolicy(sizePolicy)
        self.icon_un.setMaximumSize(QtCore.QSize(30, 30))
        self.icon_un.setText("")
        self.icon_un.setPixmap(QtGui.QPixmap("../../../../../../../static/svg/un.svg\n"
                                             " "))
        self.icon_un.setScaledContents(True)
        self.icon_un.setObjectName("icon_un")
        self.horizontalLayout_4.addWidget(self.icon_un)
        self.lineEdit_un = QtWidgets.QLineEdit(self.widget_un)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_un.sizePolicy().hasHeightForWidth())
        self.lineEdit_un.setSizePolicy(sizePolicy)
        self.lineEdit_un.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_un.setFont(font)
        self.lineEdit_un.setObjectName("lineEdit_un")
        self.horizontalLayout_4.addWidget(self.lineEdit_un)
        self.verticalLayout_3.addWidget(self.widget_un)
        self.widget_psd = QtWidgets.QWidget(self.widget_login_form)
        self.widget_psd.setObjectName("widget_psd")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_psd)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_psd = QtWidgets.QLabel(self.widget_psd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_psd.sizePolicy().hasHeightForWidth())
        self.icon_psd.setSizePolicy(sizePolicy)
        self.icon_psd.setMaximumSize(QtCore.QSize(30, 30))
        self.icon_psd.setPixmap(QtGui.QPixmap("../../../../../../../static/svg/psd.svg\n"
                                              " "))
        self.icon_psd.setScaledContents(True)
        self.icon_psd.setObjectName("icon_psd")
        self.horizontalLayout.addWidget(self.icon_psd)
        self.lineEdit_psd = QtWidgets.QLineEdit(self.widget_psd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_psd.sizePolicy().hasHeightForWidth())
        self.lineEdit_psd.setSizePolicy(sizePolicy)
        self.lineEdit_psd.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_psd.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_psd.setFont(font)
        self.lineEdit_psd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_psd.setClearButtonEnabled(True)
        self.lineEdit_psd.setObjectName("lineEdit_psd")
        self.horizontalLayout.addWidget(self.lineEdit_psd)
        self.verticalLayout_3.addWidget(self.widget_psd)
        self.verticalLayout.addWidget(self.widget_login_form)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_5.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.loginWidget)
        self.widget_main = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy)
        self.widget_main.setObjectName("widget_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_main)
        self.verticalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.frame_2 = QtWidgets.QFrame(self.widget_main)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_jg = QtWidgets.QPushButton(self.frame_2)
        self.btn_jg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_jg.setObjectName("btn_jg")
        self.horizontalLayout_5.addWidget(self.btn_jg)
        self.btn_ry = QtWidgets.QPushButton(self.frame_2)
        self.btn_ry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ry.setObjectName("btn_ry")
        self.horizontalLayout_5.addWidget(self.btn_ry)
        self.btn_dq = QtWidgets.QPushButton(self.frame_2)
        self.btn_dq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_dq.setObjectName("btn_dq")
        self.horizontalLayout_5.addWidget(self.btn_dq)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.widget = QtWidgets.QWidget(self.widget_main)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.cb_target = QtWidgets.QComboBox(self.frame_3)
        self.cb_target.setObjectName("cb_target")
        self.cb_target.addItem("")
        self.cb_target.addItem("")
        self.verticalLayout_8.addWidget(self.cb_target)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 10, -1, 20)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_mohu = QtWidgets.QFrame(self.frame_3)
        self.frame_mohu.setObjectName("frame_mohu")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_mohu)
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.comboBox = QtWidgets.QComboBox(self.frame_mohu)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_11.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_mohu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_11.addWidget(self.lineEdit)
        self.verticalLayout_9.addWidget(self.frame_mohu)
        self.frame_xiangxi = QtWidgets.QFrame(self.frame_3)
        self.frame_xiangxi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_xiangxi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_xiangxi.setObjectName("frame_xiangxi")
        self.formLayout = QtWidgets.QFormLayout(self.frame_xiangxi)
        self.formLayout.setContentsMargins(-1, 0, -1, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_xiangxi)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.cb_sj = QtWidgets.QComboBox(self.frame_xiangxi)
        self.cb_sj.setObjectName("cb_sj")
        self.cb_sj.addItem("")
        self.cb_sj.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_sj)
        self.label_7 = QtWidgets.QLabel(self.frame_xiangxi)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.cb_dq = QtWidgets.QComboBox(self.frame_xiangxi)
        self.cb_dq.setObjectName("cb_dq")
        self.cb_dq.addItem("")
        self.cb_dq.addItem("")
        self.cb_dq.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_dq)
        self.cb_sf = QtWidgets.QComboBox(self.frame_xiangxi)
        self.cb_sf.setObjectName("cb_sf")
        self.cb_sf.addItem("")
        self.cb_sf.addItem("")
        self.cb_sf.addItem("")
        self.cb_sf.addItem("")
        self.cb_sf.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cb_sf)
        self.label_8 = QtWidgets.QLabel(self.frame_xiangxi)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout_9.addWidget(self.frame_xiangxi)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_10.addWidget(self.pushButton_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.btn_logout = QtWidgets.QPushButton(self.widget_main)
        self.btn_logout.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout_7.addWidget(self.btn_logout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addWidget(self.widget_main)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.label_2 = QtWidgets.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "信息管理系统"))
        self.label.setText(_translate("Form", "用户登录"))
        self.lineEdit_un.setPlaceholderText(_translate("Form", "用户名"))
        self.lineEdit_psd.setPlaceholderText(_translate("Form", "密码"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.btn_jg.setText(_translate("Form", "机构"))
        self.btn_ry.setText(_translate("Form", "人员"))
        self.btn_dq.setText(_translate("Form", "地区"))
        self.label_5.setText(_translate("Form", "全局搜索"))
        self.label_4.setText(_translate("Form", "搜索方式"))
        self.cb_target.setItemText(0, _translate("Form", "模糊搜索"))
        self.cb_target.setItemText(1, _translate("Form", "详细搜索"))
        self.comboBox.setItemText(0, _translate("Form", "按人名搜索"))
        self.comboBox.setItemText(1, _translate("Form", "按地名搜索"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入条件"))
        self.label_6.setText(_translate("Form", "时间"))
        self.cb_sj.setItemText(0, _translate("Form", "20190105"))
        self.cb_sj.setItemText(1, _translate("Form", "20201231"))
        self.label_7.setText(_translate("Form", "地区"))
        self.cb_dq.setItemText(0, _translate("Form", "地区1"))
        self.cb_dq.setItemText(1, _translate("Form", "地区2"))
        self.cb_dq.setItemText(2, _translate("Form", "地区3"))
        self.cb_sf.setItemText(0, _translate("Form", "基层"))
        self.cb_sf.setItemText(1, _translate("Form", "青年"))
        self.cb_sf.setItemText(2, _translate("Form", "商界"))
        self.cb_sf.setItemText(3, _translate("Form", "学界"))
        self.cb_sf.setItemText(4, _translate("Form", "政界"))
        self.label_8.setText(_translate("Form", "身份"))
        self.pushButton_2.setText(_translate("Form", "搜索"))
        self.btn_logout.setText(_translate("Form", "退出"))
        self.label_2.setText(_translate("Form", "信息管理系统"))
