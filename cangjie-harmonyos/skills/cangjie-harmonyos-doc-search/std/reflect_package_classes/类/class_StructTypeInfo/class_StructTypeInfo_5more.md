## class StructTypeInfo

```cangjie
public class StructTypeInfo <: TypeInfo {}
```

功能：描述 `struct` 类型的类型信息。

父类型：

- [TypeInfo](#class-typeinfo)

由于实现限制，目前 `Struct` 类型的变量/属性修改需要参考如下代码手动 box/unbox。

```cangjie
import std.reflect.*

public struct SA {
    public var v1 = 11
}

main() {
    var sa = SA()
    let saObj: Any = sa
    StructTypeInfo.of<SA>().getInstanceVariable("v1").setValue(saObj, 22)
    sa = (saObj as SA).getOrThrow()
    println(sa.v1) // should be 22
}
```

### prop constructors

```cangjie
public prop constructors: Collection<ConstructorInfo>
```

功能：获取该 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) 对应的 `struct` 的所有 `public` 构造函数信息，返回对应集合。

> **注意：**
>
> - 如果该 `struct` 类型无任何 `public` 构造函数，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[ConstructorInfo](reflect_package_classes.md#class-constructorinfo)>

### prop instanceVariables

```cangjie
public prop instanceVariables: Collection<InstanceVariableInfo>
```

功能：获取该 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) 对应的 `struct` 的所有 `public` 实例成员变量信息，返回对应集合。

> **注意：**
>
> - 如果该 `struct` 类型无任何 `public` 实例成员变量，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[InstanceVariableInfo](reflect_package_classes.md#class-instancevariableinfo)>

### prop staticVariables

```cangjie
public prop staticVariables: Collection<StaticVariableInfo>
```

功能：获取该 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) 对应的 `struct` 的所有 `public` 静态成员变量信息，返回对应集合。

> **注意：**
>
> - 如果该 `struct` 类型无任何 `public` 静态成员变量，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo)>

### static func get(String)

```cangjie
public static redef func get(qualifiedName: String): StructTypeInfo
```

功能：获取给定 `qualifiedName` 所对应的类型的 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo)。

参数：

- qualifiedName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 类型的限定名称。

返回值：

- [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) - 类型的限定名称 `qualifiedName` 所对应的 `Struct` 类型的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获取与给定类型的限定名称 `qualifiedName` 匹配的类型所对应的类型信息，则抛出异常。
- [IllegalTypeException](./reflect_package_exceptions.md#class-illegaltypeexception) - 如果获取到的类型信息不是 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo)， 则抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public struct Rectangular {}

main(): Unit {
    let ty = StructTypeInfo.get("default.Rectangular")
    println(ty)
    return
}
```

运行结果：

```text
default.Rectangular
```