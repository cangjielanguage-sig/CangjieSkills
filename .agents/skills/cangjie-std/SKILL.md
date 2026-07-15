---
name: cangjie-std
description: "Use for every .cj generation/edit paired with cangjie-lang-features to verify whether the candidate needs Cangjie std.* APIs and, when it does, their packages/imports, signatures, return values, mutation effects, failure models, collections, String/Rune, sort, math, unicode, convert, I/O, networking, processes, or tests. Invoke before the first .cj write; use cangjie-stdx for extension capabilities or stdx availability decisions."
---

## 职责边界

- 本 Skill 负责 `std.*` API 的选择与契约核对，不重复语言语法；语法、捕获、类型和顶层结构由 `cangjie-lang-features` 负责。
- 具体 API 以本目录专题文档为唯一权威来源。主文件负责识别能力、加载专题和检查调用闭包，不维护针对单个评测错误的黑名单。
- 具体摘要算法、Hex/Base64/URL、JSON、HTTP/TLS、压缩和日志等扩展能力交给 `cangjie-stdx`；是否已配置不是加载该 Skill 的前置条件。

## 标准库选路流程

1. 从任务契约识别能力和输入输出形状，区分核心类型、集合、排序、数学、Unicode、转换、I/O、网络、进程或测试。
2. 为每项能力读取对应专题，记录实际符号、所属包、完整签名、返回类型、是否修改输入以及失败方式；不要凭其它语言的同名 API 推断。
3. 枚举符合约束的调用路径，比较数据结构、错误语义、是否保留输入和所需 import；选择后再生成代码。
4. 将所有非 `std.core` 符号加入依赖清单，确认顶层 import 可见且不存在别名或本地声明冲突。
5. 完整候选写入前按“签名、类型、效果、失败、依赖”复核每个 API 调用；任一项不闭合都不得写入。写后再对实际文件复核传输结果；验证不可用时至少手算契约样例。

## 解法路径选择

| 需求 | 合理路径 | 选择依据 |
| --- | --- | --- |
| 构造结果集合 | 固定长度 `Array`、动态集合、迭代器收集 | 结果长度、追加/去重需求、回调状态模型 |
| 排序 | 原地排序，或先复制再排序 | 是否允许修改输入；返回值与副作用以 [sort](./sort/README.md) 为准 |
| 字符大小写与分类 | String 的 ASCII 核心方法、Unicode 扩展、逐 Rune 转换 | ASCII/Unicode 语义和 import 可用性 |
| 文本解析 | `parse`、`tryParse` 或显式校验 | 失败应抛异常、返回 Option 还是由调用方处理 |
| 多步变换 | 纯回调组合、显式循环或局部函数 | 是否存在可变状态、提前退出和多阶段控制流 |

## API 契约闭包

- **符号与依赖**：每个类型、自由函数和扩展成员都能映射到专题中的包与 import。
- **签名**：参数位置、命名参数标记、泛型约束和回调类型与文档一致。
- **类型**：返回值、Option、下标和转换结果在后续表达式中的用法匹配静态类型。
- **效果**：明确 API 是原地修改、返回新值还是返回 `Unit`；需要保留输入时先选择复制路径。
- **失败**：区分抛异常、返回 Option、运行时前置条件和 I/O 错误，并让调用方完整处理。
- **平台**：涉及文件、网络、进程或 native 依赖时，确认目标平台和运行方式满足专题前提。

## 高频专题路由

| 能力 | 必读专题 |
| --- | --- |
| Array、ArrayList、Map/Set、迭代收集 | [std.collection](./collection/README.md) |
| 排序及比较器 | [std.sort](./sort/README.md) |
| 数学函数和扩展数值 | [std.math](./math/README.md) 与 [std.math.numeric](./math_numeric/README.md) |
| Rune/String 的 Unicode 操作 | [std.unicode](./unicode/README.md) |
| 解析、进制与格式化 | [解析](./convert/parsable.md) 与 [格式化](./convert/formattable.md) |
| 摘要接口与具体算法边界 | [std.crypto.digest](./crypto_digest/README.md)，具体算法再加载 `cangjie-stdx` |

请按需查询当前目录下的标准库文档：

[std.core](./core/README.md)：核心包（自动导入），包括基本类型(Int/Float/Bool/String/Array/Option)、核心接口(Comparable/Hashable/Iterable/Resource)、StringBuilder、Duration 时间间隔、全局函数(print/println/spawn/sleep/min/max)、异常体系等。

[std.collection](./collection/README.md)：集合数据结构，包括 ArrayList 动态数组、HashMap/HashSet 哈希集合、TreeMap/TreeSet 有序集合、LinkedList 双向链表、ArrayDeque/ArrayQueue/ArrayStack 双端队列/队列/栈、函数式迭代操作(filter/map/fold/reduce)、收集函数(collectArray/collectHashMap)等。

[std.time](./time/README.md)：时间日期处理，包括 DateTime 构造/格式化/解析/时区转换、MonoTime 单调时钟计时、Duration 时间间隔、Month/DayOfWeek 枚举等。

[std.math](./math/README.md)：数学运算，包括 abs/sqrt/pow/log 等常用函数、sin/cos/tan 三角函数、ceil/floor/round 取整、gcd/lcm 整数运算、浮点数特殊值(NaN/Inf)检查等。

[std.math.numeric](./math_numeric/README.md)：扩展数值类型，包括 BigInt 任意精度整数（parse/divAndMod/modPow/bitLen）、Decimal 任意精度十进制数（precision/scale）、相关数学函数(abs/gcd/lcm/sqrt)等。

[std.sync](./sync/README.md)：并发同步原语，包括 Atomic 原子类型（AtomicInt64/AtomicBool 等）、Mutex 互斥锁与 synchronized 块、Condition 条件变量(wait/notify)、Timer 定时器、Barrier/Semaphore/SyncCounter 等。

[std.collection.concurrent](./collection_concurrent/README.md)：并发安全集合，包括 ConcurrentHashMap 线程安全哈希表、ArrayBlockingQueue/LinkedBlockingQueue 阻塞队列、ConcurrentLinkedQueue 非阻塞队列等。

[std.regex](./regex/README.md)：正则表达式，包括 Regex 创建与匹配标志(IgnoreCase/MultiLine)、find/findAll 查找、replace/replaceAll 替换、split 分割、捕获组与命名组等。

[std.fs](./fs/README.md)：文件系统操作，包括 File 读写(read/write/append)、Directory 目录操作(create/readFrom/walk)、Path 路径处理(join/parent/extensionName)、FileInfo 文件信息、HardLink/SymbolicLink 链接操作等。

[std.io](./io/README.md)：I/O 流模型，包括 InputStream/OutputStream 接口、ByteBuffer 内存流、BufferedInputStream/BufferedOutputStream 缓冲流、StringReader/StringWriter 字符串流、ChainedInputStream/MultiOutputStream 链式流、流工具函数(copy/readToEnd/readString)等。

[std.net](./net/README.md)：Socket 编程总览，包括类型层次、地址类型（IPAddress/IPPrefix/SocketAddress）、Socket 选项配置、异常处理等。详细文档：[TCP 编程](./net/TCP.md)、[UDP 编程](./net/UDP.md)、[Unix Domain Socket](./net/UDS.md)。

[std.process](./process/README.md)：进程管理，包括 launch 创建子进程、execute/executeWithOutput 执行命令、SubProcess 标准流重定向(Pipe/Inherit/Null)、findProcess 查找进程、进程等待与终止等。

[std.env](./env/README.md)：进程环境，包括环境变量读写(getVariable/setVariable)、进程信息(getProcessId/getWorkingDirectory)、标准流(getStdIn/getStdOut/getStdErr)、进程退出(exit/atExit)等。

[std.sort](./sort/README.md)：排序功能，包括对 Array/ArrayList/List 排序、自定义比较器(by/lessThan/key)、稳定排序(stable)、降序排序(descending)等。

[std.random](./random/README.md)：随机数生成，包括 Random 类、nextInt/nextFloat/nextBool 方法、指定范围随机数(upper)、高斯分布(nextGaussianFloat64)、种子控制等。

[std.binary](./binary/README.md)：二进制端序转换，包括 BigEndianOrder/LittleEndianOrder 大端序/小端序读写接口、支持 Bool/Float/Int/UInt 等基本类型、网络字节序处理等。

[std.overflow](./overflow/README.md)：整数溢出处理，包括 CheckedOp（返回 Option）、SaturatingOp（饱和截断）、ThrowingOp（抛异常）、WrappingOp（回绕截断）、CarryingOp（进位检测）五种溢出策略。

[std.unicode](./unicode/README.md)：Unicode 字符处理，包括 Rune 字符分类(isLetter/isNumber/isWhiteSpace)、大小写转换(toLowerCase/toUpperCase)、语言特定转换(CasingOption)等。

[std.deriving](./deriving/README.md)：自动派生，包括 @Derive[ToString/Hashable/Equatable/Comparable] 编译期自动实现接口、@DeriveExclude/@DeriveInclude 字段控制、@DeriveOrder 字段顺序等。

[std.reflect](./reflect/README.md)：运行时反射，包括 TypeInfo.of() 获取类型信息、ClassTypeInfo/StructTypeInfo 类型元数据、ConstructorInfo/InstanceFunctionInfo 成员信息、动态成员访问等。

[std.crypto.digest](./crypto_digest/README.md)：摘要算法，包括 Digest 接口(write/finish/reset)、digest() 便捷哈希函数、BlockCipher 对称加密接口等。

[std.convert](./convert/)：类型转换与格式化，包括[字符串解析为基础类型](./convert/parsable.md)（Parsable 接口、整数/浮点/布尔解析、进制转换）和[数值格式化输出](./convert/formattable.md)（Formattable 接口、宽度/对齐/精度/进制格式化）。

[std.unittest](./unittest/README.md)：单元测试框架，包括 @Test/@TestCase 声明测试、@Assert/@Expect/@PowerAssert 断言、@BeforeAll/@AfterAll/@BeforeEach/@AfterEach 生命周期、参数化测试、基准测试(@Bench)、Mock/Spy 对象与桩配置(@On)等。

[std.stdio](./stdio/README.md)：标准输入输出，包括 print/println 标准输出、eprint/eprintln 标准错误输出、readln/read 标准输入、Console 控制台读写等。

[std.args](./args/README.md)：命令行参数处理，包括 main(args) 接收命令行参数、std.argopt 包解析短选项(-v)/长选项(--output)/组合选项、ArgumentSpec/ParsedArguments API 等。

[std.ref](./ref/README.md)：弱引用，包括 WeakRef 弱引用管理、CleanupPolicy 清理策略(EAGER/DEFERRED)、缓存场景用法等。
