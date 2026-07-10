---
name: cangjie-std
description: "Use when generating, reviewing, or repairing Cangjie .cj code that may need std APIs, core types, collections, String/Rune, sort, math, unicode, convert, tests, or common API pitfalls. Pair with cangjie-lang-features for .cj code; route to cangjie-stdx only for configured extension-library APIs."
---

## 标准库使用流程

1. 先从签名、返回类型、输入输出形状和已有 import 判断需求属于核心类型、集合、字符串、数学、转换、I/O、进程、网络还是扩展库；不要把其它语言的 API 习惯直接迁移到仓颉。
2. 写标准库 API 前先定位所属包和 import：`std.core` 自动导入，其它常用包如 `std.collection.*`、`std.sort.*`、`std.math.*`、`std.unicode.*`、`std.convert.*` 通常需要显式导入；不能新增 import 时不要调用对应扩展成员。
3. 先选数据结构再写逻辑：固定长度结果用 `Array<T>`，需要追加/过滤/收集用 `ArrayList<T>`，需要去重或计数用 `HashSet`/`HashMap`，需要有序语义再考虑 `TreeMap`/`TreeSet`。
4. 对会改变状态、提前退出、多步构造或依赖下标移动的逻辑，优先使用显式循环和可变容器；只有在函数签名明确、lambda 纯表达式且不读取此前被 `var` 更新过的局部值时才使用迭代器组合。
5. 标准库只覆盖 `std.*`。发现 `stdx.*`、具体摘要算法、Hex/Base64/URL、JSON、HTTP/TLS、压缩、日志等需求时，切换或并用 `cangjie-stdx` 并确认项目配置。

## import 闭包速查

| 使用的符号或能力 | 必须确认的 import | 禁止替代写法 |
| --- | --- | --- |
| `ArrayList`、`HashMap`、`HashSet` | `import std.collection.*` | 裸用集合类、`Array.append`、`HashMap.put`、`HashSet.put` |
| `sort(...)` | `import std.sort.*` | `arr.sort()`、`let sorted = sort(arr)`、`sort(arr)[i]` |
| `abs`、`sqrt`、`pow`、`ceil`、`floor`、`round` | `import std.math.*` | 假设数学自由函数内置、写 `x.ceil()` |
| `String.toLower()`/`toUpper()`/`trim()`、`Rune.isLetter()`/`toLowerCase()` | `import std.unicode.*` | 无 import 调用 Unicode 扩展、逐个 Rune 调 `toAsciiLower()` |
| `parse`、`tryParse`、`toString(radix:)` | `import std.convert.*` | 对 `parse()` 使用 `??`、把 `String(n)` 当数值转换 |

新增任何上表符号后，写入后必须回看顶层声明区，确认 import 位于 `package` 之后、其它声明之前；不能新增 import 时改写为不依赖该能力的实现。

## 写入后 API 闭包检查

- 集合：`Array<T>` 固定长度，出现 `.append` 一律改为 `ArrayList.add` 或预分配数组下标赋值；出现 `put` 时按目标类型改为 `add`、下标赋值或已有 API。
- 排序：`sort` 原地修改并返回 `Unit`，不得把返回值赋给变量、继续下标或作为表达式传参。
- 字符串：`for (c in s)` 得到 `UInt8`，只有按 UTF-8 字节处理时才保留；要与字符、字符串或 Unicode 分类比较时改为 `s.runes()`。
- Option：只有静态类型为 `?T`/`Option<T>` 的表达式才能用 `??`；和比较、算术混用时给 `??` 表达式加括号。
- 命名参数：只在文档签名带 `!` 时使用；不确定时使用位置参数，避免 `item:`、`initElement:` 等其它语言习惯。

## 代码生成 API 首检

### 集合与数组

- `Array<T>` 固定长度，没有 `append`/成员 `sort`。需要动态追加时用 `ArrayList<T>` 的 `add`，最后 `toArray()`；知道结果长度时可预分配 `Array<T>(size, repeat: value)` 并用显式循环按下标赋值。
- `Array<T>(size, repeat: value)` 用于重复填充值；按下标生成元素时可写 `Array<T>(size, { i => expr })`，但该 lambda 只能读取不可变局部值。若 `expr` 依赖扫描、排序、条件更新后仍为 `var` 的局部或可变容器，改用预分配数组加显式循环，不要把外层可变结果捕获进初始化器。
- `ArrayList`、`HashMap`、`HashSet` 来自 `std.collection`，使用前写 `import std.collection.*`。`ArrayList` 和 `HashSet` 添加元素都用 `add`；不要写 `append` 或 `put`。
- `HashMap` 更新可写 `map[key] = value` 或 `map.add(key, value)`；安全取值后参与比较时先加括号，例如 `(map.get(key) ?? 0) == 1`。不要把 `put` 当作 HashMap/HashSet API。
- 排序使用 `std.sort` 的自由函数：`import std.sort.*` 后写 `sort(arr)`、`sort(arr, descending: true)` 或 `sort(arr, lessThan: { a, b => ... })`；`sort` 原地修改集合并返回 `Unit`，不要写 `arr.sort()`、`let sorted = sort(arr)`、`sort(arr)[i]`，也不要把排序调用结果继续下标。
- `Array` 没有成员 `filter`/`map` 时，优先用显式循环加 `ArrayList` 收集；若使用迭代器函数，确认已导入对应集合工具并用 `collectArray`/`collectArrayList` 收尾。不要写 `filter(func...)` 或 `sort(func...)`。
- `get`、`remove`、`peek`、`tryRemove`、`tryParse`、溢出检查等 API 常返回 `?T`/`Option<T>`；比较、算术或传参前先模式匹配、`??` 提供默认值或显式解包，并给 `??` 表达式加括号。

### 字符串、Rune 与 Unicode

- `String` 长度属性是 `size`，判空调用 `isEmpty()`；不要写 `.length` 或 `.isEmpty`。子串用区间下标，例如 `s[start..end]`；简单查找优先 `contains`、`indexOf`、`startsWith`、`endsWith`。
- `String.trim()`、`String.toLower()`、`String.toUpper()`、`Rune.isLetter()`、`Rune.isUpperCase()`、`Rune.toLowerCase()` 等 Unicode 扩展需要 `import std.unicode.*`；没有该 import 时 `toLower` 不是 `String` 成员。ASCII-only 整串场景可用 `String` 核心方法 `toAsciiLower()`、`toAsciiUpper()`、`trimAscii()`；逐个 `Rune` 没有这些成员，需用 `UInt32(r)` 加减后转回 `Rune`、`match` 分支，或补 Unicode import。
- 按字符处理字符串时用 `s.runes()` 或 `toRuneArray()`，字符集合常用 `HashSet<Rune>`；需要字符串结果时用 `ArrayList<Rune>` 收集、`String(list.toArray())` 返回。

### 数学、排序与转换

- `ceil`、`floor`、`round`、`sqrt`、`pow`、`abs` 等数学自由函数需要 `import std.math.*`，调用方式是 `ceil(x)`，不要写 `x.ceil()`；静态复核时必须确认 import 实际出现在顶层声明区，否则 `abs` 等会是未声明标识符。
- 数值转字符串不要写 `String(n)` 或 `String(digit)`；十进制使用 `n.toString()` 或 `"${n}"`，指定进制使用 `std.convert.*` 的 `n.toString(radix: base)` 并确认 import，或手写 digit 表。
- 字符串解析、进制解析、格式化宽度/精度等能力属于 `std.convert.*`；`parse` 返回普通值并可能抛异常，`tryParse` 才返回 `?T`。只有 `tryParse` 等可空结果能用 `??`，不要对 `Int64.parse(...)` 再写 `??`。
- `std.crypto.digest` 只定义摘要接口和 `digest()` 便捷函数；MD5、SHA、HMAC 等具体算法以及 Hex/Base64 编码属于扩展库，必须交给 `cangjie-stdx` 处理配置和 import。

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
