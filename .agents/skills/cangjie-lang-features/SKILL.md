---
name: cangjie-lang-features
description: "用于生成或编辑任何仓颉 .cj 文件、填充函数骨架等；即使任务简单、只用 std.core，也必须在第一次写入前加载。Use for every Cangjie .cj generation/edit or one-shot implementation involving syntax, types, control flow, Array, String/Rune, Option, match, lambda, ranges, packages/imports, or compile errors. Pair every .cj write with cangjie-std; load cangjie-stdx before any extension-library path."
---

# 仓颉编程语言特性目录

## 职责与协作

- 本 Skill 负责语言层语义：顶层结构、控制流、类型、绑定与可变性、函数/闭包、String/Rune、Option、包与 import 语法。
- 生成或修改 `.cj` 时同步使用 `cangjie-std` 核对标准库 API；出现 JSON、编码、摘要、HTTP/TLS、压缩、日志等扩展需求或需要判断 `stdx` 是否可用时，同时加载 `cangjie-stdx`，由它完成环境选路。
- 语言语法与核心类型边界以本目录专题文档为权威来源；非核心 API 的精确调用形态、签名和 import 仍以 `cangjie-std` / `cangjie-stdx` 对应专题为准。主文件只保留流程、路由和跨专题闭包，不复制专题中的反模式清单。

## 实现流程

1. 读取目标文件和契约：确认签名、返回类型、注释样例、现有 `package/import`、辅助声明、允许修改范围和可用验证方式。
2. 枚举符合约束的实现路径；比较状态模型、依赖、复杂度和可验证性。若只有一条可行路径，明确排除其它路径的原因。
3. 按下表读取首轮可预见的语言专题，并在构造候选前确认本次会话已有成功的 `cangjie-lang-features` 与 `cangjie-std` Skill 调用；直接读取 Skill 目录文件、计划稍后调用或认为任务只用 `std.core` 都不能替代加载。建立写前收据：最终构造 → 已读专题，非核心符号 → 精确签名/返回类型/副作用/包/import，契约样例 → 期望结果；依赖清单为空也要显式记录。若需求涉及扩展能力，必须在候选中出现任何 `stdx` import 之前加载 `cangjie-stdx` 并完成环境选路。
4. 选择路径并构造完整候选源码，暂不写入目标文件。不要把“lambda”“显式循环”或“局部函数”预设为唯一风格；依据捕获、状态更新、提前退出和返回形状选择。候选源码中新引入一种构造时，按“构造触发重路由”补读专题后再继续构造。
5. 在第一次写入任何 `.cj` 前运行确定性闭包扫描，再完成静态类型复核和样例手算。输入必须由 Agent 先确认为目标文件的完整、非空候选源码，包含保留的 `package/import`、辅助声明和本次实现，不能只传补丁片段或函数体；扫描器只拒绝空输入，不能替 Agent 证明候选完整。固定脚本位于 `.agents/skills/cangjie-lang-features/scripts/check_cangjie_closure.py`，应直接调用该路径，不得用会忽略隐藏目录的 Glob 结果判定脚本不存在。扫描器未实际运行、候选不完整或退出码为 `1`/`2` 都是门禁失败，不得写入；退出码 `0` 无 `warning` 才完成扫描门禁，退出码 `0` 有非阻断 `warning` 时必须逐条按接收者类型和权威专题复核并裁决，不能为消除提示机械改写有文档依据的合法源码。one-shot、single-pass 或只允许一次编辑时，通过后才执行唯一一次目标写入；写后再对目标文件复扫传输结果。不能编译或测试时如实说明验证边界，不能把扫描通过等同于已编译通过。

## 解法路径选择

| 需求形态 | 可选路径 | 选择依据 |
| --- | --- | --- |
| 纯映射、谓词、比较器 | 纯表达式 lambda 或普通函数 | 捕获值是否不可变、签名是否明确、回调是否需要逃逸 |
| 累加、交换、多指针、提前退出 | 显式循环或局部函数 | 是否存在跨步骤状态和控制流 |
| 固定长度或动态结果 | 预分配 `Array`，或由 `cangjie-std` 选择集合/迭代器 | 结果长度是否可先确定、是否需要追加或去重 |
| 字符串处理 | UTF-8 字节、ASCII、Unicode Rune 三类路径 | 契约要求的字符语义，而非输入样例恰好只含 ASCII |
| 扩展能力 | 已配置 stdx、补配置、可验证的源码替代或报告依赖缺口 | 项目配置、修改权限和任务是否必须产出实现 |

## 构造触发重路由

首轮专题选择只覆盖计划中已经出现的构造。写入前列出最终源码实际使用的构造；新增或改写下列任一构造时，必须先读取对应权威专题。已经读取且相关构造未变化时无需重复加载。

| 最终源码出现 | 写入前动作 |
| --- | --- |
| `if`、`while`、局部/顶层声明 | 读取 [基本概念](./basic_concepts/README.md)；涉及 `package`、`import` 或 `main` 时再读 [包机制](./package/README.md) |
| `match`、`case`、`if-let`、`while-let` 或其它模式 | 读取 [基本概念](./basic_concepts/README.md) 与 [模式匹配](./pattern_match/README.md)；涉及 Option 再读 [Option](./option/README.md) |
| lambda、数组初始化函数、map/filter/sort 回调、局部函数 | 读取 [函数与闭包](./function/README.md)，检查捕获和逃逸 |
| 数值极值/转换、String/Rune 构造或字符迭代 | 读取 [基本数据类型](./basic_data_type/README.md)；涉及字符串 API 再读 [String](./string/README.md) |
| Array、动态集合、迭代收集或排序 | 读取 [集合类型](./collections/README.md)，并由 `cangjie-std` 核对所用 API |
| 任一非 `std.core` 符号 | 确认所属包、顶层 import、签名、返回值和副作用；扩展能力再加载 `cangjie-stdx` |

## 源码闭包检查

- **结构闭包**：`package`、`import` 和其它顶层声明顺序合法；新增声明不破坏已有包结构或名称绑定。
- **语法闭包**：使用的控制流、lambda、模式和运算符均能在对应专题中定位；没有从其它语言迁移而来的语法猜测。
- **状态闭包**：参数、`let`、迭代变量和捕获变量的可变性与生命周期一致；闭包是否允许逃逸以 [函数与闭包](./function/README.md) 为准。
- **类型闭包**：操作数、下标、分支、Option 解包和所有可达返回路径的静态类型一致。循环表达式的类型是 `Unit`；不能仅因循环体内存在 `return` 就把尾部循环视为非 `Unit` 函数的返回闭包。递归局部函数若无法由上下文唯一推断返回类型，应显式标注返回类型。
- **依赖闭包**：每个非核心符号都能映射到已确认的包和 import；API 的返回值、副作用与失败模型由 `cangjie-std` 或 `cangjie-stdx` 核对。加载 `cangjie-stdx` 只表示开始环境选路，不是依赖可用证据；未找到匹配项目与目标平台的 `cjpm.toml`/等效配置时，完整候选不得包含无法解析的 `stdx` import，必须选择可复核的 `std.*`/源码替代或在写入前报告依赖阻塞。
- **行为闭包**：为契约中的每条可见样例建立 witness，逐项记录输入、期望输出、候选推演和最终输出，并核对输出形状、顺序、重复项、精度/舍入与哨兵值；再覆盖空输入、单元素、边界值和错误路径。禁止执行验证时，不得用自造样例、静态扫描或主观推断替代契约样例，也不得声称已编译或测试。

首次写入前，将未落盘的完整候选源码传入标准输入。以下 PowerShell 示例中的 `$candidateSource` 必须已经包含完整源码；若 Python 或脚本不可用，应报告门禁未执行，不得把人工目检表述为扫描通过：

```shell
$candidateSource | python .agents/skills/cangjie-lang-features/scripts/check_cangjie_closure.py -
```

参数 `-` 只声明 stdin 模式；绝不能在没有管道或重定向内容时单独运行该命令。扫描器会把空或仅空白 stdin 作为输入错误并返回退出码 `2`，但非空不代表候选完整，完整性仍由第 1、4 步核对。扫描结果为 `ok` 也不能替代写前收据中的专题、依赖、静态类型和样例 witness。

普通任务写入后，或 one-shot 写入完成后需要复核传输结果时，对每个改动后的 `.cj` 文件执行：

```shell
python .agents/skills/cangjie-lang-features/scripts/check_cangjie_closure.py <target.cj>
```

扫描器以退出码 `0` 表示没有阻断 `error`（可以同时报告 `warning`），以 `1` 表示存在可由当前源码证明的 `error`，以 `2` 表示输入失败。`1`/`2` 自动失败；`0` 无 `warning` 表示扫描阶段通过；`0` 有 `warning` 只表示进程不阻断，在逐条结合接收者类型、import、项目配置和权威专题完成裁决前仍不能写入。确认合法时保留源码并继续，不能为消除提示机械改写合法代码。扫描器是保守 linter，不是编译器或完整静态类型证明，仍需人工完成类型与行为闭包。

新增或收紧扫描规则时，只把不依赖隐含类型、跨文件符号或项目配置且能由当前源码证明的可迁移语言不变量标为 `error`；其余规则标为 `warning`。阻断规则至少同时提供非法正例、独立合法反例和边界测试，不能只根据单个 rollout 的变量名、任务数据或表面代码形状建立硬门禁。

## 高频专题路由

| 触发内容 | 必读专题 |
| --- | --- |
| `if`、`while`、顶层结构 | [基本概念](./basic_concepts/README.md)；涉及包、导入或入口再读 [包机制](./package/README.md) |
| `match`、`case`、`if-let`、`while-let`、模式 | [基本概念](./basic_concepts/README.md) 与 [模式匹配](./pattern_match/README.md)；涉及 Option 再读 [Option](./option/README.md) |
| 函数、lambda、闭包、命名参数 | [函数与闭包](./function/README.md) |
| 数值、Rune、String 构造、运算符 | [基本数据类型](./basic_data_type/README.md)；字符串 API 再读 [String](./string/README.md) |
| Option、`?.`、`??`、异常 | [Option](./option/README.md) 与 [错误处理](./error_handle/README.md) |
| `for-in`、迭代器、模式解构 | [for-in](./for/README.md) 与 [模式匹配](./pattern_match/README.md) |
| Array/集合与标准库算法 | [集合类型](./collections/README.md)，并加载 `cangjie-std` |
| package、import、cjpm | [包机制](./package/README.md) 与 [项目管理](./project_management/README.md) |

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
