# scripts
&nbsp;&nbsp;存放一些自测脚本

## check_pm2.py
&nbsp;&nbsp;由于serv00服务器不稳定，pm2服务经常宕机，定时执行该脚本，发现pm2进程不存在，执行pkill杀死用户所有进程，拉起pm2，并执行pm2 resurrect恢复相关进程
