### init(Float64)

```cangjie
public init(n: Float64)
```

功能：通过双精度浮点数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

将丢弃浮点数的小数部分，即向零取整。

参数：

- n: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 单精度浮点数。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 n 为 `Inf` 或 `NaN`，则抛此异常。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let float64: Float64 = 24.8
    let bigInt = BigInt(float64)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(Int16)

```cangjie
public init(n: Int16)
```

功能：通过 16 位有符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 16 位有符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let int16: Int16 = 24
    let bigInt = BigInt(int16)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(Int32)

```cangjie
public init(n: Int32)
```

功能：通过 32 位有符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 32 位有符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let int32: Int32 = 24
    let bigInt = BigInt(int32)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(Int64)

```cangjie
public init(n: Int64)
```

功能：通过 64 位有符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 64 位有符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let int64: Int64 = 24
    let bigInt = BigInt(int64)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(Int8)

```cangjie
public init(n: Int8)
```

功能：通过 8 位有符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 8 位有符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let int8: Int8 = 24
    let bigInt = BigInt(int8)
    println(bigInt)
}
```

运行结果：

```text
24
```

### init(IntNative)

```cangjie
public init(n: IntNative)
```

功能：通过平台相关有符号整数构建一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 结构体。

参数：

- n: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 平台相关有符号整数。

示例：

<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let intNative: IntNative = 24
    let bigInt = BigInt(intNative)
    println(bigInt)
}
```

运行结果：

```text
24
```