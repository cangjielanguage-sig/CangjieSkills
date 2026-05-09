### func apply(Any, Array\<Any>)

```cangjie
public func apply(instance: Any, args: Array<Any>): Any
```

功能：调用该 [InstanceFunctionInfo](reflect_package_classes.md#class-instancefunctioninfo) 对应实例成员函数，指定实例并传入实参列表，返回调用结果。

> **注意：**
>
> `args` 的类型确保和函数入参类型完全一致。

参数：

- instance: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 实例。
- args: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Any](../../core/core_package_api/core_package_interfaces.md#interface-any)> - 实参列表。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该实例成员函数的调用结果。

异常：

- [InvocationTargetException](../reflect_package_api/reflect_package_exceptions.md#class-invocationtargetexception) - 如果存在泛型参数的函数调用了该方法，则抛出异常。
- [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) - 如果该实例成员函数信息所对应的实例成员函数是抽象的，或不存在相应的函数实现，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果实参列表 `args` 中的实参的数目与该实例成员函数信息所对应的实例成员函数的形参列表中的形参的数目不等，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实例 `instance` 的运行时类型与该实例成员函数信息所对应的实例成员函数所属的类型不相同，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实参列表 `args` 中的任何一个实参的运行时类型不是该实例成员函数信息所对应的实例成员函数的对应形参的声明类型的子类型，则抛出异常。
- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 如果被调用的实例成员函数信息所对应的实例成员函数内部抛出异常，则该异常将被封装为 [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) 异常并抛出。