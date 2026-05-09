### extend Float64

```cangjie
extend Float64
```

功能：支持与 [UInt64](core_package_intrinsics.md#uint64) 互相转换。

#### static func fromBits(UInt64)

```cangjie
public static func fromBits(bits: UInt64): Float64
```

功能：将指定的 [UInt64](core_package_intrinsics.md#uint64) 数转换为 [Float64](core_package_intrinsics.md#float64) 数。

参数：

- bits: [UInt64](core_package_intrinsics.md#uint64) - 要转换的数字。

返回值：

- [Float64](core_package_intrinsics.md#float64) - 转换结果，其位与参数 bits 值相同。

示例：

<!-- verify -->
```cangjie
main() {
    let v = Float64.fromBits(0x402BC28F5C28F5C3)
    println(v)
}
```

运行结果：

```text
13.880000
```

#### func toBits()

```cangjie
public func toBits(): UInt64
```

功能：将指定的 Float64 数转换为以位表示的对应 [UInt64](core_package_intrinsics.md#uint64) 数。

返回值：

- [UInt64](core_package_intrinsics.md#uint64) - 转换结果，其值与 [Float64](core_package_intrinsics.md#float64) 的位表示相同。

示例：

<!-- verify -->
```cangjie
main() {
    println(13.88f64.toBits()) // 0x402BC28F5C28F5C3 4624003363408246211
}
```

运行结果：

```text
4624003363408246211
```

### extend Float64 <: Comparable\<Float64>

```cangjie
extend Float64 <: Comparable<Float64>
```

功能：为 [Float64](core_package_intrinsics.md#float64) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[Float64](core_package_intrinsics.md#float64)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[Float64](#float64)>

#### func compare(Float64)

```cangjie
public func compare(rhs: Float64): Ordering
```

功能：判断当前 [Float64](core_package_intrinsics.md#float64) 值与指定 [Float64](core_package_intrinsics.md#float64) 值的大小关系。

参数：

- rhs: [Float64](core_package_intrinsics.md#float64) - 待比较的另一个 [Float64](core_package_intrinsics.md#float64) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Float64 = 0.12
    var num2: Float64 = 0.234
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend Float64 <: Hashable

```cangjie
extend Float64 <: Hashable
```

功能：为 [Float64](core_package_intrinsics.md#float64) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。

### extend Float64 <: ToString

```cangjie
extend Float64 <: ToString
```

功能：为 [Float64](core_package_intrinsics.md#float64) 类型其扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，实现向 [String](core_package_structs.md#struct-string) 类型的转换。默认保留 6 位小数。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [Float64](core_package_intrinsics.md#float64) 值转换为可输出的字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。