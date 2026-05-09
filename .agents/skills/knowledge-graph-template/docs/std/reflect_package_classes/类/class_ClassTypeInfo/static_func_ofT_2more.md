### static func of\<T>()

```cangjie
public redef static func of<T>(): ClassTypeInfo
```

功能：获取给定类型 `T` 对应的类型信息。

返回值：

- [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) - `T` 类型对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得类型 T 所对应的类型信息，抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public class Rectangular {}

main(): Unit {
    let ty = ClassTypeInfo.of<Rectangular>()
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

功能：在该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型中根据实参列表搜索匹配的构造函数并调用，传入实参列表，返回调用结果。

参数：

- args: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Any](../../core/core_package_api/core_package_interfaces.md#interface-any)> - 实参列表。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该 `class` 类型的实例。

异常：

- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果该 `class` 类型拥有 `abstract` 语义，调用 `construct` 则抛出异常，因为抽象类不可被实例化。
- [MisMatchException](reflect_package_exceptions.md#class-mismatchexception) - 如果 `args` 未能成功匹配任何该 `class` 类型的可见性为 `public` 的构造函数，则抛出异常。
- [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) - 在被调用的构造函数内部抛出的任何异常均将被封装为 [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) 异常并抛出。

示例：

<!-- run -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public var length = 4
    public var width = 5
    public var myName = ""
    public init() {}
    public init(name: String) {
        myName = name
    }
    public init(name: String, length: Int64, width: Int64) {
        myName = name
        this.length = length
        this.width = width
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 通过不同入参构造实例
    ty.construct()
    ty.construct("Small rectangular")
    ty.construct("Big rectangular", 1, 1)
    return
}
```