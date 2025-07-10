import subprocess
import datetime

# 获取当前时间并格式化为字符串
current_time = datetime.datetime.now().strftime('%Y%m%d%H%M')

# 定义需要执行的 Git 命令
commands = [
    'git add .',
    f'git commit -m "{current_time}"',
    'git push origin main'
]

# 依次执行命令
for command in commands:
    subprocess.run(command, shell=True, check=True)

