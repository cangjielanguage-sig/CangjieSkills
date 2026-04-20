## class StaticPropertyInfo

```cangjie
public class StaticPropertyInfo <: Equatable<StaticPropertyInfo> & Hashable & ToString {}
```

功能：描述静态成员属性信息。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[StaticPropertyInfo](#class-staticpropertyinfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop annotations

```cangjie
public prop annotations: Collection<Annotation>
```

功能：获取所有作用于该 [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) 所对应的静态成员属性的注解所组成的集合。

> **注意：**
>
> - 如果无任何注解作用于该静态成员属性信息所对应的静态成员属性，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[Annotation](../../ast/ast_package_api/ast_package_classes.md#class-annotation)>

### prop modifiers

```cangjie
public prop modifiers: Collection<ModifierInfo>
```

功能：获取该 [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) 对应的静态成员属性所拥有的所有修饰符的信息，返回对应集合。

> **注意：**
>
> - 如果该静态成员属性无任何修饰符，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 目前获取到的修饰符集合内容较为混乱，尚未统一。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[ModifierInfo](reflect_package_enums.md#enum-modifierinfo)>

### prop name

```cangjie
public prop name: String
```

功能：获取该 [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) 对应的静态成员属性的名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop typeInfo

```cangjie
public prop typeInfo: TypeInfo
```

功能：获取该 [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) 对应的静态成员属性的声明类型的类型信息。

类型：[TypeInfo](reflect_package_classes.md#class-typeinfo)

### func findAnnotation\<T>() where T <: Annotation

```cangjie
public func findAnnotation<T>(): Option<T> where T <: Annotation
```

功能：尝试获取拥有给定限定名称且作用于该对象的注解。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 如果成功匹配则返回该注解，重复标注或者无法匹配时返回 `None`。

### func getValue()

```cangjie
public func getValue(): Any
```

功能：获取该 [StaticPropertyInfo](reflect_package_classes.md#class-staticpropertyinfo) 对应的静态成员属性的值。

> **注意：**
>
> 如果该静态成员属性缺少合法实现，如 `interface` 类型中的抽象静态成员属性，则应抛出 [UnsupportedException](../../core/core_package_api/core_package_exceptions.md#class-unsupportedexception) 异常，但由于后端尚未支持，故尚未实现。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该静态成员属性的值。

示例：

<!-- verify -->
```cangjie
package test

import std.reflect.*

public class Rectangular {
    public static prop sides: Int64 {
        get() { 4 }
    }
    public static prop angles: Int64 {
        get() { 4 }
    }
}

main(): Unit {
    // 此处是通过 Rectangular 的类型的限定名称获取 ClassTypeInfo，也可以通过实例获取 ClassTypeInfo
    let ty = ClassTypeInfo.get("test.Rectangular")

    // 获取静态属性
    let sp = ty.getStaticProperty("sides")

    let result = sp.getValue() as Int64
    println(result)
    return
}
```

运行结果：

```text
Some(4)
```