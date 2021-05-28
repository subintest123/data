

# Linux



## 1.发展史

C语言------Unix------stallman-------linus-------Linux

Unix：solaris，AIX，HP-Unix

stallman：自由软件之父-------GNU

linus：Linux之父-------Git

linux：Redhat，Centos，Suse，Ubuntu，Fedora....

移动市场：基于linux内核，google发行了Android

​                   苹果的底层：Unix

**[总结]**

Linux是一个内核开源的操作系统，主要应用在服务器端，作为服务器的操作系统使用

**[偏外]**

服务器的概念：

服务器是计算机的一种，比普通计算机运行更快、负载更高、价格更贵。

在网络中为其它客户机（如PC机、智能手机、ATM等终端甚至是火车系统等大型设备）提供计算或者应用服务。

具有高速的CPU运算能力、长时间的可靠运行、强大的I/O外部数据吞吐能力以及更好的扩展性。

一般来说服务器都具备承担响应服务请求、承担服务、保障服务的能力。

与普通的计算机内部结构相差不大，如：cpu、硬盘、内存，系统、系统总线等。

**本文档内容很多，请耐心观看**



## 2.安装环境



### 2.1 虚拟机+镜像

虚拟机：vmware workstation

镜像：***.iso



### 2.2 连接服务器

只需要提供给我：ip，用户名，密码

工具：puuty，SSH，CRT，Xshell等

**[附加]**

修改字体和颜色等

![putty](Linux.assets/putty.png)

![putty2](Linux.assets/putty2.png)

![putty3](Linux.assets/putty3.png)



## 3.正式学习



### 	3.1 背目录

Linux是个文件系统，它把所有的东西都当成文件，相同文件组成文件夹，不断嵌套后形成一个树状结构

常见目录：

/：根目录，相当于''我的电脑''

dev：是device的简写，设备目录

etc：配置文件目录

root：超管目录

home：普通用户的目录

mnt：即mount，挂载

usr：软件的默认安装目录

var：软件的工作目录

tmp：即temp，临时文件目录，我们一般做试验在这个里面做

**[附加]**

请自行百度，了解其他目录等

[https：//www.runoob.com/linux/linux-system-contents.html]



### 	3.2 了解前缀

不管你敲什么，前面都有这一堆，这个你先要认识例：

```shell
[root@iZwz99707cbxm1n1b9vjj7Z ~]#
```

整个这一堆叫shell，linux用的是bash，也叫 bash shell

按照这个理解：有其他的shell才对，unix用CShell（cqdb%），windows用winshell

root：你当前所在的用户

添加用户：

```shell
useradd 用户名
passwd 用户名
输入密码
确认密码
```

![1](Linux.assets/1.png)

切换用户：

（1）超管用户切换到普通用户

```shell
su 用户名    #不用输密码
```

![3](Linux.assets/3.png)

（2）普通用户切换到超管用户

```shell
su -或su root    #需要密码
```

![2](Linux.assets/2.png)

iZwz99707cbxm1n1b9vjj7Z：机器名

~：当前用户的工作目录 

超管用户目录：/root

普通用户目录：/home/用户名

$、#：

$：普通权限

#：超管权限



### 	3.3 基本命令



#### 3.3.1 查看当前所在位置------pwd

![8](Linux.assets/8.png)



#### 3.3.2 切换目录------cd

cd .：只有一个“.”表示本层

![9](Linux.assets/9.png)

cd ..：上一层cd ../../.：返回上两层

![10](Linux.assets/10.png)

![11](Linux.assets/11.png)

相对路径/绝对路径：

相对路径：cd 文件或目录名

进入当前所在目录下的某个文件或目录

绝对路径：cd /文件或目录名

进入/目录下的某个文件或目录

**[总结]**

（1）使用相对路径和绝对路径都可以，只是你觉得哪种场景下而已（你要切目录时告诉你自己：1.我在哪个位置，2.我要去哪个位置），根据实际需求选择

我在哪个位置：pwd

我要去哪个位置：如果是本层下的，就用相对路径

如果不是在本层下，就用绝对路径

（2）如何区分相对路径和绝对路径：带/的就是绝对路径



#### 3.3.3 查看当前目录都有哪些内容------ls

常见参数：

```shell
ls -l    #linux中可简写为“ll“，但“ll”不能作用在unix系统中
```

![12](Linux.assets/12.png)

```shell
ls -la    #查看当前目录中所有内容
```

![13](Linux.assets/13.png)

```shell
ll /目录名/    #查看其他目录有哪些内容
```

![4](Linux.assets/4.png)

**[附加]**

（1）我们常用ll替代ls -l  （因为”ll”是ls -l的别名）

```shell
alias 别名='命令'    #取别名,只在当前窗口生效
```

![6](Linux.assets/6.png)

```shell
unalias 别名    #取消别名
```

![7](Linux.assets/7.png)



#### 3.3.4 linux查看手册命令------man

man后面加空格加命令（如“man ls”）

![5](Linux.assets/5.png)

回车键：往下找（按字母顺序排序）

q：退出man手册 （quit的简写）

Ctrl+l 或clear 清屏



### 3.4 文件系统

linux是把所有都当文件，就要学文件和文件夹的操作

操作：新建，删除，复制，粘贴，剪切，重命名，查找



#### 3.4.1 新建

新建文件夹：mkdir

```shell
mkdir 文件夹名   #新建文件夹
mkdir 文件夹1 文件夹2 文件夹3   #同时新建多个文件夹
mkdir -p test001/test002/test003    #新建一个多级文件夹
```

![001](Linux.assets/001.png)

![新建1](Linux.assets/新建1.png)

![新建2](Linux.assets/新建2.png)

![新建2.1](Linux.assets/新建2.1.png)

新建文件：touch

```shell
touch 文件名    #新建文件
touch 文件名1 文件名2 文件名3    #同时新建多个文件
```

![文件](Linux.assets/文件.png)



#### 3.4.2 删除

删除文件夹：rmdir

```shell
rmdir 文件夹名字    #可以同时删除多个空文件夹，remdir 文件夹1 文件夹2
```

提醒：rmdir只能删除空文件夹，所以几乎不用

![删除1](Linux.assets/删除1.png)

删除文件：rm -rf		-r 递归		-f：强制

```shell
rm -rf 文件夹名
rm -rf 文件名
```

**提醒**

我们工作无论是删除文件夹还是文件都采用rm -rf 文件夹/文件均可，删除时请小心看清楚名称，别误删

![删除2](Linux.assets/删除2.png)

![删除3](Linux.assets/删除3.png)



#### 3.4.3 复制------cp

即copy的缩写，**注意：如果是复制文件夹，需要带-r参数**

```shell
cp 文件名 目标位置    #复制文件
cp  -r 文件夹名 目标位置    #复制文件夹
```

![复制1](Linux.assets/复制1-1619421236779.png)

![复制2](Linux.assets/复制2.png)



#### 3.4.4 剪切------mv

```shell
mv 原目录 现目录
mv 原文件 现目录
```

**[注意]**

如果是本层，表示重命名，如果是不同层，表示剪切

![重命名](Linux.assets/重命名.png)

![剪切](Linux.assets/剪切.png)



#### 3.4.5 查找文件或文件夹------find

```shell
find 目录 -name '内容'
#技巧多集中在内容上，你可以自己百度搜炫的效果的查找方案
find / -name '*12345*'
```

![查找](Linux.assets/查找.png)



#### 3.4.6 查看（重点）

（1）静态：cat、more、less、head、tac

```shell
cat 文件名    #比较适合hc看小文件，最好不超过一屏
more 文件名    #回车 空格，可以向下翻，不能向前看
less 文件名    #优于more，可以向上翻
head 文件名-------head -n 行数 文件名（查看文件的前面多少行）
tac 文件名    #反着看文件内容
```

![查看1](Linux.assets/查看1.png)

![查看2](Linux.assets/查看2.png)

![查看3](Linux.assets/查看3-1619426503956.png)

![查看4](Linux.assets/查看4.png)

![查看5](Linux.assets/查看5.png)

（2）动态：tail -f 文件名，常用这个命令来看日志文件

```shell
tail -f 文件名
```

想要看文件后面多少行，可用下面这条命令，不常用

```shell
tail -f -n 行数 文件名
```

![查看6](Linux.assets/查看6.png)



### 3.5 压缩和解压缩

windows提供的方案：rar，zip，它是边打包边压缩

Linux不支持rar，只支持zip包



#### 3.5.1 压缩、解压------zip

（1）压缩

```shell
zip -r 压缩名 目标文件/文件夹
```

![压缩1](Linux.assets/压缩1.png)

（2）解压

```shell
unzip 压缩名
```

![删除1](Linux.assets/删除1-1619430474129.png)

![解压1](Linux.assets/解压1.png)



#### 3.5.2 打包------tar

Linux打包和压缩是2个方案

**tar   打包之前多少MB，打包后就多少MB，并不改变文件大小**

（1）压缩：

```shell
tar cvf 压缩名(xx.tar) 目标文件/文件夹
```

![tar压缩](Linux.assets/tar压缩.png)

（2）解压缩：

```shell
tar xvf 压缩名(xx.tar) 
```

![tar删除](Linux.assets/tar删除.png)

![tar解压](Linux.assets/tar解压.png)

（3）查看压缩包内容：

```shell
tar -tf 压缩名(xx.tar) 
```

![tar查看](Linux.assets/tar查看.png)

（4）追加内容到压缩包：

```shell
tar -rf 压缩名(xx.tar) 目标文件/文件夹
```

![tar追加](Linux.assets/tar追加.png)

（5）删除压缩包中的内容：

```shell
tar --delete -f 压缩名(xx.tar) 目标文件/文件夹
```

![tar删除内容](Linux.assets/tar删除内容.png)



#### 3.5.3 压缩、解压------gz

tar只是进行了打包，并没有进行压缩

（1）压缩：

```shell
gzip 压缩名(xx.tar) 
```

![gz压缩](Linux.assets/gz压缩.png)

（2）解压缩：

```shell
gunzip 压缩名(xx.tar.gz) 
```

![gz解压](Linux.assets/gz解压.png)



#### 3.5.4  一次性既打包又压缩 

（1）压缩：

```shell
tar zcvf 压缩名(xx.tar.gz) 目标文件/文件夹
```

![一次性压](Linux.assets/一次性压.png)

（2）解压缩：

```shell
tar zxvf 压缩名(xx.tar.gz) 
```

![一次性删](Linux.assets/一次性删.png)

![一次性接](Linux.assets/一次性接.png)

**[注意]**

**压缩和解压缩是不限定文件名后缀的，但工作中还是要写后缀（.tar       .tar.gz等，否则你根本不知道是个压缩包**



### 3.6 vi（必会）

vi编辑器可以简单理解为Linux中的记事本

```shell
vi 文件名
```

**一定不能直接写vi或vi 文件夹**

**玩vi眼睛盯着左下角**，它决定了你处于什么模式

![vi 1](Linux.assets/vi 1.png)

![vi 2](Linux.assets/vi 2.png)

**[理解]**

其实vi非常符合人的习惯

（1）打开我要编辑的文件------vi 文件名

（2）定位到我要编辑的地方，开始准备编辑，定位后输入a、i、o

（3）编辑我要的内容，正常写数据

（4）关闭我的编辑------esc

（5）保存退出------wq



#### 3.6.1 模式和模式切换

**命令模式切换到编辑模式------a，i，o**

a：append 追加，在光标后进行插入

![vi 4](Linux.assets/vi 4.png)

i：insert 插入，在光标前进行插入

![vi 3](Linux.assets/vi 3.png)

o：other 在光标下一行插入

![vi 5](Linux.assets/vi 5.png)



#### 3.6.2  末行模式技巧

w	q	!

w：write		q：quit		!：强制

工作用法：  

```shell
wq   # 保存并退出

例：
...
// DISABLED: do not color [STANDARD BEHAVIOUR]
$tlCfg->gui->usersAssignGlobalRoleColoring = DISABLED;

:wq
```

```shell
w    # 保存，但不退出

例：
...
// DISABLED: do not color [STANDARD BEHAVIOUR]
$tlCfg->gui->usersAssignGlobalRoleColoring = DISABLED;

:w
```

```shell
q    # 退出，没进行更改时使用

例：
...
// DISABLED: do not color [STANDARD BEHAVIOUR]
$tlCfg->gui->usersAssignGlobalRoleColoring = DISABLED;

:q
```

```shell
q!     # 强制退出

例：
...
// DISABLED: do not color [STANDARD BEHAVIOUR]
$tlCfg->gui->usersAssignGlobalRoleColoring = DISABLED;

:q!
```

```shell
：set number    #显示行号

例：
...
    491 // ENABLED: on features that assign user role to test projects an        d test plan, colour user name
    492 //          according GLOBAL role

:set number
```

```shell
：set nonumber    #取消行号

例：
...
// DISABLED: do not color [STANDARD BEHAVIOUR]
$tlCfg->gui->usersAssignGlobalRoleColoring = DISABLED;

:set nonumber
```



#### 3.6.3 命令模式技巧

**vi的很多技巧都集中在命令模式中，在门道我讲授最常见的，其他的可自行学习**

1. 光标的纵向移动------G

   nG（“n”表示想要移动到哪一行）

2. 光标的横向移动------w、e

3. 光标上下左右移动------h、j、k、l

   小键盘：上下左右

   向左移动：删除键

   向右移动：空格键

4. 行首------^（shift+6）

   行尾------$（shift+4）

5. 复制------y

   yy：复制一行

   nyy：复制n行

   y^：复制光标到行首的内容

   y$：复制光标到行尾的内容

6. 粘贴------p

7. 删除------d

   dd：删除一行

   ndd：删除n行

   d^：删除光标到行首

   d$：删除光标到行尾

8. 删除一个字符------x

   （先向后删除，当前行后面没了，再向前删除）主要用来做微调，非常有用

9. 查找------/

   /n：向下查找(next)

   /N：向上查找		

10. 撤销------u



#### 3.6.4 vim和gvim

vi是自带的，没有语法高亮等"炫"功能，我们可以通过安装vim来实现

如果你想在windows上玩vi，可以装一个gvim来玩



### 3.7 进程（必会）



#### 3.7.1 查看进程

1. ps -ef或ps aux

   ps -ef用得更多，aux一般运维用

2. 我们关注的点是，第二列：pid  进程号

   工作往往是查是否有某一进程

   ```shell
   [root@localhost tmp]# ps -ef | grep java
   root      7709  7510  0 19:29 pts/2    00:00:00 grep java
   # 命令返回只有一行的，表示没有该进程
   
   
   # |:管道符,类似于插入一个管子
   # grep:过滤字符串,他是shell编程重要的家族
   
   
   [root@localhost tmp]# ps -ef | grep httpd
   root      7739     1  0 19:33 ?        00:00:00 /usr/sbin/httpd
   apache    7742  7739  0 19:33 ?        00:00:00 /usr/sbin/httpd
   apache    7743  7739  0 19:33 ?        00:00:00 /usr/sbin/httpd
   ...
   # 命令返回有一堆的，表示有该进程
   
   
   # 可以通过service httpd start来启动这个服务(centos6)
   [root@localhost tmp]# service httpd start
   Starting httpd: httpd: Could not reliably determine the server's fully qualified domain name, using localhost.localdomain for ServerName
                                                              [  OK  ]
   [root@localhost tmp]# ps -ef | grep httpd
   root     27905     1  0 20:34 ?        00:00:00 /usr/sbin/httpd
   apache   27908 27905  0 20:34 ?        00:00:00 /usr/sbin/httpd
   ...
   ```
   
3. 查看实时进程：top   (有点像windows的任务管理器)，只能通过ctrl+c来强制退出

   

#### 3.7.2 杀死进程

1. kill -9 pid（进程号,即我们查询出来的第二列），这种工作中用得多

   -9：强制执行

   ![kill一](Linux.assets/kill一.png)

2. pkill 进程名

   killall 进程名（如不知道进程名,问开发）

   ```shell
   [root@localhost tmp]# pkill httpd
   [root@localhost tmp]#
   [root@localhost tmp]# ps -ef | grep httpd
   root     27937 27422  0 20:39 pts/1    00:00:00 grep httpd
   [root@localhost tmp]#
   ```

   ![kill二](Linux.assets/kill二.png)



### 3.8 系统管理（理解）

1. 查看cpu信息------more /proc/cpuinfo

   ```shell
   例：
   [root@localhost tmp]# more /proc/cpuinfo
   processor       : 0
   vendor_id       : GenuineIntel
   ...
   ```
   
2. 查看内存信息------more /proc/meminfo

   ```shell
   例：
   [root@localhost tmp]# more /proc/meminfo
   MemTotal:        1030316 kB
   MemFree:          152780 kB
   ...
   ```
   
3. 内存占用------free -m

   ```shell
   例：
   [root@localhost tmp]# free -m
                total   used   free   shared   buffers   cached
   Mem:         1006    856    149    3        102       527
   -/+ buffers/cache:        227        778
   Swap:         2015          0       2015
   [root@localhost tmp]#
   ```

4. 硬盘占用------df -h

   ```shell
   例：
   [root@localhost tmp]# df -h
   Filesystem      Size  Used Avail Use% Mounted on
   /dev/sda2        18G  2.5G   15G  15% /
   tmpfs           504M  228K  503M   1% /dev/shm
   /dev/sda1       283M   33M  236M  13% /boot
   [root@localhost tmp]#
   ```

   windows的分区方案和linux完全是2回事,如果你有兴趣慢慢了解

5. 查看某目录下具体的各个文件/文件夹比重------du -sh *

   ```shell
   例：
   #进入需要查看的目录再使用该命令
   [root@localhost tmp]# du -sh *
   4.0K    11111.txt
   32K     anaconda-tb-AHDhzA
   ...
   ```
   
6. 查看历史命令------history

   ```shell
   例：
     ...
     317  du -sh *
     318  history
   [root@localhost tmp]# history
   ```
   
7. 查看ip

   centos6中使用的是：ifconfig

   centos7中使用的是：ip addr

8. 服务------service 服务名 状态

   例：关闭防火墙：

   ```shell
   service iptables stop
   ```

​		如果不知道服务名（查或问） 

​		如果不知道状态，状态可以随便敲，回车后会提示都有哪些状态

​		**[提醒]**

​		CentOs6和CentOs7在防火墙在完全是2个概念，请下来自我学习7的防火墙

​		或者说CentOs7上都没有service这个动作，变成了systemctl这个命令



## 4 环境搭建

Linux部署（安装）软件有3种方式，每一种你必会，否则没办法上班



### 4.1 rpm安装

rpm（英文全拼：redhat package manager），原本是 Red Hat Linux 发行版专门用来管理 Linux 各项套件的程序，由于遵循 GPL 规则且功能强大、方便，因而广受欢迎，逐渐受到其他发行版的采用。

rpm 套件管理方式的出现，让 Linux 易于安装，升级，间接提升了 Linux 的适用度。

蕴含道理：

1. 凡RedHat这个分支下的所有发行版，均采用rpm包管理方案
2. 其他发行版不一定是rpm包，如：ubuntu（deb）

3. 它比较容易让新人接受和安装部署

常见使用方式:

```shell
# 安装
rpm -ivh xxx.rpm

例：安装jdk
[root@localhost tmp]# rpm -ivh jdk-8u131-linux-i586.rpm
Preparing...                ########################################### [100%]
        package jdk1.8.0_131-2000:1.8.0_131-fcs.i586 is already installed
[root@localhost tmp]#
```

```shell
# 卸载
rpm -e xxx    #xxx名是要通过查才知道

例：卸载jdk
[root@localhost tmp]# rpm -e jdk-8u131-linux-i586.rpm
...
[root@localhost tmp]#
```

```shell
# 查询
rpm -ql xxx 
rpm -ql xxx | more    # 慢慢展示着看

例：
[root@localhost tmp]# rpm -ql httpd | more
/etc/httpd
/etc/httpd/conf
...
--More--
```

```shell
#列出所有用rpm来安装的包
rpm -qa

例：
[root@localhost tmp]# rpm -qa
iwl5150-firmware-8.24.2.2-1.el6.noarch
tmpwatch-2.9.16-6.el6.i686
...
```

```shell
# 列出是否安装过某包
rpm -qa | grep xxx

例：查询是否安装jdk
[root@localhost tmp]# rpm -qa | grep jdk
jdk1.8.0_131-1.8.0_131-fcs.i586
[root@localhost tmp]#
```

**[注意]**

rpm包有个非常恶心的问题：**包依赖**----有依赖关系的安装包

演示：安装mysql（rpm方式）

```shell
# 先试着安装mysql_server
[root@localhost tmp]# rpm -ivh mysql-server-5.1.73-8.el6_8.i686.rpm
warning: mysql-server-5.1.73-8.el6_8.i686.rpm: Header V3 RSA/SHA1 Signature, key ID c105b9de: NOKEY
error: Failed dependencies:    # 报错，提示需要安装有依赖关系的安装包
        perl(DBI) is needed by mysql-server-5.1.73-8.el6_8.i686
        perl-DBD-MySQL is needed by mysql-server-5.1.73-8.el6_8.i686
        perl-DBI is needed by mysql-server-5.1.73-8.el6_8.i686
[root@localhost tmp]#
```

```shell
# 先试着安装DBD
[root@localhost tmp]# rpm -ivh perl-DBD-MySQL-4.013-3.el6.i686.rpm
warning: perl-DBD-MySQL-4.013-3.el6.i686.rpm: Header V3 RSA/SHA256 Signature, key ID c105b9de: NOKEY
error: Failed dependencies:    # 发现DBD依赖于DBI
        perl(DBI) is needed by perl-DBD-MySQL-4.013-3.el6.i686
        perl(DBI::Const::GetInfoType) is needed by perl-DBD-MySQL-4.013-3.el6.i686
[root@localhost tmp]#
```

```shell
# 安装DBI，发现没有依赖关系，可直接安装
[root@localhost tmp]# rpm -ivh perl-DBI-1.609-4.el6.i686.rpm
warning: perl-DBI-1.609-4.el6.i686.rpm: Header V3 RSA/SHA256 Signature, key ID c105b9de: NOKEY
Preparing...                ########################################### [100%]
   1:perl-DBI               ########################################### [100%]
[root@localhost tmp]#
```

```shell
# DBI的安装成功，DBD的也可以安装了
[root@localhost tmp]# rpm -ivh perl-DBD-MySQL-4.013-3.el6.i686.rpm
warning: perl-DBD-MySQL-4.013-3.el6.i686.rpm: Header V3 RSA/SHA256 Signature, key ID c105b9de: NOKEY
Preparing...                ########################################### [100%]
   1:perl-DBD-MySQL         ########################################### [100%]
[root@localhost tmp]#
```

```shell
# 依赖包全部安装完成，现在安装MySQL-server
[root@localhost tmp]# rpm -ivh mysql-server-5.1.73-8.el6_8.i686.rpm
warning: mysql-server-5.1.73-8.el6_8.i686.rpm: Header V3 RSA/SHA1 Signature, key ID c105b9de: NOKEY
Preparing...                ########################################### [100%]
   1:mysql-server           ########################################### [100%]
[root@localhost tmp]#
```

```shell
# 启动服务
[root@localhost tmp]# service mysqld start
Initializing MySQL database:  Installing MySQL system tables...
...
You can test the MySQL daemon with mysql-test-run.pl
cd /usr/mysql-test ; perl mysql-test-run.pl

Please report any problems with the /usr/bin/mysqlbug script!

                                                           [  OK  ]
Starting mysqld:                                           [  OK  ]
[root@localhost tmp]#
```



### 4.2 yum安装

yum（ Yellow dog Updater, Modified）是一个在 Fedora 和 RedHat 以及 SUSE 中的 Shell 前端软件包管理器。

基于 RPM 包管理，**能够从指定的服务器自动下载 RPM 包并且安装**，可以**自动处理依赖性关系**，并且**一次安装所有依赖的软件包**，无须繁琐地一次次下载、安装。

提供了查找、安装、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。



能够从指定的服务器自动下载:

1. 默认是从官方的镜像库中去拉取，但由于受到网络影响，有可能你下载并安装会很慢
2. 我们要能够切换回国内源（阿里云，163云，清华大学等）
3. 如果服务器上没有这个rpm包，你就拉不动，想哭:(



**常见命令:**

```shell
#安装
yum install 软件名

#更新
yum update 软件名

#查找
yum search 软件名
```



**切换源**

```shell
# 1.备份一个出来
cd /etc/yum.repos.d/
cp CentOS-Base.repo CentOS-Base.repo_bak

[root@localhost tmp]# cd /etc/yum.repos.d/
[root@localhost yum.repos.d]# ll
total 24
-rw-r--r--. 1 root root 1991 Mar 28  2017 CentOS-Base.repo
...
[root@localhost yum.repos.d]# cp CentOS-Base.repo CentOS-Base.repo_bak
[root@localhost yum.repos.d]# ll
total 28
-rw-r--r--. 1 root root 1991 Mar 28  2017 CentOS-Base.repo
-rw-r--r--. 1 root root 1991 Apr 27 01:33 CentOS-Base.repo_bak
...
```

```shell
# 2.删除CentOS-Base.repo中的内容并替换成对应的源的配置信息

[root@localhost yum.repos.d]# vim CentOS-Base.repo
[root@localhost yum.repos.d]#
```

```shell
# 3.清理原来的yum信息:yum clean all

[root@localhost yum.repos.d]# yum clean all
Loaded plugins: fastestmirror, refresh-packagekit, security
Cleaning repos: base extras updates
Cleaning up Everything
Cleaning up list of fastest mirrors
[root@localhost yum.repos.d]#
```

```shell
# 4.生成新的yum仓库信息:yum makecache

[root@localhost yum.repos.d]# yum makecache
Loaded plugins: fastestmirror, refresh-packagekit, security
Determining fastest mirrors
base                    | 3.7 kB     00:00
base/group_gz           | 237 kB     00:00
...
[root@localhost yum.repos.d]#
```

```shell
# 5.查看切换:yum repolist

[root@localhost yum.repos.d]# yum repolist
Loaded plugins: fastestmirror, refresh-packagekit, security
Loading mirror speeds from cached hostfile
repo id             repo name                  status
base                CentOS-6 - Base            5,075
extras              CentOS-6 - Extras          21
updates             CentOS-6 - Updates         870
repolist: 5,966
[root@localhost yum.repos.d]#
```

**[注意]**

centos6已有很多国内国外源都不维护了，因此我们好不容易找到了华中科技大学的镜像源站

http://mirrors.hust.edu.cn/help.html#centos（按住Ctrl，鼠标点击）



**案例**：php，subversion

注意 -y的意义

```shell
例：
yum install php                      # 安装时会询问是否安装依赖包
yum install -y subversion            # 安装时会直接安装依赖包，不会询问
```



### 4.3 源码安装

Linux上几乎所有的软件都经过了GPL授权，因此几乎所有的软件都会提供源码。 

而一个软件要在Linux上执行，必须是二进制文件，因此当我们拿到软件源码后，需要将它**编译成二进制文件才能在Linux上运行。**



步骤:

1. 获取源码
2. 解压
3. 进入文件夹
4. 执行创建Makefile文件（configure脚本）
5. 编译（make），很遗憾,很多时候make不通过（编译器过老）
6. 安装（make install）



案例：nginx（反向代理服务器）

```shell
# 预处理
cd /usr/local/
mkdir nginx
cd nginx

[root@localhost local]# cd nginx/    # 进入目录
[root@localhost nginx]# ll    # 查看目录
total 0
```

```shell
# 预处理它的目的是为了在make时不出错
yum -y install gcc gcc-c++ autoconf automake
yum -y install zlib zlib-devel openssl openssl-devel pcre pcre-devel

[root@localhost nginx]# yum -y install gcc gcc-c++ autoconf automake
...
Complete!
[root@localhost nginx]# yum -y install zlib zlib-devel openssl openssl-devel pcre pcre-devel
...
Complete!
```

```shell
# 1.获取源码
wget https://nginx.org/download/nginx-1.9.9.tar.gz    # 如果你有这个包,直接拖动到目录下也可

[root@localhost nginx]# wget https://nginx.org/download/nginx-1.9.9.tar.gz
...
```

```shell
# 2.解压
tar zxvf nginx-1.9.9.tar.gz

[root@localhost nginx]# tar zxvf nginx-1.9.9.tar.gz
...
```

```shell
# 3.进入文件夹
cd nginx-1.9.9

[root@localhost nginx]# cd nginx-1.9.9    # 进入目录
[root@localhost nginx-1.9.9]# ll    # 查看目录
...
```

```shell
# 4.执行脚本
./configure --prefix=/usr/local/nginx/ --with-http_ssl_module
# 执行这条命令后，会有一个Makefile的文件

[root@localhost nginx-1.9.9]# ./configure --prefix=/usr/local/nginx/ --with-http_ssl_module
[root@localhost nginx-1.9.9]# ll    # 查看是否有Makefile文件
total 680
...
-rw-r--r--. 1 root root    370 Apr 28 03:02 Makefile
...
```

```shell
# 5.编译
make
# 很遗憾,你会各种错,如果错,就执行如上的yum安装依赖等,装好后,删除Makefile的文件,然后重新执行第4步

[root@localhost nginx-1.9.9]# make
...
```

```shell
# 6.安装
make install

[root@localhost nginx-1.9.9]# make install
...
```

```shell
# 7.关闭防火墙
service iptables stop

[root@localhost nginx-1.9.9]# service iptables stop
iptables: Setting chains to policy ACCEPT: filter          [  OK  ]
iptables: Flushing firewall rules:                         [  OK  ]
iptables: Unloading modules:                               [  OK  ]
```

```shell
# 8.进入nginx的sbin目录,执行：./nginx即可

[root@localhost nginx]# ll    # 查看目录
total 1756
...
drwxr-xr-x. 2 root root   4096 Apr 28 03:27 sbin
[root@localhost nginx]# cd sbin/    # 进入目录
[root@localhost sbin]# ll    # 查看目录
total 9784
-rwxr-xr-x. 1 root root 5008572 Apr 28 03:27 nginx
[root@localhost sbin]# ./nginx
```

```shell
# 9.测试,启动chrome,输入:http://ip，如下
```

![查看](Linux.assets/查看.png)

案例2：Tomcat

```shell
# 1.把压缩包上传到/tmp (其他目录也可,但是tmp更好)

[root@localhost nginx-1.9.9]# cd /tmp/    # 进入目录
[root@localhost tmp]#
[root@localhost tmp]# ll    # 查看目录
total 188712
...
-rw-r--r--. 1 root  root    9375265 Apr 27 18:34 apache-tomcat-8.5.13.tar.gz
...
```

```shell
# 2.解压
tar zxvf apache-tomcat-8.5.13.tar.gz

[root@localhost tmp]# tar zxvf apache-tomcat-8.5.13.tar.gz
...
```

```shell
# 3.复制到/usr/java (你复制到/usr/local下也可,只是我们这里和java保持同目录)
cp -r apache-tomcat-8.5.13 /usr/java

```

```shell
# 4.进入/usr/java下,重命名成tomcat8080 (tomcat的默认端口是8080)
cd /usr/java
mv apache-tomcat-8.5.13 tomcat8080

[root@localhost tmp]# cp -r apache-tomcat-8.5.13 /usr/local/    #复制到/usr/local/下
[root@localhost tmp]# ll /usr/local/    # 查看目录
total 44
drwxr-xr-x.  9 root root 4096 Apr 28 03:37 apache-tomcat-8.5.13
...
[root@localhost java]# cd /usr/local/    # 进入目录
[root@localhost local]# ll    # 查看目录
total 44
drwxr-xr-x.  9 root root 4096 Apr 28 03:37 apache-tomcat-8.5.13
...
[root@localhost local]# mv apache-tomcat-8.5.13 tomcat8080    # 重命名
[root@localhost local]# ll    # 查看目录
total 44
...
drwxr-xr-x.  9 root root 4096 Apr 28 03:37 tomcat8080
```

```shell
# 5.进入tomcat8080下的bin并启动tomcat
cd tomcat8080/bin
./startup.sh

[root@localhost local]# cd tomcat8080/bin    # 进入目录
[root@localhost bin]# ll    # 查看目录
total 812
...
-rwxr-x---. 1 root root   1904 Apr 28 03:37 startup.sh
...
[root@localhost bin]# ./startup.sh   #启动服务
...
Tomcat started.
```

```shell
# 6.测试,启动chrome,输入:http://ip:8080，如下
```

![tomcat](Linux.assets/tomcat.png)



**[备注]**

*wget* 是一个从网络上自动下载文件的自由工具，最最简单的理解：Linux自带的迅雷下载

通过./configure --help，可以看configure的详细说明



**三种安装方式的比较：**

rpm：

​	好：安装简单；不依赖网络，硬盘上有rpm包上传后就可以安

​	不好：包依赖；不能自定义安装路径



yum：

​	  好：解决了rpm的不好

​	  不好：源不好找；需要网络；如果源没有需要的版本，得切换源



源码:

​		好：完全自定义安装路径等一系列配置，甚至有的解压就可以用，如Tomcat

​		不好：需要更新编译器，新人太麻烦了



## 5 Nginx+tomcat



### 5.1 nginx

*Nginx* (engine x) 是一个高性能的[HTTP](https://baike.baidu.com/item/HTTP)和[反向代理](https://baike.baidu.com/item/反向代理/7793488)web服务器.其特点是占有内存少，[并发](https://baike.baidu.com/item/并发/11024806)能力强



### 5.2 正向代理&反向代理

代理：可以理解为中介

正向代理：vpn，客户端

反向代理：nginx，服务器端

参考文章:[https://www.cnblogs.com/xuepei/p/10437114.html]

**[注意]**

**理解正向代理和反向代理的区别**



案例：nginx+tomcat（负载均衡）

1.复制出3个tomcat，分别叫tomcat8080、8081、8082

```shell
[root@localhost local]# cp -r /tmp/apache-tomcat-8.5.13 tomcat8081
[root@localhost local]# cp -r /tmp/apache-tomcat-8.5.13 tomcat8082
[root@localhost local]# ll
total 52
...
drwxr-xr-x.  9 root root 4096 Apr 28 03:37 tomcat8080
drwxr-xr-x.  9 root root 4096 Apr 28 08:41 tomcat8081
drwxr-xr-x.  9 root root 4096 Apr 28 08:41 tomcat8082
```

2.分别改3个tomcat的端口（启动端口和关闭端口都要改）

端口：tomcat/conf/server.xml

22行：关闭端口			69行：启动端口

可参考：启动8080、8081、8082    关闭：8005、8006、8007

```shell
# tomcat8081
[root@localhost local]# cd tomcat8081/conf/
[root@localhost conf]# ll
...
-rw-------. 1 root root   7511 Apr 28 08:41 server.xml
...
[root@localhost conf]# vim server.xml
...
<Server port="8006" shutdown="SHUTDOWN">
...
    <Connector port="8081" protocol="HTTP/1.1"
    ... />
...
:wq
```

```shell
# tomcat8082
[root@localhost conf]# vim /usr/local/tomcat8082/conf/server.xml
...
<Server port="8007" shutdown="SHUTDOWN">
...
    <Connector port="8082" protocol="HTTP/1.1"
    ... />
...
:wq
```

3.为了区分和能看懂我到底是哪个tomcat，我修改他的标题来区分（你改其他也可以）

```shell
vi tomcatxxxx/webapps/ROOT/index.jsp
```

第29行：分别取名 tomcat8080、tomcat8081、tomcat8082

```shell
# tomcat8081
[root@localhost conf]# vim /usr/local/tomcat8081/webapps/ROOT/index.jsp
...
    <head>
        <meta charset="UTF-8" />
        <title>tomcat8081</title>
        ...
    </head>
...
```

```shell
# tomcat8082
[root@localhost conf]# vim /usr/local/tomcat8081/webapps/ROOT/index.jsp
...
    <head>
        ...
        <title>tomcat8082</title>
        ...
    </head>
...
```

4.完成前面3个tomcat的修改，其实你已经可以分别把项目部署在不同的tomcat中

分别启动这三个tomcat

```shell
[root@localhost local]# ./tomcat8080/bin/startup.sh
...
Tomcat started.
```

```shell
[root@localhost local]# ./tomcat8081/bin/startup.sh
...
Tomcat started.
```

```shell
[root@localhost local]# ./tomcat8082/bin/startup.sh
...
Tomcat started.
```

```shell
[root@localhost local]# ps -ef | grep java
...
.../usr/local/tomcat8080/conf/l...
.../usr/local/tomcat8081/bin/bo...
.../usr/local/tomcat8082/bin/boo...
...
```

5.**修改nginx的配置文件，让他分别认识前面的tomcat**（重中之重） ，写错一个字符都不行

编辑nginx的配置文件：

```shell
vi /usr/local/nginx/conf/nginx.conf
```

修改2处即可，一处是纯添加，一处是在已有的后面添加，注意名称的一致性

```shell
[root@localhost local]# vi /usr/local/nginx/conf/nginx.conf
...
     33     #gzip  on;
     34     #添加下面的5行
     35     upstream tomcat_server{
     36         server 192.168.48.132:8080;
     37         server 192.168.48.132:8081;
     38         server 192.168.48.132:8082;
     39     }
...
     52         location / {
					...#添加下面一行
     55             proxy_pass http://tomcat_server;
     56         }
...
```

6.测试：启动ngxin，访问http://linux的ip，你不断刷新，你注意看标题栏，他在8080、8081、8082之间切换

```shell
[root@localhost nginx]# cd sbin/
[root@localhost sbin]# ll
total 9784
-rwxr-xr-x. 1 root root 5008572 Apr 28 03:27 nginx
[root@localhost sbin]# pkill nginx    # 杀死进程
[root@localhost sbin]# ./nginx    # 杀死进程
```

![111](Linux.assets/111.png)

![222](Linux.assets/222.png)

![333](Linux.assets/333.png)



## 6 动态日志

**我们看日志，往往用------tail -f [-n 20] 日志文件的方式来看**

案例：tomcat的日志

1. 双开2个putty，一个正常操作，一个看动态日志
2. tomcat的日志文件在tomcat/logs/catalina.out

**日志是我们测试的利器，我们排查bug往往通过日志，就能很好的定位到底是什么引起的bug**