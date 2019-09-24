# 微服务概述
## 什么是微服务
微服务化的核心就是将传统的一站式应用，根据业务拆分成一个一个的服务，彻底地去耦合,每一个微服务提供单个业务功能的服务，一个服务做一件事，从技术角度看就是一种小而独立的处理过程，类似进程概念，能够自行单独启动或销毁，拥有自己独立的数据库。
 ## 微服务与微服务架构
 ### 微服务
强调的是服务的大小，它关注的是某一个点，是具体解决某一个问题/提供落地对应服务的一个服务应用,狭意的看,可以看作Eclipse里面的一个个微服务工程/或者Module
### 微服务架构
微服务架构是一种架构模式，它提倡将单一应用程序划分成一组小的服务，服务之间互相协调、互相配合，为用户提供最终价值。每个服务运行在其独立的进程中，服务与服务间采用轻量级的通信机制互相协作（通常是基于HTTP协议的RESTful API）。每个服务都围绕着具体业务进行构建，并且能够被独立的部署到生产环境、类生产环境等等。另外，应当尽量避免统一的、集中式的服务管理机制，对具体的一个服务而言，应根据业务上下文，选择合适的语言、工具对其进行构建。
![1](/SpringCloud/SpringCloudFile/1.png)  
 ## 微服务优缺点
 ### 优点
1. 每个服务足够内聚，足够小，代码容易理解这样能聚焦一个指定的业务功能和业务需求，开发简单、开发效率提高，一个服务可能就是专一的只干一件事情。
2. 微服务能够被小团队单独开发，这个小团队是2到5人的开发人员组成。
3. 微服务是松耦合的，是有意义的服务，无论是在开发阶段或部署阶段都是独立的。
微服务能使用不同的语言开发
4. 易于和第三方集成，微服务允许容易且灵活的方式集成自动部署，通过持续集成工具，如Jenkins,Hudson,bamboo。
5. 微服务易于被一个开发人员理解，修改和维护，这样小团队能够更关注自己的工作成果。无需通过合作才能体现价值。
6. 微服务允许利用融合最新技术。
7. 微服务知识业务逻辑的代码，不会和HTML,CSS或者其他界面混合。
8. 每个微服务都有自己的储存能力，可以有自己的数据库，也可以有统一数据库。
### 缺点
1. 开发人员要处理分布式系统的复杂性
2. 多服务运维难度，随着服务的增加，运维的压力也在增大
3. 系统部署依赖
4. 服务间通信成本
5. 数据一致性
6. 系统集成测试
7. 性能监控.....
## 微服务技术栈有哪些
微服务条目|落地技术|备注
-|-|-  
服务开发|Springboot、spring、springMVC|
服务配置与管理|Netflix公司的Archaius、阿里的Diamond等|
服务的注册与发现|Eureka、Consul、Zookeeper等|
服务的调用|Rest、RPC、gRPC|
服务的熔断|Hystrix、Envoy等|
负载均衡|Ribbon、Nginx等|
服务接口调用(客户端调用服务的简化工具)|Feign|
消息队列|Kafka、RabbitMQ、ActiveMQ等|
服务配置中心管理|SpringCloudConfig、Chef等|
服务路由网关|Zuul等|
服务监控|Zabbix、Nagios、Metrics、Spectator|
服务部署|Docker、OpenStack、Kubernetes等|
数据流操作开发包|SpringCloudStream(封装与Redis，Rabbit、Kafka等发送接收消息)|
事件消息总线|SpringCloudBus|
## SpringCloud作为微服务架构优点
1. 选型依据  
(1) 整体解决方案和框架成熟度  
(2) 社区热度  
(3) 可维护性  
(4) 学习曲线
2. 当前各大IT公司用的微服务架构有哪些？
(1) 阿里Dubbo/HSF
(2) 京东JSF
(3) 新浪微博Motan
(4) 当当网Dubbox
3. 各大服务框架对比  
![2](/SpringCloud/SpringCloudFile/2.png)  
# springCloud概述
## 什么是springCloud
![3](/SpringCloud/SpringCloudFile/3.png)  
SpringCloud=分布式微服务架构下的一站式解决方案，是各个微服务架构落地技术的集合，俗称微服务全家桶。  
## SpringBoot和SpringCloud是什么关系
  SpringBoot专注于快速方便的开发单个个体微服务。  
  SpringCloud是关注全局的微服务协调整理治理框架，它将SpringBoot开发的一个个单体微服务整合起并管理起来，为各个微服务之间提供，配置管理、服务发现、断路器、路由、微代理、事件总线、全局所、决策竞选、分布式会话等等集成服务。  
  SpringBoot可以离开SpringCloud独立使用开发项目，但是SpringCloud离不开SpringBoot，属于依赖关系。  
  SpringBoot专注于快速、方便的开发单个微服务个体，SpringCloud关注全局的服务治理框架。  
  ## SpiringCloud作用有哪些
  1. Distributed/versioned configuration(分布式/版本控制配置)  
  2. Service registration and discovery(服务注册与发现)  
  3. Routing(路由)  
  4. Service-to-service calls(服务到服务的调用)  
  5. Load balancing(负载均衡配置)  
  6. Circuit Breakers(断路器)  
  7. Distributed messaging(分布式消息管理)  
  ## 下载地址
  官方网站：http://projects.spring.io/spring-cloud/  
  参考书：  
    1. https://springcloud.cc/spring-cloud-netflix.html  
    2. springcloud中国社区  
    3. springcloud中文网  
    API：  
    1. http://cloud.spring.io/spring-cloud-static/Dalston.SR1/  
    2. https://springcloud.cc/spring-cloud-dalston.html  
# 案例分析
## 总体介绍 
+ 以部门(Dept)模块做一个微服务通用案例，Consumer消费者(Client)，通过REST调用Provider提供者(Server)提供的服务。  
## 构建步骤
1. 构建maven工程micro-cloud-project  
pom文件如下  
```xml
<groupId>micro.cloud</groupId>
    <artifactId>micro-cloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <properties>
        <java.version>1.8</java.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
        <junit.version>4.12</junit.version>
        <log4j.version>1.2.17</log4j.version>
        <lombok.version>1.16.18</lombok.version>
        <eureka.client.version>2.1.1.RELEASE</eureka.client.version>
    </properties>

    <!--dependencyManagement 只是生命版本和坐标，不实际引入，还需子模块引入（不必添加版本）-->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Greenwich.SR3</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.1.8.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>5.0.4</version>
            </dependency>
            <dependency>
                <groupId>com.alibaba</groupId>
                <artifactId>druid</artifactId>
                <version>1.0.31</version>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>1.3.0</version>
            </dependency>
            <dependency>
                <groupId>ch.qos.logback</groupId>
                <artifactId>logback-core</artifactId>
                <version>1.2.3</version>
            </dependency>
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>${junit.version}</version>
            </dependency>
            <dependency>
                <groupId>log4j</groupId>
                <artifactId>log4j</artifactId>
                <version>${log4j.version}</version>
            </dependency>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
                <version>${eureka.client.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

    <!--各个子模块-->
    <modules>
        <module>micro-api</module>
        <module>micro-eureka-7001</module>
        <module>micro-provider-8001</module>
        <module>micro-provider-8002</module>
        <module>micro-consumer-9001</module>
        <module>micro-provider-hystrix-8003</module>
        <module>micro-api-feign</module>
        <module>micro-consumer-feign-9002</module>
        <module>micro-zuul-6001</module>
        <module>micro-config-server-5001</module>
        <module>micro-provider-config-8004</module>
        <module>micro-eureka-config-7002</module>
        <module>micro-consumer-config-9003</module>
        <module>micro-consumer-feign-config-9004</module>
        <module>micro-zuul-config-6002</module>
    </modules>

```  
这里pom文件值为各个子模块的父工程，统一声明jar包的版本，```</dependencyManagement>```只是声明jar包的版本，不实际引入jar包。  
2. 创建公共的Api工程，工程中只包含实体类，目录结构如下：  
![4](/SpringCloud/SpringCloudFile/4.png)  
pom文件如下：  
```xml
    <parent>
        <artifactId>micro-cloud</artifactId>
        <groupId>micro.cloud</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>micro-api</artifactId>
```   
实体类如下：  
```java
package com.entity;

public class Dept {
    private Integer id;
    private String deptname;
    private String descs;
    private String db;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getDeptname() {
        return deptname;
    }

    public void setDeptname(String deptname) {
        this.deptname = deptname;
    }

    public String getDescs() {
        return descs;
    }

    public void setDescs(String descs) {
        this.descs = descs;
    }

    public String getDb() {
        return db;
    }

    public void setDb(String db) {
        this.db = db;
    }
}
```
## Eureka  
### 什么是Eureka  
Eureka是Netflix开发的，一个基于REST服务的，服务注册与发现的组件  
它主要包括两个组件：Eureka Server和Eureka Client  
+ Eureka Client:一个Java客户端，用于简化与Eureka Server的交互(通常就是微服务中的客户端和服务端)  
+ Eureka Server：提供服务注册和发现的能力(通常就是微服务中的注册中心)  
![5](/SpringCloud/SpringCloudFile/5.png)   
各个微服务启动时，会通过Eureka Client向Eureka Server注册自己，会存储改服务的信息也就是所，每个微服务的客户端和服务端，都会注册到Eureka Server，这就衍生出了微服务相互识别。  
+ 同步：每个Eureka Server同时也是Eureka Client(逻辑上的)duoge Eureka Server之间通过复制的方式完成服务注册表的同步，形成Eureka的高可用。  
+ 识别：Eurek Client会缓存Eureka Server中的信息，即使所有Eureka Client都宕掉，服务消费者认可使用缓存中的信息找到服务提供者  
+ 续约：微服务会周期性(默认30s)地想EurekaServer发送心跳Renew(续约)信息(类似于hearbeat)  
+ 续期：Eureka Server会定期(默认60s)执行一次失效服务检测功能，他检查超过一定时间(默认90s)没有Renew的微服务，发现则会注销该微服务节点。  
SpringCloud已经把Eureka集成在其子项目Spring Cloud Netflix里面  

### 单个Eureka的部署  
1. 目录结构  
![6](/SpringCloud/SpringCloudFile/6.png)  
2. pom文件  
```xml
<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>micro.cloud</groupId>
		<artifactId>micro-cloud</artifactId>
		<version>1.0-SNAPSHOT</version>
	</parent>
	<groupId>com.micro.cloud</groupId>
	<artifactId>micro-eureka-7001</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>micro-eureka-7001</name>
	<description>Demo project for Spring Boot</description>

	<properties>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>
```
3. 配置application  
```yml
server:
  port: 7001

eureka:
  instance:
    hostname: eureka7001.com #eureka服务端的实例名称
  client:
    register-with-eureka: false     #false表示不向注册中心注册自己。
    fetch-registry: false     #false表示自己端就是注册中心，我的职责就是维护服务实例，并不需要去检索服务
    service-url:
      #单机
      #设置与Eureka Server交互的地址查询服务和注册服务都需要依赖这个地址（单机）。
      defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
      #defaultZone: http://eureka7002.com:7002/eureka/,http://eureka7003.com:7003/eureka/   #集群配置

```
4. 开启Eureka Server   
```java
@SpringBootApplication
@EnableEurekaServer
public class MicroEureka7001Application {
	public static void main(String[] args) {
		SpringApplication.run(MicroEureka7001Application.class, args);
	}
}
```  
开启成功后访问地址会有Eureka主页  
![7](/SpringCloud/SpringCloudFile/7.png)  
Eureka支持集群，配置多个Eureka只需要修改新建的工程中修改yml配置文件即可  

### Zookeeper和Eureka的比较  
作为服务注册中心，Eureka比Zookeeper好在哪里  
CAP理论之处，一个分布式系统不可能同时满足C(一致性)、A(可用性)和P(分区容错性)。由于分区容错性P在是分布式系统中必须要保证的，因此我们只能在A和C之间进行权衡。  
因此  
+ Zookeeper保证的是CP，Eureka则是AP。  
当向注册中心查询服务列表使时，我们可以容忍注册中心返回的是几分钟以前的注册信息，但不能接受服务直接宕掉不可用。也就是说，服务注册功能对可用性的要求要高于一致性。但是zookeeper会出现这样一种情况，当master节点因为网络故障与其他节点失去联系时，剩余节点会重新进行leader选举。问题在于，选举leader的时间太长，30~120s，且选举期间整个zookeeper集群都是不可用的，这就导致在选举期间注册服务摊款。在云部署的环境下，因网络问题使得zookeeper集群失去master节点是较大概率发生的事，虽然服务能够最终回复，但是漫长的选举时间导致的注册长期不可用是不能容忍的。  
+ Eureka保证AP  
Eureka看明白了这一点，因此在设计时就优先保证可用性。Eureka各个节点都是平等的，几个节点挂掉不会影响正常节点的工作，剩余的节点依然可以提供注册和查询服务。而Eureka注册如果发现连接失败，则会自动切换至其他节点，只要有一台Eureka还在，技能保证注册服务可用性(保证可用性),只不过查到的信息可能不是最新的(不保证强一致性)。除此之外，Eureka还有一种自我保护机制，如果在15分钟内超过85%的节点都没有正常的心跳，那么Eureka就认为客户端与注册中心出现了网络故障，此时会出现以下几种情况：  
1. Eureka不再从注册表中移除 因为长时间没收到心跳而应该过期的服务。  
2. Eureka仍然能够接受新服务的注册和查询请求，但是不会被同步到其他节点上(即保证当前节点依然可用)  
3. 当网络稳定时，，当前实例新的注册信息会被同步到其他的节点中  
因此，Eureka可以很好的应对网络故障导致部分节点失去联系的情况。而不会像zookeeper那样是整个注册服务瘫痪。  
## Ribbin 负载均衡
Spring Cloud Ribbon是基于Netflix Ribbon实现的一套客户端负载均衡的工具。  
加单的说，Ribbon是Netflix发布的开源项目，主要功能是提供客户端的软件负载均衡算法，将Netflix中的中间层无服务链接在一起。Ribbon客户端组件提供一系列完善的配置项如连接超时，重试等。简单的说，就是在配置文件中列出LoadBalancer(简称LB)后面所有的机器，Ribbon会自动的帮助你基于某种规则(如简单轮训，随机链接等)去链接这些机器。我们也很容易使用Ribbon实现自定义的负载均衡算法。  
负载均衡分为集中式LB和进程内LB  
集中式LB：  
即在服务的消费方和提供方之间使用独立的LB设施(可以是硬件，如F5, 也可以是软件，如nginx), 由该设施负责把访问请求通过某种策略转发至服务的提供方；  
进程内LB：  
将LB逻辑集成到消费方，消费方从服务注册中心获知有哪些地址可用，然后自己再从这些地址中选择出一个合适的服务器。  
Ribbon就属于进程内LB，它只是一个类库，集成于消费方进程，消费方通过它来获取到服务提供方的地址。  

### 核心组件IRule
根据特定算法中从服务列表中选取一个要访问的服务  
1. RoundRobinRule轮询  
2. RandpmRule随机  
3. AvailabilityFilteringRule会先过滤掉多余多次访问故障而处于断路器跳闸状态的服务，还有并发链接数量超过阈值的服务，然后对剩余的服务列表按照轮训策略进行访问  
4. WeightedResponseTimeRule根据平均响应事件计算所有服务的权重，响应时间越快服务权重越大，被选中的概率越高，刚启动时候如果统计信息不足，则使用RoundRobinRule策略，等统计信息足够，会切换到WeightedResponseTimeRule  
5. RetryRule先按照RoundRobinRule的策略获取服务，如果获取服务失败则在指定时间内会进行重试，获得可用的服务  
6. RestAvailableRule会先过滤掉有多次访问故障而处于断路器跳闸状态的服务，然后选择一个并发量最小的服务。
7. ZoneAvoidanceRule默认规则，复合判断server所在区域的性能和server的可用性选择服务器。  
### 开启Ribbon
```java
public class ConfigBean {

    @Bean
    @LoadBalanced
    public RestTemplate getRestTemplate() {

        return new RestTemplate();
    }

}
```
### 自定义规则
1. 创建自定义规则类  
```java
@Configuration
public class MySelfRule
{
  @Bean
  public IRule myRule()
  {
   return new RandomRule();//Ribbon默认是轮询，我自定义为随机
  }
}

```
2. 使用自定义规则  
```java
@RibbonClient(name="MICROSERVICECLOUD-DEPT",configuration=MySelfRule.class)
```
3. 注意细节  
官方文档明确给出了警告：
这个自定义配置类不能放在@ComponentScan所扫描的当前包下以及子包下，否则我们自定义的这个配置类就会被所有的Ribbon客户端所共享，也就是说我们达不到特殊化定制的目的了。  
![8](/SpringCloud/SpringCloudFile/8.png)  
## Feign 负载均衡
1. 添加maven依赖  
```xml
<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```
2. 声明feign的服务  
```java
@FeignClient(value = "MICRO-PROVIDER", fallbackFactory = DeptClientServiceFallbackFactory.class)
public interface DeptService {

    //服务中方法的映射路径,去注册中心寻找其他的相同映射的服务，实现服务在均衡
    @RequestMapping(value = "/getlist", method = RequestMethod.GET)
    public List<Dept> getList();
}
```
3. 开启Feign  
```java
@SpringBootApplication
@EnableEurekaClient
@EnableFeignClients(basePackages = {"com.micro.api.feign.microapifeign.dept.service"})
@ComponentScan(value = {"com.micro.api.feign.microapifeign.dept.service","com.micro.consumer.feign.microconsumerfeign9002.controller"})
public class MicroConsumerFeign9002Application {
	public static void main(String[] args) {
		SpringApplication.run(MicroConsumerFeign9002Application.class, args);
	}
}
```
## hystrix 服务降级与熔断  
### 分布式系统面临的问题  
服务雪崩
多个微服务之间调用的时候，假设微服务A调用微服务B和微服务C，微服务B和微服务C又调用其它的微服务，这就是所谓的“扇出”。如果扇出的链路上某个微服务的调用响应时间过长或者不可用，对微服务A的调用就会占用越来越多的系统资源，进而引起系统崩溃，所谓的“雪崩效应”.
 
对于高流量的应用来说，单一的后端依赖可能会导致所有服务器上的所有资源都在几秒钟内饱和。比失败更糟糕的是，这些应用程序还可能导致服务之间的延迟增加，备份队列，线程和其他系统资源紧张，导致整个系统发生更多的级联故障。这些都表示需要对故障和延迟进行隔离和管理，以便单个依赖关系的失败，不能取消整个应用程序或系统。
 
 
备注：一般情况对于服务依赖的保护主要有3中解决方案：
 
（1）熔断模式：这种模式主要是参考电路熔断，如果一条线路电压过高，保险丝会熔断，防止火灾。放到我们的系统中，如果某个目标服务调用慢或者有大量超时，此时，熔断该服务的调用，对于后续调用请求，不在继续调用目标服务，直接返回，快速释放资源。如果目标服务情况好转则恢复调用。
 
（2）隔离模式：这种模式就像对系统请求按类型划分成一个个小岛的一样，当某个小岛被火少光了，不会影响到其他的小岛。例如可以对不同类型的请求使用线程池来资源隔离，每种类型的请求互不影响，如果一种类型的请求线程资源耗尽，则对后续的该类型请求直接返回，不再调用后续资源。这种模式使用场景非常多，例如将一个服务拆开，对于重要的服务使用单独服务器来部署，再或者公司最近推广的多中心。
 
（3）限流模式：上述的熔断模式和隔离模式都属于出错后的容错处理机制，而限流模式则可以称为预防模式。限流模式主要是提前对各个类型的请求设置最高的QPS阈值，若高于设置的阈值则对该请求直接返回，不再调用后续资源。这种模式不能解决服务依赖的问题，只能解决系统整体资源分配问题，因为没有被限流的请求依然有可能造成雪崩效应。
 
 ### 服务降级  
 Hystrix服务降级，其实就是线程池中单个线程障碍处理，防止单个线程请求时间太长，导致资源长期被占有而得不到释放，从而导致线程池被快速占用完，导致服务崩溃。  
 Hystrix能解决如下问题：  
 1. 请求超时降级，线程资源不足降级，降级之后可以返回自定义数据  
 2. 线程池隔离降级，分布式服务可以针对不同的服务使用不同的线程池，从而互不影响  
 3. 自动触发降级与恢复  
 4. 实现请求缓存和请求合并  
 ### 服务熔断  
 熔断模式：这种模式主要是参考电路熔断，如果一条线路电压过高，保险丝会熔断。放到我们的系统中，如果某个目标服务调用慢或者有大量超时时，此时，熔断该服务的调用，对于后续调用请求，不再继续调用目标服务，直接放回，快速释放资源。如果目标服务情况好转则恢复调用。  
 1. 开启Hystrix
 ```java
@SpringBootApplication
@EnableEurekaClient //本服务启动后会自动注册进eureka服务中
@EnableDiscoveryClient //服务发现
@EnableCircuitBreaker//对hystrixR熔断机制的支持
public class MicroProviderHystrix8003Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroProviderHystrix8003Application.class, args);
	}

}
 ```
 2. controller  
 ```java
@RestController
public class DeptController {

    @Autowired
    DeptService deptService;

    @GetMapping("/getlist/{id}")
    @HystrixCommand(fallbackMethod = "processHystrix_Get")
    public Dept getList(@PathVariable("id") Integer id) {
        List<Dept> list = deptService.list();
        Dept dept = list.get(id);
        if (dept == null) {
            throw new RuntimeException("该ID：" + id + "没有没有对应的信息");
        }
        return dept;
    }

    public Dept processHystrix_Get(@PathVariable("id") Integer id) {
        Dept dept = new Dept();
        dept.setId(10);
        dept.setDeptname("没有没有对应的信息--@HystrixCommand");
        dept.setDb("0");
        dept.setDescs("没有没有对应的信息--@HystrixCommand");
        return dept;
    }

}
 ```
 从上述内容可以看出，每增加一个方法便会增加一个回调方法，这样会导致方法膨胀，所以增加公共配置类  
 ```java
@Component
public class DeptClientServiceFallbackFactory implements FallbackFactory<DeptService> {

    @Override
    public DeptService create(Throwable throwable) {
        return new DeptService() {
            @Override
            public List<Dept> getList() {
                Dept dept = new Dept();
                dept.setDb(String.valueOf(3));
                dept.setDeptname("3");
                dept.setDescs("3");
                dept.setId(3);
                List<Dept> data = new ArrayList<>();
                data.add(dept);
                return data;
            }
        };
    }
}
 ```
 3. server接口声明使用实现类  
 ```java
@FeignClient(value = "MICRO-PROVIDER", fallbackFactory = DeptClientServiceFallbackFactory.class)
public interface DeptService {

    //服务中方法的映射路径,去注册中心寻找其他的相同映射的服务，实现服务在均衡
    @RequestMapping(value = "/getlist", method = RequestMethod.GET)
    public List<Dept> getList();
}
 ```

 ## zuul路由网关  
 1. 开启zuul网关  
 ```java
@SpringBootApplication
@EnableZuulProxy
public class MicroZuul6001Application {
    public static void main(String[] args) {
        SpringApplication.run(MicroZuul6001Application.class, args);
    }
}
 ```
 2. 配置zuul网关
 ```yml
zuul:
  prefix: /micro
  ignored-services: '*'
  routes: 
    mydept.serviceId: micro-provider
    mydept.path: /mydept/**
 ```

 ### config 配置中心  
 1. config配置  
 ```yml
spring:
  application:
    name: config-server
  profiles:
    active: native
  # 配置中心
  cloud:
    config:
      server:
        native:
          search-locations: classpath:/config/
 ```
 2. config-consumer配置  
 ```yml
 server:
  port: 9003
 ```
  2. config-feign配置  
 ```yml
eureka:
  client:
    register-with-eureka: false
    service-url:
      defaultZone: http://eureka7003.com:7003/eureka/

spring:
  application:
    name: application-consumer-fegin-config
 ```

3. config-provider配置  
 ```yml
server:
  port: 8004
spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource            # 当前数据源操作类型
    driver-class-name: com.mysql.jdbc.Driver              # mysql驱动包
    url: jdbc:mysql://localhost:3306/mirodemo?serverTimezone=UTC  # 数据库名称
    username: root
    password: 123456
    dbcp2:
      min-idle: 5                                           # 数据库连接池的最小维持连接数
      initial-size: 5                                       # 初始化连接数
      max-total: 5                                          # 最大连接数
      max-wait-millis: 200
eureka:
  client: #客户端注册进eureka服务列表内
    service-url:
      defaultZone: http://eureka7001.com:7001/eureka
       #defaultZone: http://eureka7001.com:7001/eureka/,http://eureka7002.com:7002/eureka/,http://eureka7003.com:7003/eureka/
  instance:
    instance-id: ${spring.application.name}:${server.port}
    prefer-ip-address: true

mybatis:
#  config-location: classpath:mybatis/mybatis.cfg.xml        # mybatis配置文件所在路径
  type-aliases-package: com.atguigu.springcloud.entities    # 所有Entity别名类所在包
  mapper-locations:
  - classpath:mybatis/mapper/**/*.xml                       # mapper映射文件
 ```
4. config-zuul配置  
 ```yml
  #ignored-services: microservicecloud-dept
  #同一网关区别？
zuul:
  prefix: /micro
  ignored-services: '*'
  routes:
    mydept.serviceId: micro-provider
    mydept.path: /mydept/**

info:
  app.name: atguigu-microcloud
  company.name: www.atguigu.com
  build.artifactId: $project.artifactId$
  build.version: $project.version$
 ```
 5. 其他服务引用config以provider为例  
 ```yml
spring:                            # 等待连接获取的最大超时时间
  application:
    name: micro-provider
  profiles:
    active: dev
  cloud:
    config:
      fail-fast: true
      name: application-micro-provider
      profile: ${spring.profiles.active}
      discovery:
        enabled: true
        service-id: config-server
      uri: http://127.0.0.1:5001


# 注册中心配置
eureka:
  client: #客户端注册进eureka服务列表内
    service-url:
       defaultZone: http://eureka7001.com:7001/eureka
       #defaultZone: http://eureka7001.com:7001/eureka/,http://eureka7002.com:7002/eureka/,http://eureka7003.com:7003/eureka/
  instance:
    instance-id: micro-provider:${server.port}
    prefer-ip-address: true     #访问路径可以显示IP地址
 ```