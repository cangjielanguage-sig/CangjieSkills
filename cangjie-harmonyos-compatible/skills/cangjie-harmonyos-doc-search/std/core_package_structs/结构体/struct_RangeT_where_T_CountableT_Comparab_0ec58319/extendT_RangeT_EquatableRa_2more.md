### extend\<T> Range\<T> <: Equatable\<Range\<T>> where T <: Countable\<T> & Comparable\<T> & Equatable\<T>

```cangjie
extend<T> Range<T> <: Equatable<Range<T>> where T <: Countable<T> & Comparable<T> & Equatable<T>
```

功能：为 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<T> 类型扩展 [Equatable](core_package_interfaces.md#interface-equatablet)\<[Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<T>> 接口。

父类型：

- [Equatable](core_package_interfaces.md#interface-equatablet)\<[Range](#struct-ranget-where-t--countablet--comparablet--equatablet)\<T>>

#### operator func ==(Range\<T>)

```cangjie
public operator func ==(that: Range<T>): Bool
```

功能：判断两个 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例是否相等。

两个 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例相等指的是它们表示同一个区间，即 `start`、`end`、[step](#let-step)、`isClosed` 值相等。

参数：

- that: [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<T> - 待比较的 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - true 代表相等，false 代表不相等。

### extend\<T> Range\<T> <: Hashable where T <: Hashable & Countable\<T> & Comparable\<T> & Equatable\<T>

```cangjie
extend<T> Range<T> <: Hashable where T <: Hashable & Countable<T> & Comparable<T> & Equatable<T>
```

功能：为 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值，该值为 `start`、`end`、[step](#let-step)、`isClosed` 的组合哈希运算结果。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。