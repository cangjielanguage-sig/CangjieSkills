### func getStaticProperty(String)

```cangjie
public func getStaticProperty(name: String): StaticPropertyInfo
```

功能：尝试获取该类型中与给定属性名称匹配的静态成员属性的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 属性名称。

返回值：

- [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) - 如果成功匹配则返回该静态成员属性的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 静态成员属性，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    private static var valueArea = 0
    public static mut prop area: Int64 {
        get() { valueArea }
        set(v) { valueArea = v }
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 TypeInfo，也可以通过实例获取 TypeInfo
    let ty = TypeInfo.get("test.Rectangular")

    // 获取静态属性
    let sp = ty.getStaticProperty("area")

    println(sp)
    return
}
```

运行结果：

```text
static mut prop area: Int64
```

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取该类型信息的哈希值。

> **注意：**
>
> 内部实现为该类型信息的限定名称字符串的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该类型信息的哈希值。

### func isSubtypeOf(TypeInfo)

```cangjie
public func isSubtypeOf(supertype: TypeInfo): Bool
```

功能：判断当前 [TypeInfo](reflect_package_classes.md#class-typeinfo) 实例对应的类型是否是参数中指定的 [TypeInfo](reflect_package_classes.md#class-typeinfo) 实例表示的类型的子类型。

参数：

- supertype: [TypeInfo](reflect_package_classes.md#class-typeinfo) - 目标类型的类型信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型是 `supertype` 所对应的类型的子类型则返回 `true`，否则返回 `false`。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public abstract class Rectangular {}

public class Square <: Rectangular {}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 TypeInfo，也可以通过实例获取 TypeInfo
    let tyr = ClassTypeInfo.get("test.Rectangular")
    let tys = ClassTypeInfo.get("test.Square")
    println(tys.isSubtypeOf(tyr))
    return
}
```

运行结果：

```text
true
```

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该类型信息。

> **注意：**
>
> 内部实现为该类型信息的限定名称字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该类型信息。

### operator func !=(TypeInfo)

```cangjie
public operator func !=(that: TypeInfo): Bool
```

功能：判断该类型信息与给定的另一个类型信息是否不等。

参数：

- that: [TypeInfo](reflect_package_classes.md#class-typeinfo) - 被比较相等性的另一个类型信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型信息的限定名称与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(TypeInfo)

```cangjie
public operator func ==(that: TypeInfo): Bool
```

功能：判断该类型信息与给定的另一个类型信息是否相等。

参数：

- that: [TypeInfo](reflect_package_classes.md#class-typeinfo) - 被比较相等性的另一个类型信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该类型信息的限定名称与 `that` 相等则返回 `true`，否则返回 `false`。