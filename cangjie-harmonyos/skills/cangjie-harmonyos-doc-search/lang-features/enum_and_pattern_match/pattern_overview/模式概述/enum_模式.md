## enum 模式

enum 模式用于匹配 `enum` 类型的实例，它的定义和 `enum` 的构造器类似：无参构造器 `C` 或有参构造器 `C(p_1, p_2, ..., p_n)`，构造器的类型前缀可以省略，区别在于这里的 `p_1` 到 `p_n`（`n` 大于等于 `1`）是模式。例如，`Some(1)` 是一个包含一个常量模式的 enum 模式，`Some(x)` 是一个包含一个绑定模式的 enum 模式。

给定一个 enum 实例 `ev` 和一个 enum 模式 `ep`，当且仅当 `ev` 的构造器名字和 `ep` 的构造器名字相同，且 `ev` 参数列表中每个位置处的值均能与 `ep` 中对应位置处的模式相匹配，才称 `ep` 能匹配 `ev`。例如，`Some("one")` 仅可以匹配 `Option<String>` 类型的`Some` 构造器 `Option<String>.Some("one")`，`Some(x)` 可以匹配任何 Option 类型的 `Some` 构造器。

下面的例子中，展示了 enum 模式的使用，因为 `x` 的构造器是 `Year`，所以会和第一个 `case` 匹配：

<!-- verify -->

```cangjie
enum TimeUnit {
    | Year(UInt64)
    | Month(UInt64)
}

main() {
    let x = Year(2)
    let s = match (x) {
        case Year(n) => "x has ${n * 12} months" // Matched.
        case TimeUnit.Month(n) => "x has ${n} months"
    }
    println(s)
}
```

编译执行上述代码，输出结果为：

```text
x has 24 months
```

当使用 `|` 连接多个 enum 模式时，每个模式必须独立且不能引入新的变量。这是因为 `|` 表示“或”的关系，而变量的引入需要明确的上下文，不能在多个模式之间共享。下面示例为反例示范，其中第五、六个 `case` 不符合该条规则：

<!-- compile.error -->

```cangjie
enum TimeUnit {
    | Year(UInt64)
    | Month(UInt64)
}

main() {
    let x = Year(2)
    let s = match (x) {
        case Year(5) => "1:OK"
        case Month(m) => "2:OK"
        case Year(0) | Year(1) | Month(_) => "3:OK"
        case Year(_) => "4:OK"
        case Year(2) | Month(m) => "5:invalid" // Error, Variable cannot be introduced in patterns connected by '|'
        case Year(n: UInt64) | Month(n: UInt64) => "6:invalid" // Error, Variable cannot be introduced in patterns connected by '|'
    }
    println(s)
}
```

上述示例中，第二个 `case` 引入了一个新变量 `m`，但没有使用 `|` 连接其他模式，故此是合法的。

使用 `match` 表达式匹配 `enum` 值时，要求 `case` 之后的模式要覆盖待匹配 `enum` 类型中的所有构造器，如果未做到完全覆盖，编译器将报错：

<!-- compile.error -->

```cangjie
enum RGBColor {
    | Red | Green | Blue
}

main() {
    let c = Green
    let cs = match (c) { // Error, Not all constructors of RGBColor are covered.
        case Red => "Red"
        case Green => "Green"
    }
    println(cs)
}
```

可以通过加上 `case Blue` 来实现完全覆盖，也可以在 `match` 表达式的最后通过使用 `case _` 来覆盖其他 `case` 未覆盖的到的情况，如：

<!-- verify -->

```cangjie
enum RGBColor {
    | Red | Green | Blue
}

main() {
    let c = Blue
    let cs = match (c) {
        case Red => "Red"
        case Green => "Green"
        case _ => "Other" // Matched.
    }
    println(cs)
}
```

上述代码的执行结果为：

```text
Other
```