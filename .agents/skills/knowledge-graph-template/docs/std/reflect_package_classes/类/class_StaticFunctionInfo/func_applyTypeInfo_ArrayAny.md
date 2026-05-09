### func apply(TypeInfo, Array\<Any>)

```cangjie
public func apply(thisType: TypeInfo, args: Array<Any>): Any
```

功能：调用该 [StaticFunctionInfo](reflect_package_classes.md#class-staticfunctioninfo) 对应静态成员函数，传入方法所属的类型信息和实参列表并返回调用结果。

> **注意：**
>
> `args` 的类型确保和函数入参类型完全一致，否则会导致参数检查失败。

参数：

- thisType: [TypeInfo](./reflect_package_classes.md#class-typeinfo) - 该方法所属的类。
- args: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Any](../../core/core_package_api/core_package_interfaces.md#interface-any)> - 实参列表。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该静态成员函数的调用结果。

异常：

- [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) - 如果该函数信息对应的静态成员函数存在泛型参数，则会抛出异常。
- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果该函数信息对应的静态成员函数的函数体未实现，则会抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果实参列表 `args` 中的实参的数目与该静态成员函数信息所对应的静态成员函数的形参列表中的形参的数目不等，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 `thisType` 和该静态函数的函数签名不一致，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实参列表 `args` 中的任何一个实参的运行时类型不是该静态成员函数信息所对应的静态成员函数的对应形参的声明类型的子类型，则抛出异常。
- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 如果被调用的静态成员函数信息所对应的静态成员函数内部抛出异常，则该异常将被封装为 [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) 异常并抛出。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public static func myName(): String {
        "my name is Rectangular"
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取静态函数
    let sf = ty.getStaticFunction("myName")

    let result = sf.apply(ty) as String
    println(result)
    return
}
```

运行结果：

```text
Some(my name is Rectangular)
```