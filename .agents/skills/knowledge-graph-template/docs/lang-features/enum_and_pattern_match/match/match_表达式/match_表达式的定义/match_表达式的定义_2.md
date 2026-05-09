```cangjie
enum RGBColor {
    | Red(Int16) | Green(Int16) | Blue(Int16)
}
main() {
    let c = RGBColor.Green(-100)
    let cs = match (c) {
        case Red(r) where r < 0 => "Red = 0"
        case Red(r) => "Red = ${r}"
        case Green(g) where g < 0 => "Green = 0" // Matched.
        case Green(g) => "Green = ${g}"
        case Blue(b) where b < 0 => "Blue = 0"
        case Blue(b) => "Blue = ${b}"
    }
    print(cs)
}
```

编译执行上述代码，输出结果为：

```text
Green = 0
```

**没有匹配值的 match 表达式**：

<!-- verify -->

```cangjie
main() {
    let x = -1
    match {
        case x > 0 => print("x > 0")
        case x < 0 => print("x < 0") // Matched.
        case _ => print("x = 0")
    }
}
```

与包含待匹配值的 `match` 表达式相比，关键字 `match` 之后并没有待匹配的表达式，并且 `case` 之后不再是 `pattern`，而是类型为 `Bool` 的表达式（上述代码中的 `x > 0` 和 `x < 0`）或者 `_`（表示 `true`），当然，`case` 中也不再有 `pattern guard`。

无匹配值的 `match` 表达式执行时依次判断 `case` 之后的表达式的值，直到遇到值为 `true` 的 `case` 分支；一旦某个 `case` 之后的表达式值等于 `true`，则执行此 `case` 中 `=>` 之后的代码，然后退出 `match` 表达式的执行（意味着不会再去判断该 `case` 之后的其他 `case`）。

上例中，因为 `x` 的值等于 `-1`，所以第二条 `case` 分支中的表达式（即 `x < 0`）的值等于 `true`，执行 `print("x < 0")`。

编译并执行上述代码，输出结果为：

```text
x < 0
```