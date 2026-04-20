## 一个 dprint 宏的扩展

本节一开始使用了一个打印表达式的宏作为案例，但这个宏一次只能接受一个表达式。希望扩展这个宏，使其能够接受多个表达式，由逗号分开。下面展示如何使用 `parseExprFragment` 来实现这个功能。

宏的实现如下：

<!-- verify -macro15 -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package define

import std.ast.*

public macro dprint2(input: Tokens) {
    let exprs = ArrayList<Expr>()
    var index: Int64 = 0
    while (true) {
        let (expr, nextIndex) = parseExprFragment(input, startFrom: index)
        exprs.add(expr)
        if (nextIndex == input.size) {
            break
        }
        if (input[nextIndex].kind != TokenKind.COMMA) {
            diagReport(DiagReportLevel.ERROR, input[nextIndex..nextIndex+1],
                       "Input must be a comma-separated list of expressions",
                       "Expected comma")
        }
        index = nextIndex + 1  // 跳过逗号
    }
    let result = quote()
    for (expr in exprs) {
        result.append(quote(
            print($(expr.toTokens().toString()) + " = ")
            println($(expr))
        ))
    }
    return result
}
```

使用案例：

<!-- verify -macro15 -->
<!-- cfg="--debug-macro" -->

```cangjie
import define.*

main() {
    let x = 3
    let y = 2
    @dprint2(x, y, x + y)
}
```

输出结果为：

<!-- verify -macro15 -->

```text
x = 3
y = 2
x + y = 5
```

在宏的实现中，使用 while 循环从索引 0 开始依次解析每个表达式。变量 `index` 保存当前解析的位置。每次调用 `parseExprFragment` 时，从当前位置开始，并返回解析后的位置（以及解析得到的表达式）。如果解析后的位置到达了输入的结尾，则退出循环。否则检查到达的位置是否是一个逗号，如果不是逗号，报错并退出，如果是逗号，跳过这个逗号并开始下一轮的解析。在得到表达式的列表后，依次输出每个表达式。