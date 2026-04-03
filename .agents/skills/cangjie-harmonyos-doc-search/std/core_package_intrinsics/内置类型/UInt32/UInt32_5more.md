## UInt32

功能：表示 32 位无符号整型，表示范围为 [0, 2^{32} - 1]。

### extend UInt32

```cangjie
extend UInt32
```

功能：拓展 32 位无符号整数以支持一些数学常数。

#### static prop Max

```cangjie
public static prop Max: UInt32
```

功能：获取 32 位无符号整数的最大值。

类型：[UInt32](./core_package_intrinsics.md#uint32)

#### static prop Min

```cangjie
public static prop Min: UInt32
```

功能：获取 32 位无符号整数的最小值。

类型：[UInt32](./core_package_intrinsics.md#uint32)

### extend UInt32 <: Comparable\<UInt32>

```cangjie
extend UInt32 <: Comparable<UInt32>
```

功能：为 [UInt32](core_package_intrinsics.md#uint32) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt32](core_package_intrinsics.md#uint32)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt32](#uint32)>

#### func compare(UInt32)

```cangjie
public func compare(rhs: UInt32): Ordering
```

功能：判断当前 [UInt32](core_package_intrinsics.md#uint32) 值与指定 [UInt32](core_package_intrinsics.md#uint32) 值的大小关系。

参数：

- rhs: [UInt32](core_package_intrinsics.md#uint32) - 待比较的另一个 [UInt32](core_package_intrinsics.md#uint32) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt32 = 2
    var num2: UInt32 = 3
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend UInt32 <: Countable\<UInt32>

```cangjie
extend UInt32 <: Countable<UInt32>
```

功能：为 [UInt32](core_package_intrinsics.md#uint32) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[UInt32](core_package_intrinsics.md#uint32)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[UInt32](#uint32)>

#### func next(Int64)

```cangjie
public func next(right: Int64): UInt32
```

功能：获取在数轴上当前 [UInt32](core_package_intrinsics.md#int32) 位置往右移动 `right` 后对应位置的 [UInt32](core_package_intrinsics.md#int32) 值。如果值溢出，则会从数轴最左边继续移动。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [UInt32](core_package_intrinsics.md#uint32) - 往右数 `right` 后所到位置的 [UInt32](core_package_intrinsics.md#uint32) 值。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt32 = 3
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

功能：获取当前 [UInt32](core_package_intrinsics.md#uint32) 值的位置信息，即将该 [UInt32](core_package_intrinsics.md#uint32) 转换为 [UInt64](core_package_intrinsics.md#uint64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [UInt32](core_package_intrinsics.md#uint32) 值的位置信息。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt32 = 8
    println(num.position())
}
```

运行结果：

```text
8
```

### extend UInt32 <: Hashable

```cangjie
extend UInt32 <: Hashable
```

功能：为 [UInt32](core_package_intrinsics.md#uint32) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。