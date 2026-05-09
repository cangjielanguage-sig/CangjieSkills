### 涉及 “let pattern” 的“条件”示例

“let pattern” 属于语法糖。一个 “let pattern” 的构成为 `let pattern <- expression`，其中各字段含义为：

- `pattern` ：模式，用于匹配 `expression` 的值类型和内容。
- `<-` ：模式匹配操作符。
- `expression` ：表达式，该表达式求值后，再和模式进行匹配。`expression` 表达式的优先级不能低于 `..` 运算符，但是可以用 `()` 改变优先级。运算符优先级请参见[操作符](../Appendix/operator.md)。

此处介绍“条件”是两个 “let pattern” 进行逻辑与或逻辑或操作以及 “let pattern” 与其他表达式进行逻辑与或逻辑或操作的示例。

<!-- run -expression_example5 -->

```cangjie
main() {
    let a = Some(3)
    let c = if (let Some(b) <- a) {
            1 // 模式匹配成功，c = 1
        } else {
            2
        }
    let d = Some(1)

    if (let Some(e) <- a && let Some(f) <- d) { // 两种模式都匹配，条件的值为真
        println("${e} ${f}") // print 3 1
    }

    if (let Some(f) <- d && f > 3) { // 模式匹配；f = 1，f > 3 检查失败，跳转到 else 分支
        println("${f}")
    } else {
        println("d is None or value of d is less or equal to 3") // 打印该行
    }

    if (let Some(_) <- a || let Some(_) <- d) { // 枚举模式通过||连接，没有变量绑定，正确
        println("at least one of a and d is Some") // 打印该行
    } else {
        println("both a and d are None")
    }

    let g = 3
    if (let Some(_) <- a || g > 1) {
        println("this") // 打印该行
    } else {
        println("that")
    }
}
```

“let pattern” 中表达式部分运算符优先级不能低于 `..` 运算符，此处介绍对应的错误和正确示例。其中， [`Option` 类型](../enum_and_pattern_match/option_type.md)的相关介绍在后文给出。

<!-- compile.error -->

```cangjie
if (let Some(a) <- fun() as Option<Int64>) {}   // 解析错误，`as` 的优先级低于  `..`
if (let Some(a) <- (fun() as Option<Int64>)) {} // 正确
if (let Some(a) <- b && a + b > 3) {}           // 正确，解析为 (let Some(a) <- b) && (a + b > 3)
if (let m <- 0..generateSomeInt()) {}           // 正确
```

### 错误的表达式示例

此处介绍错误的“条件”示例。

<!-- compile.error -->

```cangjie
if (let Some(a) <- b || a > 1) {} // 由 `||` 连接的条件不能使用会绑定变量的 enum 模式
if (let Some(a) <- b && a + 1) {} // `&&` 右侧既不是 let pattern，也不是类型为 Bool 的普通表达式
if (a > 3 && let Some(a) <- b) {} // a 由 Some(a) pattern 绑定，不能在绑定它的 pattern 左侧使用
if (let Some(a) <- b && a > 3) {
    println("${a} > 3")
} else {
    println("${a} < 3") // a 只能在 if 分支使用，不能在 else 分支使用
}
if (let Some(a) <- b where a > 3) {} // 使用 `&&` 表示条件检查，而不是 `where`
```