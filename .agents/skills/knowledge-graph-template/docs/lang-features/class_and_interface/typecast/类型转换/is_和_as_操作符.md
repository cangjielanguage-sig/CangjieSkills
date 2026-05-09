## `is` 和 `as` 操作符

仓颉支持使用 `is` 操作符来判断某个表达式的类型是否是指定的类型（或其子类型）。具体而言，对于表达式 `e is T`（`e` 可以是任意表达式，`T` 可以是任何类型），当 `e` 的运行时类型是 `T` 的子类型时，`e is T` 的值为 `true`，否则 `e is T` 的值为 `false`。

下面的例子展示了 `is` 操作符的使用：

<!-- verify -->

```cangjie
open class Base {
    var name: String = "Alice"
}
class Derived <: Base {
    var age: UInt8 = 18
}

main() {
    let a = 1 is Int64
    println("Is the type of 1 'Int64'? ${a}")
    let b = 1 is String
    println("Is the type of 1 'String'? ${b}")

    let b1: Base = Base()
    let b2: Base = Derived()
    var x = b1 is Base
    println("Is the type of b1 'Base'? ${x}")
    x = b1 is Derived
    println("Is the type of b1 'Derived'? ${x}")
    x = b2 is Base
    println("Is the type of b2 'Base'? ${x}")
    x = b2 is Derived
    println("Is the type of b2 'Derived'? ${x}")
}
```

上述代码的执行结果为：

```text
Is the type of 1 'Int64'? true
Is the type of 1 'String'? false
Is the type of b1 'Base'? true
Is the type of b1 'Derived'? false
Is the type of b2 'Base'? true
Is the type of b2 'Derived'? true
```

`as` 操作符可以用于将某个表达式的类型转换为指定的类型。因为类型转换有可能会失败，所以 `as` 操作返回的是一个 `Option` 类型。具体而言，对于表达式 `e as T`（`e` 可以是任意表达式，`T` 可以是任何类型），当 `e` 的运行时类型是 `T` 的子类型时，`e as T` 的值为 `Option<T>.Some(e)`，否则 `e as T` 的值为 `Option<T>.None`。

下面的例子展示了 `as` 操作符的使用（注释中标明了 `as` 操作的结果）：

<!-- compile -->

```cangjie
open class Base {
    var name: String = "Alice"
}
class Derived <: Base {
    var age: UInt8 = 18
}

let a = 1 as Int64     // a = Option<Int64>.Some(1)
let b = 1 as String    // b = Option<String>.None

let b1: Base = Base()
let b2: Base = Derived()
let d: Derived = Derived()
let r1 = b1 as Base    // r1 = Option<Base>.Some(b1)
let r2 = b1 as Derived // r2 = Option<Derived>.None
let r3 = b2 as Base    // r3 = Option<Base>.Some(b2)
let r4 = b2 as Derived // r4 = Option<Derived>.Some(b2)
let r5 = d as Base     // r5 = Option<Base>.Some(d)
let r6 = d as Derived  // r6 = Option<Derived>.Some(d)
```