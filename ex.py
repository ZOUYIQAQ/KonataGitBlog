import subprocess
run_exe = subprocess.Popen(
    'tasklist',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)
n_out, e_out = run_exe.communicate()
if 'GitBlog' in n_out.decode('gbk'):
    print('程序未结束')
else:
    print('程序结束')