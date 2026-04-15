## quote 表达式和插值

在大多数情况下，直接构造和拼接 `Tokens` 会比较繁琐。因此，仓颉语言提供了 `quote` 表达式来从代码模板构造 `Tokens`。之所以说是代码模板，因为在 `quote` 中可以使用 `$(...)` 来插入上下文中的表达式。插入的表达式的类型需要支持被转换为 `Tokens`（具体来说，实现了 `ToTokens` 接口）。在标准库中，以下类型实现了 `ToTokens` 接口：

- 所有的节点类型（节点将在[语法节点](./syntax_node.md)中讨论）
- `Token` 和 `Tokens` 类型
- 所有基础数据类型：整数、浮点数、`Bool`、`Rune` 和 `String`
- `Array<T>` 和 `ArrayList<T>`，这里对 `T` 的类型有限制，并根据 `T` 的类型不同，输出不同的分隔符，详细请见《仓颉编程语言库 API》文档。

下面的例子展示 `Array` 和基础数据类型的插值：

<!-- verify -->

```cangjie
import std.ast.*

let intList: Array<Int64> = [1, 2, 3, 4, 5]
let float: Float64 = 1.0
let str: String = "Hello"
let tokens = quote(
    arr = $(intList)
    x = $(float)
    s = $(str)
)

main() {
    println(tokens)
}
```

输出结果是：

```text

arr =[1, 2, 3, 4, 5]
x = 1.0
s = "Hello"

```

更多插值的用法可以参考  [使用 quote 插值语法节点](./syntax_node.md#使用-quote-插值语法节点)。

特别地，当 `quote` 表达式包含某些特殊 `Token` 时，需要进行转义：

- `quote` 表达式中不允许出现不匹配的小括号，但是通过 `\` 转义的小括号，不计入小括号的匹配规则。
- 当 `$` 表示一个普通 `Token`，而非用于代码插值时，需要通过 `\` 进行转义。
- 除以上情况外，`quote` 表达式中出现 `\` 会编译报错。

> **注意：**
>
> `#` 符号仅能用于构造多行原始字符串字面量，不支持单独使用。

下面是一些 `quote` 表达式内包含这些特殊 `Token` 的例子：

<!-- compile.error -->

```cangjie
import std.ast.*

let tks1 = quote((x))       // ok
let tks2 = quote(\()        // ok
let tks3 = quote( ( \) ) )  // ok
let tks4 = quote())         // error: unmatched delimiter: ')'
let tks5 = quote( ( \) )    // error: unclosed delimiter: '('
let tks6 = quote(\$(1))     // ok
let tks7 = quote(\x)        // error: unknown start of token: \
let tks8 = quote(#)         // error: expected '#' or '"' in raw string
```