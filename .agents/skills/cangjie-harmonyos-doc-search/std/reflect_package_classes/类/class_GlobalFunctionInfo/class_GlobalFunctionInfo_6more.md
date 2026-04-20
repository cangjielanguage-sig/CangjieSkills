## class GlobalFunctionInfo

```cangjie
public class GlobalFunctionInfo <: Equatable<GlobalFunctionInfo> & Hashable & ToString {}
```

功能：描述全局函数信息。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[GlobalFunctionInfo](#class-globalfunctioninfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop annotations

```cangjie
public prop annotations: Collection<Annotation>
```

功能：获取所有 [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) 对应的全局函数的注解，返回对应集合。

> **注意：**
>
> - 如果无任何注解作用于该全局函数信息所对应全局函数，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[Annotation](../../ast/ast_package_api/ast_package_classes.md#class-annotation)>

### prop genericParams

```cangjie
public prop genericParams: Collection<GenericTypeInfo>
```

功能：获取该 [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) 对应的实例成员函数的泛型参数信息列表。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[GenericTypeInfo](reflect_package_classes.md#class-generictypeinfo)>

异常：

- [InfoNotFoundException](./reflect_package_exceptions.md#class-infonotfoundexception) - [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) 没有泛型参数时抛出异常。

### prop name

```cangjie
public prop name: String
```

功能：获取该 [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) 对应的全局函数的名称。

> **注意：**
>
> 构成重载的所有全局函数将拥有相同的名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop parameters

```cangjie
public prop parameters: ReadOnlyList<ParameterInfo>
```

功能：获取该 [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) 对应的全局函数的参数信息列表。

> **注意：**
>
> 不保证参数顺序，可根据 `ParameterInfo`的 `index` 属性确定参数实际位置。

类型：[ReadOnlyList](../../collection/collection_package_api/collection_package_interface.md#interface-readonlylistt)\<[ParameterInfo](reflect_package_classes.md#class-parameterinfo)>

### prop returnType

```cangjie
public prop returnType: TypeInfo
```

功能：获取该 [GlobalFunctionInfo](reflect_package_classes.md#class-globalfunctioninfo) 对应的全局函数的返回类型的类型信息。

类型：[TypeInfo](reflect_package_classes.md#class-typeinfo)