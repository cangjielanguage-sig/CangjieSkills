## class ParameterInfo

```cangjie
public class ParameterInfo <: Equatable<ParameterInfo> & Hashable & ToString {}
```

功能：描述函数形参信息。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[ParameterInfo](#class-parameterinfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop annotations

```cangjie
public prop annotations: Collection<Annotation>
```

功能：获取所有作用于该 [ParameterInfo](reflect_package_classes.md#class-parameterinfo) 对应的函数形参的注解，返回对应集合。

> **注意：**
>
> - 如果无任何注解作用于该函数形参信息所对应的函数形参，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[Annotation](../../ast/ast_package_api/ast_package_classes.md#class-annotation)>

### prop index

```cangjie
public prop index: Int64
```

功能：获知该 [ParameterInfo](reflect_package_classes.md#class-parameterinfo) 对应的形参是其所在函数的第几个形参。

> **注意：**
>
> `index` 从 0 开始计数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### prop name

```cangjie
public prop name: String
```

功能：获取该 [ParameterInfo](reflect_package_classes.md#class-parameterinfo) 对应的形参的名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop typeInfo

```cangjie
public prop typeInfo: TypeInfo
```

功能：获取该 [ParameterInfo](reflect_package_classes.md#class-parameterinfo) 对应的函数形参的声明类型所对应的类型信息。

类型：[TypeInfo](reflect_package_classes.md#class-typeinfo)

### func findAnnotation\<T>() where T <: Annotation

```cangjie
public func findAnnotation<T>(): Option<T> where T <: Annotation
```

功能：尝试获取拥有给定限定名称且作用于该对象的注解。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 如果成功匹配则返回该注解，重复标注或者无法匹配时返回 `None`。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取该函数形参信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该函数形参信息的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该函数形参信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该函数形参信息。

### operator func !=(ParameterInfo)

```cangjie
public operator func !=(that: ParameterInfo): Bool
```

功能：判断该函数形参信息与给定的另一个函数形参信息是否不等。

参数：

- that: [ParameterInfo](reflect_package_classes.md#class-parameterinfo) - 被比较相等性的另一个函数形参信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该函数形参信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(ParameterInfo)

```cangjie
public operator func ==(that: ParameterInfo): Bool
```

功能：判断该函数形参信息与给定的另一个函数形参信息是否相等。

参数：

- that: [ParameterInfo](reflect_package_classes.md#class-parameterinfo) - 被比较相等性的另一个函数形参信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该函数形参信息与 `that` 相等则返回 `true`，否则返回 `false`。