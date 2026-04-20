### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取该静态成员属性信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该静态成员属性信息的哈希值。

### func isMutable()

```cangjie
public func isMutable(): Bool
```

功能：判断该静态成员属性信息所对应的静态成员属性是否可修改。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该静态成员属性信息所对应的静态成员属性可被修改则返回 `true` ，否则返回 `false`。

> **注意：**
>
> 如果静态成员属性被 `mut` 修饰符所修饰，则该静态成员属性可被修改，否则不可被修改。

### func setValue(Any)

```cangjie
public func setValue(newValue: Any): Unit
```

功能：设置该 [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) 对应的静态成员属性的值。

> **注意：**
>
> 如果该静态成员属性缺少合法实现，如 `interface` 类型中的抽象静态成员属性，则应抛出 [UnsupportedException](../../core/core_package_api/core_package_exceptions.md#class-unsupportedexception) 异常，但由于后端尚未支持，故尚未实现。

参数：

- newValue: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 新值。

异常：

- [IllegalSetException](reflect_package_exceptions.md#class-illegalsetexception) - 如果该静态成员属性信息所对应的静态成员属性不可修改，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果新值 `newValue` 的运行时类型不是该静态成员属性信息所对应的静态成员属性的声明类型的子类型，则抛出异常。

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
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取静态属性
    let sp = ty.getStaticProperty("area")

    // 设置静态成员属性的值
    sp.setValue(10)
    let result = sp.getValue() as Int64
    println(result)
    return
}
```

运行结果：

```text
Some(10)
```

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该静态成员属性信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该静态成员属性信息。

### operator func !=(StaticPropertyInfo)

```cangjie
public operator func !=(that: StaticPropertyInfo): Bool
```

功能：判断该静态成员属性信息与给定的另一个静态成员属性信息是否不等。

参数：

- that: [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) - 被比较相等性的另一个静态成员属性信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该静态成员属性信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(StaticPropertyInfo)

```cangjie
public operator func ==(that: StaticPropertyInfo): Bool
```

功能：判断该静态成员属性信息与给定的另一个静态成员属性信息是否相等。

参数：

- that: [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) - 被比较相等性的另一个静态成员属性信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该静态成员属性信息与 `that` 相等则返回 `true`，否则返回 `false`。