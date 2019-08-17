# Shell是什么 
![37](/linux/linuxfile/37.png)  
shell是一个命令解释器，它为用户提供了一个向Linux内核发送请求以便运行程序的界面系统程序，用户可以用shell来启动、挂起、停止甚至是编写一些程序。  
# Shell脚本的执行方式  
# 脚本格式要求 
1. 脚本以#!/bin/bash开头  
2. 脚本需要有可执行权限  
# 编写第一个Shell脚本
1. 需求说明  
2. 创建一个Shell脚本，输出Hello World  
![38](/linux/linuxfile/38.png)  
# 脚本的常用执行方式  
方式一: (输入脚本的绝对路径或相对路径)  
1)首先要赋予helloworld.sh脚本的+x权限  
2)执行脚本  
![39](/linux/linuxfile/39.png)  
方式二: (sh+脚本)  
说明:不用赋予脚本+x权限，直接执行即可  
![40](/linux/linuxfile/40.png)  
# Shell的变量
Shell的变量介绍  
1. Linux Shell中的变量分为，系统变量和用户自定义变量  
2. 系统变量：$HOME、$PWD、$SHELL、$USER等等  
比如:echo $HOME等等  
3. 显示当前shell中所有变量:set  
# shell变量的定义
基本语法  
1. 定义变量:变量=值  
2. 撤销变量:unset 变量  
3. 声明静态变量:readonly 变量，注意:不能unset  
>快速入门  
>案例1. 定义变量A  
>案例2. 撤销变量A  
>案例3. 声明静态的变量B=2，不能unset  
>案例4. 可把变量提升为全局环境变量，可供其他shell程序使用  

输出系统变量:  
![41](/linux/linuxfile/41.png)  
输出自定义变量:  
![42](/linux/linuxfile/42.png)  

## 定义变量的规则  
1. 变量名称可以由字母、数字、下划线组成，但不能用数字开头  
2. 等号两侧不能有空格  
3. 变量名称一般习惯为大写  
## 将命令的返回值赋给变量(重点)  
1. A=`` `ls -la` ``反引号，运行里面的命令，并把结果返回到变量A  
2. A=$(ls -la)等价于反引号  
![43](/linux/linuxfile/43.png)  
# 设置环境变量 
## 基本语法
1. export 变量名=变量值(功能描述：将shell变量输出为环境变量)  
2. source 配置文件(功能描述:让修改后的配置信息立即生效)  
3. echo $变量名(功能描述:查询环境变量的值)  
![44](/linux/linuxfile/44.png)  
# 位置参数变量
## 基本语法
$n(功能描述：n为数字，$0代表命令本身，$1-$9代表第一到第九个参数，十个以上的参数需要用大括号包含,如${10})  
$*(功能描述：这个变量代表命令行中所有的参数,$*把所有的参数看做一个整体)  
$@(功能描述：这个变量也代表命令行中所有的参数，不过$@把每个参数区分对待)  
$#(功能描述：这个变量代表命令行中所有参数的个数)  
![45](/linux/linuxfile/45.png)  
![46](/linux/linuxfile/46.png)  
# 与定义变量
就是shell设计者实现已经定义好的变量，可以直接在shell脚本中使用  
## 基本语法
$$(功能描述:当前进程的进程号(PID))  
$!(功能描述:后台运行的最后一个进程的进程号(PID))  
$?(功能描述:最后一次执行的命令的返回状态，如果这个变量的值为0，证明上一个命令正确执行；如果这个变量的值非0(具体是哪个数字，由命令自己来决定)，则证明上一个命令执行不正确了。)  
![47](/linux/linuxfile/47.png)  
![48](/linux/linuxfile/48.png)  
# 运算符
## 基本介绍
学习如何在shell中进行各种运算符操作。  
## 基本语法
1. $((运算符))或者$[运算符]  
2. expr m + n  
*注意expr运算符间要有空格*  
3. expr m - n  
4. expr \ *,/,%乘除取余  
## 应用实例
案例一：计算(2+3)*4的值  
![50](/linux/linuxfile/50.png)  
案例二：请求出命令行的两个参数的和  
![51](/linux/linuxfile/51.png)  
# 条件判断
## 基本语法
[condition](注意condition前后要有空格)  
*注意非空返回true，可使用$?验证(0为true，>1为false)*  
## 应用实例
[atguigu]返回true  
[]返回false  
[condition]&&echo OK || echo notok  
# 条件判断
## 常用判断条件
1. 两个整数的比较  
=字符串比较  
-lt小于  
-le小于等于  
-eq等于  
-gt大于  
-ge大于等于  
-ne不等于  
2. 按照文件权限进行判断  
-r有读的权限  
-w有写的权限  
-x有执行的权限  
3. 按照文件类型进行判断  
-f文件存在并且是一个常规的文件  
-e文件存在  
-d文件存在并是一个目录  
## 应用实例
案例一："ok"是否等于"ok"  
![52](/linux/linuxfile/52.png)  
案例二：23是否大于等于22  
![53](/linux/linuxfile/53.png)  
案例三：/home/shell/目录中的文件是否存在aa.txt  
![54](/linux/linuxfile/54.png)  
# 流程控制
## if判断
基本语法  
if[ 条件判断 ];then  
    程序  
fi  
或者  
if[ 条件判断式 ]  
then
程序
elif[ 条件判断式 ]  
then  
程序  
fi  
注意事项:  
1[ 条件判断式 ]，中括号和条件判断式之间必须有空格  
2推荐使用第二种方式  
## case语句
基本语法  
case $变量名 in  
"值1" )  
如果变量的值等于1 ,则执行程序1  
;;  
"值2" )  
如果变量的值等于2 ,则执行程序2  
;;  
*)  
输出其他语句  
;;
esac  
![57](/linux/linuxfile/57.png)  
## for循环
基本语法1  
```
for 变量in 值1 值2 值3..  
do  
    程序
done  
```  
基本语法2  
```  
for((初始化;循环控制条件;变量变化))
do
    程序  
done
```  
![58](/linux/linuxfile/58.png)  
![59](/linux/linuxfile/59.png)  
## while
基本语法1  
```
while[条件片段式]
do
    程序
done
```
![60](/linux/linuxfile/60.png)  
## 读取控制台的输入
基本语法  
read(选项)(参数)  
选项:
-p:指定读取值是的提示符；
-t:指定读取值时等待的时间(秒),如果没有在指定的时间内输入，就不再等待了。  
参数：  
变量:指定读取值的变量名  
![61](/linux/linuxfile/61.png)  
# 函数
## 系统函数
basename基本语法  
功能:返回完整路径后/部分，常用语获取文件名  
```
basename[pathname][suffix]
basename[string][suffix]
(功能描述:basename命令会删除掉所有的前缀包括最后一个('/')字符串，然后将字符串显示出来)。  
```
选项：  
suffix为后缀，如果suffix被指定了，basename会将pathname或string中的suffix去掉。  
dirname基本语法  
功能:返回完整路径最后/的前面部分，常用语返回路径部分  
dirname文件绝对路径（功能描述：从给定的包含绝对路径的文件名中去去除文件名(非目录的部分），然后返回剩下的路径（目录部分））  
![62](/linux/linuxfile/62.png)   
## 自定义函数
基本语法  
```
[function]funname[{}]
{
    Acction;
    [return int;]
}
```  
调用直接写函数名:funname  
![63](/linux/linuxfile/63.png)   

# shell编程综合案例
## 需求分析
1. 每天凌晨2:10备份数据库到atguiguDB到/data/backup/db  
2. 备份开始和备份结束能给出相应的提示信息  
3. 备份后的文件要求以备份时间为文件名，并打包成.tar.gz的形式，比如:2018-03-12_230201.tar.gz  
4. 在备份的同时，检查是否有10天前备份的数据库文件，如果有就将其删除。  
脚本命令：  
![64](/linux/linuxfile/64.png)  
创建定时器：  
![65](/linux/linuxfile/65.png)  
写定时任务：  
![66](/linux/linuxfile/66.png)  