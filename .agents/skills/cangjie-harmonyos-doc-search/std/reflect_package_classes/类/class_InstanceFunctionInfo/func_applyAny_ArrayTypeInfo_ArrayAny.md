### func apply(Any, Array\<TypeInfo>, Array\<Any>)

```cangjie
public func apply(instance: Any, genericTypeArgs: Array<TypeInfo>, args: Array<Any>): Any
```

功能：调用该 [InstanceFunctionInfo](reflect_package_classes.md#class-instancefunctioninfo) 对应泛型成员函数，指定实例并传入泛型参数的类型列表和参数列表，返回调用结果。

> **注意：**
>
> `args` 的类型确保和函数入参类型完全一致。

参数：

- instance: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 实例。
- genericTypeArgs: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[TypeInfo](./reflect_package_classes.md#class-typeinfo)> - 泛型参数类型信息列表。
- args: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Any](../../core/core_package_api/core_package_interfaces.md#interface-any)> - 泛型参数列表。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该实例泛型函数的调用结果。

异常：

- [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) - 如果该函数信息对应的成员函数是 `abstract` 或不存在函数体，则会抛出异常。
- [InvacationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) - 如果非泛型函数调用了此方法，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实例 `instance` 的运行时类型与该成员函数信息所对应的成员函数所属的类型不相同，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果实参列表 `args` 中的实参的数目与该成员函数信息所对应的成员函数的形参列表中的形参的数目不等，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果函数泛型参数列表 `genericTypeArgs` 中的参数数目与该成员函数信息所对应的成员函数的泛型参数列表 `genericParams` 中的参数数目不等，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果参数列表 `args` 中的任何一个参数的运行时类型不是该实例成员函数信息所对应的实例成员函数的对应形参的声明类型的子类型，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果传入的参数列表 `args` 和泛型参数类型列表 `genericTypeArgs` 不满足该成员函数信息所对应的成员函数的参数的类型约束，则抛出异常。
- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 如果被调用的实例成员函数信息所对应的实例成员函数内部抛出异常，则该异常将被封装为 [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) 异常并抛出。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public class Rectangular {
    public var length = 4
    public var width = 5
    public func area(): Int64 {
        return length * width
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("default.Rectangular")
    // 获取 InstanceFunctionInfo
    var gif = ty.getInstanceFunction("area")

    // 调用反射函数
    var r = Rectangular()
    var result = gif.apply(r) as Int64
    println(result)
    return
}
```

运行结果：

```text
Some(20)
```