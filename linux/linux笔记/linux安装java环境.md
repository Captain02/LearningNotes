# 版本一
1)解压jdk  
2)配置环境变量的配置文件  
#java environment
export JAVA_HOME=/usr/local/src/jdk/jdk1.8.0_202  
export CLASSPATH=.:${JAVA_HOME}/jre/lib/rt.jar:$   {JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar  
export PATH=$PATH:${JAVA_HOME}/bin  
3)java -version/javac进行测试  
# 版本二 
JAVA_HOME=/opt/jdk1.7.0  
PATH=/opt/jdk1.7.0/bin:$PATH  
export JAVA_HOME PATH  

*注意：刷新资源文件source /etc/profile*