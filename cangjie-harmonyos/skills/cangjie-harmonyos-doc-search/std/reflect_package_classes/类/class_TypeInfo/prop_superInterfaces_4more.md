### prop superInterfaces

```cangjie
public prop superInterfaces: Collection<InterfaceTypeInfo>
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型直接实现的所有 `interface` 类型的信息，返回对应集合。

> **注意：**
>
> - 所有类型均默认直接实现 interface [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) 类型。
> - 该集合不保证遍历顺序恒定。
> - 目前， `struct` 类型只支持获取到 interface [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) 类型。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo)>

### static func get(String)

```cangjie
public static func get(qualifiedName: String): TypeInfo
```

功能：获取给定 `qualifiedName` 所对应的类型的 [TypeInfo](reflect_package_classes.md#class-typeinfo)。

> **注意：**
>
> 目前， 类型的限定名称 `qualifiedName` 不支持 `Nothing` 类型、函数类型、元组类型和`enum` 类型的限定名称。

参数：

- qualifiedName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 类型的限定名称。

返回值：

- [TypeInfo](reflect_package_classes.md#class-typeinfo) - 类型的限定名称 `qualifiedName` 所对应的类型的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获取与给定类型的限定名称 `qualifiedName` 匹配的类型所对应的类型信息，则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public class Rectangular {}

main(): Unit {
    let ty = TypeInfo.get("default.Rectangular")
    println(ty)
    return
}
```

运行结果：

```text
default.Rectangular
```

### static func of(Any)

```cangjie
public static func of(a: Any): TypeInfo
```

功能：获取给定的任意类型实例的运行时类型所对应的类型信息。

运行时类型是指在程序运行时，通过动态绑定确定的类型，运行时类型与实例对象相绑定。在继承等场景下运行时类型和静态类型可能不一致。

> **注意：**
>
> 目前，实例 `a` 不支持运行时类型为函数类型、元组类型、`enum` 类型。

参数：

- a: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 任意类型的实例。

返回值：

- [TypeInfo](reflect_package_classes.md#class-typeinfo) - 实例 `a` 的运行时类型所对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得实例 `a` 的运行时类型所对应的类型信息，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {}

main(): Unit {
    var r: Any = Rectangular()
    let ty = TypeInfo.of(r)
    println(ty)
    return
}
```

运行结果：

```text
test.Rectangular
```

### static func of(Object) <sup>(deprecated)</sup>

```cangjie
public static func of(a: Object): ClassTypeInfo
```

功能：获取给定的 `class` 类型的实例的运行时类型所对应的 `class` 类型信息。

> **注意：**
>
> 未来版本即将废弃，使用 [ClassTypeInfo](#class-classtypeinfo) 的 [static func of(Object)](#static-func-ofobject) 函数替代。

参数：

- a: [Object](../../core/core_package_api/core_package_classes.md#class-object) - `class` 类型的实例。

返回值：

- [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) - `class` 类型的实例 `a` 的运行时类型所对应的 `class` 类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得实例 `a` 的运行时类型所对应的 `class` 类型信息，则抛出异常。