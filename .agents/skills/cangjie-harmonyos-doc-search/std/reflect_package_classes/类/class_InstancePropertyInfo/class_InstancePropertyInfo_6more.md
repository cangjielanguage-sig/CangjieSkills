## class InstancePropertyInfo

```cangjie
public class InstancePropertyInfo <: Equatable<InstancePropertyInfo> & Hashable & ToString {}
```

功能：描述实例成员属性信息。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[InstancePropertyInfo](#class-instancepropertyinfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop annotations

```cangjie
public prop annotations: Collection<Annotation>
```

功能：获取所有作用于该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性的注解，返回对应集合。

> **注意：**
>
> - 如果无任何注解作用于该实例成员属性信息所对应的实例成员属性，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[Annotation](../../ast/ast_package_api/ast_package_classes.md#class-annotation)>

### prop modifiers

```cangjie
public prop modifiers: Collection<ModifierInfo>
```

功能：获取该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性所拥有的所有修饰符的信息，返回对应集合。

> **注意：**
>
> - 如果该实例成员属性无任何修饰符，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 即便未被某修饰符修饰，如果拥有该修饰符的语义，该修饰符信息也将被包括在该集合中。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[ModifierInfo](reflect_package_enums.md#enum-modifierinfo)>

### prop name

```cangjie
public prop name: String
```

功能：获取该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性的名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop typeInfo

```cangjie
public prop typeInfo: TypeInfo
```

功能：获取该 [InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo) 对应的实例成员属性的声明类型的类型信息。

类型：[TypeInfo](reflect_package_classes.md#class-typeinfo)

### func findAnnotation\<T>() where T <: Annotation

```cangjie
public func findAnnotation<T>(): Option<T> where T <: Annotation
```

功能：尝试获取拥有给定限定名称且作用于该对象的注解。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 如果成功匹配则返回该注解，重复标注或者无法匹配时返回 `None`。