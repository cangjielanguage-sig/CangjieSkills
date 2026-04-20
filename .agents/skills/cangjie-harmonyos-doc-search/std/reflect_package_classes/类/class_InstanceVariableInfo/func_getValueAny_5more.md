### func getValue(Any)

```cangjie
public func getValue(instance: Any): Any
```

功能：获取该 [InstanceVariableInfo](reflect_package_classes.md#class-instancevariableinfo) 对应的实例成员变量在给定实例中的值。

参数：

- instance: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 实例。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该实例成员变量在实例 `instance` 中的值。

异常：

- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实例 `instance` 的运行时类型与该实例成员变量信息所对应的实例成员变量所属的类型不严格相同，则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public class Rectangular {
    public var length = 4
    public var width = 5
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("default.Rectangular")
    // 获取 InstanceVariableInfo
    var gip = ty.getInstanceVariable("width")
    // 获取实例值
    var r = Rectangular()
    let v = gip.getValue(r) as Int64
    println(v)
    return
}
```

运行结果：

```text
Some(5)
```

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取该实例成员变量信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该实例成员变量信息的哈希值。

### func isMutable()

```cangjie
public func isMutable(): Bool
```

功能：判断该 [InstanceVariableInfo](reflect_package_classes.md#class-instancevariableinfo) 对应的实例成员变量是否可修改。

> **注意：**
>
> - 如果实例成员变量被 `var` 修饰符所修饰，则该实例成员变量可被修改。
> - 如果实例成员变量被 `let` 修饰符所修饰，则该实例成员变量不可被修改。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该实例成员变量信息所对应的实例成员变量可被修改则返回 `true` ，否则返回 `false`。

### func setValue(Any, Any)

```cangjie
public func setValue(instance: Any, newValue: Any): Unit
```

功能：设置该 [InstanceVariableInfo](reflect_package_classes.md#class-instancevariableinfo) 对应的实例成员变量在给定实例中的值。

参数：

- instance: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 实例。
- newValue: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 新值。

异常：

- [IllegalSetException](reflect_package_exceptions.md#class-illegalsetexception) - 如果该实例成员变量信息所对应的实例成员变量不可修改，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实例 `instance` 的运行时类型与该实例成员变量信息所对应的实例成员变量所属的类型不严格相同，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果新值 `newValue` 的运行时类型不是该实例成员变量信息所对应的实例成员变量的声明类型的子类型，则抛出异常。

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该实例成员变量信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该实例成员变量信息。