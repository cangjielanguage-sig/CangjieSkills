### func apply(Array\<Any>)

```cangjie
public func apply(args: Array<Any>): Any
```

功能：调用该 [ConstructorInfo](reflect_package_classes.md#class-constructorinfo) 对应的构造函数，传入实参列表，并返回调用结果。

参数：

- args: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Any](../../core/core_package_api/core_package_interfaces.md#interface-any)> - 实参列表。

返回值：

- [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 由该构造函数构造得到的类型实例。

异常：

- [InvocationTargetException](reflect_package_exceptions.md#class-invocationtargetexception) - 如果该构造函数信息所对应的构造函数所属的类型是抽象类，则会抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果实参列表 `args` 中的实参的数目与该构造函数信息所对应的构造函数的形参列表中的形参的数目不等，则抛出异常。
- [IllegalTypeException](reflect_package_exceptions.md#class-illegaltypeexception) - 如果实参列表 `args` 中的任何一个实参的运行时类型不是该构造函数信息所对应的构造函数的对应形参的声明类型的子类型，则抛出异常。
- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 如果被调用的构造函数信息所对应的构造函数内部抛出异常，则该异常将被封装为 [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) 异常并抛出。

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

功能：获取该构造器信息的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 该构造器信息的哈希值。

### func toString()

```cangjie
public func toString(): String
```

功能：获取字符串形式的该构造函数信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的该构造函数信息。

### operator func !=(ConstructorInfo)

```cangjie
public operator func !=(that: ConstructorInfo): Bool
```

功能：判断该构造器信息与给定的另一个构造器信息是否不等。

参数：

- that: [ConstructorInfo](reflect_package_classes.md#class-constructorinfo) - 被比较相等性的另一个构造器信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该构造器信息与 `that` 不等则返回 `true`，否则返回 `false`。

### operator func ==(ConstructorInfo)

```cangjie
public operator func ==(that: ConstructorInfo): Bool
```

功能：判断该构造器信息与给定的另一个构造器信息是否相等。

参数：

- that: [ConstructorInfo](reflect_package_classes.md#class-constructorinfo) - 被比较相等性的另一个构造器信息。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果该构造器信息与 `that` 相等则返回 `true`，否则返回 `false`。