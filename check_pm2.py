import subprocess
import datetime
import time
import sys
import os

def self_check():
    script_name = sys.argv[0]
    result = subprocess.run(['pgrep', '-fl', script_name], stdout=subprocess.PIPE)
    running_scripts = result.stdout.decode('utf-8').strip().split('\n')

    # 过滤掉当前进程
    current_pid = os.getpid()

    # 检查是否有其他相同脚本在运行
    if len(running_scripts) > 0:
        for script in running_scripts:
            if script and script.split()[0] != current_pid:
                ##print("进程已存在")
                sys.exit()

def check_pm2_process():
    # 获取当前用户名
    result = subprocess.run(['whoami'], stdout=subprocess.PIPE)
    username = result.stdout.decode('utf-8').strip()
    logfile_path = "/usr/home/%s/check_pm2.log" % username
    pm2 = "/usr/home/%s/.npm-global/bin/pm2" % username

    # 检查 PM2 进程是否存在
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE)
    processes = result.stdout.decode('utf-8')

    if 'PM2' in processes:
        # # 如果存在 PM2 进程，检查process list是否与saved list一致
        # _result = subprocess.run([pm2, 'list'], stdout=subprocess.PIPE)
        # _processes = _result.stdout.decode('utf-8')
        # if 'Current process list is not synchronized with saved list' in _processes:
        #     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     log_message = f"{current_time} - pm2 Current process list is not synchronized with saved list"
        #     with open(logfile_path, 'a') as logfile:
        #         logfile.write(log_message + '\n')
        #     subprocess.run([pm2, 'resurrect'])
        pass
    else:
        # 如果不存在 PM2 进程，输出日志并执行命令
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{current_time} - pm2进程不存在"

        # 写入日志文件
        with open(logfile_path, 'a') as logfile:
            logfile.write(log_message + '\n')

        # 执行命令
        subprocess.run(['pkill', '-kill', '-u', username])
        subprocess.run([pm2, 'list'])
        subprocess.run([pm2, 'resurrect'])

if __name__ == "__main__":
    self_check()
    check_pm2_process()
