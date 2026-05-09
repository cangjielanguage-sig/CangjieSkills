### static func of(Any)

```cangjie
public static redef func of(a: Any): StructTypeInfo
```

功能：获取给定的任意类型实例的运行时类型所对应的类型信息。

运行时类型是指在程序运行时，通过动态绑定确定的类型，运行时类型与实例对象相绑定。在继承等场景下运行时类型和静态类型可能不一致。

参数：

- a: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 任意类型的实例。

返回值：

- [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) - 实例 `a` 的运行时类型所对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得实例 `a` 的运行时类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public struct Rectangular {}

main(): Unit {
    var r = Rectangular()
    let ty = StructTypeInfo.of(r)
    println(ty)
    return
}
```

运行结果：

```text
test.Rectangular
```

### static func of\<T>()

```cangjie
public static redef func of<T>(): StructTypeInfo
```

功能：获取给定 `T` 类型对应的类型信息。

返回值：

- [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) - `T` 类型对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得类型 T 所对应的类型信息，抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public struct Rectangular {}

main(): Unit {
    let ty = StructTypeInfo.of<Rectangular>()
    println(ty)
    return
}
```

运行结果：

```text
default.Rectangular
```

### func construct(Array\<Any>)

```cangjie
public func construct(args: Array<Any>): Any
```

功能：在该 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) 对应的 `struct` 类型中根据实参列表搜索匹配的构造函数并调用，传入实参列表，返回调用结果。

参数：

- args: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Any](../../core/core_package_api/core_package_interfaces.md#interface-any)> - 实参列表。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该 `struct` 类型的实例。

异常：

- [MisMatchException](reflect_package_exceptions.md#class-mismatchexception) - 如果 `args` 未能成功匹配任何该 `struct` 类型的 `public` 构造函数，则抛出异常
- [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) - 在被调用的构造函数内部抛出的任何异常均将被封装为 [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) 异常并抛出。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public struct Rectangular {
    public var length = 4
    public var width = 5
    public init() {}
    public init(length: Int64, width: Int64) {
        this.length = length
        this.width = width
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 StructTypeInfo，也可以通过实例获取 StructTypeInfo
    let ty = StructTypeInfo.get("default.Rectangular")
    // 匹配构造函数并调用
    let v = ty.construct(2, 3) as Rectangular
    println(v.getOrThrow().length)
    return
}
```

运行结果：

```text
2
```