### static func of(Any)

```cangjie
public static redef func of(a: Any): PrimitiveTypeInfo
```

功能：获取给定的任意类型实例的运行时类型所对应的类型信息。

运行时类型是指在程序运行时，通过动态绑定确定的类型，运行时类型与实例对象相绑定。在继承等场景下运行时类型和静态类型可能不一致。

参数：

- a: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 任意类型的实例。

返回值：

- [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo) - 实例 `a` 的运行时类型所对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得实例 `a` 的运行时类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

main(): Unit {
    var a = 10
    var pti = PrimitiveTypeInfo.of(a)
    println(pti)
    return
}
```

运行结果：

```text
Int64
```

### static func of\<T>()

```cangjie
public static redef func of<T>(): PrimitiveTypeInfo
```

功能：获取给定 `T` 类型对应的类型信息。

返回值：

- [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo) - `T` 类型对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得类型 T 所对应的类型信息，抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

main(): Unit {
    var pti = PrimitiveTypeInfo.of<Int64>()
    println(pti)
    return
}
```

运行结果：

```text
Int64
```