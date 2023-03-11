import subprocess
import re
import threading
import os
import sys
# from multiprocessing import Process, Queue
from PySide2.QtWidgets import QMessageBox
# 重写Process来防止代码大改
# class My_threading(Process):
#     def __init__(self, func, args):
#         super(My_threading, self).__init__()
#         self.func = func
#         self.args = args
#         self.queue = Queue()
#     def run(self):
#         result = self.func(*self.args)
#         self.queue.put(result)
#     def get_result(self):
#         return self.queue
# 重写threading增加获取返回函数
class My_threading(threading.Thread):
    def __init__(self, func, args=()):
        super(My_threading, self).__init__()
        self.result = None
        self.func = func
        self.args = args
    def run(self):
        self.result = self.func(*self.args)
    def stop(self):
        sys.exit()
    def get_result(self):
        return self.result
class Order:
    def __init__(self, mian):
        self.work = []
        self.main_win = mian
        self.mian = mian.ui
    # 便于调用命令
    def cmd(self, order, signal=None, massage=None):
        # 检查地址并发出警告
        if self.mian.blog_file.text() == '' or self.mian.markdown_file.text() == '' or self.mian.git_file.text() == '':
            # 使用标准输出流打印文字以便于更换颜色
            sys.stdout.write('警告，配置未填写完成', color='orange')
        # 添加环境变量
        # 拷贝环境变量
        env = os.environ.copy()
        git_root_path = self.mian.git_file.text()
        blog_driver = re.findall(r'^\w:', self.mian.blog_file.text())[0]
        git_path = []
        git_path.append(os.path.join(git_root_path, r'bin'))
        git_path.append(os.path.join(git_root_path, r'cmd'))
        git_path.append(os.path.join(git_root_path, r'mingw64\libexec\git-core'))
        git_path.append(os.path.join(git_root_path, r'mingw64\bin'))
        for git in git_path:
            env['PATH'] += git + os.pathsep
        run = subprocess.Popen(
            f'{blog_driver} && cd {self.mian.blog_file.text()} && '+order,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            env=env
        )
        nout, eout = run.communicate()
        if self.main_win.select_out_mod == '详细输出模式':
            # 使用标准输出流打印文字以便于更换颜色
            sys.stdout.write('执行的命令为；')
            sys.stdout.write('-----------------', color='navy')
            sys.stdout.write(f'{blog_driver} && cd {self.mian.blog_file.text()} && ' + order, color='fuchsia')
            sys.stdout.write('-----------------', color='navy')
            try:
                print(nout.decode())
                # 使用标准输出流打印文字以便于更换颜色
                sys.stdout.write(eout.decode(), color='red')
                # print(eout.decode())
            except:
                print('系统输出不支持utf-8编码, 以下是gbk编码')
                try:
                    print(nout.decode('gbk'))
                    # 使用标准输出流打印文字以便于更换颜色
                    sys.stdout.write(eout.decode('gbk'), color='red')
                    # print(eout.decode('gbk'))
                except:
                    print('同时也不支持gbk编码，下面是源码')
                    print(nout)
                    # 使用标准输出流打印文字以便于更换颜色
                    sys.stdout.write(eout, color='red')
                    # print(eout)
        # 判断是否存在信号以便于传递信号
        if signal is not None and eout == '':
            signal.emit(massage, None)
        elif signal is not None and eout != '':
            signal.emit('执行命令发生错误', 'red')
        return nout, eout
    # 显示更多命令,暂时弃用
    def look_more_order(self, text_win):
        with open('more_order.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        text_win.append(text)
        text_win.ensureCursorVisible()
    # 开始本地博客运行
    def run_blog(self, ui):
        ui.run_cmd.setEnabled(False)
        ui.updata_github.setEnabled(False)
        ui.run_local_blog.setEnabled(False)
        ui.updata_local_blog.setEnabled(False)
        blog_path = ui.blog_file.text()
        blog_run = My_threading(func=self.cmd, args=(f'cd {blog_path} && hexo s', ))
        blog_run.start()
        self.work.append(blog_run)
        print('请访问 http://localhost:4000/ 来查看本地博客')
    # 停止博客
    def stop_blog(self, ui):
        ui.run_cmd.setEnabled(True)
        ui.updata_github.setEnabled(True)
        ui.run_local_blog.setEnabled(True)
        nout, eout = self.cmd('netstat -ano | findstr :4000')
        out_list = nout.decode().splitlines()
        run_port = []
        for line in out_list:
            if not re.findall('LISTENING +(\d+)', line) == []:
                run_port.append(re.findall('LISTENING +(\d+)', line)[0])
        for port in run_port:
            self.cmd(fr'taskkill /PID {port} /F')
        for working in self.work:
            working.join()
        print('本地博客已关闭')
    # 更新本地博客网页文件
    def update_local_blog(self, ui, signal):
        print('本地更新已开始')
        blog_path = ui.blog_file.text()
        ui.updata_local_blog.setEnabled(False)
        run_update_local = My_threading(func=self.cmd, args=(f'cd {blog_path} && hexo c && hexo g', signal, '本地更新已完成'))
        run_update_local.start()
        self.work.append(run_update_local)
    def update_github(self, ui, signal):
        ui.updata_github.setEnabled(False)
        print('请稍等，少女祈祷中...')
        up_github_work = My_threading(func=self.cmd, args=('hexo c && hexo g && hexo d', signal, 'github更新完成'))
        up_github_work.start()
        self.work.append(up_github_work)
    def stop_all_work(self, main):
        select = QMessageBox.information(
            main,
            '警告',
            '确定要强制关闭所有任务吗\n这可能导致不可预知的问题\n同时也会关闭本程序',
            buttons=QMessageBox.Yes | QMessageBox.No
        )
        if select == QMessageBox.Yes:
            self.stop_blog(main.ui)
            self.cmd(r'taskkill /IM GitBlog /F')
            self.cmd(r'taskkill /IM python.exe /F')
        else:
            pass
    def run_any_order(self, ui, signal):
        n_order = ui.cmd_orders.toPlainText()
        if n_order != '':
            all_order = n_order.splitlines()
            run_orders = ' && '.join(all_order)
            print('自定义命令开始执行，少女祈祷中...')
            run_any_orders = My_threading(func=self.cmd, args=(run_orders, signal, '所有命令均已执行完毕'))
            run_any_orders.start()
            self.work.append(run_any_orders)
            ui.run_cmd.setEnabled(False)
        else:
            print('内容空空')