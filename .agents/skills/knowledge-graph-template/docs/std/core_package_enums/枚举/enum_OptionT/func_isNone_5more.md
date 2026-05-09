### func isNone()

```cangjie
public func isNone(): Bool
```

功能：判断当前实例值是否为 [None](#none)。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果当前实例值是 [None](#none)，则返回 true，否则返回 false。

### func isSome()

```cangjie
public func isSome(): Bool
```

功能：判断当前实例值是否为 [Some](#somet)。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果当前实例值是 [Some](#somet)，则返回 true，否则返回 false。

### func map\<R>((T)->R)

```cangjie
public func map<R>(transform: (T)-> R): Option<R>
```

功能：提供从 [Option](#enum-optiont)\<T> 类型到 [Option](#enum-optiont)\<R> 类型的映射函数，如果当前实例值是 [Some](#somet)，执行 transform 函数，并且返回 [Some](#somet) 封装的结果，否则返回 [None](#none)。

参数：

- transform: (T)-> R - 映射函数。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<R> - 如果当前实例值是 [Some](#somet)，执行 transform 函数，并且返回 [Option](#enum-optiont)\<R> 类型的结果，否则返回 [None](#none)。

### extend\<T> Option\<Option\<T>>

```cangjie
extend<T> Option<Option<T>>
```

功能：为 Option\<Option\<T>> 类型扩展实现某些功能。

#### func flatten()

```cangjie
public func flatten(): Option<T>
```

功能：将 [Option](core_package_enums.md#enum-optiont)\<[Option](core_package_enums.md#enum-optiont)\<T>> 类型展开，如果当前实例是 [Some](#somet)([Option](core_package_enums.md#enum-optiont)\<T>.[Some](#somet)(v)), 展开后的结果为 [Some](#somet)(v)。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<T> - [Option](core_package_enums.md#enum-optiont)\<[Option](core_package_enums.md#enum-optiont)\<T>> 类型展开后的结果。

### extend\<T> Option\<T> <: Equatable\<Option\<T>> where T <: Equatable\<T>

```cangjie
extend<T> Option<T> <: Equatable<Option<T>> where T <: Equatable<T>
```

功能：为 [Option](core_package_enums.md#enum-optiont)\<T> 枚举扩展 [Equatable](core_package_interfaces.md#interface-equatablet)\<[Option](core_package_enums.md#enum-optiont)\<T>> 接口，支持判等操作。

父类型：

- [Equatable](core_package_interfaces.md#interface-equatablet)\<[Option](#enum-optiont)\<T>>

#### operator func !=(Option\<T>)

```cangjie
public operator func !=(that: Option<T>): Bool
```

功能：判断当前实例与参数指向的 [Option](core_package_enums.md#enum-optiont)\<T> 实例是否不等。

参数：

- that: [Option](core_package_enums.md#enum-optiont)\<T> - 待比较的 [Option](core_package_enums.md#enum-optiont)\<T> 实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果不相等，则返回 true，否则返回 false。

#### operator func ==(Option\<T>)

```cangjie
public operator func ==(that: Option<T>): Bool
```

功能：判断当前实例与参数指向的 [Option](core_package_enums.md#enum-optiont)\<T> 实例是否相等。

如果两者同为 None，则相等；如果两者为 Some(v1) 和 Some(v2)，且 v1 和 v2 相等，则相等。

参数：

- that: [Option](core_package_enums.md#enum-optiont)\<T> - 待比较的 [Option](core_package_enums.md#enum-optiont)\<T> 实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果相等，则返回 true，否则返回 false。