### static func of\<T>()

```cangjie
public static func of<T>(): TypeInfo
```

功能：获取给定 `T` 类型对应的类型信息。

> **注意：**
>
> - 目前，泛型 `T` 不支持 `Nothing` 类型、函数类型、元组类型和`enum` 类型。
> - `T` 支持传入类型别名，包括内置类型别名（如 [Int](../../core/core_package_api/core_package_types.md#type-int)、[UInt](../../core/core_package_api/core_package_types.md#type-uint) 和 `Rune` 等）与用户自定义类型别名。

返回值：

- [TypeInfo](reflect_package_classes.md#class-typeinfo) - `T` 类型对应的类型信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果无法获得类型 T 所对应的类型信息，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.reflect.*

public class Rectangular {}

main(): Unit {
    let ty = TypeInfo.of<Rectangular>()
    println(ty)
    return
}
```

运行结果：

```text
default.Rectangular
```

### func findAnnotation\<T>()

```cangjie
public func findAnnotation<T>(): Option<T>
```

功能：尝试获取拥有给定限定名称且作用于该对象的注解。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 如果成功匹配则返回该注解，重复标注或者无法匹配时返回 `None`。

### func getInstanceFunction(String, Array\<TypeInfo>)

```cangjie
public func getInstanceFunction(name: String, parameterTypes: Array<TypeInfo>): InstanceFunctionInfo
```

功能：给定函数名称与函数形参类型列表所对应的类型信息列表，尝试获取该类型中匹配的实例成员函数的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 函数名称。
- parameterTypes: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[TypeInfo](reflect_package_classes.md#class-typeinfo)> - 函数形参类型列表所对应的类型信息列表。

返回值：

- [InstanceFunctionInfo](reflect_package_classes.md#class-instancefunctioninfo) - 如果成功匹配则返回该实例成员函数的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 实例成员函数，则抛出异常。

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
    // 此处是通过 Rectangular 的类型的限定名称获取 TypeInfo，也可以通过实例获取 TypeInfo
    let ty = TypeInfo.get("default.Rectangular")
    // 获取 InstanceFunctionInfo
    var gif = ty.getInstanceFunction("area")

    println(gif)
    return
}
```

运行结果：

```text
func area(): Int64
```

### func getInstanceFunctions(String)

```cangjie
public func getInstanceFunctions(name: String): Array<InstanceFunctionInfo>
```

功能：给定函数名称，尝试获取该类型中所有匹配的实例成员函数的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 函数名称。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[InstanceFunctionInfo](reflect_package_classes.md#class-instancefunctioninfo)> - 如果成功匹配则返回所有匹配到的实例成员函数信息。

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
    // 此处是通过 Rectangular 的类型的限定名称获取 TypeInfo，也可以通过实例获取 TypeInfo
    let ty = TypeInfo.get("default.Rectangular")
    // 获取 InstanceFunctionInfo
    var gif = ty.getInstanceFunctions("area")

    println(gif)
    return
}
```

运行结果：

```text
[func area(): Int64]
```