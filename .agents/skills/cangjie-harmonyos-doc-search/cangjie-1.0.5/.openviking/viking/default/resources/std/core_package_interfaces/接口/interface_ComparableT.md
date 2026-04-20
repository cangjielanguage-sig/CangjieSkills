## interface Comparable\<T>

```cangjie
public interface Comparable<T> <: Equatable<T> & Less<T> & Greater<T> & LessOrEqual<T> & GreaterOrEqual<T> {
    func compare(that: T): Ordering
    operator func <(rhs: T): Bool
    operator func <=(rhs: T): Bool
    operator func ==(rhs: T): Bool
    operator func >(rhs: T): Bool
    operator func >=(rhs: T): Bool
}
```

功能：该接口表示比较运算，是等于、不等于、小于、大于、小于等于、大于等于接口的集合体。

该接口中提供运算符 ==、!=、<、<=、>、>= 重载的默认实现，默认实现根据 compare 函数的返回值来确定其返回值。例如：如果 a.compare(b) 的返回值为 EQ，则 a == b 返回 true，否则返回 false。

父类型：

- [Equatable](#interface-equatablet)\<T>
- [Less](#interface-lesst)\<T>
- [Greater](#interface-greatert)\<T>
- [LessOrEqual](#interface-lessorequalt)\<T>
- [GreaterOrEqual](#interface-greaterorequalt)\<T>

### func compare(T)

```cangjie
func compare(that: T): Ordering
```

功能：判断当前 `T` 类型实例与参数指向的 `T` 类型实例的大小关系。

参数：

- that: T - 待与当前实例比较的另一个实例。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT，如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ，如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

### operator func <(T)

```cangjie
operator func <(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否小于参数指向的 `T` 类型实例，该函数是此接口的一个默认实现函数。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果小于，返回 true，否则返回 false。

### operator func <=(T)

```cangjie
operator func <=(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否小于等于参数指向的 `T` 类型实例，该函数是此接口的一个默认实现函数。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果小于等于，返回 true，否则返回 false。

### operator func ==(T)

```cangjie
operator func ==(rhs: T): Bool
```

功能：判断两个实例是否相等，该函数是此接口的一个默认实现函数。

参数：

- rhs: T - 待比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果相等，返回 true，否则返回 false。

### operator func >(T)

```cangjie
operator func >(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否大于参数指向的 `T` 类型实例，该函数是此接口的一个默认实现函数。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果大于，返回 true，否则返回 false。

### operator func >=(T)

```cangjie
operator func >=(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否大于等于参数指向的 `T` 类型实例，该函数是此接口的一个默认实现函数。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果大于等于，返回 true，否则返回 false。