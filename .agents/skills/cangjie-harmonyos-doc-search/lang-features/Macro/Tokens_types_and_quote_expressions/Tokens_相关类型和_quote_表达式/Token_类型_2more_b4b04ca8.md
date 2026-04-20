## Token 类型

宏操作的基本类型是 `Tokens`，代表一个程序片段。`Tokens` 由若干个 `Token` 组成，每个 `Token` 可以理解为用户可操作的词法单元。一个 `Token` 可能是一个标识符（例如变量名等）、字面量（例如整数、浮点数、字符串）、关键字或运算符。每个 `Token` 包含它的类型、内容和位置信息。

`Token` 的类型取值为 enum `TokenKind` 中的元素。`TokenKind` 的可用值详见《仓颉编程语言库 API》文档。通过提供 `TokenKind` 和 `Token` 的值（`TokenKind` 对应的标识符或字面量），可以直接构造任何 `Token`。具体的构造函数如下：

<!-- code_no_check -->

```cangjie
Token(k: TokenKind)
Token(k: TokenKind, v: String)
```

下面给出一些`Token`构造的例子：

<!-- compile -->

```cangjie
import std.ast.*

let tk1 = Token(TokenKind.ADD)   // '+' 运算符
let tk2 = Token(TokenKind.FUNC)   // func 关键字
let tk3 = Token(TokenKind.IDENTIFIER, "x")   // x 标识符
let tk4 = Token(TokenKind.INTEGER_LITERAL, "3")  // 整数字面量
let tk5 = Token(TokenKind.STRING_LITERAL, "xyz")  // 字符串字面量
```

## Tokens 类型

一个 `Tokens` 代表由多个 `Token` 组成的序列。可以通过 `Token` 数组直接构造 `Tokens`。下面是 3 种基本的构造 `Tokens` 实例的方式：

<!-- code_no_check -->

```cangjie
Tokens()   // 构造空列表
Tokens(tks: Array<Token>)
Tokens(tks: ArrayList<Token>)
```

此外，`Tokens` 类型支持以下功能：

- `size`：返回 `Tokens` 中包含 `Token` 的数量
- `get(index: Int64)`：获取指定下标的 `Token` 元素
- `[]`：获取指定下标的 `Token` 元素
- `+`：拼接两个 `Tokens`，或者直接拼接 `Tokens` 和 `Token`
- `dump()`：打印包含的所有 `Token`，供调试使用
- `toString()`：打印 `Tokens` 对应的程序片段

在下面的案例中，使用构造函数直接构造 `Token` 和 `Tokens`，然后打印详细的调试信息：

<!-- run -->

```cangjie
import std.ast.*

let tks = Tokens([
    Token(TokenKind.INTEGER_LITERAL, "1"),
    Token(TokenKind.ADD),
    Token(TokenKind.INTEGER_LITERAL, "2")
])
main() {
    println(tks)
    tks.dump()
}
```

预期输出如下（具体的位置信息可能不同）：

```text
1 + 2
description: integer_literal, token_id: 140, token_literal_value: 1, fileID: 1, line: 4, column: 5
description: add, token_id: 12, token_literal_value: +, fileID: 1, line: 5, column: 5
description: integer_literal, token_id: 140, token_literal_value: 2, fileID: 1, line: 6, column: 5
```

在 dump 信息中，包含了每个 `Token` 的类型（`description`）和值（`token_literal_value`），最后打印每个 `Token` 的位置信息。