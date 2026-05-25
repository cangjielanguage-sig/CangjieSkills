### prop superClass

```cangjie
public prop superClass: Option<ClassTypeInfo>
```

功能：获取该 `class` 类型信息所对应的 `class` 类型的直接父类。

> **注意：**
>
> 理论上只有 class [Object](../../core/core_package_api/core_package_classes.md#class-object) 没有直接父类。

类型：[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo)>

### static func get(String)

```cangjie
public redef static func get(qualifiedName: String): ClassTypeInfo
```

功能：获取给定限定名称所对应类型的 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo)。

参数：

- qualifiedName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 类型的限定名称。

返回值：

- [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) - 类型的限定名称 `qualifiedName` 所对应的类型的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获取与给定类型的限定名称 `qualifiedName` 匹配的类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public class Rectangular {}

main(): Unit {
    let ty = ClassTypeInfo.get("default.Rectangular")
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
public redef static func of(a: Any): ClassTypeInfo
```

功能：获取给定的任意类型的实例的运行时类型所对应的类型信息。

运行时类型是指在程序运行时，通过动态绑定确定的类型，运行时类型与实例对象相绑定。在继承等场景下运行时类型和静态类型可能不一致。

参数：

- a: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 任意类型的实例。

返回值：

- [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) - 实例 `a` 的运行时类型所对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得实例 `a` 的运行时类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {}

main(): Unit {
    var r = Rectangular()
    let ty = ClassTypeInfo.of(r)
    println(ty)
    return
}
```

运行结果：

```text
test.Rectangular
```

### static func of(Object)

```cangjie
public static func of(a: Object): ClassTypeInfo
```

功能：获取给定的 `class` 类型的实例的运行时类型所对应的 `class` 类型信息。

参数：

- a: [Object](../../core/core_package_api/core_package_classes.md#class-object) - `class` 类型的实例。

返回值：

- [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) - `class` 类型的实例 `a` 的运行时类型所对应的 `class` 类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得实例 `a` 的运行时类型所对应的 `class` 类型信息，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {}

main(): Unit {
    var r = Rectangular()
    let ty = ClassTypeInfo.of(r)
    println(ty)
    return
}
```

运行结果：

```text
test.Rectangular
```