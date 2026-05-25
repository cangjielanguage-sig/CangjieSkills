## 常见的 Deriving 语法

`@Derive` 宏支持以逗号分隔的接口名称列表。此外，该宏可以重复多次被调用，但所有 `@Derive` 宏调用都应位于声明的顶部，而其他宏（如 `@DeriveOrder` ）应始终位于其后。

支持的接口列表的顺序没有影响。

<!-- compile -->
```cangjie
import std.deriving.*

@Derive[ToString, Hashable]
@Derive[Equatable]
@DeriveOrder[currency, price, quantity]
struct Order {
    let currency = 1
    let price = 100
    let quantity = 200
}
main(){}
```

当 Deriving 多个相交的接口时，例如，`Comparable` 还包括 `Equatable` ，则允许两者同时存在，等同于仅有范围最广的一个：

```cangjie
@Derive[Comparable] // does also generate Equatable
```

等同于：

```cangjie
@Derive[Comparable, Equatable]
```

## 包含和排除

默认情况下会处理所有字段，包括定义为主构造函数参数的字段。
当需要排除某个字段时，可以对其应用 `@DeriveExclude` ：

<!-- compile -->
```cangjie
import std.deriving.*

@Derive[ToString]
struct S {
    S(let id: Int) {
        key = "s_${id}"
    }

    @DeriveExclude
    let key: String
}
main(){}
```

默认情况下不处理属性，需要通过 `@DeriveInclude` 包含属性。

<!-- compile -->
```cangjie
import std.deriving.*

@Derive[ToString]
struct S {
    S(let id: Int) {}

    @DeriveInclude
    prop key: String {
        get() {
            "s_${id}"
        }
    }
}
main(){}
```

被 Deriving 的字段和属性都不能是 `private` 的。因此，`private` 的字段或者属性应被除外或者使其为包内可见属性。

> **注意**
>
> 静态的字段和属性始终会被忽略，因此它们都不能被 `@DeriveInclude` 和 `@DeriveExclude` 修饰。

## 支持的接口

当前仅支持如下接口:

- `ToString`
- `Hashable`
- `Equatable`
- `Comparable`

暂不支持用户自定义的接口。

## 变更顺序

在对由多个字段组成的复杂类型的实例进行排序和比较时，测试字段的顺序通常很重要。默认情况下，所有字段都按声明顺序考虑。可以使用 `@DeriveOrder` 宏修改顺序。

<!-- verify -->

```cangjie
import std.deriving.*
import std.sort.*

@Derive[Comparable, ToString]
struct Floor {
    Floor(
        let level: Int,
        let building: Int
    ) {}
}

main() {
    let floors = [
        Floor(1, 2),
        Floor(3, 2),
        Floor(2, 1)
    ]
    sort(floors)
    for (f in floors) {
        println(f)
    }
}
```

上述示例将打印以下内容，看起来顺序没有很大影响。

```text
Floor(level: 1, building: 2)
Floor(level: 2, building: 1)
Floor(level: 3, building: 2)
```

但是当我实现 `Comparable` 时，不同的顺序将影响结果。

<!-- verify -->
```cangjie
import std.deriving.*
import std.sort.*

@Derive[Comparable, ToString]
@DeriveOrder[building, level] // 相比上面示例多了这一行代码
struct Floor {
    Floor(
        let level: Int,
        let building: Int
    ) {}
}
main() {
    let floors = [
        Floor(1, 2),
        Floor(3, 2),
        Floor(2, 1)
    ]
    sort(floors)
    for (f in floors) {
        println(f)
    }
}
```

此时，结果将首先按 `building` 排序，然后按 `level` 排序：

```text
Floor(building: 1, level: 2)
Floor(building: 2, level: 1)
Floor(building: 2, level: 3)
```