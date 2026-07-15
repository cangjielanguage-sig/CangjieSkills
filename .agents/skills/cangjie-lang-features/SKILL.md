---
name: cangjie-lang-features
description: "Use when generating or editing any Cangjie .cj file, filling a TODO/function skeleton, or answering one-shot/single-pass implementation requests involving func, let/var, control flow, Array, String/Rune, Option, match, lambda, ranges, packages/imports, or compile errors. This Skill must be invoked before the first .cj write. Pair every .cj generation/edit with cangjie-std; add cangjie-stdx before choosing any extension-library path."
---

# 仓颉编程语言特性目录

## 职责与协作

- 本 Skill 负责语言层语义：顶层结构、控制流、类型、绑定与可变性、函数/闭包、String/Rune、Option、包与 import 语法。
- 生成或修改 `.cj` 时同步使用 `cangjie-std` 核对标准库 API；出现 JSON、编码、摘要、HTTP/TLS、压缩、日志等扩展需求或需要判断 `stdx` 是否可用时，同时加载 `cangjie-stdx`，由它完成环境选路。
- 具体语法和边界以本目录专题文档为权威来源；主文件只保留流程、路由和跨专题闭包，不复制专题中的反模式清单。

## 实现流程

1. 读取目标文件和契约：确认签名、返回类型、注释样例、现有 `package/import`、辅助声明、允许修改范围和可用验证方式。
2. 枚举符合约束的实现路径；比较状态模型、依赖、复杂度和可验证性。若只有一条可行路径，明确排除其它路径的原因。
3. 按下表读取首轮可预见的语言专题，并在构造候选前加载 `cangjie-std`，形成非核心符号、精确签名、返回类型、副作用与 import 的依赖清单；即使最终清单为空也要完成核对。若需求涉及扩展能力，必须在候选中出现任何 `stdx` import 之前加载 `cangjie-stdx` 并完成环境选路。
4. 选择路径并构造完整候选源码，暂不写入目标文件。不要把“lambda”“显式循环”或“局部函数”预设为唯一风格；依据捕获、状态更新、提前退出和返回形状选择。候选源码中新引入一种构造时，按“构造触发重路由”补读专题后再继续构造。
5. 在第一次写入任何 `.cj` 前运行确定性闭包扫描，再完成静态类型复核和样例手算。输入必须是目标文件的完整、非空候选源码，包含保留的 `package/import`、辅助声明和本次实现，不能只传补丁片段或函数体。扫描器未实际运行、输入为空/仅空白、候选不完整或退出码非 `0` 都是门禁失败，不得写入；在未落盘候选上修正并重扫。one-shot、single-pass 或只允许一次编辑时，通过后才执行唯一一次目标写入；写后再对目标文件复扫传输结果。不能编译或测试时如实说明验证边界，不能把“未发现扫描项”等同于已编译通过。

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
- **类型闭包**：操作数、下标、分支、Option 解包和所有可达返回路径的静态类型一致。
- **依赖闭包**：每个非核心符号都能映射到已确认的包和 import；API 的返回值、副作用与失败模型由 `cangjie-std` 或 `cangjie-stdx` 核对。加载 `cangjie-stdx` 只表示开始环境选路，不是依赖可用证据；未找到匹配项目与目标平台的 `cjpm.toml`/等效配置时，完整候选不得包含无法解析的 `stdx` import，必须选择可复核的 `std.*`/源码替代或在写入前报告依赖阻塞。
- **行为闭包**：用契约样例覆盖空输入、单元素、边界值和错误路径；验证不可用时不声称已编译或测试。

若环境可运行 Python，one-shot 或只允许一次编辑时，先将未落盘的完整候选源码传入标准输入。以下 PowerShell 示例中的 `$candidateSource` 必须已经包含完整源码：

```shell
$candidateSource | python .opencode/skills/cangjie-lang-features/scripts/check_cangjie_closure.py -
```

参数 `-` 只声明 stdin 模式；绝不能在没有管道或重定向内容时单独运行该命令。扫描器会把空或仅空白 stdin 作为输入错误并返回退出码 `2`。

普通任务写入后，或 one-shot 写入完成后需要复核传输结果时，对每个改动后的 `.cj` 文件执行：

```shell
python .opencode/skills/cangjie-lang-features/scripts/check_cangjie_closure.py <target.cj>
```

扫描器以退出码 `0` 表示未发现规则命中，以 `1` 表示存在 finding，以 `2` 表示输入失败；后两者都不能通过写入门禁。扫描器负责可确定识别的结构、控制流、常见跨语言 API 猜测和可变捕获风险；每条报告都必须通过修改候选源码或查阅其指向的权威专题解决。扫描器不能推导完整静态类型和业务契约，仍需人工完成类型与行为闭包。

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
