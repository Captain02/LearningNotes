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
*特别注意：由于locate指令基于数据库进行查询，所以第一次运行前，必须使用updatedb指令创建locate数据库。*  
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
 ![6](/linux/linuxfile/6.png)   
## 权限的基本介绍
ls -l中显示内容如下  
待修改  
 ![8](/linux/linuxfile/8.png)  
 ## rwx权限详解
 1. rwx作用到文件  
 >1. [r] 代表可读(read):可以读取，查看  
 >2. [w] 代表写(write):可以修改，但是不代表可以删除文件，删除一个文件的前提条件是对该文件所在的目录有写权限，才能删除该文件。  
 >3. [x] 代表可执行(execute):可以被执行
2. rwx作用到目录  
>1. [r]代表可读(read):可以读取，ls查看目录内容  
>2. [w]代表可写(write):可以修改，目录内创建+删除+重命名目录  
>3. [x]代表可执行(execute):可以进入该目录  

*注意：r=4、w=2、x=1,因此rwx=4+2+1=7*
## 修改权限-chmod
基本说明：  
通过chmod指令，可以修改文件或者目录的权限  
1. 第一种方式：+、-、=变更权限  
u:所有者  
g:所有组  
o:其他人  
a:所有人(u、g、o的总和)  
(1) chmod u=rwx,g=rx,o=x 文件目录名  
(2) chmod o+w 文件目录名  
(3) chmod a-x 文件目录名  
> 练习  
>(1) 给abc文件的所有者读写执行的权限，给所在组读执行权限。  
> ![9](/linux/linuxfile/9.png)  
>(2) 给abc文件的所有者除去执行的权限，增加组写的权限  
>![10](/linux/linuxfile/10.png)  
>(3) 给abc文件的所有用户添加读的权限  
>![11](/linux/linuxfile/11.png)  
2. 第二种方式：通过数字变更权限  
r=4、w=2,、x=1，rwx=4+2+1=7  
chmod u=rwx,g=rx,o=x 文件名  
相当于chmod 751 文件目录名  
>练习  
>将/home/tom/abc文件的权限修改成rwxr-xr-x,使用数组的方式。   
>rwx = 4+2+1=7  
>r-x = 4+1=5  
>chmod 755 /home/tom/abc  
## 修改文件所有者-chown  
基本介绍  
chown newowner file  
chown newowner:newgroup file 改变用户的所有者和所有组  
-R 若果是目录 则使其下所有子文件或者目录递归生效  
>练习  
>1. 将/home/abc.txt文件的所有者修改成tom  
>![12](/linux/linuxfile/12.png)  
>2. 请将/home/kkk目录下的文件和目录的所有者都修改成tom   
>![13](/linux/linuxfile/13.png)  
## 修改文件所在组-chgrp
chgrp newgroup file 改变文件的所有组  
>1. 请将/home/abc.txt文件的所在组修改成bandit(土匪)  
>chgrp bandit /home/abc.txt  
>2. 请将/home/kkk目录下所有文件和目录所在组都修改成bandit(土匪)  
>chgrp -R bandit /home/abc.txt  


## 小结：
>1. chown-修改文件所属用户  
>2. chgrp-修改文件所属组  
>3. usermod-修改用户所在组  
>4. chmod-修改文件或者目录的权限 

# 定时任务调度  
## 原理图  
![14](/linux/linuxfile/14.png)  
## 概述  
任务调度：是指操作系统在某个时间执行的特定的命令或程序。  
任务调度分类：  
1. 系统工作：有些重要的工作必须周而复始的执行，比如病毒扫描等等。  
2. 个别用户工作：个别用户可能希望执行某些程序，比如mysql数据库备份。
## 基本语法  
crontab [选项]  
## 常用选项  
-e 编辑crontab定时任务  
-l chaxun crontab任务  
-r 删除当前用户所有的crontab任务  
## 快速入门  
设置任务调度文件：/etc/crontab  
设置个人任务调度。执行crontab -e命令。  
接着输入任务调度文件  
如：*/1 * * * * |ls -l /etc/>tmp/to.txt  
意思就是每小时的每分钟执行一次ls -l /etc/>tmp/to.txt命令  
## 参数细节说明  
5个占位符的说明  
项目|含义|范围  
-|-|-  
第一个*|一小时中的第几分钟|0-59  
第二个*|一天当中的第几个小时|0-23  
第三个*|一月当中的第几天|1-31  
第四个*|一年当中的第几个月|1-12  
第五个*|一周当中的星期几|0-7（0、7都代表星期日）  

参数细节说明  
特殊符号|含义
-|-  
" * "|代表任何时间。比如第一个*就代表一小时中每分钟都执行一次的意思。
,|代表不连续的时间。比如"0 8,12,16 * * * 命令"，就带表在每天的8点0分，12点0分，16点0分都执行一次  
-|代表连续的时间范围。比如"0 5 * * 1-6"命令，代表在每周一到周六的凌晨5点0分执行命令  
*/n|代表每个多久执行一次。比如"*/10 * * * *"命令，代表每个1分钟就执行一遍命令。
>注意:  
>1. 如果只是简单的任务，可以不写脚本，直接在crontab中加入任务即可。
>2. 对于比较复杂的任务，需要写脚本(shell编程)。  
## 任务调度的几个应用实例
1. 每隔1分钟，就将当前的日期信息，追加到/tmp/mydate文件中  
1)先编写一个文件mytask.sh  
data >> /tmp/mydate  
2)给mytask.sh给一个执行权限  
3)crontab -e  
4)*/1 * * * * /home/mytask.sh  
# Linux磁盘分区、挂载
## 分区基础知识
1. mbr分区：  
1).最多支持四个主分区  
2).系统只能安装在主分区  
3).扩展分区要占一个主分区  
4).MBR最大只支持2TB，但拥有最好的兼容性  
2. gtp分区：  
1).支持无限读个主分区（但操作系统可能限制，比如windos下最多128个分区）  
2).最大只会18EB的大容量（EB=1024PB,1PB=1024GB） 
3).windows7 64位以后支持gtp  
## Linux分区
### 原理介绍
1) linux来说无论有几个分区，分给那一目录，它归根结底就只有一个根目录，一个独立且唯一的文件结构，Linux中每个分区都是用来组成文件系统的一部分。
2) linux采用了一种叫“挂载”的处理方法，他的整个文件系统中包含了一整他的文件和目录，且将一个分区和一个目录连接起来，这时要载入一个分区将使它的存储空间在一个目录下获得  
3) 示意图：  
![15](/linux/linuxfile/15.png)  
### 硬盘说明
1. Linux硬盘分IDE硬盘和SCSI硬盘，目前基本上是SCSI硬盘。  
2. 对于IDE硬盘，驱动器标识为“hdx~”,其中"hd"表名分区所设备的类型，这里是指IDE硬盘了，x为盘号(a为基本盘,b为基本从属盘,c为辅助主盘,为辅助从属盘),~代表分区，前四个分区用数字1到4标识，他们是主分区和扩展分区，从5开始就是逻辑分区，例如：hda3标识为第一个IDE硬盘上的第三个主分区或扩展分区，hdb2表示为第二个IDE硬盘上的第二个主分区或扩展分区。  
3. 对于SCSI硬盘则表示为"sdx"，SCSI硬盘是用"sd"来表示分区所在设备的类型的，其余则和IDE硬盘的表示方法一样。  
4. 使用lsblk -f指令进行查看分区情况  
![17](/linux/linuxfile/17.png)  
### 如何增加一块新硬盘
1)虚拟机添加硬盘  
2)分区 fdisk /dev/sdb  
3)格式化 mkfs -t ext4 /dev/sdb1  
4)挂载 先创建一个/home/newdisk，挂载到mount /dev/sdb1 /home/newdisk  
5)设置可以自动挂载  
vim /etc/fatab  
/dev/sdb1  /home/newdisk ext4 defaults 0 0  
### 磁盘使用情况查询
1. 查询系统整个磁盘的使用情况  
df -h  
![18](/linux/linuxfile/18.png)  
2. 查询指定目录占用磁盘的情况  
du -h  
-s 指定目录占用大小汇总  
-h 带计量单位  
-a 含文件  
--max-depth=1 子目录深度  
-c 列出明细的同时，增加汇总值  
![19](/linux/linuxfile/19.png)  
3. 磁盘工作情况  
1)统计/home文件夹下文件的个数  
![20](/linux/linuxfile/20.png)  
2)统计/home文件夹下目录的个数  
![21](/linux/linuxfile/21.png)  
3)统计/home文件夹下文件的个数，包括子文件夹里的  
![22](/linux/linuxfile/22.png)  
4)统计文件夹下目录的个数，包括子文件夹里的  
![23](/linux/linuxfile/23.png)  
5)以树状显示目录结构  
![24](/linux/linuxfile/24.png)  
# Linux网络配置
## Linu网络配置原理图
目前我们的网络采用的是NAT模式  
![25](/linux/linuxfile/25.png)  
## 指定固定ip  
编辑网络配置文件：vim /etc/sysconfig/network-scripts/ifcfg-enp0s3  
![26](/linux/linuxfile/26.png)  
重启网络服务：service network restart  
## 防火墙添加端口
开端口命令：firewall-cmd --zone=public --add-port=80/tcp --permanent  
重启防火墙：systemctl restart firewalld.service  
命令含义：  
--zone #作用域  
--add-port=80/tcp  #添加端口，格式为：端口/通讯协议  
--permanent   #永久生效，没有此参数重启后失效  
## 查看防火墙设置开机自启是否成功
systemctl is-enabled firewalld.service;echo $?  
![56](/linux/linuxfile/56.png)  
## 检查防火墙状态是否打开  
firewall-cmd --state  
## 自启防火墙  
systemctl start firewalld.service  
## 设置开机自启  
systemctl enable firewalld.service  
## 重启防火墙
systemctl restart firewalld.service  
# 进程管理
基本介绍  
1. 在Linux中，每个执行的程序都称为一个进程，每一个进程都分配一个ID号。  
2. 每一个进程，都会对应一个父进程，而这个父进程可以复制多个子进程。例如www服务器。  
3. 每个进程都可能以两种方式存在的，前台与后台，所谓前台进程就是用户目前的屏幕上可以进行操作的，后台进程则是实际在操作，但是由于屏幕上无法看到进程，通常使用后台方式执行。  
4. 一般系统的服务都是以后台进程的方式存在，而且都会常驻在系统中。直到关机才结束。  
## 基本介绍  
ps命令是用来查看目前系统中，有哪些正在执行，以及他们执行的状况。可以不参加任何参数。  
PID:进程识别号  
TTY:终端机号  
TIME:此进程所消CPU时间  
CMD:正在执行的命令或者进程名  
ps -a:显示当前终端的所有进程消息  
ps -u:以用户的格式显示进程信息  
ps -x:显示后台进程运行的参数  
![28](/linux/linuxfile/28.png)  
使用grep进行筛选  
![29](/linux/linuxfile/29.png)  
*注意：STAT：进程状态，其中S-睡眠，s-便是该进程是会话的先导进程,N-表示进程拥有比普通优先级更低的优先级，R-正在运行，D-短期等待，Z-僵死进程，T-被跟踪或者被停止等等*  

ps -ef 可查看父id  
![30](/linux/linuxfile/30.png)  
## 终止进程
kill [选项]  
例如：  
1. kill -9  
2. killall gedit 通过进程名称来终止进程  
## 服务管理
### service管理指令
service 服务名 [start|stop|restart|reload|status]  
7.0以后使用systemctl    
### 使用案例
1)查看当前防火墙的状况，关闭和重启防火墙。  
![31](/linux/linuxfile/31.png)  
可以使用netstat -tunlp命令来查看端口占用的情况  
![32](/linux/linuxfile/32.png)  
查看服务列表  
centos6 可以使用ls -l /etc/init.d  
centos7 可以使用ls -l  systemctl list-units --type=service  
### chkconfig命令  
介绍  
通过chkconfig命令可以给每个服务的各个运行级别设置自启动/关闭  
基本语法  
1)查看服务 chkconfig --list|grep xxx  
2)chkconfig 服务名  --list  
3)chkconfig --level 5 服务名 on/off(设置)  
![33](/linux/linuxfile/33.png)  
### 进程的监控指令 top
基本语法  
top [选项]  
选项说明  
选项|功能
-|-
-d秒数|指定top命令间隔几秒更新，默认是3秒在top命令的交互模式当中可以执行的命令
-i|使top不显示任何闲置或者僵死进程
-p|通过指定监控进程id来仅仅监控某个进程的状态  
交互操作说明  
操作|功能
-|-
P|以CPU使用率进行排序，默认就是此项
M|以内存的使用率进行排序
N|以PID进行排序
Q|退出top  
![34](/linux/linuxfile/34.png)  
### 查看系统网络情况 netstat
基本语法  
netstat [选项]  
netstat -anp  
-an 按一定顺序排列输出  
-p 显示那个进程在调用  
![35](/linux/linuxfile/35.png)  
# RPM和YUM的管理
## rpm
查询已安装的rpm列表 rpm -qa|grep xx  
*注意：格式中带有noarch代表32/64通用*  
rpm -ql xxx查看软件安装位置  
rpm -e xxx卸载  
rpm -e --nodeps xx强制删除  
安装rpm包  
rpm -ivh xxx  
i = install安装  
v = verbose提示  
h = hash进度条  

## yum
查询yum服务器是否有需要安装的软件  
yum list|grep xx软件列表  
安装指定的yum包  
yum install xxx下载安装  
yum list installed查看已安装的软件包
![36](/linux/linuxfile/36.png)  


