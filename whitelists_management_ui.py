# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whitelists_management_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 360)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.whitelist = QListWidget(Form)
        self.whitelist.setObjectName(u"whitelist")

        self.verticalLayout.addWidget(self.whitelist)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_whitelist = QPushButton(Form)
        self.add_whitelist.setObjectName(u"add_whitelist")

        self.horizontalLayout.addWidget(self.add_whitelist)

        self.del_wheitlist = QPushButton(Form)
        self.del_wheitlist.setObjectName(u"del_wheitlist")

        self.horizontalLayout.addWidget(self.del_wheitlist)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.save_wheitlist = QPushButton(Form)
        self.save_wheitlist.setObjectName(u"save_wheitlist")

        self.verticalLayout.addWidget(self.save_wheitlist)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406md\u6587\u4ef6\u767d\u540d\u5355", None))
        self.add_whitelist.setText(QCoreApplication.translate("Form", u"\u589e\u52a0", None))
        self.del_wheitlist.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.save_wheitlist.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u767d\u540d\u5355\u914d\u7f6e\u6587\u4ef6", None))
    # retranslateUi

