## 一个简单的 DSL

这个案例展示了如何使用宏实现一个简单的 DSL（Domain Specific Language，领域特定语言）。LINQ（Language Integrated Query，语言集成查询）是微软 .NET 框架的一个组成部分，它提供了一种统一的数据查询语法，允许开发者使用类似 SQL 的查询语句来操作各种数据源。在这里，仅展示一个最简单的 LINQ 语法的支持。

希望支持的语法为：

```text
from <variable> in <list> where <condition> select <expression>
```

其中，`variable` 是一个标识符，`list`、`condition` 和 `expression` 都是表达式。因此，实现宏的策略是先后提取标识符和表达式，同时检查中间的关键字是正确的。最后，生成由提取部分组成的查询结果。

宏的实现如下：

<!-- verify -macro16 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package define

import std.ast.*

public macro linq(input: Tokens) {
    let syntaxMsg = "Syntax is \"from <attrib> in <table> where <cond> select <expr>\""
    if (input.size == 0 || input[0].value != "from") {
        diagReport(DiagReportLevel.ERROR, input[0..1], syntaxMsg,
                   "Expected keyword \"from\" here.")
    }
    if (input.size <= 1 || input[1].kind != TokenKind.IDENTIFIER) {
        diagReport(DiagReportLevel.ERROR, input[1..2], syntaxMsg,
                   "Expected identifier here.")
    }
    let attribute = input[1]
    if (input.size <= 2 || input[2].value != "in") {
        diagReport(DiagReportLevel.ERROR, input[2..3], syntaxMsg,
                   "Expected keyword \"in\" here.")
    }
    var index: Int64 = 3
    let (table, nextIndex) = parseExprFragment(input, startFrom: index)
    if (nextIndex == input.size || input[nextIndex].value != "where") {
        diagReport(DiagReportLevel.ERROR, input[nextIndex..nextIndex+1], syntaxMsg,
                   "Expected keyword \"where\" here.")
    }
    index = nextIndex + 1  // 跳过where
    let (cond, nextIndex2) = parseExprFragment(input, startFrom: index)
    if (nextIndex2 == input.size || input[nextIndex2].value != "select") {
        diagReport(DiagReportLevel.ERROR, input[nextIndex2..nextIndex2+1], syntaxMsg,
                   "Expected keyword \"select\" here.")
    }
    index = nextIndex2 + 1  // 跳过select
    let (expr, nextIndex3) = parseExprFragment(input, startFrom: index)

    return quote(
        for ($(attribute) in $(table)) {
            if ($(cond)) {
                println($(expr))
            }
        }
    )
}
```

使用案例：

<!-- verify -macro16 -->
<!-- cfg="--debug-macro" -->

```cangjie
import define.*

main() {
    @linq(from x in 1..=10 where x % 2 == 1 select x * x)
}
```

这个例子从 1, 2, ... 10 列表中筛选出奇数，然后返回所有奇数的平方。输出结果为：

<!-- verify -macro16 -->

```text
1
9
25
49
81
```

可以看到，宏的实现的很大部分用于解析并校验输入的 Tokens，这对宏的可用性至关重要。实际的 LINQ 语言（以及大多数 DSL）的语法更加复杂，需要一整套解析的机制，通过识别不同的关键字或连接符来决定下一步解析的内容。