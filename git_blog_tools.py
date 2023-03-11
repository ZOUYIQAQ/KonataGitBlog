import os
import re
import sys
from PySide2.QtWidgets import QFileDialog
# 重写标准输入输出流函数
# 正确输出类
class Normal_out:
    # 备份输出方法
    def __init__(self, signal):
        self.save_out = sys.stdout
        sys.stdout = self
        self.signal = signal
    def write(self, massage, color=None):
        self.signal.emit(massage, color)
    def restore(self):
        sys.stdout = self.save_out
class Err_out:
    # 备份输出方法
    def __init__(self, signal):
        self.save_out = sys.stderr
        sys.stderr = self
        self.signal = signal
    def write(self, massage):
        self.signal.emit(massage)
        with open('enrror.log', 'a', encoding='utf-8') as f:
            f.write(massage)
    def restore(self):
        sys.stderr = self.save_out
class tools:
    def __init__(self):
        self.path_dictionary = {
            'hexo_bolg_path': '',
            'markdown_path': '',
            'git_path': ''
        }
    def check_path(self, ui):
        if os.path.exists('configuration.ini'):
            with open('configuration.ini', 'r', encoding='utf-8') as c:
                path_list = c.read().splitlines()
            for line in path_list:
                try:
                    self.path_dictionary[line.split(' = ')[0]] = re.findall('\"(.+)\"', line.split(' = ')[1])[0]
                except IndexError:
                    self.path_dictionary[line.split(' = ')[0]] = ''
            ui.blog_file.setText(self.path_dictionary['hexo_bolg_path'])
            ui.markdown_file.setText(self.path_dictionary['markdown_path'])
            ui.git_file.setText(self.path_dictionary['git_path'])
    def save_path(self, ui):
        self.path_dictionary['hexo_bolg_path'] = ui.blog_file.text()
        self.path_dictionary['markdown_path'] = ui.markdown_file.text()
        self.path_dictionary['git_path'] = ui.git_file.text()
        with open('configuration.ini', 'w', encoding='utf-8') as c:
            for name, path in self.path_dictionary.items():
                c.write(f'{name} = \"{path}\"\n')
    def select_file(self, ui, line_edit, mode=1):
        if mode == 1:
            file_path = QFileDialog.getExistingDirectory(ui, '选择文件夹')
            if not file_path == '':
                new_file_path = re.sub(r'/', r'\\', file_path)
                line_edit.setText(f'{new_file_path}')
        else:
            dir_path = QFileDialog.getOpenFileNames(
                ui,
                '请选择markdown文件',
                os.getcwd(),
                'md文件类型(*.md)'
            )
            if not dir_path == ([], ''):
                new_dir_path = re.sub(r'/', r'\\', dir_path[0][0])
                line_edit.setText(f'{new_dir_path}')