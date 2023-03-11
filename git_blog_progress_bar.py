from progress_bar_ui import Ui_Form
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Signal, QObject
from markdown_dispose import md_dispose
class add_progress_bar(QObject):
    add_p_signal = Signal(None)
class P_Start(QDialog):
    def __init__(self, main_ui, mode):
        super().__init__()
        self.progress = 0
        self.main_ui = main_ui
        self.p_ui = Ui_Form()
        self.p_ui.setupUi(self)
        self.mode = mode
        self.md = md_dispose()
        # 判断处理类型
        if self.main_ui.ui.blog_name.text() == '':
            self.p_ui.progressBar.setRange(0, self.get_md_num())
        else:
            self.p_ui.progressBar.setRange(0, 1)
        self.p_ui.progressBar.reset()
        # 实例化信号
        self.add = add_progress_bar()
        self.add.add_p_signal.connect(self.add_progress_bar)
        self.judgment()
    def get_md_num(self):
        num = self.md.find_p_num(self.main_ui.ui.markdown_file.text())
        return num
    def add_progress_bar(self):
        self.progress += 1
        self.p_ui.progressBar.setValue(self.progress)
        if self.progress == self.get_md_num():
            self.p_ui.label.setText('已完成')
    def judgment(self):
        if self.mode == '更新本地md文件':
            self.md.dispose_md(self.main_ui.ui, self.main_ui.select_name, self.add.add_p_signal)
        elif self.mode == '还原本地md文件':
            self.md.restore_md(self.main_ui.ui, self.main_ui.select_name, self.add.add_p_signal)