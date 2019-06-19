# 1. Linux目录结构

/bin : 常用的指令。

/dev ：管理设备,如同windows设备管理器。

/etc : CPU、硬盘的一些配置文件。

/media : U盘识别在media下。

/opt : 软件存放位置。

/proc : 内核一些文件，这个目录是一个虚拟目录，他是系统内存的映射，访问这个目录来获取系统信息。

/root : root用户的一些文件。

/sbin : supper才可以操作的一些高权限的一些指令。

/selinux[security-enhanced linux] : 安全相关子系统。

/var : 变量文件夹、如日志。

/usr : 用户安装的软件。如：user/local/mysql

/home : 存放普通用户的主目录，在linux中每一个用户都有一个自己的目录，一般该目录名就是用户的账号命名的。

/lib : 系统开机后所需要的最基本的动态链接共享库，其作用类似于Windows里的DLL文件，几乎所有的应用程序都需要这些共享库。

/boot : 存放的是启动Linux时使用的一些核心文件，包括一些链接文件以及镜像文件。

/srv : service缩写，改目录存放一些服务启动之后需要提取的数据

/sys : 这是linux2.6内核的一个很大的变化。该目录下安装了2..6内核中新出现的一个文件系统sysfs。

/tmp : 这个目录是用来存放一些临时的文件。

/mnt : 临时挂载别的文件系统的，比如虚拟机和linux的共享文件夹。 


#### 总结：
1. linux只有一个根目录

2. linux的各个目录存放的内容是规划好的

3. linux是以文件的形式管理我们的设备，因此linux系统，一切皆文件

# 2. vi和vim编辑器的使用

## 基本介绍

Vim是vi的增强版，可以主动的以字体颜色辨别语法的正确性，方便程序设计、代码补完、编译及错误跳转等方便编程，功能特别丰富。

## vi与vim的三种常见模式
1. 正常模式
在正常模式下可以使用快捷键
2. 插入模式/编辑模式
在此模式下，可以输入内容
3. 命令行模式
可以提供相关指令，完成读取、存盘、替换、离开、显示行号等

## 模式切换
![模式转换](/linux/linuxfile/模式切换.png)
1. :wq  保存并退出
2. :q  退出不报错
3. :q!  强制退出不报错

## 常用快捷键
1. 拷贝当前行 yy,拷贝当前行向下的5行 [5yy],并黏贴[p]
2. 删除当前行 dd,删除当前行向下的行 5dd
3. 在文家中查找某个单词  
[命令行下 /关键字，回车 查找，输入n就是查找下一个]
4. 设置文件的行号，取消文件的行号  
[命令行模式下 :set nu 和 :set noun]
5. 文档的末行[G]，首行[gg]
6. 撤销动作，正常模式下u，如同撤销
7. 取消黄色标记 [:noh]
8. 跳转到某一行  
   1)显示行号 :set nu  
   2)输入20这个数  
   3)输入shift+g  

# 3. 关机、重启、用户注销
## 关机&重启命令
### 基本介绍
shutdown:  
shutdown -h now： 立即关机  
shutdown -h 1:表示一分钟后关机  
shutdown -r now:立即重启

halt:关机  

reboot:重启系统

syn:将内存的数据同步到磁盘[关机或者重启之前使用]

### 注意细节
当我们关机或者重启时，都应该执行一下sync指令，把内存的数据写入磁盘，避免丢失。
## 用户的登录和注销
### 基本介绍:
1. 登录时候尽量少使用root，尽量使用'su-用户名'的命令来切换成系统管理员身份。
2. 在提示符下输入logout即可注销用户。

### 使用细节：
1. logout只有在运行级别为3的时候才能使用,图形界面是无效的。

# 4. 用户管理
## 基本介绍
基本规则：  
1. linux中有很多用户和组，每个用户至少数以一个组。  
2. 用户家目录概念：/home/目录下有各个创建的家目录，当用户登录时，会自动的进入到自己的家目录。
![用户和组](/linux\linuxfile\用户组.png)

## 添加用户
### 基本语法
useradd [选项] 用户名  

useradd xm  
xm后面没有加参数，默认创建一个xm用户和一个xm组，并将xm用户放到xm组中。  

useradd -d /home/tiger/ xh  
指定xh的家目录为/home/tiger

## 修改/指定 用户密码：  
passwd xh

## 用户删除
### 基本用法
userdel 用户名

userdel -r xm  
删除用户但是保留家目录

userdel xm  
删除用户并删除家目录

*注：工作过程中一般保留家目录*

## 查询用户信息
### 基本用法
id 用户名
![用户信息](/linux\linuxfile\用户信息.png)  
uid：用户id  
gid：用户所属组id  
groups：用户所属组名称

cat /etc/passwd  
查询所有用户
![cxsyyh3](/linux\linuxfile\cxsyyh3.png)

## 切换用户
### 基本用法
su - 切换用户名
![切换用户](/linux\linuxfile\用户切换.png)  
从普通用户向root进行切换的时候需要重新输入密码  
![切换到root](/linux\linuxfile\切换到root.png)
exit  
返回到原来的用户  
![返回用户](/linux\linuxfile\返回用户.png)  
whoami
查询当前用户  
![qdyh](/linux\linuxfile\当前用户.png)
# 5. 组管理
## 基本介绍
类似于角色，系统可以对有多个共性的多个用户进行统一的管理。
## 增加组
groupadd 组名  
![创建组](/linux\linuxfile\创建组.png)  
## 删除组
groupdel 组名
## 增加用户时直接加入上组
useradd -g 用户组 用户名
![tjyhdz](/linux\linuxfile\添加用户直接添加到组.png)  
## 用该用户组
usermod -g 用户组 用户名
![gbyhz](/linux\linuxfile\改变用户组.png)  

# 6. 用户和组相关的文件
/etc/passwd：用户配置文件（用户互信息）  
![zxsyyh2](/linux\linuxfile\cxsyyh2.png)

/etc/group：组配置文件（组信息）  
![zxx](/linux\linuxfile\组信息.png)

/etc/shadow：口令配置文件（密码和登录信息,，包括密码，是加密）
![sd](/linux\linuxfile\shadow.png)






