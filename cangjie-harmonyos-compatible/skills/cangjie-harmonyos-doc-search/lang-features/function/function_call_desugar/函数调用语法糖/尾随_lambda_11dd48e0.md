## 尾随 lambda

尾随 lambda 可以使函数的调用看起来像是语言内置的语法一样，增加语言的可扩展性。

当函数最后一个形参是函数类型，并且函数调用对应的实参是 lambda 时，可以使用尾随 lambda 语法，将 lambda 放在函数调用的尾部，圆括号外面。

例如，下例中定义了一个 `myIf` 函数，它的第一个参数是 `Bool` 类型，第二个参数是函数类型。当第一个参数的值为 `true` 时，返回第二个参数调用后的值，否则返回 `0`。调用 `myIf` 时可以像普通函数一样调用，也可以使用尾随 lambda 的方式调用。

<!-- compile -->

```cangjie
func myIf(a: Bool, fn: () -> Int64) {
    if(a) {
        fn()
    } else {
        0
    }
}

func test() {
    myIf(true, { => 100 }) // General function call

    myIf(true) {        // Trailing closure call
        100
    }
}
```

当函数调用有且只有一个 lambda 实参时，还可以省略 `()`，只写 lambda。

示例：

<!-- compile -->

```cangjie
func f(fn: (Int64) -> Int64) { fn(1) }

func test() {
    f { i => i * i }
}
```