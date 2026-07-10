---
name: cangjie-lang-features
description: "Use when generating, filling, or editing Cangjie .cj code: TODO/function skeletons, standalone funcs from signatures/comments/examples, one-shot source fills, compile errors, or syntax/import/type/lambda/String/Rune/Array/Option questions. For .cj code generation, load cangjie-std as the baseline; add cangjie-stdx only for configured extension-library APIs."
---

# 仓颉编程语言特性目录

## 生成前流程

1. 先读目标 `.cj` 文件的签名、返回类型、已有 `package/import`、辅助类型和注释约束；不要在不了解现有顶层结构时直接追加代码。
2. 只要任务要求生成、填充或修改 `.cj` 源码，就把 `cangjie-std` 作为基线同步加载或消费其规则；只有明确需要 JSON、编码、哈希、HTTP/TLS、压缩、日志等扩展库且项目配置可确认时，才额外加载 `cangjie-stdx`。
3. 先决定实现策略，再写代码：优先使用语法稳定、导入可满足、可静态检查的显式控制流；只有在 lambda 不捕获可变状态时才使用高阶函数。
4. 对 TODO 函数骨架、签名/注释/示例驱动的独立实现，或“一次填充且禁止编译/调试/修复”的源码任务，先按注释示例和测试推导返回形状、空输入、单元素、边界值和错误路径；不得只按直觉填入占位实现。
5. 写入后至少做静态复核；若用户禁止编译/调试/修复，仍必须复核语法、导入、返回路径、可变性、库配置风险和注释样例的手算结果，并在回复中说明未运行验证。

## .cj 生成闭包检查

### 写代码前

- 列出实现会使用的非 `std.core` 符号和所需 import：`ArrayList`/`HashMap`/`HashSet` 需要 `std.collection.*`，`sort` 需要 `std.sort.*`，`abs`/`sqrt`/`pow`/`ceil`/`floor`/`round` 需要 `std.math.*`，Unicode 大小写和 Rune 分类需要 `std.unicode.*`，`parse`/`tryParse`/指定进制 `toString(radix:)` 需要 `std.convert.*`。
- 若返回动态长度数组或需要追加/过滤/收集，优先计划 `ArrayList<T> + add + toArray()` 并同步添加 `import std.collection.*`；不能新增 import 时，先计算目标长度，再用 `Array<T>(size, repeat: value)` 和下标赋值。
- 处理字符串时先决定是按字节、按 ASCII 字符还是按 Unicode `Rune`：需要与 `String` 或 `Rune` 字面量比较时用 `s.runes()` 或 `toRuneArray()`，不要直接 `for (c in s)`。
- 若使用 `stdx.*`，先证明当前项目有可用 `cjpm.toml` 和依赖配置；不能证明时把 `stdx.*` 视为不可用路径。

### 写入后

- 扫描禁止模式并修正：`Array.append`、`HashMap.put`、`HashSet.put`、`arr.sort()`、`let sorted = sort(arr)`、`sort(arr)[i]`、`Array<T>(..., item:)`、无 `=>` 的 lambda、lambda 体内直接声明多步 `var/let`。
- 扫描类型和字符串风险：`String(n)`/`String(digit)`、`for (c in s)` 后把 `c` 与 `String`/`Rune` 比较、对 `parse()`/数组下标/普通算术使用 `??`、把 `Rune` 直接做算术、把 `~` 当按位取反。
- 扫描 import 闭包：新增了 `ArrayList`/`HashMap`/`HashSet`、`sort`、数学自由函数、Unicode 扩展或 convert API 时，顶层声明区必须有对应 import，且 import 不得出现在函数体或其它声明之后。
- 若不能运行编译或测试，至少用文件内注释示例或测试样例手算一次，确认返回类型、空集合、单元素、负数/零、字符串边界和所有可达路径。

## 一次性填充硬门禁

- 生成 `Array<T>(size, { ... })`、map/filter/sort 回调或尾随 lambda 前，先列出 lambda 读取的外层局部值；只要其中任一值来自此前 `var` 扫描、累加、交换、追加、排序、记录状态或条件更新，或读取任何仍为 `var` 的局部/可变容器，禁止使用该 lambda，改用预分配数组按下标赋值，或用 `ArrayList` 加显式 `while`/`for` 收集。
- 当任务只能修改 `.cj` 源码、用户禁止改配置，或项目中没有可确认的 `cjpm.toml`/`bin-dependencies` 时，不得写入 `stdx.*` import；应改用可用的 `std.*` 能力，给出可编译的降级实现，或明确说明该函数无法只靠当前源码完成。
- 当无 `stdx` 配置但任务要求 MD5/SHA/Hex/Base64 等扩展能力时，不要把复杂手写算法当作默认降级；只有能用已确认的仓颉语法逐项静态复核时才手写，否则说明当前约束下无法可靠完成。若手写位运算代码，按仓颉语法使用 `!x` 做按位取反，不要写 C/Java 风格的 `~x`。
- 使用 `abs`、`sqrt`、`pow`、`ceil`、`floor`、`round` 等数学自由函数时，必须在顶层声明区确认已有或新增 `import std.math.*`；若不能安全添加 import，改写成不依赖该函数的显式比较或四则逻辑。
- 使用 `std.core` 之外的标准库扩展 API 前必须确认 import 实际存在或可新增：`String.toLower()`/`toUpper()`/`trim()`、`Rune.isLetter()`/`toLowerCase()` 属于 `std.unicode.*`，进制解析/`toString(radix:)` 属于 `std.convert.*`。不能加 import 时，`String` 可用核心 ASCII 方法 `toAsciiLower()`/`toAsciiUpper()`/`trimAscii()`；`Rune` 没有这些 ASCII 成员，需用 `UInt32(r)` 加减 32 后 `Rune(code)`，或用 `match`/分支手写。
- 当 `String` 拼接、返回值或数组元素需要由数值产生时，不要写 `String(n)`、`String(digit)` 或把类型构造函数当通用 stringify；十进制用 `n.toString()` 或 `"${n}"`，指定进制必须先满足 `std.convert.*` import，或用显式 digit 表/分支生成字符。
- 使用 `std.convert.*` 的 `parse` / `tryParse` 时先确认返回类型：`Int64.parse("1")` 返回 `Int64` 并可能抛异常，不能再写 `??`；只有 `tryParse`、`get`、`indexOf` 等返回 `?T`/`Option<T>` 的表达式才能使用 `??`。

## 经验使用

- 若任务触发 lambda/可变状态、`stdx` 扩展库、数学/Unicode/convert API、数值字符串转换或 Option 语法等高风险场景，先查看 [反模式经验](./references/experiences.md)，只采用触发条件和适用边界都匹配当前任务的条目。
- experience 只作为动作级提醒或主规则索引；若条目与本文件硬门禁或主规则重复，以硬门禁为准，不得把经验降级成可选提醒，也不得把来源 rollout 的题目、路径或样例写成当前任务特判。

## 代码生成首检

### 顶层结构

- `package` 必须是第一个非空非注释声明；`import` 只能出现在顶层声明区：有 `package` 时放在 package 后、其它声明前；没有 package 时放在所有函数/类型声明前。不要在函数或声明后追加 import。
- 生成新 import 前先检查目标文件是否已有同包导入、通配导入、别名导入或冲突本地声明；不确定时保留最小导入，并避免重复导入。
- 非 `Unit` 返回函数必须在所有可达路径显式 `return` 对应类型；编译器不一定把 `while (true)` 识别为永不结束，循环后补一个保底 `return`。

### 控制流与模式

- `if`、`while`、`match` 的条件/匹配目标使用括号：`if (cond) { ... }`、`while (cond) { ... }`、`match (x) { ... }`。不要写 `if a < b {` 或 `while x {`。
- `match` 的每个 `case` 右侧必须有表达式或语句；空分支写 `case _ => ()`，不要只写 `case _ =>`。
- `for-in` 迭代变量不可重新赋值；需要修改值时新建 `var` 局部副本。需要精确控制索引、反向遍历或多指针移动时优先使用显式 `while`。
- 区间写 `0..n` 或 `0..=n`；仓颉没有 `0..<n` 语法。遍历下标时优先 `while (i < arr.size)`，避免越界。

### 类型、可变性与 lambda

- 函数参数、`let` 绑定和 `for-in` 迭代变量不可重新赋值；需要更新时创建 `var` 局部变量承接当前值。
- 初始化器、高阶函数或回调中的 lambda 只用于纯表达式或不可变捕获。凡是需要累加、交换、追加、记录状态、提前退出、修改外层 `var`，或读取此前由 `var` 扫描/更新得到的局部结果，必须改用显式 `while`/`for` 循环或可变容器，避免 mutable capture 编译失败。
- lambda 语法必须包含 `=>`，尾随 lambda 位置才可省略；lambda 体内若要声明 `var/let`、执行多步逻辑或多处返回，优先改成普通控制流或局部函数。
- 命名实参只在参数定义带 `!` 时可用；不确定时优先用位置参数，例如 `s.indexOf(sub, start)`、`Array<Int64>(n, { i => ... })`。

### 字符、数字与 Option

- `String` 默认迭代得到 `Byte`/`UInt8`，按字符处理时使用 `for (r in s.runes())`、`toRuneArray()` 和 Rune 字面量 `r'a'`。不要把 `for (r in s)` 得到的 `UInt8` 与 `Rune`/`String` 直接比较。
- 字符串、数组和集合的下标/大小通常用 `Int64`；循环计数器显式写 `var i: Int64 = 0`。不要混用 `UInt32` 计数器和 `.size`。
- 仓颉使用类型构造函数转换数值和字符：`Int64(x)`、`UInt32(r)`、`Rune(code)`；不要写 `.toInt64()`，也不要写 `Int64(rune)`，Rune 转整数先用 `Int64(UInt32(rune))`。`String(...)` 不是数值转字符串构造器；`String(runes)` 仅用于 Rune 数组/集合，数字转字符串用 `n.toString()`、插值或带 import 的 `std.convert.*`。
- `Option<T>` 的类型简写是 `?T`，安全成员访问是 `?.`，提供默认值用 `??`；`??` 的左操作数必须静态为 `Option`，不要对 `parse()`、普通算术、数组下标或非可空返回值使用。`??` 与 `==`、`!=`、`<`、`>` 混用时给 coalescing 表达式加括号。
- 位运算使用 `&`、`|`、`^`、`<<`、`>>`；按位取反是一元 `!x`，不是 `~x`。移植 MD5/SHA/位掩码代码时逐项替换其它语言的 `~`，并确认操作数是整数而非 `Bool`。

### 库能力路由

- `abs`、`sqrt`、`pow`、`ceil`、`floor`、`round` 等数学自由函数属于 `std.math.*`；需要这些 API 时加载 `cangjie-std`，并在代码中确认顶层存在 `import std.math.*`。
- `sort`、集合构造、字符串 API、解析/格式化、HashMap/HashSet 等标准库能力以 `cangjie-std` 为准；不要只凭语言语法猜 API 名称。
- `String.toLower()`/`toUpper()`/`trim()` 等 Unicode 扩展必须有 `import std.unicode.*`；ASCII-only 的整串转换优先用 `String` 核心方法 `toAsciiLower()`/`toAsciiUpper()`/`trimAscii()`，逐个 `Rune` 转大小写则用编码分支或 Unicode import。`parse`、`tryParse`、`toString(radix:)` 等 convert 能力必须有 `import std.convert.*`，且 `parse` 返回普通值、`tryParse` 才返回 `Option`。
- MD5/SHA/HMAC、Hex/Base64/URL、JSON、HTTP/TLS、压缩和日志等扩展库能力以 `cangjie-stdx` 为准；未知、裸编译、无 `cjpm.toml` 或禁止改配置时，把 `stdx.*` import 视为不可用，不得生成会直接编译失败的源码。

> 请按需查阅相关文档

- [基本概念](./basic_concepts/README.md): 介绍仓颉编程语言的关键字、标识符、程序结构、变量定义(let/var/const)、值类型与引用类型、作用域规则、表达式(if/while/for-in/break/continue)、函数等基本概念和规则
- [基本数据类型](./basic_data_type/README.md): 介绍仓颉语言的整数、浮点、布尔、字符(Rune)、字符串(String)、Unit、Nothing、元组(Tuple)、数组(Array/VArray)、区间(Range)类型以及基本运算符的语法和规则
- [字符串/String](./string/README.md): 介绍仓颉标准库 String 类型的构造、搜索、替换、分割、拼接、裁剪、大小写转换、编码处理、下标访问、迭代等操作的完整 API 和用法
- [for-in 迭代](./for/README.md): 介绍仓颉语言 for-in 循环语法、Iterable/Iterator 接口、Range 区间类型、迭代控制（break/continue/where）、元组解构、自定义迭代器、迭代最优实践等特性
- [函数/function](./function/README.md): 介绍仓颉语言的函数定义、调用、命名参数、默认值、函数类型、Lambda表达式、闭包、嵌套函数、函数重载、运算符重载、尾随Lambda、管道运算符(|>)、组合运算符(~>)、变长参数等特性
- [常量/const](./const/README.md): 介绍仓颉语言的 const 变量定义、const 表达式、const 函数、编译时求值、const init 构造函数等特性

- [类/class](./class/README.md): 介绍仓颉语言的类定义、抽象类、构造函数(init/主构造函数)、终结器(~init)、继承(单继承/sealed)、重写(override)、重定义(redef)、成员变量、成员函数、属性(prop)、访问修饰符、This类型、对象创建等特性
- [结构体/struct](./struct/README.md): 介绍仓颉语言的struct定义、构造函数(init/主构造函数)、值语义、成员访问与修改规则、mut函数及其限制等特性
- [接口/interface](./interface/README.md): 介绍仓颉语言的接口定义、接口实现(单个/多个)、接口继承、默认实现(实例/静态)、sealed接口、泛型成员、Any类型、属性(prop)在接口中的使用、菱形继承解决方案等特性
- [枚举/enum](./enum/README.md): 介绍仓颉语言的enum定义规则、构造器（有参/无参/同名/非穷举）、枚举的使用与名称冲突、枚举成员函数和属性、递归枚举、枚举实现Equatable接口等特性
- [泛型/generic](./generic/README.md): 介绍仓颉语言的泛型函数、泛型类、泛型接口、泛型结构体、泛型枚举、泛型约束(where)、泛型子类型关系、型变(不变/协变/逆变)等特性
- [类型系统](./type_system/README.md): 介绍仓颉语言的子类型关系（继承/接口实现/元组/函数类型）、型变规则（协变/逆变/不型变）、类型转换（is/as操作符）、数值类型转换、Rune转换、Nothing/Any/Object等基础类型关系、类型别名(type)等特性
- [扩展/extend](./extend/README.md): 介绍仓颉语言的直接扩展(extend)、接口扩展、泛型扩展、扩展中的访问规则、孤儿规则、导出与导入规则等特性

- [Option 类型](./option/README.md): 介绍仓颉语言 Option\<T\> 定义与用法、?T 简写、自动包装、模式匹配解构、coalescing 操作符(??)、问号操作符(?.)、getOrThrow()、if-let 条件解构、while-let 循环解构等特性
- [模式匹配](./pattern_match/README.md): 介绍仓颉语言 match 表达式、模式类型（常量/通配符/绑定/元组/类型/枚举）、模式嵌套、模式守卫(where)、穷举性、模式可反驳性、if-let 条件匹配、while-let 循环匹配、模式在变量定义和 for-in 中的使用等特性
- [错误处理](./error_handle/README.md): 介绍仓颉语言的异常层次(Error/Exception)、自定义异常、throw、try/catch/finally、try-with-resources、CatchPattern、Option类型错误处理(?./??/getOrThrow)、内置运行时异常等错误处理特性

- [并发编程](./concurrency/README.md): 介绍仓颉语言的M:N线程模型、spawn创建线程、sleep、原子操作(Atomic)、互斥锁(Mutex)、条件变量(Condition)、synchronized、Future、线程取消、ThreadLocal等并发编程特性
- [宏/macro](./macro/README.md): 介绍仓颉语言宏与元编程，包括Token/Tokens类型、quote表达式与插值、非属性宏、属性宏、嵌套宏与通信、std.ast包与语法节点解析
- [反射与注解](./reflect_and_annotation/README.md): 介绍仓颉语言的整数溢出注解(@OverflowThrowing/@OverflowWrapping/@OverflowSaturating)、自定义注解(@Annotation)、反射(TypeInfo)等特性

- [包机制/package](./package/README.md): 介绍仓颉语言的包声明(package)、程序入口(main)、包导入(import)、重新导出(public import)、顶层访问修饰符(private/internal/protected/public)等特性
- [项目管理/cjpm](./project_management/README.md): 介绍仓颉项目管理工具 cjpm 的用法，包括创建项目、项目配置(cjpm.toml)、管理依赖、构建、运行、测试、清理、安装、工作区、交叉编译、构建脚本(build.cj)、增量编译、环境变量替换等

- [集合类型](./collections/README.md): 介绍仓颉集合数据类型，包括Array/ArrayList/HashMap/HashSet

- [C 互操作/CFFI](./cffi/README.md): 介绍仓颉程序与C程序互操作，包括foreign声明、CFunc、inout参数、unsafe块、调用约定、类型映射(基础类型/结构体/CPointer/VArray/CString)、C回调仓颉、内存管理等特性
