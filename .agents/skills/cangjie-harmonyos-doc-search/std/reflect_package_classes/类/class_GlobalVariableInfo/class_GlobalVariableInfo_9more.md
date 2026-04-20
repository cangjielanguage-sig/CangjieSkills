## class GlobalVariableInfo

```cangjie
public class GlobalVariableInfo <: Equatable<GlobalVariableInfo> & Hashable & ToString {}
```

功能：描述全局变量信息。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[GlobalVariableInfo](#class-globalvariableinfo)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop annotations

```cangjie
public prop annotations: Collection<Annotation>
```

功能：获取所有作用于该 [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) 对应的全局变量的注解，返回对应集合。

> **注意：**
>
> - 如果无任何注解作用于该全局变量信息所对应的全局变量，则返回空集合。
> - 该集合不保证遍历顺序恒定。

类型：[Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<[Annotation](../../ast/ast_package_api/ast_package_classes.md#class-annotation)>

### prop name

```cangjie
public prop name: String
```

功能：获取该 [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) 对应的全局变量的名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop typeInfo

```cangjie
public prop typeInfo: TypeInfo
```

功能：获取该 [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) 对应的全局变量的声明类型的类型信息。

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

功能：获取该 [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) 对应的全局变量的值。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 该全局变量的值。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取该全局变量信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该全局变量信息的哈希值。

### func isMutable()

```cangjie
public func isMutable(): Bool
```

功能：判断该 [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) 对应的全局变量是否可修改。

> **注意：**
>
> - 如果实例成员变量被 `var` 修饰符所修饰，则该全局变量可被修改。
> - 如果实例成员变量被 `let` 修饰符所修饰，则该全局变量不可被修改。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该全局变量可被修改则返回 `true` ，否则返回 `false`。

### func setValue(Any)

```cangjie
public func setValue(newValue: Any): Unit
```

功能：设置该 [GlobalVariableInfo](reflect_package_classes.md#class-globalvariableinfo) 对应的全局变量的值。

参数：

- newValue: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 新的值。

异常：

- [IllegalSetException](reflect_package_exceptions.md#class-illegalsetexception) - 如果该全局变量信息所对应的全局变量不可修改，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果新值 `newValue` 的运行时类型不是全局变量信息所对应的全局变量的声明类型的子类型，则抛出异常。