## check_pm2.py
&emsp;&emsp;由于serv00服务器不稳定，pm2服务经常宕机，定时执行该脚本，发现pm2进程不存在，执行pkill杀死用户所有进程，拉起pm2，并执行pm2 resurrect恢复相关进程

### 使用方法
1.获取维护脚本：
wget https://raw.githubusercontent.com/Candy141029/scripts/main/check_pm2.py  
2.设置crontab每10分钟执行：python check_pm2.py >> /dev/null 2>&1
![image](https://github.com/Candy141029/scripts/assets/175073750/321f4cec-52e4-4e53-9d6f-2cb493ac4433)


