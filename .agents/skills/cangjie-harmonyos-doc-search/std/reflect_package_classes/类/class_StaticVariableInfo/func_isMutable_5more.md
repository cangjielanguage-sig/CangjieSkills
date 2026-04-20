### func isMutable()

```cangjie
public func isMutable(): Bool
```

功能：判断该 [StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo) 对应的静态成员变量是否可修改。

> **注意：**
>
> - 如果静态成员变量被 `var` 修饰符所修饰，则该静态成员变量可被修改。
> - 如果静态成员变量被 `let` 修饰符所修饰，则该静态成员变量不可被修改。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该静态成员变量信息所对应的静态成员变量可被修改则返回 `true` ，否则返回 `false`。

### func setValue(Any)

```cangjie
public func setValue(newValue: Any): Unit
```

功能：设置该 [StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo) 对应的静态成员变量的值。

参数：

- newValue: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 新值。

异常：

- [IllegalSetException](reflect_package_exceptions.md#class-illegalsetexception) - 如果该 [StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo) 对应的静态成员变量不可修改，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果新值 `newValue` 的运行时类型不是该静态成员变量信息所对应的静态成员变量的声明类型的子类型，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public static var area: Int64 = 10
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取静态变量
    let sv = ty.getStaticVariable("area")

    // 设置值
    sv.setValue(20)
    println(sv.getValue() as Int64)
    return
}
```

运行结果：

```text
Some(20)
```

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该静态成员变量信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该静态成员变量信息。

### operator func !=(StaticVariableInfo)

```cangjie
public operator func !=(that: StaticVariableInfo): Bool
```

功能：判断该静态成员变量信息与给定的另一个静态成员变量信息是否不等。

参数：

- that: [StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo) - 被比较相等性的另一个静态成员变量信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该静态成员变量信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(StaticVariableInfo)

```cangjie
public operator func ==(that: StaticVariableInfo): Bool
```

功能：判断该静态成员变量信息与给定的另一个静态成员变量信息是否相等。

参数：

- that: [StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo) - 被比较相等性的另一个静态成员变量信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该静态成员变量信息与 `that` 相等则返回 `true`，否则返回 `false`。