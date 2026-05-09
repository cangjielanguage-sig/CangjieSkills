## IntNative

功能：表示平台相关的有符号整型，其长度与当前系统的位宽一致。

### extend IntNative

```cangjie
extend IntNative
```

功能：拓展平台相关有符号整数以支持一些数学常数。

#### static prop Max

```cangjie
public static prop Max: IntNative
```

功能：获取平台相关有符号整数的最大值。

类型：[IntNative](./core_package_intrinsics.md#intnative)

#### static prop Min

```cangjie
public static prop Min: IntNative
```

功能：获取平台相关有符号整数的最小值。

类型：[IntNative](./core_package_intrinsics.md#intnative)

### extend IntNative <: Comparable\<IntNative>

```cangjie
extend IntNative <: Comparable<IntNative>
```

功能：为 [IntNative](core_package_intrinsics.md#intnative) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[IntNative](core_package_intrinsics.md#intnative)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[IntNative](#intnative)>

#### func compare(IntNative)

```cangjie
public func compare(rhs: IntNative): Ordering
```

功能：判断当前 [IntNative](core_package_intrinsics.md#intnative) 值与指定 [IntNative](core_package_intrinsics.md#intnative) 值的大小关系。

参数：

- rhs: [IntNative](core_package_intrinsics.md#intnative) - 待比较的另一个 [IntNative](core_package_intrinsics.md#intnative) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: IntNative = 8
    var num2: IntNative = 10
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend IntNative <: Countable\<IntNative>

```cangjie
extend IntNative <: Countable<IntNative>
```

功能：为 [IntNative](core_package_intrinsics.md#intnative) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[IntNative](core_package_intrinsics.md#intnative)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[IntNative](#intnative)>

#### func next(Int64)

```cangjie
public func next(right: Int64): IntNative
```

功能：获取在数轴上当前 [IntNative](core_package_intrinsics.md#int32) 位置往右移动 `right` 后对应位置的 [IntNative](core_package_intrinsics.md#int32) 值。如果值溢出，则会从数轴最左边继续移动。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [IntNative](core_package_intrinsics.md#intnative) - 往右数 `right` 后所到位置的 [IntNative](core_package_intrinsics.md#intnative) 值。

示例：

<!-- verify -->
```cangjie
main() {
    var num: IntNative = 8
    println(num.next(4))
}
```

运行结果：

```text
12
```

#### func position()

```cangjie
public func position(): Int64
```

功能：获取当前 [IntNative](core_package_intrinsics.md#intnative) 值的位置信息，即将该 [IntNative](core_package_intrinsics.md#intnative) 转换为 [Int64](core_package_intrinsics.md#int64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [IntNative](core_package_intrinsics.md#intnative) 值的位置信息。

示例：

<!-- verify -->
```cangjie
main() {
    var num: IntNative = 8
    println(num.position())
}
```

运行结果：

```text
8
```