### func getConstructor(Array\<TypeInfo>)

```cangjie
public func getConstructor(parameterTypes: Array<TypeInfo>): ConstructorInfo
```

功能：尝试在该 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) 对应的 `struct` 类型中获取与给定形参类型信息列表匹配的 `public` 构造函数的信息。

参数：

- parameterTypes: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[TypeInfo](reflect_package_classes.md#class-typeinfo)> - 形参类型信息列表。

返回值：

- [ConstructorInfo](reflect_package_classes.md#class-constructorinfo) - 如果成功匹配则返回该 `public` 构造函数的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 构造函数，则抛出异常。

### func getInstanceVariable(String)

```cangjie
public func getInstanceVariable(name: String): InstanceVariableInfo
```

功能：给定变量名称，尝试获取该 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) 对应的 `struct` 类型中匹配的实例成员变量的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 变量名称。

返回值：

- [InstanceVariableInfo](reflect_package_classes.md#class-instancevariableinfo) - 如果成功匹配则返回该实例成员变量的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 实例成员变量，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public var length = 4
    public var width = 5
    public var myName = ""
    public init() {}
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取结构实例成员变量信息
    let ivi = ty.getInstanceVariable("myName")
    println(ivi)
    return
}
```

运行结果：

```text
myName: String
```

### func getStaticVariable(String)

```cangjie
public func getStaticVariable(name: String): StaticVariableInfo
```

功能：给定变量名称，尝试获取该 [StructTypeInfo](reflect_package_classes.md#class-structtypeinfo) 对应的 `struct` 类型中匹配的静态成员变量的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 变量名称。

返回值：

- [StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo) - 如果成功匹配则返回该静态成员变量的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 静态成员变量，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public struct Rectangular {
    public static var area: Int64 = 10
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 StructTypeInfo，也可以通过实例获取 StructTypeInfo
    let ty = StructTypeInfo.get("test.Rectangular")

    // 获取静态变量
    let sv = ty.getStaticVariable("area")
    println(sv)
    return
}
```

运行结果：

```text
static area: Int64
```