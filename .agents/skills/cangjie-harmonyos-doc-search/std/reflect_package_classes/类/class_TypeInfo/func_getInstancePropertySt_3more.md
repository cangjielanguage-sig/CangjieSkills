### func getInstanceProperty(String)

```cangjie
public func getInstanceProperty(name: String): InstancePropertyInfo
```

功能：尝试获取该类型中与给定属性名称匹配的实例成员属性的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 属性名称。

返回值：

- [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) - 如果成功匹配则返回该实例成员属性的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 实例成员属性，则抛出异常。

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
    // 此处是通过 Rectangular 的类型的限定名称获取 TypeInfo，也可以通过实例获取 TypeInfo
    let ty = TypeInfo.get("default.Rectangular")
    // 获取 InstancePropertyInfo
    var gip = ty.getInstanceProperty("width")

    println(gip)
    return
}
```

运行结果：

```text
prop width: Int64
```

### func getStaticFunction(String, Array\<TypeInfo>)

```cangjie
public func getStaticFunction(name: String, parameterTypes: Array<TypeInfo>): StaticFunctionInfo
```

功能：通过给定函数名称与函数形参类型列表所对应的类型信息列表，尝试获取该类型中匹配的静态成员函数的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 函数名称。
- parameterTypes: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[TypeInfo](reflect_package_classes.md#class-typeinfo)> - 函数形参类型列表所对应的类型信息列表。

返回值：

- [StaticFunctionInfo](reflect_package_classes.md#class-staticfunctioninfo) - 如果成功匹配则返回该静态成员函数的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 静态成员函数，则抛出异常。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public static func myName(): String { "" }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 TypeInfo，也可以通过实例获取 TypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取静态函数
    let sf = ty.getStaticFunction("myName")

    println(sf)
    return
}
```

运行结果：

```text
static func myName(): String
```

### func getStaticFunctions(String)

```cangjie
public func getStaticFunctions(name: String): Array<StaticFunctionInfo>
```

功能：给定函数名称，尝试获取该类型中所有匹配的静态成员函数的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 函数名称。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[StaticFunctionInfo](reflect_package_classes.md#class-staticfunctioninfo)> - 如果成功匹配则返回所有匹配到的静态成员函数信息。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public static func myName(): String { "" }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 TypeInfo，也可以通过实例获取 TypeInfo
    let ty = TypeInfo.get("test.Rectangular")

    // 获取静态函数
    let sf = ty.getStaticFunctions("myName")

    println(sf)
    return
}
```

运行结果：

```text
[static func myName(): String]
```