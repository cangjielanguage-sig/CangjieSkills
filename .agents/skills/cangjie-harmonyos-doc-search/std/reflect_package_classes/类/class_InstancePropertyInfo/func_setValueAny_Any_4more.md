### func setValue(Any, Any)

```cangjie
public func setValue(instance: Any, newValue: Any): Unit
```

功能：设置该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性在给定实例中的值。

参数：

- instance: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 实例。
- newValue: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 新值。

异常：

- [IllegalSetException](reflect_package_exceptions.md#class-illegalsetexception) - 如果该实例成员属性信息所对应的实例成员属性不可修改，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实例 `instance` 的运行时类型与该实例成员属性信息所对应的实例成员属性所属的类型不严格相同，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果新值 `newValue` 的运行时类型不是该实例成员属性信息所对应的实例成员属性的声明类型的子类型，则抛出异常。

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该实例成员属性信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该实例成员属性信息。

### operator func !=(InstancePropertyInfo)

```cangjie
public operator func !=(that: InstancePropertyInfo): Bool
```

功能：判断该实例成员属性信息与给定的另一个实例成员属性信息是否不等。

参数：

- that: [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) - 被比较相等性的另一个实例成员属性信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该实例成员属性信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(InstancePropertyInfo)

```cangjie
public operator func ==(that: InstancePropertyInfo): Bool
```

功能：判断该实例成员属性信息与给定的另一个实例成员属性信息是否相等。

参数：

- that: [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) - 被比较相等性的另一个实例成员属性信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该实例成员属性信息与 `that` 相等则返回 `true`，否则返回 `false`。