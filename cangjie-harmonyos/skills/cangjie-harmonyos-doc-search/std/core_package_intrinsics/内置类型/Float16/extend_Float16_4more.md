### extend Float16

```cangjie
extend Float16
```

功能：支持与 [UInt16](core_package_intrinsics.md#uint16) 互相转换。

#### static func fromBits(UInt16)

```cangjie
public static func fromBits(bits: UInt16): Float16
```

功能：将指定的 [UInt16](core_package_intrinsics.md#uint16) 数转换为 [Float16](core_package_intrinsics.md#float16) 数。

参数：

- bits: [UInt16](core_package_intrinsics.md#uint16) - 要转换的数字。

返回值：

- [Float16](core_package_intrinsics.md#float16) - 转换结果，其位与参数 bits 值相同。

示例：

<!-- verify -->
```cangjie
main() {
    let v = Float16.fromBits(0x4A40)
    println(v)
}
```

运行结果：

```text
12.500000
```

#### func toBits()

```cangjie
public func toBits(): UInt16
```

功能：将指定的 [Float16](core_package_intrinsics.md#float16) 数转换为以位表示的对应 [UInt16](core_package_intrinsics.md#uint16) 数。

返回值：

- [UInt16](core_package_intrinsics.md#uint16) - 转换结果，其值与 [Float16](core_package_intrinsics.md#float16) 的位表示相同。

示例：

<!-- verify -->
```cangjie
main() {
    println(12.5f16.toBits()) // 0x4A40 19008
}
```

运行结果：

```text
19008
```

### extend Float16 <: Comparable\<Float16>

```cangjie
extend Float16 <: Comparable<Float16>
```

功能：为 [Float16](core_package_intrinsics.md#float16) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[Float16](core_package_intrinsics.md#float16)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[Float16](#float16)>

#### func compare(Float16)

```cangjie
public func compare(rhs: Float16): Ordering
```

功能：判断当前 [Float16](core_package_intrinsics.md#float16) 值与指定 [Float16](core_package_intrinsics.md#float16) 值的大小关系。

参数：

- rhs: [Float16](core_package_intrinsics.md#float16) - 待比较的另一个 [Float16](core_package_intrinsics.md#float16) 值。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: Float16 = 0.12
    var num2: Float16 = 0.234
    println(num1.compare(num2))
}
```

运行结果：

```text
Ordering.LT
```

### extend Float16 <: Hashable

```cangjie
extend Float16 <: Hashable
```

功能：为 [Float16](core_package_intrinsics.md#float16) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。

### extend Float16 <: ToString

```cangjie
extend Float16 <: ToString
```

功能：为 [Float16](core_package_intrinsics.md#float16) 类型其扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，实现向 [String](core_package_structs.md#struct-string) 类型的转换。默认保留 6 位小数。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [Float16](core_package_intrinsics.md#float16) 值转换为可输出的字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。