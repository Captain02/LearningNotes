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

sync:将内存的数据同步到磁盘[关机或者重启之前使用]

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
![用户和组](/linux/linuxfile/用户组.png)

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
![用户信息](/linux/linuxfile/用户信息.png)  
uid：用户id  
gid：用户所属组id  
groups：用户所属组名称

cat /etc/passwd  
查询所有用户
![cxsyyh3](/linux/linuxfile/cxsyyh3.png)

## 切换用户
### 基本用法
su - 切换用户名  
![切换用户](/linux/linuxfile/用户切换.png)  
从普通用户向root进行切换的时候需要重新输入密码  
![切换到root](/linux/linuxfile/切换到root.png)  
exit  
返回到原来的用户  
![返回用户](/linux/linuxfile/返回用户.png)  
whoami
查询当前用户  
![qdyh](/linux/linuxfile/当前用户.png)
# 5. 组管理
## 基本介绍
类似于角色，系统可以对有多个共性的多个用户进行统一的管理。
## 增加组
groupadd 组名  
![创建组](/linux/linuxfile/创建组.png)  
## 删除组
groupdel 组名
## 增加用户时直接加入上组
useradd -g 用户组 用户名  
![tjyhdz](/linux/linuxfile/添加用户直接添加到组.png)  
## 用该用户组
usermod -g 用户组 用户名  
![gbyhz](/linux/linuxfile/改变用户组.png)  

# 6. 用户和组相关的文件
/etc/passwd：用户配置文件（用户互信息）  
![zxsyyh2](/linux/linuxfile/cxsyyh3.png)

/etc/group：组配置文件（组信息）  
![zxx](/linux/linuxfile/组信息.png)

/etc/shadow：口令配置文件（密码和登录信息,，包括密码，是加密）  
![sd](/linux/linuxfile/shadow.png)

# 7. 实用指令
## 1. 运行级别
1. linux一共七个运行级别，分别是  
0：关机  
1：单用户（用于找回密码）  
2：多用户无网络服务  
3：多用户有网络服务  
4：保留  
5：图形界面  
6：重启
2. 系统的运行级别配置文件  
/etc/inittable
3. 切换到指定运行级别的指令  
init [级别编号]
4. 单用户模式找回密码(Centos6)  
1)开机上下键进入操作系统选择界面，再按回车键  
![找回密码1](/linux/linuxfile/找回密码1.png)  
2)将光标移动到第二行再按e键。  
![找回密码](/linux/linuxfile/修改密码2.png)  
3)输入空格，再输入1,让我们进入单用户模式，再次输入enter键。  
![修改密码](/linux/linuxfile/修改密码3.png)  
4)再输入b,回车直接进入单用户模式。  
![修改密码](/linux/linuxfile/修改密码4.png)  
5)使用passwd root直接修改root密码。  
![修改密码](/linux/linuxfile/修改密码5.png)
## 2. 帮助指令
1. man 获得帮助信息  
man [命令或者配置文件]  (功能描述：获得帮助信息)  
*按j或者k进行滚动查看*
2. help指令
help 命令(功能描述：获得shell内置命令的帮助信息)
## 3. 文件目录类指令  
1. pwd指令  
(1) 显示当前工作目录的绝对路径
2. ls指令  
基本语法  
(1)ls [选项] [目录或是文件]  
常用选项  
(1) -a 显示当前目录所有的文件和目录，包括隐藏的  
(2) -l 以列表的方式显示信息  
3. cd 指令  
基本语法  
(1) cd [参数]  
常用参数  
(1) 绝对路径和相对路径  
(2) cd~ 回到家目录  
(3) cd .. 回到上一级目录  
4. mkdir指令    
基本语法  
(1) mkdir [选项] 要创建的目录  
常用选项  
(1) -p 创建多级目录  
5. rmdir指令  
基本语法  
(1)rmdir[选项] 要删除的空目录  
常用参数  
(1)-rf 删除非空的目录  
6. touch 指令  
基本语法  
(1) touch 文件名称  
7. cp 指令  
基本语法  
(1) cp [选项] source dest  
常用选项  
(1) -r 递归拷贝  
*注：\cp -r [拷贝文件/目录] [存放位置] 可以进行强制覆盖*
8. rm指令  
基本用法  
rm [选项] 要删除的文件或者目录  
常用语法  
(1) -r 递归删除整个文件夹  
(2) -f 强制删除不提示  
9. mv 指令  
基本用法  
mv oldNameFile newNameFile 重命名  
mv /temp/movefile /targetFolder  
10. cat指令  
基本语法  
cat [选项] 要查看的文件  
常用选项  
(1) -n 显示行号  
(2) cat [选项] 文件名 | more 分页显示  
11. more 指令  
基本语法  
more 要查看的文件  
快捷键  
space 向下翻一页  
enter 向下翻一行  
q 代表立即离开more，不再读取文件内容  
ctrl+f 向下滚动一屏  
ctrl+b 向上滚动一屏  
= 显示当前行号  
:f 显示当前文件名和行号  
12. less 指令  
less指令用来分屏查看文件内容，他的功能与more指令类似，但是比more指令更加抢到，支持各种显示终端，less指令在显示文件内容时，并不是一次将整个文件加载之后才显示，而是根据显示需要加载内容，对于显示大型文件具有较高的效率。  
基本用法  
less 要查看的文件  
快捷键  
space 向下翻动一页  
pagedown 向下翻动一页  
pageup 向上翻动一页  
13. &gt;指令和>>指令  
&gt; 输出重定向指令  
&gt;&gt; 追加指令  
基本语法  
(1)ls -l &gt;文件  
将列表的内容写入到文件中，会进行覆盖  
(2)ls -l >>文件  
将列表内容追加到文件的末尾  
(3)cat 文件1 > 文件2  
(4)echo "内容" >> 文件  
14. echo指令  
基本语法  
echo [选项][输出内容]  
*注意：可以用来输出环境变量*
15. head指令  
基本用法  
head 文件(查看前10行文件内容)  
head -n 5 文件(查看文件头5行内容)  
16. tail指令  
tail用于输出文件中尾部的内容  
基本用法  
(1)tail 文件 (默认查看文件后10行的内容)  
(2)tail -n 5 文件 (默认查看文件后5行内容)  
(3)tail -f 文件 (实时追踪文档的所有更新)  
17. ln指令 
软连接指令也成为符号链接，类似于快捷方式，主要存放了链接以及其他文件路径。  
基本语法  
ln -s [原文件或目录] [软连接名]  (功能描述:给源文件创建一个软连接)  
*注意：在删除软连接的时候不要带/，负责显示，资源忙。*
18. history指令  
基本语法  
history(功能描述：查看已经执行过的历史指令)  
*注意：![指令历史编号] 可以执行该历史指令*
## 4.时间日期类
1. date指令-显示当前日期  
基本语法  
(1)date (功能描述：显示当前时间)  
(2)date+%Y (功能描述：显示当前年份)  
(3)date+%m (功能描述：显示当前月份)  
(4)date+%d (功能描述：显示当前是哪一天)  
![时间指令](/linux/linuxfile/时间.png)
2. 设置日期  
date -s 字符串时间  
![修改时间](/linux/linuxfile/修改时间.png)  
3. cal指令  
显示日历  
基本语法  
cal [年]  
## 5. 搜索查找  
1. find 指令  
find [搜索范围] [选项]  
![软件查找](/linux/linuxfile/文件查找.png)  
案例1：查找linux系统下大于20M的文件  
![软件查找](/linux/linuxfile/大于20M文件.png)   
![软件查找](/linux/linuxfile/文件信息.png)  
*注意：ls -lh 可以查看以M为单位的文件信息，如果文件接近1G，会以G为单位进行显示*  
2. locate指令(Centos6)  
locate指令可以快速定位文件路径，locate指令利用实现建立的系统中所有文件名称以及路径的locate数据库实现快速定位给定的文件。locate指令无需遍历整个文件系统，查询速度较快。  
基本语法  
locate搜索文件  
*特别注意：由于locate指令基于数据库进行查询，所以第一次运行前，必须使用updatedb指令创建locate数据库。  
3. grep 指令和管道指令 |  
基本用法  
grep[选项] 查找内容 源文件  
常用选项  
-n 显示匹配行以及行号。  
-i 忽略字母大小  
![grep](/linux/linuxfile/grep22.png)  
## 6. 压缩和解压缩
1. gzip/gunzip(单个文件)  
基本语法  
gzip 文件(功能描述：压缩文件，只能将文件压缩为*.gz文件)  
gunzip 文件.gz(功能描述：解压缩文件命令)  
*注意：源文件就消失了*  
压缩：  
![gzip](/linux/linuxfile/gzip.png)  
解压:  
![gzip](/linux/linuxfile/解压.png)  
2. zip/unzip指令(可用于文件夹)  
zip用于压缩文件，unzip用于解压  
基本语法  
zip [选项] xxx.zip  
unzip [选项] xxx.zip  
常用参数  
-r:递归压缩  
-d<目录>：指定解压后文件的存放目录  
压缩：  
![gzip](/linux/linuxfile/压缩2.png)  
解压：  
![gzip](/linux/linuxfile/解压2.png)  
3. tar指令  
tar指令是打包命令，最后打包的文件是.tar.gz的文件  
基本语法  
tar [选项] XXX.tar.gz 打包的内容(功能描述：打包目录，压缩后得文件格式.tar.gz)  
选项说明  
-c 产生.tar打包文件  
-v 显示详细信息  
-f 指定压缩后的文件名  
-z 打包同时压缩  
-x 解包.tar文件  
压缩：  
![gzip](/linux/linuxfile/压缩.png)  
解压：  
![gzip](/linux/linuxfile/解压4.png)  
解压到指定目录：  
![gzip](/linux/linuxfile/解压5.png)  
# 8.组管理与权限管理  
## linux组的基本介绍
1. linux中每个用户必须属于一个组，不能独立于组外，在linux中每个文件有所有者、所在组、其他组的概念。  
 ## 文件/目录 所有者  
 一般文件的创建者，谁创建了改文件，就自然成为改文件的所有者。
 1. 查看文件的所有者   
 (1)指令：ls -ahl  
 (2)应用实例：创建一个组police ,再创建一个用户tom,然后使用tom来创建一个文件。  
 ![1](/linux/linuxfile/1.png)  
 ![2](/linux/linuxfile/2.png)  
2. 修改文件的所有者  
(1)指令：chown 用户名 文件名  
(2)应用案例：使用root创建一个文件apple.txt，然后将其所有者修改成为tom  
 ![3](/linux/linuxfile/3.png)  
## 组的创建
1. 基本指令  
groupadd组名  
2. 应用实例  
创建一个组monster  
创建一个用户fox,并放入monster组中  
 ![4](/linux/linuxfile/4.png)  
## 文件/目录所在组
当某个用户创建了一个文件后，默认这个文件的所在组就是该用户所在的组。  
1. 基本指令  
ls -ahl  
2. 应用实例  
修改文件所在组  
3. 基本指令  
chgrp 组名 文件名  
4. 应用实例  
使用root用户创建文件 orange.txt,看看这个文件属于哪个组，然后将这个文件所在组，修改到police组。  
 ![5](/linux/linuxfile/5.png)  
 ## 其他组
 除了文件所有者和所在组的用户外，系统的其他用户都是文件的其他组
1. 改变用户所在组  
在添加用户时，可以指定该用户添加到那个组中，同样的用root的管理权限可以改变某个用户所在的组。  
(1)usermod -g 组名 用户名  
(2)usermod -d 目录名 用户名 改变用户登录的初始目录  
2. 应用实例  
创建一个土匪组(bandit)将tom这个用户从原来的police组修改到土匪(bandit)组。