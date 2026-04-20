## UInt64

功能：表示 64 位无符号整型，表示范围为 [0, 2^{64} - 1]。

### extend UInt64

```cangjie
extend UInt64
```

功能：拓展 64 位无符号整数以支持一些数学常数。

#### static prop Max

```cangjie
public static prop Max: UInt64
```

功能：获取 64 位无符号整数的最大值。

类型：[UInt64](./core_package_intrinsics.md#uint64)

#### static prop Min

```cangjie
public static prop Min: UInt64
```

功能：获取 64 位无符号整数的最小值。

类型：[UInt64](./core_package_intrinsics.md#uint64)

### extend UInt64 <: Comparable\<UInt64>

```cangjie
extend UInt64 <: Comparable<UInt64>
```

功能：为 [UInt64](core_package_intrinsics.md#uint64) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt64](core_package_intrinsics.md#uint64)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt64](#uint64)>

#### func compare(UInt64)

```cangjie
public func compare(rhs: UInt64): Ordering
```

功能：判断当前 [UInt64](core_package_intrinsics.md#uint64) 值与指定 [UInt64](core_package_intrinsics.md#uint64) 值的大小关系。

参数：

- rhs: [UInt64](core_package_intrinsics.md#uint64) - 待比较的另一个 [UInt64](core_package_intrinsics.md#uint64) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt64 = 2
    var num2: UInt64 = 3
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend UInt64 <: Countable\<UInt64>

```cangjie
extend UInt64 <: Countable<UInt64>
```

功能：为 [UInt64](core_package_intrinsics.md#uint64) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[UInt64](core_package_intrinsics.md#uint64)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[UInt64](#uint64)>

#### func next(Int64)

```cangjie
public func next(right: Int64): UInt64
```

功能：获取在数轴上当前 [UInt64](core_package_intrinsics.md#int32) 位置往右移动 `right` 后对应位置的 [UInt64](core_package_intrinsics.md#int32) 值。如果值溢出，则会从数轴最左边继续移动。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [UInt64](core_package_intrinsics.md#uint64) - 往右数 `right` 后所到位置的 [UInt64](core_package_intrinsics.md#uint64) 值。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt64 = 3
    println(num.next(10))
}
```

运行结果：

```text
13
```

#### func position()

```cangjie
public func position(): Int64
```

功能：获取当前 [UInt64](core_package_intrinsics.md#uint64) 值的位置信息，即将该 [UInt64](core_package_intrinsics.md#uint64) 转换为 [Int64](core_package_intrinsics.md#int64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [UInt64](core_package_intrinsics.md#uint64) 值的位置信息。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt64 = 8
    println(num.position())
}
```

运行结果：

```text
8
```

### extend UInt64 <: Hashable

```cangjie
extend UInt64 <: Hashable
```

功能：为 [UInt64](core_package_intrinsics.md#uint64) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。