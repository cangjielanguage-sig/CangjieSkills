### func getValue(Any)

```cangjie
public func getValue(instance: Any): Any
```

功能：获取该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性在给定实例中的值。

参数：

- instance: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 实例。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该实例成员属性在实例 `instance` 中的值。

异常：

- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实例 `instance` 的运行时类型与该实例成员属性信息所对应的实例成员属性所属的类型不严格相同，则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public class Rectangular {
    public var length = 4
    public prop width: Int64 {
        get() {
            5
        }
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("default.Rectangular")
    // 获取 InstancePropertyInfo
    var gip = ty.getInstanceProperty("width")

    // 获取实例值
    var r = Rectangular()
    var result = gip.getValue(r) as Int64
    println(result)
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

功能：获取该实例成员属性信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该实例成员属性信息的哈希值。

### func isAbstract()

```cangjie
public func isAbstract(): Bool
```

功能：判断该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性是否是抽象的。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性是抽象的，则返回 `true`，否则返回 `false`。

### func isMutable()

```cangjie
public func isMutable(): Bool
```

功能：判断该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性是否可修改。

> **注意：**
>
> 如果实例成员属性被 `mut` 修饰符所修饰，则该实例成员属性可被修改，否则不可被修改。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该实例成员属性信息所对应的实例成员属性可被修改则返回 `true` ，否则返回 `false`。

### func isOpen()

```cangjie
public func isOpen(): Bool
```

功能：判断该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性是否拥有 `open` 语义。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性拥有 `open` 语义则返回 `true`，否则返回 `false`。