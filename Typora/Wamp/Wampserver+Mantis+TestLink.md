# Wampserver+Mantis+TestLink

## Wampserver安装

选择安装路径，其他选项可默认下一步

![a](Wampserver+Mantis+TestLink.assets/a.png)

![b](Wampserver+Mantis+TestLink.assets/b.png)

## Mantis

![d](Wampserver+Mantis+TestLink.assets/d.png)

![c](Wampserver+Mantis+TestLink.assets/c.png)

![e](Wampserver+Mantis+TestLink.assets/e.png)

![f](Wampserver+Mantis+TestLink.assets/f.png)

![g](Wampserver+Mantis+TestLink.assets/g.png)

![h](Wampserver+Mantis+TestLink.assets/h.png)

![i](Wampserver+Mantis+TestLink.assets/i.jpg)



## TestLink

![d](Wampserver+Mantis+TestLink.assets/d.png)

![j](Wampserver+Mantis+TestLink.assets/j.png)

![k](Wampserver+Mantis+TestLink.assets/k.png)

可能会报错需要更改一些文件

![l](Wampserver+Mantis+TestLink.assets/l.png)

找到testlink下的config.inc.php文件进行一些修改：

将   $tlCfg->log_path = '/var/testlink/logs/';   修改为：$tlCfg->log_path = TL_ABS_PATH."logs"; （也就是testlink下的logs文件夹的路径）

另外还需要将   $g_repositoryPath = '/var/testlink/upload_area/';  修改为：$g_repositoryPath = TL_ABS_PATH."upload_area";  （testlink文件夹下的upload_area的路径）

![o](Wampserver+Mantis+TestLink.assets/o.png)

![p](Wampserver+Mantis+TestLink.assets/p.png)

![q](Wampserver+Mantis+TestLink.assets/q.png)

然后浏览器页面重新加载，就能看到不报错了，点击contiune

![r](Wampserver+Mantis+TestLink.assets/r.png)

[mysqld]后面添加

sql-mode=ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION![s](Wampserver+Mantis+TestLink.assets/s.png)

![t](Wampserver+Mantis+TestLink.assets/t.png)

添加并保存后，重启下全部服务

![u](Wampserver+Mantis+TestLink.assets/u.png)

浏览器重新加载，并设置内容

![v](Wampserver+Mantis+TestLink.assets/v.png)

![w](Wampserver+Mantis+TestLink.assets/w.png)

点击Steup后就能看到安装成功了，点击TestLink登录

![x](Wampserver+Mantis+TestLink.assets/x.png)

刚安装成功，可能自己创建的用户不能登陆，可用默认的用户登录，默认的用户名及密码都是“admin”

![y](Wampserver+Mantis+TestLink.assets/y.png)

登录成功

![z](Wampserver+Mantis+TestLink.assets/z.png)