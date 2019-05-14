# 1.安装saltstack
# https://docs.saltstack.com/en/latest/topics/installation/index.html#quick-install

# Master   salt-master
# Slave    salt-minion


"""
Master 准备：
    a 配置文件，监听本机IP
        vim /etc/salt/master
        interface: 本机IP地址

    b.启动master
        /etc/init.d/salt-master start

Slave准备：
    a.配置文件，连接那个master
     vim /etc/salt/minion
     master:远程程master地址
     启动 slave
     /etc/init.d/salt-minion start

1 创建关系
查看：
  Master ： salt-key -L
     Master Accepted Keys:
     Denied Key:
     ....
接受：
  salt-key -a c1.com  :接受c1.com

3 执行命令：
 master :
   salt 'c1.com' cmd.run 'ifconfig'

 #  http://www.cnblogs.com/wupeiqi/articles/6415436.html
"""

# 获取今日未采集主机名

# 运程服务器执行命令

# 发送数据