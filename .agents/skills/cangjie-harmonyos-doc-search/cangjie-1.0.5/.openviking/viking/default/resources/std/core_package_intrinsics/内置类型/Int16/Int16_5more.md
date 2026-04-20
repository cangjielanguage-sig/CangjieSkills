## Int16

功能：表示 16 位有符号整型，表示范围为 [-2^{15}, 2^{15} - 1]。

### extend Int16

```cangjie
extend Int16
```

功能：拓展 16 位有符号整数以支持一些数学常数。

#### static prop Max

```cangjie
public static prop Max: Int16
```

功能：获取 16 位有符号整数的最大值。

类型：[Int16](./core_package_intrinsics.md#int16)

#### static prop Min

```cangjie
public static prop Min: Int16
```

功能：获取 16 位有符号整数的最小值。

类型：[Int16](./core_package_intrinsics.md#int16)

### extend Int16 <: Comparable\<Int16>

```cangjie
extend Int16 <: Comparable<Int16>
```

功能：为 [Int16](core_package_intrinsics.md#int16) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[Int16](core_package_intrinsics.md#int16)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[Int16](#int16)>

#### func compare(Int16)

```cangjie
public func compare(rhs: Int16): Ordering
```

功能：判断当前 [Int16](core_package_intrinsics.md#int16) 值与指定 [Int16](core_package_intrinsics.md#int16) 值的大小关系。

参数：

- rhs: [Int16](core_package_intrinsics.md#int16) - 待比较的另一个 [Int16](core_package_intrinsics.md#int16) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int16 = 2
    var num2: Int16 = 3
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend Int16 <: Countable\<Int16>

```cangjie
extend Int16 <: Countable<Int16>
```

功能：为 [Int16](core_package_intrinsics.md#int16) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[Int16](core_package_intrinsics.md#int16)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[Int16](#int16)>

#### func next(Int64)

```cangjie
public func next(right: Int64): Int16
```

功能：获取在数轴上当前 [Int16](core_package_intrinsics.md#int16) 位置往右移动 `right` 后对应位置的 [Int16](core_package_intrinsics.md#int16) 值。如果值溢出，则会从数轴最左边继续移动。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [Int16](core_package_intrinsics.md#int16) - 往右数 `right` 后所到位置的 [Int16](core_package_intrinsics.md#int16) 值。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int16 = 32767
    var num2: Int16 = 3
    println(num1.next(5))
    println(num2.next(10))
}
```

运行结果：

```text
-32764
13
```

#### func position()

```cangjie
public func position(): Int64
```

功能：获取当前 [Int16](core_package_intrinsics.md#int16) 值的位置信息，即将该 [Int16](core_package_intrinsics.md#int16) 转换为 [Int64](core_package_intrinsics.md#int64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [Int16](core_package_intrinsics.md#int16) 值的位置信息。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Int16 = 32767
    var num2: Int16 = 3
    println(num1.position())
    println(num2.position())
}
```

运行结果：

```text
32767
3
```

### extend Int16 <: Hashable

```cangjie
extend Int16 <: Hashable
```

功能：为 [Int16](core_package_intrinsics.md#int16) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。