## check_pm2.py
现阶段的问题：  
1.不明原因导致serv00服务器非常卡顿。  
2.服务器的卡顿可能会造成服务器重启，进程被杀，进程崩溃等结果。  
3.PM2进程被杀（崩溃）后可能会导致PM2维护的子进程变成孤儿进程而存在。  
4.PM2不断地被杀（崩溃），启动，被杀（崩溃），启动导致存在大量的孤儿进程，从而导致进程数溢出。  

解决方案：  
1.依赖crontab服务定时（10分钟）检查PM2进程。PM2进程存在，检查process list是否一致。PM2进程不在，杀死所有进程，重启PM2，并恢复相关维护进程。  

### 使用方法
1.获取维护脚本：
wget https://raw.githubusercontent.com/Candy141029/scripts/main/check_pm2.py  
2.设置crontab每10分钟执行：python check_pm2.py >> /dev/null 2>&1
![image](https://github.com/Candy141029/scripts/assets/175073750/321f4cec-52e4-4e53-9d6f-2cb493ac4433)


