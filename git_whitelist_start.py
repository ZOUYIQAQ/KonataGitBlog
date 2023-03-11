from whitelists_management_ui import Ui_Form
from PySide2.QtWidgets import QDialog, QListWidget, QMessageBox, QFileDialog
from PySide2.QtGui import QDragEnterEvent, QDropEvent
from PySide2.QtCore import Signal, QObject
import os
import re
# 定义增加列表信号
class Add_List(QObject):
    add_list = Signal(str)
class W_Start(QDialog):
    # 初始化
    def __init__(self, main_win):
        super().__init__()
        self.main_win = main_win
        self.w_ui = Ui_Form()
        self.w_ui.setupUi(self)
        self.add_ = Add_List()
        # 允许拖拽文件
        self.setAcceptDrops(True)
        # 设置列表为多选模式
        self.w_ui.whitelist.setSelectionMode(QListWidget.MultiSelection)
        # 信号相关
        self.add_.add_list.connect(self.add_list_fuc)
        # 按钮点击
        self.w_ui.del_wheitlist.clicked.connect(self.del_list_fuc)
        self.w_ui.save_wheitlist.clicked.connect(self.save_list_fuc)
        self.w_ui.add_whitelist.clicked.connect(self.add_list_fuc_win)
        # 初始化列表
        self.initialize_list()
    def dragEnterEvent(self, event:QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()
    def dropEvent(self, event:QDropEvent):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.add_.add_list.emit(file_path)
    def add_list_fuc(self, path):
        w_list = []
        for i in range(self.w_ui.whitelist.count()):
            w_list.append(self.w_ui.whitelist.item(i).text())
        new_path = re.sub(r'/', r'\\', path)
        if new_path not in w_list and new_path.endswith('.md'):
            self.w_ui.whitelist.addItem(f'{new_path}')
    def del_list_fuc(self):
        for path in self.w_ui.whitelist.selectedItems():
            select_num = self.w_ui.whitelist.row(path)
            self.w_ui.whitelist.takeItem(select_num)
    def save_list_fuc(self):
        w_list = []
        for i in range(self.w_ui.whitelist.count()):
            w_list.append(self.w_ui.whitelist.item(i).text())
        all_path = '\n'.join(w_list)
        with open('whitelists.ini', 'w', encoding='utf-8') as f:
            f.write(all_path)
        QMessageBox.about(self, '提示', '白名单已成功更新并保存')
    def initialize_list(self):
        with open('whitelists.ini', 'r', encoding='utf-8') as f:
            all_path = f.read().splitlines()
        for path in all_path:
            self.add_list_fuc(path)
    def add_list_fuc_win(self):
        filepath, _ = QFileDialog.getOpenFileNames(
            self,
            '选择想要加入白名单的文件',
            os.getcwd(),
            'md文件类型(*.md)'
        )
        if not filepath == []:
            for path in filepath:
                self.add_list_fuc(path)
    def closeEvent(self, event):
        now_all_path = []
        with open('whitelists.ini', 'r', encoding='utf-8') as f:
            local_all_path = f.read().splitlines()
        for i in range(self.w_ui.whitelist.count()):
            now_all_path.append(self.w_ui.whitelist.item(i).text())
        if not local_all_path == now_all_path:
            select = QMessageBox.information(
                self,
                '警告',
                '当前文件尚未应用和保存，确定要关闭吗？',
                buttons=QMessageBox.Yes | QMessageBox.No
            )
            if select == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()