## class TypeInfo

```cangjie
sealed abstract class TypeInfo <: Equatable<TypeInfo> & Hashable & ToString
```

功能：[TypeInfo](reflect_package_classes.md#class-typeinfo) 提供了所有数据类型通用的操作接口。开发者通常无需向下转型为更具体的数据类型，如 [ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 等，就能进行反射操作。

[TypeInfo](reflect_package_classes.md#class-typeinfo) 的子类包括 [PrimitiveTypeInfo](reflect_package_classes.md#class-primitivetypeinfo)、[StructTypeInfo](reflect_package_classes.md#class-structtypeinfo)、[ClassTypeInfo](reflect_package_classes.md#class-classtypeinfo) 和 [InterfaceTypeInfo](reflect_package_classes.md#class-interfacetypeinfo)，分别对应基本数据类型，`struct` 数据类型，`class` 数据类型和 `interface` 数据类型的类型信息。

> **说明：**
>
> 类型的限定名称为`(module_name/)?(default|package_name)(.package_name)*.(type_name)`。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TypeInfo](#class-typeinfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop annotations

```cangjie
public prop annotations: Collection<Annotation>
```

功能：获取所有作用于该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型的注解，返回对应集合。

> **注意：**
>
> - 如果无任何注解作用于该类型信息所对应的类型，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[Annotation](../../ast/ast_package_api/ast_package_classes.md#class-annotation)>

### prop instanceFunctions

```cangjie
public prop instanceFunctions: Collection<InstanceFunctionInfo>
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应类型的所有 `public` 实例成员函数信息，返回对应集合。

> **注意：**
>
> - 如果该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型无任何 `public` 实例成员函数，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 如果该类型信息所对应的类型是 `struct` 或 `class` 类型，则该集合不包含继承而来的实例成员函数的信息。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[InstanceFunctionInfo](reflect_package_classes.md#class-instancefunctioninfo)>

### prop instanceProperties

```cangjie
public prop instanceProperties: Collection<InstancePropertyInfo>
```

功能：获取该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应类型的所有 `public` 实例成员属性信息，返回对应集合。

> **注意：**
>
> - 如果该 [TypeInfo](reflect_package_classes.md#class-typeinfo) 对应的类型无任何 `public` 实例成员属性，则返回空集合。
> - 该集合不保证遍历顺序恒定。
> - 如果该类型信息所对应的类型是 `struct` 或 `class` 类型，则该集合不包含继承而来的实例成员属性的信息。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[InstancePropertyInfo](reflect_package_classes.md#class-instancepropertyinfo)>