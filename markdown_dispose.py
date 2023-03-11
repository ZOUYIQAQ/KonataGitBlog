import re
import os
from shutil import copyfile
import threading
class md_dispose:
    def __init__(self):
        pass
    # 发现md依赖图片函数，返回列表
    def find_picture(self, md_dir_path, father_path):
        p_path = []
        with open(md_dir_path, 'rb') as f:
            picture_name = re.findall(r'!\[.+?]\((.+?)\)', f.read().decode('utf8'))
        with open(md_dir_path, 'rb') as f:
            head_picture = re.findall(r'header-img: \"(.*?)\"', f.read().decode('utf8'))
        for p_name in picture_name:
            p_path.append(os.path.join(father_path, p_name))
        for h_p_name in head_picture:
            p_path.append(os.path.join(father_path, h_p_name))
        return p_path
    # 寻找md文件,返回列表
    def find_md(self, working_path):
        md_dirs = []
        with open('whitelists.ini', 'r', encoding='utf-8') as f:
            whitelist = f.read().splitlines()
        for f in os.listdir(working_path):
            f_path = os.path.join(working_path, f)
            # 白名单在这里添加
            if os.path.exists(f_path) and os.path.isfile(f_path) and (f_path not in whitelist) and f_path.endswith('.md'):
                md_dirs.append(f_path)
        return md_dirs
    # 单个文件处理函数(文件夹模式)
    def a_dispose_md(self, markdown_path, md, bolg_md_path, singal):
        md_name = re.findall('(.+)\.md', md.split('\\')[-1])[0]
        blog_p_file = os.path.join(bolg_md_path, md_name)
        local_p_file = os.path.join(markdown_path, md_name)
        copyfile(md, os.path.join(bolg_md_path, md_name+'.md'))
        all_p = self.find_picture(md, markdown_path)
        if not all_p == []:
            os.makedirs(blog_p_file, exist_ok=True)
            os.makedirs(local_p_file, exist_ok=True)
        for p in all_p:
            if os.path.exists(p):
                copyfile(p, os.path.join(local_p_file, p.split('\\')[-1]))
                copyfile(p, os.path.join(blog_p_file, p.split('\\')[-1]))
                os.remove(p)
            else:
                print(f'{p} 不在当前文件夹，已跳过')
        print(f'{md_name} 已处理完成')
        singal.emit()
    # 单个文件处理(文件模式)
    def a_a_dispose_mod(self, markdown_path, md, bolg_md_path,singal):
        all_p = self.find_picture(md, markdown_path)
        md_name = re.findall('(.+)\.md', md.split('\\')[-1])[0]
        copyfile(md, os.path.join(bolg_md_path, md_name+'.md'))
        for p in all_p:
            if os.path.exists(p):
                copyfile(p, os.path.join(bolg_md_path, p.split('\\')[-1]))
            else:
                print(f'{p} 不在当前文件夹，已跳过')
        print(f'{md_name} 已处理完成')
        singal.emit()
    # 主函数
    def dispose_md(self, ui, mode, sinagl):
        name = ui.blog_name.text()
        markdown_path = ui.markdown_file.text()
        bolg_md_path = os.path.join(ui.blog_file.text(), 'source\\_posts')
        if name == '' and mode == '文件夹处理模式':
            print('文件夹模式')
            print('未选择具体文件，开始处理目标文件夹下所有文件')
            all_md = self.find_md(markdown_path)
            for md in all_md:
                if md.endswith('.md'):
                    work = threading.Thread(target=self.a_dispose_md, args=(markdown_path, md, bolg_md_path, sinagl))
                    work.start()
            print('所有文件均已处理完成')
        elif name != '' and mode == '文件夹处理模式':
            print('文件夹模式')
            print(f'开始处理 {name}')
            self.a_dispose_md(markdown_path, name, bolg_md_path, sinagl)
        elif name == '' and mode == '文件处理模式':
            print('文件模式')
            print('未选择具体文件，开始处理目标文件夹下所有文件')
            all_md = self.find_md(markdown_path)
            for md in all_md:
                if md.endswith('.md'):
                    work = threading.Thread(target=self.a_a_dispose_mod, args=(markdown_path, md, bolg_md_path, sinagl))
                    work.start()
        elif name != '' and mode == '文件处理模式':
            print('文件模式')
            self.a_a_dispose_mod(markdown_path, name, bolg_md_path, sinagl)
    # 还原md文件中的图片至md文件的同一文件夹
    def restore_md(self, ui, mode, signal):
        _name = ui.blog_name.text()
        work_path = ui.markdown_file.text()
        if mode == '文件处理模式':
            print('文件处理模式无需还原')
        elif mode == '文件夹处理模式':
            print('开始处理，少女祈祷中.....')
            if _name == '':
                print('未指定具体md文件，开始处理所有文件')
                # 获取所有文件
                all_md = self.find_md(work_path)
                for md in all_md:
                    if md.endswith('.md'):
                        md_name = re.findall(r'(.+?)\.md', md.split('\\')[-1])[0]
                        work = threading.Thread(target=self.a_restore_md, args=(md_name, work_path, signal))
                        work.start()
            else:
                name = re.findall(r'(.+?)\.md', _name.split('\\')[-1])[0]
                print(f'开始处理{name}')
                self.a_restore_md(name, work_path, signal)
            print('所有文件均已处理完成')
    def a_restore_md(self, md_name, work_path, signal):
        picture_path = os.path.join(work_path, md_name)
        if os.path.exists(picture_path):
            for f in os.listdir(picture_path):
                f_path = os.path.join(picture_path, f)
                new_path = os.path.join(work_path, f)
                if os.path.isfile(f_path):
                    copyfile(f_path, new_path)
            print(f'{md_name} 处理完成')
            signal.emit()
    # 发现含有图片的md文件的数量
    def find_p_num(self, work_path):
        p_num = len(self.find_md(work_path))
        for path in self.find_md(work_path):
            if len(self.find_picture(path, work_path)) == 0:
                p_num -= 1
        if p_num <= 0:
            return 0
        else:
            return p_num