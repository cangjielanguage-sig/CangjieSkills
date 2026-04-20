### func getConstructor(Array\<TypeInfo>)

```cangjie
public func getConstructor(parameterTypes: Array<TypeInfo>): ConstructorInfo
```

功能：尝试在该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型中获取与给定形参类型信息列表匹配的 `public` 构造函数的信息。

参数：

- parameterTypes: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[TypeInfo](reflect_package_classes.md#class-typeinfo)> - 形参类型信息列表。

返回值：

- [ConstructorInfo](reflect_package_classes.md#class-constructorinfo) - 如果成功匹配则返回该 `public` 构造函数的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应 `public` 构造函数，则抛出异常。

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
    public init(name: String) {
        myName = name
    }
    public init(name: String, length: Int64, width: Int64) {
        myName = name
        this.length = length
        this.width = width
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取指定构造函数信息
    let ci01 = ty.getConstructor(StructTypeInfo.get("String"))
    println(ci01)

    // 获取指定构造函数信息
    let ci02 = ty.getConstructor(StructTypeInfo.get("String"), PrimitiveTypeInfo.get("Int64"),
        PrimitiveTypeInfo.get("Int64"))
    println(ci02)
    return
}
```

运行结果：

```text
init(String)
init(String, Int64, Int64)
```

### func getInstanceVariable(String)

```cangjie
public func getInstanceVariable(name: String): InstanceVariableInfo
```

功能：给定变量名称，尝试获取该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 所对应的 `class` 类型中匹配的实例成员变量的信息。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 变量名称。

返回值：

- [InstanceVariableInfo](reflect_package_classes.md#class-instancevariableinfo) - 如果成功匹配则返回该实例成员变量的信息。

异常：

- [InfoNotFoundException](reflect_package_exceptions.md#class-infonotfoundexception) - 如果没找到对应实例成员变量，则抛出异常。

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

    // 获取类实例成员信息
    let ivi = ty.getInstanceVariable("myName")
    println(ivi)
    return
}
```

运行结果：

```text
myName: String
```