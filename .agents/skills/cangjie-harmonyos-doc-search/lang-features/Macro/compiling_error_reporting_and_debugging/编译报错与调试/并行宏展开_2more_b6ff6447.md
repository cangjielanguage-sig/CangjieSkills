## 并行宏展开

可以在编译宏调用文件时添加 `--parallel-macro-expansion` 选项，启用并行宏展开的能力。编译器会自动分析宏调用之间的依赖关系，无依赖关系的宏调用可以并行执行，如上述例子中的两个 `@Inner` 就可以并行展开，如此可以缩短整体编译时间。

> **注意：**
>
> 如果宏函数依赖一些全局变量，使用并行宏展开会存在风险。

<!-- compile -macro1 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package define
import std.ast.*
import std.collection.HashMap

var Counts = HashMap<String, Int64>()

public macro Inner(input: Tokens) {
    for (t in input) {
        if (t.value.size == 0) {
            continue
        }
        // 统计所有有效token value的出现次数
        if (!Counts.contains(t.value)) {
            Counts[t.value] = 0
        }
        Counts[t.value] = Counts[t.value] + 1
    }
    return input
}

public macro B(input: Tokens) {
    return input
}
```

参考上述代码，如果 `@Inner` 的宏调用出现在多处，并且启用了并行宏展开选项，则访问全局变量 `Counts` 就可能存在冲突，导致最后获取的结果不正确。

建议不要在宏函数中使用全局变量，如果必须使用，要么关闭并行宏展开选项，或者可以通过仓颉线程锁对全局变量进行保护。

## diagReport 报错机制

仓颉标准库 `std.ast` 包提供了自定义报错接口 `diagReport`。方便定义宏的用户，在解析传入 Tokens 时，对错误 Tokens 内容进行自定义报错。

自定义报错接口提供同原生编译器报错一样的输出格式，允许用户报 warning 和 error 两类错误提示信息。

`diagReport` 的函数原型如下：

<!-- code_no_check -->

```cangjie
public func diagReport(level: DiagReportLevel, tokens: Tokens, message: String, hint: String): Unit
```

其参数含义如下：

- level: 报错信息等级
- tokens: 报错信息中所引用源码内容对应的 Tokens
- message: 报错的主信息
- hint: 辅助提示信息

参考如下使用示例。

宏定义文件：

<!-- compile.error -macro2 -->
<!-- cfg="--compile-macro" -->

```cangjie
// macro_definition.cj
macro package macro_definition

import std.ast.*

public macro testDef(input: Tokens): Tokens {
    for (i in 0..input.size) {
        if (input[i].kind == IDENTIFIER) {
            diagReport(DiagReportLevel.ERROR, input[i..(i + 1)],
                       "This expression is not allowed to contain identifier",
                       "Here is the illegal identifier")
        }
    }
    return input
}
```

宏调用文件：

<!-- compile.error -macro2 -->

```cangjie
// macro_call.cj
package macro_calling

import std.ast.*
import macro_definition.*

main(): Int64 {
    let a = @testDef(1)
    let b = @testDef(a)
    let c = @testDef(1 + a)
    return 0
}
```

编译宏调用文件过程中，会出现如下报错信息：

```text
error: This expression is not allowed to contain identifier
 ==> call.cj:9:22:
  |
9 |     let b = @testDef(a)
  |                      ^ Here is the illegal identifier
  |

error: This expression is not allowed to contain identifier
  ==> call.cj:10:26:
   |
10 |     let c = @testDef(1 + a)
   |                          ^ Here is the illegal identifier
   |

2 errors generated, 2 errors printed.
```