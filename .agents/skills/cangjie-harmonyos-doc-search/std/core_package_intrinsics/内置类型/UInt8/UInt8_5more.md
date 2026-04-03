## UInt8

功能：表示 8 位无符号整型，表示范围为 [0, 2^8 - 1]。

### extend UInt8

```cangjie
extend UInt8
```

功能：拓展 8 位无符号整数以支持一些数学常数。

#### static prop Max

```cangjie
public static prop Max: UInt8
```

功能：获取 8 位无符号整数的最大值。

类型：[UInt8](./core_package_intrinsics.md#uint8)

#### static prop Min

```cangjie
public static prop Min: UInt8
```

功能：获取 8 位无符号整数的最小值。

类型：[UInt8](./core_package_intrinsics.md#uint8)

### extend UInt8 <: Comparable\<UInt8>

```cangjie
extend UInt8 <: Comparable<UInt8>
```

功能：为 [UInt8](core_package_intrinsics.md#uint8) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt8](core_package_intrinsics.md#uint8)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[UInt8](#uint8)>

#### func compare(UInt8)

```cangjie
public func compare(rhs: UInt8): Ordering
```

功能：判断当前 [UInt8](core_package_intrinsics.md#uint8) 值与指定 [UInt8](core_package_intrinsics.md#uint8) 值的大小关系。

参数：

- rhs: [UInt8](core_package_intrinsics.md#uint8) - 待比较的另一个 [UInt8](core_package_intrinsics.md#uint8) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt8 = 2
    var num2: UInt8 = 3
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend UInt8 <: Countable\<UInt8>

```cangjie
extend UInt8 <: Countable<UInt8>
```

功能：为 [UInt8](core_package_intrinsics.md#uint8) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[UInt8](core_package_intrinsics.md#uint8)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[UInt8](#uint8)>

#### func next(Int64)

```cangjie
public func next(right: Int64): UInt8
```

功能：获取在数轴上当前 [UInt8](core_package_intrinsics.md#int32) 位置往右移动 `right` 后对应位置的 [UInt8](core_package_intrinsics.md#int32) 值。如果值溢出，则会从数轴最左边继续移动。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [UInt8](core_package_intrinsics.md#uint8) - 往右数 `right` 后所到位置的 [UInt8](core_package_intrinsics.md#uint8) 值。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt8 = 3
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

功能：获取当前 [UInt8](core_package_intrinsics.md#uint8) 值的位置信息，即将该 [UInt8](core_package_intrinsics.md#uint8) 转换为 [Int64](core_package_intrinsics.md#int64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [UInt8](core_package_intrinsics.md#uint8) 值的位置信息。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UInt8 = 8
    println(num.position())
}
```

运行结果：

```text
8
```

### extend UInt8 <: Hashable

```cangjie
extend UInt8 <: Hashable
```

功能：为 [UInt8](core_package_intrinsics.md#uint8) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。