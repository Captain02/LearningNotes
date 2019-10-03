# 内容概述
1. nginx简介  
(1) 介绍nginx的应用场景和具体可以做什么事情  
(2) 什么是反向代理  
(3) 什么是负载均衡  
(4) 什么是动静分离  
2. nginx的安装  
(1) 介绍nginx在linux系统中如何进行安装  
3. nginx常用命令和配置文件  
(1) 介绍ngin启动、关闭、重新加载命令  
(2) 介绍nginx的配置文件
4. nginx配置实例-反向代理  
5. nginx配置实例-负载均衡  
6. nginx配置实例-动静分离
7. nginx原理与优化参数配置  
(1)搭建nginx高可用集群(主从模式)  
(2)搭建nginx高可用集群(双主模式)  
# 第一章 Nginx简介  
## Nginx概述  
Nginx是一个高性能的http和反向代理服务器，特点是占有内存少，并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等等。  
## Nginx作为web服务器  
Nginx可以作为静态页面的web服务器，同时还支持CGI协议的动态语言，比如perl、php等。但是不支持java。Java程序只能通过与tomcat配合完成。Nginx专为性能优化而开发，性能是其最重要的考量,实现上非常注重效率，能经受高负载的考验，有报告表明能支持高达50,000个并发连接数。  
https://lnmp.org/nginx.html  
## 正向代理  
Nginx不仅可以做反向代理，实现负载均衡。还能用作正向代理来进行上网等功能。正向代理:如果把局域网外的Internet想象成一个巨大的资源库，则局域网中的客户端要访问Internet,则需要通过代理服务器来访问，这种代理服务就称为正向代理。  
![1](/Nginx/nginxFile/1.png)  
## 反向代理  
反向代理，其实客户端对代理是无感知的，因为客户端不需要任何配置就可以访问，我们只需要将请求发送到反向代理服务器，由反向代理服务器去选择目标服务器获取数据后，在返回给客户端，此时反向代理服务器和目标服务器对外就是-一个服务器，暴露的是代理服务器地址，隐藏了真实服务器IP地址。
![2](/Nginx/nginxFile/2.png)  
## 负载均衡  
客户端发送多个请求到服务器，服务器处理请求，有- -些可能要与数据库进行交互，服务器处理完毕后，再将结果返回给客户端。这种架构模式对于早期的系统相对单- ~,并发请求相对较少的情况下是比较适合的，成本也低。但是随着信息数量的不断增长，访问量和数据量的飞速增长，以及系统业务的复杂度增加，这种架构会造成服务器相应客户端的请求8益缓慢，并发量特别大的时候，还容易造成服务器直接崩溃。很明显这是由于服务器性能的瓶颈造成的问题，那么如何解决这种情况呢?  
我们首先想到的可能是升级服务器的配置，比如提高CPU执行频率，加大内存等提高机器的物理性能来解决此问题，但是我们知道摩尔定律的日益失效，硬件的性能提升已经不能满足日益提升的需求了。最明显的一个例子，天猫双十一当天，某个热销商品的瞬时访问量是极其庞大的，那么类似上面的系统架构，将机器都增加到现有的顶级物理配置，都是不能够满足需求的。那么怎么办呢?  
上面的分析我们去掉了增加服务器物理配置来解决问题的办法,也就是说纵向解决问题的办法行不通了,那么横向增加服务器的数量呢?这时候集群的概念产生了，单个服务器解决不了，我们增加服务器的数量,然后将请求分发到各个服务器上，将原先请求集中到单个服务器上的情况改为将请求分发到多个服务器上,将负载分发到不同的服务器，也就是我们所说的负载均衡。
![3](/Nginx/nginxFile/3.png)  
## 动静分离
为了加快网站的解析速度，可以把动态页面和静态页面由不同的服务器来解析,加快解析速度。降低原来单个服务器的压力。
![4](/Nginx/nginxFile/4.png)  
# 第二章 安装Nginx
## 进入nginx官网，下载  
http://nginx.org/
![5](/Nginx/nginxFile/5.png)  
1. 安装pcre依赖  
(1)联网下载pcre压缩文件依赖wget htp://downloads.sourceforge.net/project/pcre/pcre/8.37/pcre-8.37.tar.gz
![6](/Nginx/nginxFile/6.png)  
(2))解压压缩文件  
使用命令tar -xvf pcre-8.37.tar.gz  
(3)./configure完成后，回到pcre目录下执行make,最后执行make install  
![7](/Nginx/nginxFile/7.png)  
安装openssl、zlib、gcc 依赖  
yum -V install make zlib zlib-devel gcc-c++ libtoo openssl openssl-devel  
(4)安装nginx,使用命令解压，./configure进行检查，make && make install进入目录/usr/local/nginx/sbin/nginx启动服务
![8](/Nginx/nginxFile/8.png)  
```
注意:  
在windows系统中访问linux 中nginx，默认不能访问的，因为防火墙问题  
(1)关闭防火墙  
(2)开放访问的端口号，80 端口  
查看开放的端口号   
firewall-cmd -list-all  
firewall-cmd -add-service=http -permanent  
firewall-cmd -add-port=80/tcp -permanent  
重启防火墙   
firewall-cmd -reload  
```
# 第三章 nginx常用的命令和配置文件  
## nginx常用命令：  
(1)启动命令  
在/usr/local/nginx/sbin目录下执行./nginx  
(2)关闭命令  
在/usr/local/nginx/sbin录下执行./nginx -S stop  
(3)重新加载命令
在/usr/local/nginx/sbin目录下执行./nginx -s reload  
## nginx.conf  
nginx安装目录下，其默认的配置文件都放在这个目录的conf目录下，而主配置文件nginx. conf也在其中，后续对nginx的使用基本上都是对此配置文件进行相应的修改  
![9](/Nginx/nginxFile/9.png)  
```
注意：nginx重载的时候回出现配置文件找不到时，使用./nginx -c 配置文件路径
```
![10](/Nginx/nginxFile/10.png)  
根据上述文件，我们可以很明显的将nginx.conf配置文件分为三部分：  
第一部分：全局快  
从配置文件开始到events块之间的内容，主要会设置一些影响nginx服务器整体运行的配置指令，主要包括配置运行Nginx服务器的用户(组)、允许生成的worker process数，进程PID存放路径、日志存放路径和类型以及配置文件的引入等等。  
worker_processess 1;  
这是Nginx服务器并发处理服务的关键配置，worker_processess值越大，可以支持的并发处理量也越多，但是会受到硬件、软件等设备的制约。  
第二部分：events块  
events块涉及的指令主要影响Nginx 服务器与用户的网络连接,常用的设置包括是否开启对多work process下的网络连接进行序列化,是否允许同时接收多个网络连接,选取哪种事件驱动模型来处理连接请求,每个wordprocess可以同时支持的最大连接数等。上述例子就表示每个work process支持的最大连接数为1024.这部分的配置对Nginx 的性能影响较大,在实际中应该灵活配置。  
http块这算是Nginx服务器配置中最频繁的部分，代理、缓存和日志定义等绝大多数功能和第三方模块配置都在这里。需要注意的是：http块也可以包括全局块和server块。
1. http块  
http:全局配置的指令包括文件引入、MIME-TYPE定义、日志自定义、链接超时时间、单链接请求数上限等。  
2.  server块  
这块和虚拟主机有密切联系，虚拟主机从用户角度看，和一台独立硬件主机是完全一样的，该技术的产生是为了节省互联网服务器硬件成本，每个http块班阔多个server块，而每个server块就相当于一个虚拟机。而每个server块也分为全局server块，以及可以同时包含多个location块。  
(1)全局server块  
最常见的配置是本虚拟机主机的监听配置和本虚拟机的名称或ip配置。  
(2)location块  
一个server块可以配置多个location块  
这块的主要作用是基于Nginx服务器接收到的请求字符串(例如server, name/uri-string ) , 对虚拟主机名称(也可以是IP别名)之外的字符串(例如前面的/uri-string )进行匹配,对特定的请求进行处理。地址定向、数据缓存和应答控制等功能,还有许多第三方模块的配置也在这里进行。  
# 第四章反向代理  
## 反向代理实例一  
实现效果：使用nginx反向代理，访问www.123.com直接跳转到127.0.0.1:8080  
## 实验代码  
1. 启动一个tomcat浏览器输入ip:8080会显示tomcat首页。
![11](/Nginx/nginxFile/11.png)  
2. 通过修改本地host文件，将www.123.com映射到127.0.0.1  
![12](/Nginx/nginxFile/12.png)  
3. 在nginx.conf哦诶之文件中增加如下配置  
![13](/Nginx/nginxFile/13.png)  
如上配置，我们监听80端口，访问域名为www. 123. com,不加端口号时默认为80端口，故访问该域名时会跳转到127. 0.0. 1:8080路径上。在浏览器端输入www.123. com结果如下:  
![14](/Nginx/nginxFile/14.png)  
## 反向代理实例二  
实现效果:使用nginx反向代理，根据访问的路径跳转到不同端口的服务中nginx监听端口为9001,访问http://127.0.0.1:9001/edu/直接跳转到127.0.0.1:8081访问http://127.0.0.1:9001/vod/直接跳转到127.0.0.1:8082  
### 实验代码  
第一步，准备两个tomcat, -一个8001端口，-一个8002端口，并准备好测试的页面。  
第二步，修改nginx的配置文件在http块中添加server{}  
![15](/Nginx/nginxFile/15.png)  
location指令说明  
该指令用于匹配URL。  
语法如下：  
![16](/Nginx/nginxFile/16.png)  
1. =：用于不含正则表达式的uri前，要求请求字符串与uri严格匹配，如果匹配成功，就停止继续向下搜索并立即处理该请求。  
2. ~：用于表示uri包含正则表达式，并且区分大小写。  
3. ~*：用于表示uri包含正则表达式，并且不区分大小写。  
4. ^~:用于不含正则表达式的uri前，要求Nginx服务器找到表示uri和请求字符串匹配度最高的location后，立即使用此location处理请求，而不再使用location块中的正则uri请求和请求字符串做匹配。  
```
注意：如果uri包含正则表达式，则必须要有~或者~*标识。
```
# 第五章 负载均衡
## 实验代码  
1. 准备两个tomcat  
2. 在nginx.conf中进行配置  
![18](/Nginx/nginxFile/18.png)  
![19](/Nginx/nginxFile/19.png)  
3. nginx分配服务器策略  
第一种 轮训(默认)  
每个请求按照时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。  
第二种 weight  
weight代表权重默认为1，权重越高被分配的客户越多  
第三种 ip_hash  
每个请求按访问ip的hash结果分配，这样每个方可固定方位一个后端服务器。  
第四种 fair(第三方)  
按后端服务器的响应时间来分配请求，响应时间短的优先分配。  
# 第六章 动静分离 
## 什么是动静分离  
![20](/Nginx/nginxFile/20.png)  
通过location 指定不同的后缀名实现不同的请求转发。通过expires 参数设置，可以使浏览器缓存过期时间，减少与服务器之前的请求和流量。具体Expires 定义:是给一个资源设定一个过期时间，也就是说无需去服务端验证，直接通过浏览器自身确认是否过期即可，所以不会产生额外的流量。此种方法非常适合不经常变动的资源。(如果经常更新的文件，不建议使用Expires 来缓存)，我这里设置3d,表示在这3天之内访问这个URL,发送一个请求，比对服务器该文件最后更新时间没有变化，则不会从服务器抓取，返回状态码304，如果有修改，则直接从服务器重新下载，返回状态码200。
## 搭建静态分离  
1. 在linux系统准备静态文件，用于访问  
![21](/Nginx/nginxFile/21.png)  
2. 具体配置  
![22](/Nginx/nginxFile/22.png)  
3. 最终测试  
在浏览器中输入http://192.168.17.129/image/01.jpg  
![23](/Nginx/nginxFile/23.png)  
```
因为配置了autoindex on  可以在网页中出现目录索引  
![24](/Nginx/nginxFile/24.png)  
在浏览器中输入http://192.168.17.129/www/a.html  
![26](/Nginx/nginxFile/26.png)  
```
# 第七章 Nginx配置高可用的集群  
## 什么是高可用  
![25](/Nginx/nginxFile/25.png)  
1. 需要两台nginx服务器  
2. 需要keepalived  
使用 yum install keepalived -y  
安装之后，在etc里面生成目录keepalived，有文件keepalived.conf,日志文件放在/var/log/messages  
3. 完成高可用配置(主从配置)  
(1)修改/etc/keepalived/keepalived.conf配置文件  
![27](/Nginx/nginxFile/27.png)  
![28](/Nginx/nginxFile/28.png)  
把两台服务器上的nginx和keepalived启动  
启动nginx:./nginx  
启动keepalived:systemctl start keepalived.service  
4. 最终测试  
(1)在浏览器地址栏输入虚拟机ip地址192.168.17.50
![29](/Nginx/nginxFile/29.png)  
![30](/Nginx/nginxFile/30.png)  
(2)把服务器(192.168.17.129)nginx和keepalived停止，在输入192.168.17.50  
![31](/Nginx/nginxFile/31.png)  
![32](/Nginx/nginxFile/32.png)  
# Nginx 原理
## master和worker  
![33](/Nginx/nginxFile/33.png)  
![34](/Nginx/nginxFile/34.png)  
## worker如何进行工作的  
![35](/Nginx/nginxFile/35.png)  
## 一个master和对个worker的好处  
1. 可以使用nginx -s reload热部署，利用nginx进行热部署操作  
2. 每个worker是独立的进程，如果有其中的一个woker出现问题，其他worker独立的，继续进行争抢，实现请求过程，不会造成服务终端。
## 设置多少个woker合适  
worker数量和服务器的cpu数量相等是最适宜的  
## 链接worker_connection
第一个：发送请求，占用了woker的几个线程数？  
答案：2或者4个  
第二个：nginx有一个master，有四个woker，每个woker支持最大连接数1024，支持最大并发数是多少？  
1. 普通的静态访问最大并发数是：worker_connections*worker_processes/2,  
2. 而如果是HTTP作为反向代理来说，最大并发数量应该是worker_connections*worker_processes/4  

