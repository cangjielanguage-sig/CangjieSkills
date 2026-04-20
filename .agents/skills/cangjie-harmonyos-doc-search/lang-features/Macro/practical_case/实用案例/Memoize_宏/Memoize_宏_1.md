## Memoize 宏

Memoize（记忆化）是动态规划算法的常用手段。它将已经计算过的子问题的结果存储起来，当同一个子问题再次出现时，可以直接查询表来获取结果，从而避免重复的计算，提高算法的效率。

通常 Memoize 的使用需要开发者手动实现存储和提取的功能。通过宏，可以自动化这一过程。宏的效果如下：

<!-- code_no_check -->

```cangjie
@Memoize[true]
func fib(n: Int64): Int64 {
    if (n == 0 || n == 1) {
        return n
    }
    return fib(n - 1) + fib(n - 2)
}

main() {
    let start = DateTime.now()
    let f35 = fib(35)
    let end = DateTime.now()
    println("fib(35): ${f35}")
    println("execution time: ${(end - start).toMicroseconds()} us")
}
```

在以上代码中，`fib` 函数采用简单的递归方式实现。如果没有 `@Memoize[true]` 标注，这个函数的运行时间将随着 `n` 指数增长。例如，如果在前面的代码中去掉 `@Memoize[true]` 这一行，或者把 `true` 改为 `false`，则 `main` 函数的运行结果为：

```text
fib(35): 9227465
execution time: 199500 us
```

恢复 `@Memoize[true]`，运行结果为：

```text
fib(35): 9227465
execution time: 78 us
```

相同的答案和大幅缩短的计算时间表明，`@Memoize` 的使用确实实现了记忆化。

为了理解 `@Memoize` 的原理，展示对以上 `fib` 函数进行宏展开的结果（来自 `.macrocall` 文件，但是为了提高可读性整理了格式）。

<!-- run -->

```cangjie
import std.collection.*

var memoizeFibMap = HashMap<Int64, Int64>()

func fib(n: Int64): Int64 {
    if (memoizeFibMap.contains(n)) {
        return memoizeFibMap.get(n).getOrThrow()
    }

    let memoizeEvalResult = { =>
        if (n == 0 || n == 1) {
            return n
        }

        return fib(n - 1) + fib(n - 2)
    }()
    memoizeFibMap.add(n, memoizeEvalResult)
    return memoizeEvalResult
}
```

上述代码的执行流程如下：

- 首先，定义 `memoizeFibMap` 为一个从 `Int64` 到 `Int64` 的哈希表，这里第一个 `Int64` 对应 `fib` 的唯一参数的类型，第二个 `Int64` 对应 `fib` 返回值的类型。
- 其次，在函数体中，检查入参是否在 `memoizeFibMap` 中，如果是则立即反馈哈希表中存储的值。否则，使用 `fib` 原来的函数体得到计算结果。这里使用了（不带参数的）匿名函数使 `fib` 的函数体不需要任何改变，并且能够处理任何从 `fib` 函数退出的方式（包括中间的 return，返回最后一个表达式等）。
- 最后，把计算结果存储到 `memoizeFibMap` 中，然后将计算结果返回。

有了这样一个“模板”之后，下面宏的实现就不难理解了。完整的代码如下。

<!-- compile -->
<!-- cfg="--compile-macro" -->

```cangjie
macro package define

import std.ast.*

public macro Memoize(attrib: Tokens, input: Tokens) {
    if (attrib.size != 1 || attrib[0].kind != TokenKind.BOOL_LITERAL) {
        diagReport(DiagReportLevel.ERROR, attrib,
                   "Attribute must be a boolean literal (true or false)",
                   "Expected boolean literal (true or false) here")
    }

    let memoized = (attrib[0].value == "true")
    if (!memoized) {
        return input
    }

    let fd = FuncDecl(input)
    if (fd.funcParams.size != 1) {
        diagReport(DiagReportLevel.ERROR, fd.lParen + fd.funcParams.toTokens() + fd.rParen,
                   "Input function to memoize should take exactly one argument",
                   "Expect only one argument here")
    }

    let memoMap = Token(TokenKind.IDENTIFIER, "_memoize_" + fd.identifier.value + "_map")
    let arg1 = fd.funcParams[0]

    return quote(
        var $(memoMap) = HashMap<$(arg1.paramType), $(fd.declType)>()

        func $(fd.identifier)($(arg1)): $(fd.declType) {
            if ($(memoMap).contains($(arg1.identifier))) {
                return $(memoMap).get($(arg1.identifier)).getOrThrow()
            }

            let memoizeEvalResult = { => $(fd.block.nodes) }()
            $(memoMap).add($(arg1.identifier), memoizeEvalResult)
            return memoizeEvalResult
        }
    )
}
```