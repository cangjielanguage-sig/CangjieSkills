# Deriving 示例

一个简单示例：

<!-- verify -->

```cangjie
import std.deriving.*

@Derive[ToString]
class User {
    User(
        let name: String,
        let id: Int
    ) {}
}

main() {
    println(User("id0", 0))
}
```

运行结果：

```text
User(name: id0, id: 0)
```

当 `@Derive[ToString]` 应用于类或结构体时， Deriving 会收集和使用类或结构体的可变和不可变字段，包括在主构造函数中指定的字段，并自动实现 `ToString` 的方法。当 `@Derive[ToString]` 应用于枚举时， Deriving 将收集枚举的构造函数参数。静态字段和属性将不会被收集和使用，另外， Deriving 收集的字段不允许存在私有字段，否则将抛出编译错误。

收集到的字段用于 Deriving 时，其类型需要实现目标接口，以便将字段结果组合在一起。例如，当处理 `ToString` 时，生成的代码将在所有收集到的字段上调用 `toString` ，然后将结果与对应的字段名称连接成一个字符串。如果其中一个字段的类型不支持 `ToString` ，则会抛出编译错误并且 Deriving 无法完成。

> **注意**
>
> 标记为派生的类应该是最终的：它不应该是开放的、抽象的或 `sealed` 的。

有些字段可能具有特殊含义，它们的值没有多大意义，则可通过在这些字段上应用 `@DeriveExclude` 来排除这些字段：

<!-- compile -->
```cangjie
import std.deriving.*

@Derive[ToString]
class User {
    User(let name: String) {}

    @DeriveExclude
    let lazyHashCode = 0 // it will not be printed because it's excluded
}
main(){}
```

默认情况 Deriving 仅使能字段，对于属性则需要通过 `@DeriveInclude` 来显式使能：

<!-- verify -->
```cangjie
import std.deriving.*

@Derive[ToString]
class User {
    User(let id: Int) {}

    @DeriveInclude
    prop name: String {
        get() {
            "id0"
        }
    }
}

main() {
    println(User(0))
}
```

运行结果：

```text
User(id: 0, name: id0)
```

请注意，因为属性 `name` 是在 `id` 之后声明的，因此打印的顺序为先 `id` 后 `name` 。

如果需要更改打印的顺序，可以使用 `@DeriveOrder` ：

<!-- verify -->
```cangjie
import std.deriving.*

@Derive[ToString]
@DeriveOrder[name, id]
class User {
    User(let id: Int) {}

    @DeriveInclude
    prop name: String {
        get() {
            "id${id}"
        }
    }
}

main() {
    println(User(0))
}
```

运行结果：

```text
User(name: id0, id: 0)
```