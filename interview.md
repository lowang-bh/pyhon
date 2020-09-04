# GO 基础
- golang中的引用类型和传值类型分别有哪些
- interface有哪些用途
- Slice与数组区别
- 如何实现map顺序读取
- go什么情况下会发生内存泄漏？（goruntime未退出等）
- 如果把slice当做函数参数，在函数内部修改和append slice时候原来的slice会发生变化吗
- 函数定义的接受者可以有指针和值，函数的调用者也有指针和值，两两组合四种情况都能通过编译吗，为啥？
- struct中属性定义的先后顺序有影响吗

## go 源码
- 协程工作原理
- chan工作原理
- gc原理

# Linux 基础
## 常用linux工具命令
- top，lsof，strace，netstat，ss 等；
- 如何查看一个端口被哪个进程占用？（lsof, netstat）
- top列出的进程状态有哪些，分别什么意思？
- Z状态的进程如何处理？D状态的进程能杀死吗？如何处理

## 操作系统
- 进程虚拟空间分布，初始化和未初始化的全局变量放哪里
- 线程，进程的区别和联系
- 多进程通信机制有哪些，分别有什么区别
- 说出几个常见信号，进程收到同一个信号多次会怎样？
- select， epoll 有啥区别
- 简述CFS调度算法
- Cache和swap原理
- 文件系统VFS，inode和dentry关系，硬链接软链接

# 网络基础
- 针对一台机器多次HTTP请求，建立了多少个TCP连接
- HTTP2和HTTP1区别和优势
- 如果使用UDP可以建立有状态连接吗
- HTTP常见状态码，200、201 、301、302、308、309 、401、403 、404、413、 415 、429、499、500 
- TCP三次握手，四次挥手流程；以及为啥握手是三次，挥手是四次
- SYN Flood了解吗？有什么解决方案（启用syncookies:net.ipv4.tcp_syncookies=1）
- 为啥要有timewait状态？没有可以吗
- 服务器TIME_WAIT很多，如何产生的？ 该如何处理？

# 数据库
## Mysql
- mysql存储引擎有哪些？InnoDb使用什么数据结构？为啥
- 索引类型
- mysql优化

## Redis
- Redis基本数据结构
- Redis有哪几种数据淘汰策略
- redis容灾，备份，扩容

# k8s 基础
- 容器资源限制和隔离使用什么技术？有哪些namespace？POD里面有哪些共享的ns
- k8s集群常用组件及主要作用
- kubectl常用命令举例
- 什么情况下pod会被驱逐，发生驱逐的时候通过get pod查看pod处于什么状态？
- 用过k8s哪种网络？
- vxlan 原理

## k8s高级
- cgroup和namespace的工作原理？
- kubectl 创建一个POD的流程
- flannel网络工作模式(vxlan，hostgw，udp)，前两种的原理和优缺点
- 容器内的流量是如何进入flannel.1 网卡的
- 通过clusterIP访问服务的过程，通过nodeIP+port访问服务的过程
- scheduler调度过程
- scheduler抢占机制
- controller的工作原理， informer是如何工作的？
- etcd了解吗？如何保证数据一致性？

# 算法题
- 二分查找，快排
- topK排序
- lru实现
- B+树
- 跳表

# 开放性问题
- 平时怎么学习
- 最近看什么书
- 在浏览器输入www.taobao.com,后发生了哪些事情
- 为啥go可以支持多个返回值