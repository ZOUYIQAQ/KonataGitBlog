# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'git_blog_main_ui.ui'
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
        Form.resize(572, 505)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.clear_order = QPushButton(self.tab_2)
        self.clear_order.setObjectName(u"clear_order")

        self.horizontalLayout_3.addWidget(self.clear_order)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.cmd_orders = QTextEdit(self.tab_2)
        self.cmd_orders.setObjectName(u"cmd_orders")

        self.verticalLayout_3.addWidget(self.cmd_orders)

        self.run_cmd = QPushButton(self.tab_2)
        self.run_cmd.setObjectName(u"run_cmd")

        self.verticalLayout_3.addWidget(self.run_cmd)

        self.restore_md = QPushButton(self.tab_2)
        self.restore_md.setObjectName(u"restore_md")

        self.verticalLayout_3.addWidget(self.restore_md)

        self.run_local_blog = QPushButton(self.tab_2)
        self.run_local_blog.setObjectName(u"run_local_blog")

        self.verticalLayout_3.addWidget(self.run_local_blog)

        self.stop_run_local_blog = QPushButton(self.tab_2)
        self.stop_run_local_blog.setObjectName(u"stop_run_local_blog")

        self.verticalLayout_3.addWidget(self.stop_run_local_blog)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.clear_out = QPushButton(self.tab_2)
        self.clear_out.setObjectName(u"clear_out")

        self.horizontalLayout_9.addWidget(self.clear_out)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.cmd_out_massage = QTextBrowser(self.tab_2)
        self.cmd_out_massage.setObjectName(u"cmd_out_massage")

        self.verticalLayout_4.addWidget(self.cmd_out_massage)

        self.updata_local_blog = QPushButton(self.tab_2)
        self.updata_local_blog.setObjectName(u"updata_local_blog")

        self.verticalLayout_4.addWidget(self.updata_local_blog)

        self.updata_markdown = QPushButton(self.tab_2)
        self.updata_markdown.setObjectName(u"updata_markdown")

        self.verticalLayout_4.addWidget(self.updata_markdown)

        self.updata_github = QPushButton(self.tab_2)
        self.updata_github.setObjectName(u"updata_github")

        self.verticalLayout_4.addWidget(self.updata_github)

        self.forced_stop = QPushButton(self.tab_2)
        self.forced_stop.setObjectName(u"forced_stop")

        self.verticalLayout_4.addWidget(self.forced_stop)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.blog_file = QLineEdit(self.tab_3)
        self.blog_file.setObjectName(u"blog_file")

        self.horizontalLayout_2.addWidget(self.blog_file)

        self.select_blog_path = QPushButton(self.tab_3)
        self.select_blog_path.setObjectName(u"select_blog_path")

        self.horizontalLayout_2.addWidget(self.select_blog_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.markdown_file = QLineEdit(self.tab_3)
        self.markdown_file.setObjectName(u"markdown_file")

        self.horizontalLayout.addWidget(self.markdown_file)

        self.select_markdown_path = QPushButton(self.tab_3)
        self.select_markdown_path.setObjectName(u"select_markdown_path")

        self.horizontalLayout.addWidget(self.select_markdown_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.git_file = QLineEdit(self.tab_3)
        self.git_file.setObjectName(u"git_file")

        self.horizontalLayout_4.addWidget(self.git_file)

        self.select_git_path = QPushButton(self.tab_3)
        self.select_git_path.setObjectName(u"select_git_path")

        self.horizontalLayout_4.addWidget(self.select_git_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.blog_name = QLineEdit(self.tab_3)
        self.blog_name.setObjectName(u"blog_name")

        self.horizontalLayout_5.addWidget(self.blog_name)

        self.select_blog = QPushButton(self.tab_3)
        self.select_blog.setObjectName(u"select_blog")

        self.horizontalLayout_5.addWidget(self.select_blog)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.file_mode = QRadioButton(self.tab_3)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.file_mode)
        self.file_mode.setObjectName(u"file_mode")
        self.file_mode.setTabletTracking(False)

        self.horizontalLayout_6.addWidget(self.file_mode)

        self.dir_mode = QRadioButton(self.tab_3)
        self.buttonGroup.addButton(self.dir_mode)
        self.dir_mode.setObjectName(u"dir_mode")

        self.horizontalLayout_6.addWidget(self.dir_mode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.simple_out = QRadioButton(self.tab_3)
        self.buttonGroup_2 = QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.simple_out)
        self.simple_out.setObjectName(u"simple_out")

        self.horizontalLayout_7.addWidget(self.simple_out)

        self.complx_out = QRadioButton(self.tab_3)
        self.buttonGroup_2.addButton(self.complx_out)
        self.complx_out.setObjectName(u"complx_out")

        self.horizontalLayout_7.addWidget(self.complx_out)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.whitelist_managment = QPushButton(self.tab_3)
        self.whitelist_managment.setObjectName(u"whitelist_managment")

        self.horizontalLayout_8.addWidget(self.whitelist_managment)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.confirm_select_path = QPushButton(self.tab_3)
        self.confirm_select_path.setObjectName(u"confirm_select_path")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_select_path.sizePolicy().hasHeightForWidth())
        self.confirm_select_path.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.confirm_select_path)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u547d\u4ee4\uff1a", None))
        self.clear_order.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u547d\u4ee4", None))
        self.cmd_orders.setDocumentTitle("")
        self.cmd_orders.setMarkdown("")
        self.cmd_orders.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u8981\u6267\u884c\u7684\u547d\u4ee4\uff0c\u6bcf\u884c\u4e00\u6761", None))
        self.run_cmd.setText(QCoreApplication.translate("Form", u"\u6267\u884c\u547d\u4ee4", None))
        self.restore_md.setText(QCoreApplication.translate("Form", u"\u8fd8\u539f\u672c\u5730md\u6587\u4ef6", None))
        self.run_local_blog.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u672c\u5730\u535a\u5ba2", None))
        self.stop_run_local_blog.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f\u8fd0\u884c\u672c\u5730\u535a\u5ba2", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u4fe1\u606f\uff1a", None))
        self.clear_out.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u6d88\u606f", None))
        self.updata_local_blog.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u672c\u5730\u535a\u5ba2\u6587\u4ef6", None))
        self.updata_markdown.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u672c\u5730md\u6587\u4ef6", None))
        self.updata_github.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0github\u7aef\u535a\u5ba2\u6587\u4ef6", None))
        self.forced_stop.setText(QCoreApplication.translate("Form", u"\u5f3a\u884c\u505c\u6b62\u547d\u4ee4\u6267\u884c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u672c\u5730\u6d4b\u8bd5", None))
        self.label.setText(QCoreApplication.translate("Form", u"Hexo\u535a\u5ba2\u4f4d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.blog_file.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u535a\u5ba2\u4f4d\u7f6e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.blog_file.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f8b\u5982:D:\\software\\Hexo_blog\\Hexo", None))
        self.select_blog_path.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Markdown\u6587\u6863\u4f4d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.markdown_file.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u6587\u6863\u4f4d\u7f6e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.markdown_file.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f8b\u5982:D:\\software\\Hexo_blog\\Markdown", None))
        self.select_markdown_path.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"git\u8fd0\u884c\u6587\u4ef6\u4f4d\u7f6e", None))
        self.git_file.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f8b\u5982:D:\\software\\git", None))
        self.select_git_path.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5177\u4f53Markdown\u6587\u4ef6\u7684\u540d\u5b57", None))
        self.blog_name.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f8b\u5982:D:\\Markdown\\Hexo\u535a\u5ba2\u642d\u5efa\u6d41\u7a0b.md", None))
        self.select_blog.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.file_mode.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5939\u5904\u7406\u6a21\u5f0f", None))
        self.dir_mode.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5904\u7406\u6a21\u5f0f", None))
        self.simple_out.setText(QCoreApplication.translate("Form", u"\u7b80\u7565\u8f93\u51fa\u6a21\u5f0f", None))
        self.complx_out.setText(QCoreApplication.translate("Form", u"\u8be6\u7ec6\u8f93\u51fa\u6a21\u5f0f", None))
        self.whitelist_managment.setText(QCoreApplication.translate("Form", u"md\u6587\u4ef6\u767d\u540d\u5355\u7ba1\u7406", None))
        self.confirm_select_path.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u914d\u7f6e\u6587\u4ef6", None))
    # retranslateUi

