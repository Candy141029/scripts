import subprocess
import datetime

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
        # 如果存在 PM2 进程，什么也不做
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
        subprocess.run([pm2, 'resurrect'])

if __name__ == "__main__":
    check_pm2_process()
