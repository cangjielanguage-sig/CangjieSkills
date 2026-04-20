## class ClassTypeInfo

```cangjie
public class ClassTypeInfo <: TypeInfo {}
```

功能：描述 `class` 类型的类型信息。

父类型：

- [TypeInfo](#class-typeinfo)

### prop constructors

```cangjie
public prop constructors: Collection<ConstructorInfo>
```

功能：获取该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 的所有 `public` 构造函数信息，返回对应集合。

> **注意：**
>
> - 如果该 `class` 类型无任何 `public` 构造函数，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[ConstructorInfo](reflect_package_classes.md#class-constructorinfo)>

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public var myName = ""
    public init() {}
    public init(name: String) {
        myName = name
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")
    // 获取 constructors
    for (i in ty.constructors) {
        println(i)
    }
    return
}
```

运行结果：

```text
init()
init(String)
```

### prop instanceVariables

```cangjie
public prop instanceVariables: Collection<InstanceVariableInfo>
```

功能：获取该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 的所有 `public` 实例成员变量信息，返回对应集合。

> **注意：**
>
> - 如果该 `class` 类型无任何 `public` 实例成员变量，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 该集合不包含任何继承而来的 `public` 实例成员变量。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[InstanceVariableInfo](reflect_package_classes.md#class-instancevariableinfo)>

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
    // 获取 instanceVariables
    for (i in ty.instanceVariables) {
        println(i)
    }
    return
}
```

运行结果：

```text
length: Int64
width: Int64
myName: String
```

### prop sealedSubclasses

```cangjie
public prop sealedSubclasses: Collection<ClassTypeInfo>
```

功能：如果该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 类型拥有 `sealed` 语义，则获取该 `class` 类型所在包内的所有子类的类型信息，返回对应集合。

> **注意：**
>
> - 如果该 `class` 类型不拥有 `sealed` 语义，则返回空集合。
> - 如果该 `class` 类型拥有 `sealed` 语义，那么获得的集合必不可能是空集合，因为该 `class` 类型本身就是自己的子类。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo)>

### prop staticVariables

```cangjie
public prop staticVariables: Collection<StaticVariableInfo>
```

功能：获取该 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 对应的 `class` 的所有 `public` 静态成员变量信息，返回对应集合。

> **注意：**
>
> - 如果该 `class` 类型无任何 `public` 静态成员变量，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 该集合不包含任何继承而来的 `public` 静态成员变量。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[StaticVariableInfo](reflect_package_classes.md#class-staticvariableinfo)>