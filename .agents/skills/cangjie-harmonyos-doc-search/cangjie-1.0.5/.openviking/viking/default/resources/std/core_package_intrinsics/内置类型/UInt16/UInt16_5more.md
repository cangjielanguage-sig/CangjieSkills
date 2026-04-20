## UInt16

功能：表示 16 位无符号整型，表示范围为 [0, 2^{16} - 1]。

### extend UInt16

```cangjie
extend UInt16
```

功能：拓展 16 位无符号整数以支持一些数学常数。

#### static prop Max

```cangjie
public static prop Max: UInt16
```

功能：获取 16 位无符号整数的最大值。

类型：[UInt16](./core_package_intrinsics.md#uint16)

#### static prop Min

```cangjie
public static prop Min: UInt16
```

功能：获取 16 位无符号整数的最小值。

类型：[UInt16](./core_package_intrinsics.md#uint16)

### extend UInt16 <: Comparable\<UInt16>

```cangjie
extend UInt16 <: Comparable<UInt16>
```

功能：为 [UInt16](core_package_intrinsics.md#uint16) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt16](core_package_intrinsics.md#uint16)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt16](#uint16)>

#### func compare(UInt16)

```cangjie
public func compare(rhs: UInt16): Ordering
```

功能：判断当前 [UInt16](core_package_intrinsics.md#uint16) 值与指定 [UInt16](core_package_intrinsics.md#uint16) 值的大小关系。

参数：

- rhs: [UInt16](core_package_intrinsics.md#uint16) - 待比较的另一个 [UInt16](core_package_intrinsics.md#uint16) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt16 = 2
    var num2: UInt16 = 3
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend UInt16 <: Countable\<UInt16>

```cangjie
extend UInt16 <: Countable<UInt16>
```

功能：为 [UInt16](core_package_intrinsics.md#uint16) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[UInt16](core_package_intrinsics.md#uint16)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[UInt16](#uint16)>

#### func next(Int64)

```cangjie
public func next(right: Int64): UInt16
```

功能：获取在数轴上当前 [UInt16](core_package_intrinsics.md#int32) 位置往右移动 `right` 后对应位置的 [UInt16](core_package_intrinsics.md#int32) 值。如果值溢出，则会从数轴最左边继续移动。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [UInt16](core_package_intrinsics.md#uint16) - 往右数 `right` 后所到位置的 [UInt16](core_package_intrinsics.md#uint16) 值。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt16 = 3
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

功能：获取当前 [UInt16](core_package_intrinsics.md#uint16) 值的位置信息，即将该 [UInt16](core_package_intrinsics.md#uint16) 转换为 [Int64](core_package_intrinsics.md#int64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [UInt16](core_package_intrinsics.md#uint16) 值的位置信息。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt16 = 8
    println(num.position())
}
```

运行结果：

```text
8
```

### extend UInt16 <: Hashable

```cangjie
extend UInt16 <: Hashable
```

功能：为 [UInt16](core_package_intrinsics.md#uint16) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。