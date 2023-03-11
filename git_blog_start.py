from PySide2.QtWidgets import QWidget, QApplication, QTextEdit
from PySide2.QtCore import Signal, QObject
from git_blog_main_ui import Ui_Form
from git_blog_tools import *
from main_function import *
from markdown_dispose import *
from git_whitelist_start import W_Start
from git_blog_progress_bar import P_Start
from PySide2.QtGui import QIcon
import sys
# 创建信号
class N_out_signal(QObject):
    text_out = Signal(str, str)
class E_out_signal(QObject):
    text_out = Signal(str)
# 主程序
class Start(QWidget):
    def __init__(self):
        # 初始化界面
        super().__init__()
        self.ui = Ui_Form()
        self.select_name = '文件夹处理模式'
        self.select_out_mod = '简略输出模式'
        self.ui.setupUi(self)
        self.tools = tools()
        self.order = Order(self)
        self.md = md_dispose()
        self.tools.check_path(self.ui)
        # 实例化信号
        self.n_signal = N_out_signal()
        self.e_signal = E_out_signal()
        self.n_out = Normal_out(self.n_signal.text_out)
        self.e_out = Err_out(self.e_signal.text_out)
        # 连接信号和函数
        self.n_signal.text_out.connect(lambda massage, color=None: self.show_win(massage, color))
        self.e_signal.text_out.connect(lambda massage: self.show_win(massage, 'red'))
        # 连接按钮和函数
        self.ui.confirm_select_path.clicked.connect(self.save_path)
        self.ui.select_blog_path.clicked.connect(lambda: self.tools.select_file(self, self.ui.blog_file))
        self.ui.select_markdown_path.clicked.connect(lambda: self.tools.select_file(self, self.ui.markdown_file))
        self.ui.select_git_path.clicked.connect(lambda: self.tools.select_file(self, self.ui.git_file))
        self.ui.select_blog.clicked.connect(lambda: self.tools.select_file(self, self.ui.blog_name, mode=0))
        # 主页面按钮功能实现
        self.ui.restore_md.clicked.connect(self.restore_markdown)
        self.ui.run_local_blog.clicked.connect(lambda: self.order.run_blog(self.ui))
        self.ui.stop_run_local_blog.clicked.connect(lambda: self.order.stop_blog(self.ui))
        self.ui.updata_local_blog.clicked.connect(lambda: self.order.update_local_blog(self.ui, self.n_signal.text_out))
        self.ui.updata_markdown.clicked.connect(self.update_markdown)
        self.ui.buttonGroup.buttonClicked.connect(self.select_button)
        self.ui.file_mode.setChecked(True)
        self.ui.updata_github.clicked.connect(lambda: self.order.update_github(self.ui, self.n_signal.text_out))
        self.ui.forced_stop.clicked.connect(lambda: self.order.stop_all_work(self))
        self.ui.run_cmd.clicked.connect(lambda: self.order.run_any_order(self.ui, self.n_signal.text_out))
        self.ui.simple_out.setChecked(True)
        self.ui.buttonGroup_2.buttonClicked.connect(self.select_out)
        self.ui.whitelist_managment.clicked.connect(self.show_whitelist_win)
        self.ui.clear_out.clicked.connect(self.clear_out)
        self.ui.clear_order.clicked.connect(self.clear_order)
        # 禁止过长文本自动换行
        self.ui.cmd_orders.setLineWrapMode(QTextEdit.NoWrap)
    def clear_out(self):
        self.ui.cmd_out_massage.clear()
    def clear_order(self):
        self.ui.cmd_orders.clear()
    def update_markdown(self):
        if self.md.find_p_num(self.ui.markdown_file.text()) == 0:
            print('没有要处理的文件')
        else:
            p_ui = P_Start(self, '更新本地md文件')
            p_ui.setWindowTitle('此方进度')
            p_ui.exec_()
    def restore_markdown(self):
        if self.md.find_p_num(self.ui.markdown_file.text()) == 0:
            print('没有要处理的文件')
        elif self.select_name == '文件处理模式':
            print('文件处理模式无需还原')
        else:
            p_ui = P_Start(self, '还原本地md文件')
            p_ui.setWindowTitle('此方进度')
            p_ui.exec_()
    def select_out(self):
        self.select_out_mod = self.ui.buttonGroup_2.checkedButton().text()
    def select_button(self):
        self.select_name = self.ui.buttonGroup.checkedButton().text()
    def save_path(self):
        self.tools.save_path(self.ui)
        QMessageBox.about(window, '提示', '已成功保存')
    def show_win(self, massage, color=None):
        if color is not None:
            self.ui.cmd_out_massage.append(fr"<font color='{color}'>{massage}</font>")
        else:
            self.ui.cmd_out_massage.append(massage)
        # 防止文字越界（出现bug,会自动转到第一行）
        # self.ui.cmd_out_massage.ensureCursorVisible()
        if massage == '本地更新已完成':
            self.ui.updata_local_blog.setEnabled(True)
            for working in self.order.work:
                working.join()
        elif massage == 'github更新完成':
            self.ui.updata_github.setEnabled(True)
        elif massage == '所有命令均已执行完毕':
            self.ui.run_cmd.setEnabled(True)
        elif massage == '本地博客已关闭':
            self.ui.updata_local_blog.setEnabled(True)
        elif massage == '执行命令发生错误':
            self.ui.updata_local_blog.setEnabled(True)
            self.ui.run_cmd.setEnabled(True)
            self.ui.updata_github.setEnabled(True)
            self.ui.updata_local_blog.setEnabled(True)
    def show_whitelist_win(self):
        whitelist_win = W_Start(self)
        whitelist_win.setWindowTitle('此方白名单')
        whitelist_win.exec_()
    def closeEvent(self, event):
        self.order.stop_blog(self.ui)
        self.order.cmd(r'taskkill /IM GitBlog /F')
        event.accept()
# 一般起手式
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('bigf.ico'))
    window = Start()
    window.setWindowTitle('此方处理姬')
    window.show()
    sys.exit(app.exec_())