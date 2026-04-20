## enum Option\<T>

```cangjie
public enum Option<T> {
    | Some(T)
    | None
}
```

功能：[Option](core_package_enums.md#enum-optiont)\<T> 是对 `T` 类型的封装，表示可能有值也可能无值。

它包含两个构造器：[Some](#somet) 和 [None](#none)。其中，[Some](#somet) 会携带一个参数，表示有值；[None](#none) 不带参数，表示无值。当需要表示某个类型可能有值，也可能没有值的时候，可选择使用 [Option](core_package_enums.md#enum-optiont) 类型。

[Option](core_package_enums.md#enum-optiont) 类型的另一种写法是在类型名前加 `?`，即对于任意类型 `Type`，`?Type` 等价于 [Option](core_package_enums.md#enum-optiont)\<Type>。

### None

```cangjie
None
```

功能：构造一个不带参数的 [Option](core_package_enums.md#enum-optiont)\<T> 实例，表示无值。

### Some(T)

```cangjie
Some(T)
```

功能：构造一个携带参数的 [Option](core_package_enums.md#enum-optiont)\<T> 实例，表示有值。

### func filter((T)->Bool)

```cangjie
public func filter(predicate: (T) -> Bool): Option<T>
```

功能：提供 [Option](core_package_enums.md#enum-optiont) 类型的“过滤”功能。

参数：

- predicate: (T) -> [Bool](core_package_intrinsics.md#bool) - 过滤函数。

返回值：

- Option\<T> - 如果 [Option](core_package_enums.md#enum-optiont) 值是 [Some](#somet)(v)，并且 v 满足 `predicate(v) = true` 时，返回 [Some](#somet)(v)， 否则返回 [None](#none)。

### func flatMap\<R>((T) -> Option\<R>)

```cangjie
public func flatMap<R>(transform: (T) -> Option<R>): Option<R>
```

功能：提供从 [Option](core_package_enums.md#enum-optiont)\<T> 类型到 [Option](core_package_enums.md#enum-optiont)\<R> 类型的映射函数，如果当前实例值是 [Some](#somet)，执行 transform 函数，并且返回结果，否则返回 [None](#none)。

参数：

- transform: (T) -> [Option](core_package_enums.md#enum-optiont)\<R> - 映射函数。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<R> - 如果当前实例值是 [Some](#somet)，执行 transform 函数并返回，否则返回 [None](#none)。

### func getOrDefault(() -> T)

```cangjie
public func getOrDefault(other: () -> T): T
```

功能：获得值或返回默认值。如果 [Option](core_package_enums.md#enum-optiont) 值是 [Some](#somet)，则返回类型为 `T` 的实例，如果 [Option](core_package_enums.md#enum-optiont) 值是 [None](#none)，则调用入参，返回类型 `T` 的值。

参数：

- other: () -> T - 默认函数，如果当前实例的值是 [None](#none)，调用该函数得到类型为 `T` 的实例，并将其返回。

返回值：

- T - 如果当前实例的值是 [Some](#somet)\<T>，则返回当前实例携带的类型为 `T` 的实例，如果 [Option](core_package_enums.md#enum-optiont) 值是 [None](#none)，调用入参指定的函数，得到类型为 `T` 的实例，并将其返回。

示例：

<!-- verify -->
```cangjie
main() {
    var value1: Option<Int64> = Some(2)
    println(value1.getOrDefault({=> 0}))

    var value2: Option<Int64> = None
    println(value2.getOrDefault({=> 0}))
}
```

运行结果：

```text
2
0
```

### func getOrThrow(() -> Exception)

```cangjie
public func getOrThrow(exception: ()->Exception): T
```

功能：获得值或抛出指定异常。

参数：

- exception: () ->[Exception](core_package_exceptions.md#class-exception) - 异常函数，如果当前实例值是 [None](#none)，将执行该函数并将其返回值作为异常抛出。

返回值：

- T - 如果当前实例值是 [Some](#somet)\<T>，返回类型为 `T` 的实例。

异常：

- [Exception](core_package_exceptions.md#class-exception) - 如果当前实例是 [None](#none)，抛出异常函数返回的异常。

### func getOrThrow()

```cangjie
public func getOrThrow(): T
```

功能：获得值或抛出异常。

返回值：

- T - 如果当前实例值是 [Some](#somet)\<T>，返回类型为 `T` 的实例。

异常：

- [NoneValueException](core_package_exceptions.md#class-nonevalueexception) - 如果当前实例是 [None](#none)，抛出异常。