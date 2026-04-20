## struct TupleWrapper4\<T0, T1, T2, T3>

```cangjie
public struct TupleWrapper4<T0, T1, T2, T3> {
    public TupleWrapper4(public let tuple: (T0, T1, T2, T3))
}
```

功能：将闭包封装为结构体。闭包带两个参数。

### TupleWrapper4((T0, T1, T2, T3))

```cangjie
public TupleWrapper4(public let tuple: (T0, T1, T2, T3))
```

功能：TupleWrapper4 构造器。

参数：

- tuple: (T0, T1, T2, T3) - 闭包的 4 个入参。

### let tuple

```cangjie
public let tuple: (T0, T1, T2, T3)
```

功能：元组自身。

类型：(T0, T1, T2, T3)

### func apply\<R>((T0, T1, T2, T3) -> R)

```cangjie
public func apply<R>(f: (T0, T1, T2, T3) -> R): R
```

功能：执行闭包函数。

参数：

- f: (T0, T1, T2, T3) -> R - 待执行的闭包。

返回值：

- R - 闭包的执行结果。

### extend\<T0, T1, T2, T3> TupleWrapper4\<T0, T1, T2, T3> <: ToString

```cangjie
extend<T0, T1, T2, T3> TupleWrapper4<T0, T1, T2, T3> <: ToString
```

功能：为 [TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3) 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 实现。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString()
```

功能：[TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3) 的字符串表达。

### extend\<T0, T1, T2, T3> TupleWrapper4\<T0, T1, T2, T3> <: Equatable\<TupleWrapper4\<T0, T1, T2, T3>>

```cangjie
extend<T0, T1, T2> TupleWrapper3<T0, T1, T2> <: Equatable<TupleWrapper3<T0, T1, T2>>
```

功能：为 [TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3) 扩展 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet) 实现。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TupleWrapper3](#struct-tuplewrapper3t0-t1-t2)\<T0, T1, T2>>

#### operator func ==(TupleWrapper4\<T0, T1, T2, T3>)

```cangjie
public operator func ==(other: TupleWrapper4<T0, T1, T2, T3>): Bool
```

功能：比较两个元组。

参数：

- other: TupleWrapper4\<T0, T1, T2, T3> - 待比较的元组。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 相等时返回 `true` ，否则返回 `false` 。

#### operator func !=(TupleWrapper4\<T0, T1, T2, T3>)

```cangjie
public operator func !=(other: TupleWrapper4<T0, T1, T2, T3>): Bool
```

功能：比较两个元组。

参数：

- other: [TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3)\<T0, T1, T2, T3> - 待比较的元组。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 不相等时返回 `true` ，否则返回 `false` 。

### extend\<T0, T1, T2, T3> TupleWrapper4\<T0, T1, T2, T3> <: IndexAccess

```cangjie
extend<T0, T1, T2, T3> TupleWrapper4<T0, T1, T2, T3> <: IndexAccess
```

功能：为 [TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3) 扩展 [IndexAccess](./unittest_prop_test_package_interfaces.md#interface-indexaccess) 实现。

父类型：

- [IndexAccess](unittest_prop_test_package_interfaces.md#interface-indexaccess)

#### func getElementAsAny(Int64)

```cangjie
public func getElementAsAny(index: Int64): ?Any
```

功能：按索引获取元组内的值。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 索引值。

返回值：

- ?[Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 获取到的元组内的值。索引不合法时返回 `None` 。