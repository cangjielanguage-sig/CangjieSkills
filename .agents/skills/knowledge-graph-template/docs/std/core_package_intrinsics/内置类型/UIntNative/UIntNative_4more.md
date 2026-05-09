## UIntNative

功能：表示平台相关的无符号整型，其长度与当前系统的位宽一致。

### extend UIntNative

```cangjie
extend UIntNative
```

功能：拓展平台相关无符号整数以支持一些数学常数。

#### static prop Max

```cangjie
public static prop Max: UIntNative
```

功能：获取平台相关无符号整数的最大值。

类型：[UIntNative](./core_package_intrinsics.md#uintnative)

#### static prop Min

```cangjie
public static prop Min: UIntNative
```

功能：获取平台相关无符号整数的最小值。

类型：[UIntNative](./core_package_intrinsics.md#uintnative)

### extend UIntNative <: Comparable\<UIntNative>

```cangjie
extend UIntNative <: Comparable<UIntNative>
```

功能：为 [UIntNative](core_package_intrinsics.md#uintnative) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[UIntNative](core_package_intrinsics.md#uintnative)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[UIntNative](#uintnative)>

#### func compare(UIntNative)

```cangjie
public func compare(rhs: UIntNative): Ordering
```

功能：判断当前 [UIntNative](core_package_intrinsics.md#uintnative) 值与指定 [UIntNative](core_package_intrinsics.md#uintnative) 值的大小关系。

参数：

- rhs: [UIntNative](core_package_intrinsics.md#uintnative) - 待比较的另一个 [UIntNative](core_package_intrinsics.md#uintnative) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UIntNative = 2
    var num2: UIntNative = 3
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend UIntNative <: Countable

```cangjie
extend UIntNative <: Countable<UIntNative>
```

功能：为 [UIntNative](core_package_intrinsics.md#uintnative) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[UIntNative](core_package_intrinsics.md#uintnative)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[UIntNative](#uintnative)>

#### func next(Int64)

```cangjie
public func next(right: Int64): UIntNative
```

功能：获取在数轴上当前 [UIntNative](core_package_intrinsics.md#int32) 位置往右移动 `right` 后对应位置的 [UIntNative](core_package_intrinsics.md#int32) 值。如果值溢出，则会从数轴最左边继续移动。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [UIntNative](core_package_intrinsics.md#uintnative) - 往右数 `right` 后所到位置的 [UIntNative](core_package_intrinsics.md#uintnative) 值。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UIntNative = 3
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

功能：获取当前 [UIntNative](core_package_intrinsics.md#uintnative) 值的位置信息，即将该 [UIntNative](core_package_intrinsics.md#uintnative) 转换为 [Int64](core_package_intrinsics.md#int64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [UIntNative](core_package_intrinsics.md#uintnative) 值的位置信息。

示例：

<!-- verify -->
```cangjie
main() {
    var num: UIntNative = 8
    println(num.position())
}
```

运行结果：

```text
8
```