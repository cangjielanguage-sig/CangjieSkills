## class InterfaceTypeInfo

```cangjie
public class InterfaceTypeInfo <: TypeInfo {}
```

功能：`interface` 类型的类型信息。

父类型：

- [TypeInfo](#class-typeinfo)

### prop sealedSubtypes

```cangjie
public prop sealedSubtypes: Collection<TypeInfo>
```

功能：如果该 [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo) 所对应的 `interface` 类型拥有 `sealed` 语义，则获取该 `interface` 类型所在包内的所有子类型的类型信息，返回对应集合。

> **注意：**
>
> - 如果该 `interface` 类型不拥有 `sealed` 语义，则返回空集合。
> - 如果该 `interface` 类型拥有 `sealed` 语义，那么获得的集合必不可能是空集合，因为该 `interface` 类型本身就是自己的子类型。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[TypeInfo](reflect_package_classes.md#class-typeinfo)>

### static func get(String)

```cangjie
public redef static func get(qualifiedName: String): InterfaceTypeInfo
```

功能：获取给定 `qualifiedName` 所对应的类型的 [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo)。

参数：

- qualifiedName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 类型的限定名称。

返回值：

- [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo) - 类型的限定名称 `qualifiedName` 所对应的 `Interface` 类型的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获取与给定类型的限定名称 `qualifiedName` 匹配的类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public interface Rectangular {}

main(): Unit {
    let ty = InterfaceTypeInfo.get("default.Rectangular")
    println(ty)
    return
}
```

运行结果：

```text
default.Rectangular
```

### static func of(Any)

```cangjie
public redef static func of(a: Any): InterfaceTypeInfo
```

功能：获取给定的任意类型实例的运行时类型所对应的类型信息。

运行时类型是指在程序运行时，通过动态绑定确定的类型，运行时类型与实例对象相绑定。在继承等场景下运行时类型和静态类型可能不一致。

参数：

- a: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 任意类型的实例。

返回值：

- [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo) - 实例 `a` 的运行时类型所对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得实例 `a` 的运行时类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo)， 则抛出异常。

### static func of\<T>()

```cangjie
public redef static func of<T>(): InterfaceTypeInfo
```

功能：获取给定 `T` 类型对应的类型信息。

返回值：

- [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo) - `T` 类型对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得类型 T 所对应的类型信息，抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo)， 则抛出异常。