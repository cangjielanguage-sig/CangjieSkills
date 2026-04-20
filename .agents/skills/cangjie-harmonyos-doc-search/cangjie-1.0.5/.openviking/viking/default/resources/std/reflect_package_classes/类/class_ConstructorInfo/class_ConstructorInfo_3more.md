## class ConstructorInfo

```cangjie
public class ConstructorInfo <: Equatable<ConstructorInfo> & Hashable & ToString {}
```

功能：描述构造函数信息。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[ConstructorInfo](#class-constructorinfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop annotations

```cangjie
public prop annotations: Collection<Annotation>
```

功能：获取所有作用于该 [ConstructorInfo](reflect_package_classes.md#class-constructorinfo) 对应的构造函数的注解，返回对应集合。

> **注意：**
>
> - 如果无任何注解作用于该构造函数信息所对应的构造函数，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[Annotation](../../ast/ast_package_api/ast_package_classes.md#class-annotation)>

### prop parameters

```cangjie
public prop parameters: ReadOnlyList<ParameterInfo>
```

功能：获取该 [ConstructorInfo](reflect_package_classes.md#class-constructorinfo) 所对应的构造函数的参数类型列表。

> **注意：**
>
> 不保证参数顺序，可根据 `ParameterInfo`的 `index` 属性确定参数实际位置。

类型：[ReadOnlyList](../../collection/collection_package_api/collection_package_interface.md#interface-readonlylistt)\<[ParameterInfo](reflect_package_classes.md#class-parameterinfo)>

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
    // 获取 constructors
    for (i in ty.constructors) {
        // 获取 parameters
        for (j in i.parameters) {
            println("${i} 的入参有 ${j}")
        }
    }
    return
}
```

运行结果：

```text
init(String) 的入参有 String
init(String, Int64, Int64) 的入参有 String
init(String, Int64, Int64) 的入参有 Int64
init(String, Int64, Int64) 的入参有 Int64
```