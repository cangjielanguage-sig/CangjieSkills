## Tuple 模式

Tuple 模式用于 tuple 值的匹配，它的定义和 tuple 字面量类似：`(p_1, p_2, ..., p_n)`，区别在于这里的 `p_1` 到 `p_n`（`n` 大于等于 `2`）是模式（可以是本章节中介绍的任何模式，多个模式间使用逗号分隔）而不是表达式。

例如，`(1, 2, 3)` 是一个包含三个常量模式的 tuple 模式，`(x, y, _)` 是一个包含两个绑定模式，一个通配符模式的 tuple 模式。

给定一个 tuple 值 `tv` 和一个 tuple 模式 `tp`，当且仅当 `tv` 每个位置处的值均能与 `tp` 中对应位置处的模式相匹配，才称 `tp` 能匹配 `tv`。例如，`(1, 2, 3)` 仅可以匹配 tuple 值 `(1, 2, 3)`，`(x, y, _)` 可以匹配任何三元 tuple 值。

下面的例子中，展示了 tuple 模式的使用：

<!-- verify -->

```cangjie
main() {
    let tv = ("Alice", 24)
    let s = match (tv) {
        case ("Bob", age) => "Bob is ${age} years old"
        case ("Alice", age) => "Alice is ${age} years old" // Matched, "Alice" is a constant pattern, and 'age' is a variable pattern.
        case (name, 100) => "${name} is 100 years old"
        case (_, _) => "someone"
    }
    println(s)
}
```

编译执行上述代码，输出结果为：

```text
Alice is 24 years old
```

同一个 tuple 模式中不允许引入多个名称相同的绑定模式。例如，下例中最后一个 `case` 中的 `case (x, x)` 是不合法的。

<!-- compile.error -->

```cangjie
main() {
    let tv = ("Alice", 24)
    let s = match (tv) {
        case ("Bob", age) => "Bob is ${age} years old"
        case ("Alice", age) => "Alice is ${age} years old"
        case (name, 100) => "${name} is 100 years old"
        case (x, x) => "someone" // Error, Cannot introduce a variable pattern with the same name, which will be a redefinition error.
    }
    println(s)
}
```

## 类型模式

类型模式用于判断一个值的运行时类型是否是某个类型的子类型。类型模式有两种形式：`_: Type`（嵌套一个通配符模式 `_`）和 `id: Type`（嵌套一个绑定模式 `id`），它们的区别是后者会发生变量绑定，而前者不会。

对于待匹配值 `v` 和类型模式 `id: Type`（或 `_: Type`），首先判断 `v` 的运行时类型是否是 `Type` 的子类型，若成立则视为匹配成功，否则视为匹配失败；如匹配成功，则将 `v` 的类型转换为 `Type` 并与 `id` 进行绑定（对于 `_: Type`，不存在绑定这一操作）。

假设有如下两个类，`Base` 和 `Derived`，并且 `Derived` 是 `Base` 的子类，`Base` 的无参构造函数中将 `a` 的值设置为 `10`，`Derived` 的无参构造函数中将 `a` 的值设置为 `20`：

<!-- verify -mergeCase -->

```cangjie
open class Base {
    var a: Int64
    public init() {
        a = 10
    }
}

class Derived <: Base {
    public init() {
        a = 20
    }
}
```

下面的代码展示了使用类型模式并匹配成功的例子：

<!-- verify -mergeCase -->

```cangjie
func test1() {
    var d = Derived()
    var r = match (d) {
        case b: Base => b.a // Matched.
        case _ => 0
    }
    println("r = ${r}")
}
```

下面的代码展示了使用类型模式但类型模式匹配失败的例子：

<!-- verify -mergeCase -->

```cangjie
func test2() {
    var b = Base()
    var r = match (b) {
        case d: Derived => d.a  // Type pattern match failed.
        case _ => 0             // Matched.
    }
    println("r = ${r}")
}
```

<!-- verify -mergeCase -->

```cangjie
main() {
    test1()
    test2()
}
```

编译执行上述代码，输出结果为（第一行为 test1 的输出结果，第二行则是 test2 的输出结果）：

<!-- verify -mergeCase -->

```text
r = 20
r = 0
```