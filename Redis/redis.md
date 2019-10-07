# NoSql入门和概述  
## 入门概述  
1. 互联网时态背景下大机遇，为什么用nosql  
(1)点击MySQL的美好年代在90年代，一个网站的访问量一般都不大，用单个数据库完全可以轻松应付。
在那个时候，更多的都是静态网页，动态交互类型的网站不多。  
![0](/Redis/redisfile/0.png)  
上述架构下，我们来看看数据存储的瓶颈是什么？  
+ 数据量的总大小 一个机器放不下时  
+ 数据的索引（B+ Tree）一个机器的内存放不下时  
+ 访问量(读写混合)一个实例不能承受  
(2)2 Memcached(缓存)+MySQL+垂直拆分。后来，随着访问量的上升，几乎大部分使用MySQL架构的网站在数据库上都开始出现了性能问题，web程序不再仅仅专注在功能上，同时也在追求性能。程序员们开始大量的使用缓存技术来缓解数据库的压力，优化数据库的结构和索引。开始比较流行的是通过文件缓存来缓解数据库压力，但是当访问量继续增大的时候，多台web机器通过文件缓存不能共享，大量的小文件缓存也带了了比较高的IO压力。在这个时候，Memcached就自然的成为一个非常时尚的技术产品。  
![1](/Redis/redisfile/1.png)   
 Memcached作为一个独立的分布式的缓存服务器，为多个web服务器提供了一个共享的高性能缓存服务，在Memcached服务器上，又发展了根据hash算法来进行多台Memcached缓存服务的扩展，然后又出现了一致性hash来解决增加或减少缓存服务器导致重新hash带来的大量缓存失效的弊端。  
 (3)Mysql主从读写分离。由于数据库的写入压力增加，Memcached只能缓解数据库的读取压力。读写集中在一个数据库上让数据库不堪重负，大部分网站开始使用主从复制技术来达到读写分离，以提高读写性能和读库的可扩展性。Mysql的master-slave模式成为这个时候的网站标配了。  
 ![3](/Redis/redisfile/3.png)   
(4)分表分库+水平拆分+mysql集群。 在Memcached的高速缓存，MySQL的主从复制，读写分离的基础之上，这时MySQL主库的写压力开始出现瓶颈，而数据量的持续猛增，由于MyISAM使用表锁，在高并发下会出现严重的锁问题，大量的高并发MySQL应用开始使用InnoDB引擎代替MyISAM。  
 同时，开始流行使用分表分库来缓解写压力和数据增长的扩展问题。这个时候，分表分库成了一个热门技术，是面试的热门问题也是业界讨论的热门技术问题。也就在这个时候，MySQL推出了还不太稳定的表分区，这也给技术实力一般的公司带来了希望。虽然MySQL推出了MySQL Cluster集群，但性能也不能很好满足互联网的要求，只是在高可靠性上提供了非常大的保证。  
  ![4](/Redis/redisfile/4.png)   
(5)MySQL的扩展性瓶颈。MySQL数据库也经常存储一些大文本字段，导致数据库表非常的大，在做数据库恢复的时候就导致非常的慢，不容易快速恢复数据库。比如1000万4KB大小的文本就接近40GB的大小，如果能把这些数据从MySQL省去，MySQL将变得非常的小。关系数据库很强大，但是它并不能很好的应付所有的应用场景。MySQL的扩展性差（需要复杂的技术来实现），大数据下IO压力大，表结构更改困难，正是当前使用MySQL的开发人员面临的问题。  
(6)今天是什么样子？？  
  ![5](/Redis/redisfile/5.png)   
(7)为什么用NoSQL。  
今天我们可以通过第三方平台（如：Google,Facebook等）可以很容易的访问和抓取数据。用户的个人信息，社交网络，地理位置，用户生成的数据和用户操作日志已经成倍的增加。我们如果要对这些用户数据进行挖掘，那SQL数据库已经不适合这些应用了, NoSQL数据库的发展也却能很好的处理这些大的数据  
![6](/Redis/redisfile/6.png)   
2. NoSQL是什么  
NoSQL(NoSQL = Not Only SQL )，意即“不仅仅是SQL”，
泛指非关系型的数据库。随着互联网web2.0网站的兴起，传统的关系数据库在应付web2.0网站，特别是超大规模和高并发的SNS类型的web2.0纯动态网站已经显得力不从心，暴露了很多难以克服的问题，而非关系型的数据库则由于其本身的特点得到了非常迅速的发展。NoSQL数据库的产生就是为了解决大规模数据集合多重数据种类带来的挑战，尤其是大数据应用难题，包括超大规模数据的存储。  
（例如谷歌或Facebook每天为他们的用户收集万亿比特的数据）。这些类型的数据存储不需要固定的模式，无需多余操作就可以横向扩展。  
3. 能干什么  
+ 易扩展  
NoSQL数据库种类繁多，但是一个共同的特点都是去掉关系数据库的关系型特性。
数据之间无关系，这样就非常容易扩展。也无形之间，在架构的层面上带来了可扩展的能力。
+ 大数据量高性能
+ 多样灵活的数据模型  
NoSQL数据库都具有非常高的读写性能，尤其在大数据量下，同样表现优秀。
这得益于它的无关系性，数据库的结构简单。
一般MySQL使用Query Cache，每次表的更新Cache就失效，是一种大粒度的Cache，
在针对web2.0的交互频繁的应用，Cache性能不高。而NoSQL的Cache是记录级的，
是一种细粒度的Cache，所以NoSQL在这个层面上来说就要性能高很多了

+ 传统RDBMS VS NOSQL  
RDBMS vs NoSQL
RDBMS
- 高度组织化结构化数据
- 结构化查询语言（SQL）
- 数据和关系都存储在单独的表中。
- 数据操纵语言，数据定义语言
- 严格的一致性
- 基础事务  

NoSQL
- 代表着不仅仅是SQL
- 没有声明性查询语言
- 没有预定义的模式
-键 - 值对存储，列存储，文档存储，图形数据库
- 最终一致性，而非ACID属性
- 非结构化和不可预知的数据
- CAP定理
- 高性能，高可用性和可伸缩性  
4. 去哪里下载
Redis、Memcache、Mongdb  
5. 怎么玩  
KV、Cache、Persistence  
## 3V+3高  
1. 大数据时代下的3V  
+ 海量Volume
+ 多样Variety
+ 实时Velocity  
2. 互联网需求的3高  
+ 高并发  
+ 高可扩
+ 高性能
## NoSQL数据模型介绍  
1. 对比关系型数据库和非关系型数据库  
(1)关系型数据库  
![7](/Redis/redisfile/7.png)   
(2)Nosql如何设计  
+ 什么是BSON()  
BSON（）是一种类json的一种二进制形式的存储格式，简称Binary JSON，
它和JSON一样，支持内嵌的文档对象和数组对象  
```json
{
 "customer":{
   "id":1136,
   "name":"Z3",
   "billingAddress":[{"city":"beijing"}],
   "orders":[
    {
      "id":17,
      "customerId":1136,
      "orderItems":[{"productId":27,"price":77.5,"productName":"thinking in java"}],
      "shippingAddress":[{"city":"beijing"}]
      "orderPayment":[{"ccinfo":"111-222-333","txnid":"asdfadcd334","billingAddress":{"city":"beijing"}}],
      }
    ]
  }
}

```  
+ 总结  
```
为什么上述的情况可以用聚合模型来处理  
高并发的操作是不太建议有关联查询的，互联网公司用冗余数据来避免关联查询,分布式事务是支持不了太多的并发的。  
如果按照我们新设计的BSon，是不是查询起来很可爱
```  
2. 聚合模型  
+ KV键值
+ Bson
+ 列族  
顾名思义，是按列存储数据的。最大的特点是方便存储结构化和半结构化数据，方便做数据压缩，对针对某一列或者某几列的查询有非常大的IO优势。
![8](/Redis/redisfile/8.png)   
+ 图形  
![9](/Redis/redisfile/9.png)   
## NoSQL数据库四大分类  
1. KV键值：典型介绍  
+ 新浪：BerkeleyDB+redis  
+ 美团：redis+tair  
+ 阿里、百度：memcache+redis  
2. 文档型数据库(bson格式比较多)：典型介绍  
+ CouchDB  
+ MongoDB  
MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。  
MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。  
3. 列存储数据库  
+ Cassandra, HBase
+ 分布式文件系统  
4. 图关系数据库  
+ 它不是放图形的，放的是关系比如:朋友圈社交网络、广告推荐系统  
+ 社交网络，推荐系统等。专注于构建关系图谱
+ Neo4J, InfoGrid
5. 对比  
![10](/Redis/redisfile/10.png)   
## 在分布式数据库中CAP原理CAP+BASE  
1. 传统的ACID分别是什么  
 
关系型数据库遵循ACID规则
事务在英文中是transaction，和现实世界中的交易很类似，它有如下四个特性：
 
(1)A (Atomicity) 原子性
原子性很容易理解，也就是说事务里的所有操作要么全部做完，要么都不做，事务成功的条件是事务里的所有操作都成功，只要有一个操作失败，整个事务就失败，需要回滚。比如银行转账，从A账户转100元至B账户，分为两个步骤：1）从A账户取100元；2）存入100元至B账户。这两步要么一起完成，要么一起不完成，如果只完成第一步，第二步失败，钱会莫名其妙少了100元。  
 
(2)C (Consistency) 一致性
一致性也比较容易理解，也就是说数据库要一直处于一致的状态，事务的运行不会改变数据库原本的一致性约束。  
 
(3)I (Isolation) 独立性
所谓的独立性是指并发的事务之间不会互相影响，如果一个事务要访问的数据正在被另外一个事务修改，只要另外一个事务未提交，它所访问的数据就不受未提交事务的影响。比如现有有个交易是从A账户转100元至B账户，在这个交易还未完成的情况下，如果此时B查询自己的账户，是看不到新增加的100元的  
 
(4)D (Durability) 持久性
持久性是指一旦事务提交后，它所做的修改将会永久的保存在数据库上，即使出现宕机也不会丢失。    

2. CAP  
+ C:Consistency（强一致性）  
+ A:Availability（可用性）  
+ P:Partition tolerance（分区容错性）

3. CAP的3进2  
CAP理论就是说在分布式存储系统中，最多只能实现上面的两点。
而由于当前的网络硬件肯定会出现延迟丢包等问题，所以
 
分区容忍性是我们必须需要实现的。
 
所以我们只能在一致性和可用性之间进行权衡，没有NoSQL系统能同时保证这三点。

C:强一致性 A：高可用性 P：分布式容忍性
 CA 传统Oracle数据库
 
 AP 大多数网站架构的选择
 
 CP Redis、Mongodb
 
 注意：分布式架构的时候必须做出取舍。
一致性和可用性之间取一个平衡。多余大多数web应用，其实并不需要强一致性。
因此牺牲C换取P，这是目前分布式数据库产品的方向

一致性与可用性的决择
 
对于web2.0网站来说，关系数据库的很多主要特性却往往无用武之地
 
数据库事务一致性需求 
　　很多web实时系统并不要求严格的数据库事务，对读一致性的要求很低， 有些场合对写一致性要求并不高。允许实现最终一致性。
 
数据库的写实时性和读实时性需求
　　对关系数据库来说，插入一条数据之后立刻查询，是肯定可以读出来这条数据的，但是对于很多web应用来说，并不要求这么高的实时性，比方说发一条消息之 后，过几秒乃至十几秒之后，我的订阅者才看到这条动态是完全可以接受的。
 
对复杂的SQL查询，特别是多表关联查询的需求 
　　任何大数据量的web系统，都非常忌讳多个大表的关联查询，以及复杂的数据分析类型的报表查询，特别是SNS类型的网站，从需求以及产品设计角 度，就避免了这种情况的产生。往往更多的只是单表的主键查询，以及单表的简单条件分页查询，SQL的功能被极大的弱化了。  
4. 经典CAP图  
CAP理论的核心是：一个分布式系统不可能同时很好的满足一致性，可用性和分区容错性这三个需求，
最多只能同时较好的满足两个。  
因此，根据 CAP 原理将 NoSQL 数据库分成了满足 CA 原则、满足 CP 原则和满足 AP 原则三 大类：  
CA - 单点集群，满足一致性，可用性的系统，通常在可扩展性上不太强大。  
CP - 满足一致性，分区容忍必的系统，通常性能不是特别高。  
AP - 满足可用性，分区容忍性的系统，通常可能对一致性要求低一些。  
![11](/Redis/redisfile/11.png)   
5. BASE  

BASE就是为了解决关系数据库强一致性引起的问题而引起的可用性降低而提出的解决方案。  
 
BASE其实是下面三个术语的缩写：  
+ 基本可用（Basically Available）  
+ 软状态（Soft state）  
+ 最终一致（Eventually consistent）  
 
它的思想是通过让系统放松对某一时刻数据一致性的要求来换取系统整体伸缩性和性能上改观。为什么这么说呢，缘由就在于大型系统往往由于地域分布和极高性能的要求，不可能采用分布式事务来完成这些指标，要想获得这些指标，我们必须采用另外一种方式来完成，这里BASE就是解决这个问题的办法  

6. 分布式+集群简介  
分布式系统（distributed system）  
 由多台计算机和通信的软件组件通过计算机网络连接（本地网络或广域网）组成。分布式系统是建立在网络之上的软件系统。正是因为软件的特性，所以分布式系统具有高度的内聚性和透明性。因此，网络和分布式系统之间的区别更多的在于高层软件（特别是操作系统），而不是硬件。分布式系统可以应用在在不同的平台上如：Pc、工作站、局域网和广域网上等。  
简单来讲：  
+ 分布式：不同的多台服务器上面部署不同的服务模块（工程），他们之间通过Rpc/Rmi之间通信和调用，对外提供服务和组内协作。  
+ 集群：不同的多台服务器上面部署相同的服务模块，通过分布式调度软件进行统一的调度，对外提供服务和访问。
 
# Redis入门介绍  
## 入门概述  
1. 什么是Redis  
+ Redis:REmote DIctionary Server(远程字典服务器)  
![12](/Redis/redisfile/12.png)   
是完全开源免费的，用C语言编写的，遵守BSD协议，
是一个高性能的(key/value)分布式内存数据库，基于内存运行并支持持久化的NoSQL数据库，是当前最热门的NoSql数据库之一,也被人们称为数据结构服务器。
+ Redis 与其他 key - value 缓存产品有以下三个特点
Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。  
Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。  
Redis支持数据的备份，即master-slave模式的数据备份。  
2. 作用  
+ 内存存储和持久化：redis支持异步将内存中的数据写到硬盘上，同时不影响继续服务  
+ 取最新N个数据的操作，如：可以将最新的10条评论的ID放在Redis的List集合里面  
+ 模拟类似于HttpSession这种需要设定过期时间的功能  
+ 发布、订阅消息系统  
+ 定时器、计数器

3. 下载地址  
+ Http://redis.io/  
+ Http://www.redis.cn/  

4. 怎么玩  
+ 数据类型、基本操作和配置
+ 持久化和复制，RDB/AOF  
+ 事务的控制  
+ 复制

# 数据类型  
## Redis的五大数据类型  
1. String(字符串)   
String（字符串）
string是redis最基本的类型，你可以理解成与Memcached一模一样的类型，一个key对应一个value。string类型是二进制安全的。意思是redis的string可以包含任何数据。比如jpg图片或者序列化的对象.string类型是Redis最基本的数据类型，一个redis中字符串value最多可以是512M
2. Hash(哈希，类似java里面的Map)
Redis hash是一个键值对集合。  
Redis hash是String类型的fieId和value的映射表，hash特别适合用于存储对象，类似Java里面的Map  
3. List(列表)  
Redis列表时简单的字符串列表，按照插入顺序排列。你可以添加一个元素到列表的头部(左边)或者尾部(右边)  
它的底层实际是个链表。  
4. Set(集合)  
Redis的Set是string类型的无序集合。它是通过HashTable实现的。
5. Zset(sorted set:有序集合)  
Redis zset和set一样也是string类型元素的集合，且不允许重复的成员。不同的是每个元素都会关联一个double类型的分数。  
redis正式通过分数来为集合中的成员进行从小到达的排序。zset的成员是唯一的，但分数(score)确可以重复。   
```
注意:redis常见类型操作指令Http://redisdoc.com/  
```  
## 五大类型常用指令  
### Key键
1. 常用
![13](/Redis/redisfile/13.png)   
2. 案例  
+ keys *  
+ exists key的名字，判断某个key是否存在
+ move key db 当前库就没有了，被移除了  
+ expire key 秒钟:为给定的key设置过期时间  
+ ttl key查看还有多少秒过期，-1表示永不过期，-2表示已过期  
+ type key 查看你的key是什么类型  

### String字符串  
1. 常用  
![14](/Redis/redisfile/14.png)   
![15](/Redis/redisfile/15.png)   
2. 案例  
+ set/get/del/append/strlen  
+ incr/decr/incrby/decrby一定要是数字才能进行加减  
+ getrange/setrange  
getrange:获取制定区间范围内的值，类似于between...and的关系  
从零到负一表示全部  
![16](/Redis/redisfile/16.png)   
setrange设置指定区间范围内的值，格式是setrange key值具体值  
![17](/Redis/redisfile/17.png)   
+  setex(set with expire)键秒值/setnx(set if not exist)  
setex:设置带过期时间的key，动态设置。  
setex 键秒值真实值  
![18](/Redis/redisfile/18.png)   
setnx:只有在key不存在时设置key的值。  
![19](/Redis/redisfile/19.png)   
+  mset/mget/msetnx  
mset:同时设置一个或多个 key-value 对。  
![20](/Redis/redisfile/20.png)   
mget:获取所有(一个或多个)给定 key 的值。   
![21](/Redis/redisfile/21.png)   
msetnx:同时设置一个或多个 key-value 对，当且仅当所有给定 key 都不存在。  
![22](/Redis/redisfile/22.png)   
+  getset(先get再set)  
getset:将给定 key 的值设为 value ，并返回 key 的旧值(oldvalue)。简单一句话，先get然后立即set  
![23](/Redis/redisfile/23.png)   
### List列表  
+ lpush/rpush/lrange  
+ lpop/rpop  
![26](/Redis/redisfile/26.png)   
+  lindex，按照索引下标获得元素(从上到下)  
![27](/Redis/redisfile/27.png)   
+  llen  
+ 从left往right删除2个值等于v1的元素，返回的值为实际删除的数量LREM list3 0 值，表示删除全部给定的值。零个就是全部值  
![28](/Redis/redisfile/28.png)   
+ ltrim key 开始index 结束index，截取指定范围的值后再赋值给key  
![29](/Redis/redisfile/29.png)   
+  rpoplpush 源列表目的列表  
![30](/Redis/redisfile/30.png)   
+ lset key index value  
![31](/Redis/redisfile/31.png)   
+ linsert key  before/after 值1 值2  
![32](/Redis/redisfile/32.png)   
```
性能总结: 它是一个字符串链表，left、right都可以插入添加；
如果键不存在，创建新的链表；
如果键已存在，新增内容；
如果值全移除，对应的键也就消失了。
链表的操作无论是头和尾效率都极高，但假如是对中间元素进行操作，效率就很惨淡了。
```
### Set集合  
+ sadd/smembers/sismember  
![33](/Redis/redisfile/33.png)   
+ scard，获取集合里面的元素个数  
![34](/Redis/redisfile/34.png)   
+ srem key value 删除集合中元素  
![35](/Redis/redisfile/35.png)   
+ srandmember key 某个整数(随机出几个数)  
![36](/Redis/redisfile/36.png)   
+ spop key 随机出栈  
![37](/Redis/redisfile/37.png)  
+ smove key1 key2 在key1里某个值      作用是将key1里的某个值赋给key2  
![38](/Redis/redisfile/38.png)  
+ 差集：sdiff
![39](/Redis/redisfile/39.png)  
+ 交集：sinter
![40](/Redis/redisfile/40.png)  
+ 并集：sunion
![41](/Redis/redisfile/41.png)  
### Hash哈希  
+ hset/hget/hmset/hmget/hgetall/hdel  
![42](/Redis/redisfile/42.png)  
+ hlen  
+ hexists key 在key里面的某个值的key  
+ hkeys/hvals  
![43](/Redis/redisfile/43.png)  
+ hincrby/hincrbyfloat  
![44](/Redis/redisfile/44.png)  
+ hsetnx  
![44](/Redis/redisfile/44.png)  
![45](/Redis/redisfile/45.png)  
### 有序集合Zset  
在set基础上，加一个score值。  
之前set是k1 v1 v2 v3，  
现在zset是k1 score1 v1 score2 v2  
+  zadd/zrange  
![46](/Redis/redisfile/46.png)  
+ zrangebyscore key 开始score 结束score  
![47](/Redis/redisfile/47.png)  
![48](/Redis/redisfile/48.png)  
+ zrem key 某score下对应的value值，作用是删除元素  
![49](/Redis/redisfile/49.png)    
+ zcard/zcount key score区间/zrank key values值，作用是获得下标值/zscore key 对应值,获得分数  
+  zrevrank key values值，作用是逆序获得下标值  
+ zrevrange  
+  zrevrangebyscore  key 结束score 开始score  
## 配置文件  
### Units单位  
![50](/Redis/redisfile/50.png)    
1. 配置大小单位,开头定义了一些基本的度量单位，只支持bytes，不支持bit
2. 对大小写不敏感  
### INCLUDES包含  
![51](/Redis/redisfile/51.png)    
和我们的Struts2配置文件类似，可以通过includes包含，redis.conf可以作为总闸，包含其他
### GENERAL通用  
+ Daemonize
+ Pidfile
+ Port 
+ Tcp-backlog  
tcp-backlog  
设置tcp的backlog，backlog其实是一个连接队列，backlog队列总和=未完成三次握手队列 + 已经完成三次握手队列。  
在高并发环境下你需要一个高backlog值来避免慢客户端连接问题。注意Linux内核会将这个值减小到/proc/sys/net/core/somaxconn的值，所以需要确认增大somaxconn和tcp_max_syn_backlog两个值  
来达到想要的效果  
+ Timeout  
+ Bind 
+ Tcp-keepalive  
单位为秒，如果设置为0，则不会进行Keepalive检测，建议设置成60 
+ Loglevel  
+ Logfile  
+ Syslog-enabled   
是否把日志输出到syslog中  
+ Syslog-ident  
指定syslog里的日志标志
+ Syslog-facility  
指定syslog设备，值可以是USER或LOCAL0-LOCAL7  
+ Databases  
### SNAPSHOTTING快照  
+ Save  
save 秒钟 写操作次数  
RDB是整个内存的压缩过的Snapshot，RDB的数据结构，可以配置复合的快照触发条件，默认  
是1分钟内改了1万次，  
或5分钟内改了10次，  
或15分钟内改了1次。   
如果想禁用RDB持久化的策略，只要不设置任何save指令，或者给save传入一个空字符串参数也可以   
+ Stop-writes-on-bgsave-error    
如果配置成no，表示你不在乎数据不一致或者有其他的手段发现和控制   
+ rdbcompression  
rdbcompression：对于存储到磁盘中的快照，可以设置是否进行压缩存储。如果是的话，redis会采用LZF算法进行压缩。如果你不想消耗CPU来进行压缩的话，可以设置为关闭此功能  
+ rdbchecksum  
rdbchecksum：在存储快照后，还可以让redis使用CRC64算法来进行数据校验，但是这样做会增加大约10%的性能消耗，如果希望获取到最大的性能提升，可以关闭此功能  
+ dbfilename  
+ dir
### REPLICATION复制 
### SECURITY安全 
+ 访问密码的查看、设置和取消  
![52](/Redis/redisfile/52.png)  
### LIMITS限制 
+ Maxclients 
设置redis同时可以与多少个客户端进行连接。默认情况下为10000个客户端。当你无法设置进程文件句柄限制时，redis会设置为当前的文件句柄限制值减去32，因为redis会为自身内部处理逻辑留一些句柄出来。如果达到了此限制，redis则会拒绝新的连接请求，并且向这些连接请求方发出“max number of clients reached”以作回应。
+ Maxmemory 
设置redis可以使用的内存量。一旦到达内存使用上限，redis将会试图移除内部数据，移除规则可以通过maxmemory-policy来指定。如果redis无法根据移除规则来移除内存中的数据，或者设置了“不允许移除”，
那么redis则会针对那些需要申请内存的指令返回错误信息，比如SET、LPUSH等。  
但是对于无内存申请的指令，仍然会正常响应，比如GET等。如果你的redis是主redis（说明你的redis有从redis），那么在设置内存使用上限时，需要在系统中留出一些内存空间给同步队列缓存，只有在你设置的是“不移除”的情况下，才不用考虑这个因素。  
+ Maxmemory-policy  
（1）volatile-lru：使用LRU算法移除key，只对设置了过期时间的键  
（2）allkeys-lru：使用LRU算法移除key  
（3）volatile-random：在过期集合中移除随机的key，只对设置了过期时间的键  
（4）allkeys-random：移除随机的key  
（5）volatile-ttl：移除那些TTL值最小的key，即那些最近要过期的key  
（6）noeviction：不进行移除。针对写操作，只是返回错误信息  
+ Maxmemory-samples  
设置样本数量，LRU算法和最小TTL算法都并非是精确的算法，而是估算值，所以你可以设置样本的大小，redis默认会检查这么多个key并选择其中LRU的那个  
### APPEND ONLY MODE追加 
+ appendonly
+ appendfilename 
+ Appendfsync  
![54](/Redis/redisfile/54.png)  
1. Always：同步持久化 每次发生数据变更会被立即记录到磁盘  性能较差但数据完整性比较好  
2. Everysec：出厂默认推荐，异步操作，每秒记录   如果一秒内宕机，有数据丢失
3. No
+ No-appendfsync-on-rewrite：重写时是否可以运用Appendfsync，用默认no即可，保证数据安全性。  
+ Auto-aof-rewrite-min-size：设置重写的基准值  
+ Auto-aof-rewrite-percentage：设置重写的基准值
### 常见配置redis.conf介绍
```
redis.conf 配置项说明如下：
1. Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程
  daemonize no
2. 当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定
  pidfile /var/run/redis.pid
3. 指定Redis监听端口，默认端口为6379，作者在自己的一篇博文中解释了为什么选用6379作为默认端口，因为6379在手机按键上MERZ对应的号码，而MERZ取自意大利歌女Alessia Merz的名字
  port 6379
4. 绑定的主机地址
  bind 127.0.0.1
5.当 客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能
  timeout 300
6. 指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose
  loglevel verbose
7. 日志记录方式，默认为标准输出，如果配置Redis为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给/dev/null
  logfile stdout
8. 设置数据库的数量，默认数据库为0，可以使用SELECT <dbid>命令在连接上指定数据库id
  databases 16
9. 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合
  save <seconds> <changes>
  Redis默认配置文件中提供了三个条件：
``` 
# Redis的持久化  
## RDB（Redis DataBase）
### 什么是RDB  
1. 在指定的时间间隔内将内存中的数据集快照写入磁盘，也就是行话讲的Snapshot快照，它恢复时是将快照文件直接读到内存里。  
2. Redis会单独创建（fork）一个子进程来进行持久化，会先将数据写入到一个临时文件中，待持久化过程都结束了，再用这个临时文件替换上次持久化好的文件。整个过程中，主进程是不进行任何IO操作的，这就确保了极高的性能如果需要进行大规模数据的恢复，且对于数据恢复的完整性不是非常敏感，那RDB方
式要比AOF方式更加的高效。RDB的缺点是最后一次持久化后的数据可能丢失。  
### Fork  
Fork的作用是复制一个与当前进程一样的进程。新进程的所有数据（变量、环境变量、程序计数器等）
数值都和原进程一致，但是是一个全新的进程，并作为原进程的子进程
### Rdb 保存的是dump.rdb文件
### 配置文件位置  
![55](/Redis/redisfile/55.png)  
### 如何触发RDB快照
1. 配置文件中默认的快照配置  
![56](/Redis/redisfile/56.png)  
![57](/Redis/redisfile/57.png)  
2. 命令save或者是bgsave  
Save：save时只管保存，其它不管，全部阻塞  
BGSAVE：Redis会在后台异步进行快照操作，快照同时还可以响应客户端请求。可以通过lastsave命令获取最后一次成功执行快照的时间
3. 执行flushall命令，也会产生dump.rdb文件，但里面是空的，无意义  
### 如何恢复  
1. 将备份文件 (dump.rdb) 移动到 redis 安装目录并启动服务即可  
2. CONFIG GET dir获取目录
### 优势 
1. 适合大规模的数据恢复  
2. 对数据完整性和一致性要求不高  
### 劣势  
1. 在一定间隔时间做一次备份，所以如果redis意外down掉的话，就会丢失最后一次快照后的所有修改  
2. Fork的时候，内存中的数据被克隆了一份，大致2倍的膨胀性需要考虑  
### 如何停止  
动态所有停止RDB保存规则的方法：redis-cli config set save ""  
### 小总结  
![58](/Redis/redisfile/58.png)  
## AOF  
### 什么是AOF 
以日志的形式来记录每个写操作，将Redis执行过的所有写指令记录下来(读操作不记录)，只许追加文件但不可以改写文件，redis启动之初会读取该文件重新构建数据，换言之，redis重启的话就根据日志文件的内容将写指令从前到后执行一次以完成数据的恢复工作
### Aof保存的是appendonly.aof文件  
### 配置位置 
![59](/Redis/redisfile/59.png)  
### AOF启动/修复/恢复  
1. 正常恢复  
启动：设置Yes,修改默认的appendonly no，改为yes  
将有数据的aof文件复制一份保存到对应目录(config get dir)  
恢复：重启redis然后重新加载  
2. 异常恢复  
启动：设置Yes,修改默认的appendonly no，改为yes  
修改默认的appendonly no，改为yes  
修复：Redis-check-aof --fix进行修复  
恢复：重启redis然后重新加载  
### Rewrite  
1. 是什么  
AOF采用文件追加方式，文件会越来越大为避免出现此种情况，新增了重写机制,当AOF文件的大小超过所设定的阈值时，Redis就会启动AOF文件的内容压缩，只保留可以恢复数据的最小指令集.可以使用命令bgrewriteaof  
2. 重写原理  
AOF文件持续增长而过大时，会fork出一条新进程来将文件重写(也是先写临时文件最后再rename)，遍历新进程的内存中数据，每条记录有一条的Set语句。重写aof文件的操作，并没有读取旧的aof文件，而是将整个内存中的数据库内容用命令的方式重写了一个新的aof文件，这点和快照有点类似  
3. 触发机制  
Redis会记录上次重写时的AOF大小，默认配置是当AOF文件大小是上次rewrite后大小的一倍且文件大于64M时触发  
### 优势  
1. 每修改同步：appendfsync always   同步持久化 每次发生数据变更会被立即记录到磁盘  性能较差但数据完整性比较好  
2. 每秒同步：appendfsync everysec    异步操作，每秒记录   如果一秒内宕机，有数据丢失  
3. 不同步：appendfsync no从不同步  
### 劣势
1. 相同数据集的数据而言aof文件要远大于rdb文件，恢复速度慢于rdb
2. Aof运行效率要慢于rdb,每秒同步策略效率较好，不同步效率和rdb相同
### 总结
![60](/Redis/redisfile/60.png)  
## 总结  
1. 官方总结 
![61](/Redis/redisfile/61.png)  
2. RDB持久化方式能够在指定的时间间隔能对你的数据进行快照存储
3. AOF持久化方式记录每次对服务器写的操作,当服务器重启的时候会重新执行这些命令来恢复原始的数据,AOF命令以redis协议追加保存每次写的操作到文件末尾.Redis还能对AOF文件进行后台重写,使得AOF文件的体积不至于过大  
4. 只做缓存：如果你只希望你的数据在服务器运行的时候存在,你也可以不使用任何持久化方式.
5. 同时开启两种持久化方式  
6. 同时开启两种持久化方式
(1) 在这种情况下,当redis重启的时候会优先载入AOF文件来恢复原始的数据,因为在通常情况下AOF文件保存的数据集要比RDB文件保存的数据集要完整.  
(2) RDB的数据不实时，同时使用两者时服务器重启也只会找AOF文件。那要不要只使用AOF呢？
作者建议不要，因为RDB更适合用于备份数据库(AOF在不断变化不好备份)，快速重启，而且不会有AOF可能潜在的bug，留着作为一个万一的手段。  
7.  因为RDB文件只用作后备用途，建议只在Slave上持久化RDB文件，而且只要15分钟备份一次就够了，只保留save 900 1这条规则。  
如果Enalbe AOF，好处是在最恶劣情况下也只会丢失不超过两秒数据，启动脚本较简单只load自己的AOF文件就可以了。代价一是带来了持续的IO，二是AOF rewrite的最后将rewrite过程中产生的新数据写到新文件造成的阻塞几乎是不可避免的。只要硬盘许可，应该尽量减少AOF rewrite的频率，AOF重写的基础大小默认值64M太小了，可以设到5G以上。默认超过原大小100%大小时重写可以改到适当的数值。  
如果不Enable AOF ，仅靠Master-Slave Replication 实现高可用性也可以。能省掉一大笔IO也减少了rewrite时带来的系统波动。代价是如果Master/Slave同时倒掉，会丢失十几分钟的数据，启动脚本也要比较两个Master/Slave中的RDB文件，载入较新的那个。新浪微博就选用了这种架构
