### func nextBytes(Int32)

```cangjie
public func nextBytes(length: Int32): Array<Byte>
```

功能：生成指定长度的随机数数组。

参数：

- length: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 生成的随机数数组长度，`length` 大于 0。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 生成的随机数数组。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `length` 小于等于 0 时，抛出异常。

### func nextFloat16()

```cangjie
public func nextFloat16(): Float16
```

功能：获取一个 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型的伪随机数，其范围为 [0.0, 1.0)。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 一个 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Float16 = m.nextFloat16()
    if (n is Float16) {
        println("n is Float16")
    }
    return 0
}
```

运行结果：

```text
n is Float16
```

### func nextFloat32()

```cangjie
public func nextFloat32(): Float32
```

功能：获取一个 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型的伪随机数，其范围为 [0.0, 1.0)。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 一个 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Float32 = m.nextFloat32()
    if (n is Float32) {
        println("n is Float32")
    }
    return 0
}
```

运行结果：

```text
n is Float32
```

### func nextFloat64()

```cangjie
public func nextFloat64(): Float64
```

功能：获取一个 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的伪随机数，其范围为 [0.0, 1.0)。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 一个 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Float64 = m.nextFloat64()
    if (n is Float64) {
        println("n is Float64")
    }
    return 0
}
```

运行结果：

```text
n is Float64
```

### func nextGaussianFloat16(Float16, Float16)

```cangjie
public func nextGaussianFloat16(mean!: Float16 = 0.0, sigma!: Float16 = 1.0): Float16
```

功能：获取一个 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型的符合指定均值与标准差的高斯分布的随机数。

默认获取一个 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型且符合均值为 0.0 标准差为 1.0 的高斯分布的随机数。其中均值是期望值，可解释为位置参数，决定了分布的位置，标准差可解释为尺度参数，决定了分布的幅度。

参数：

- mean!: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 均值，默认值 0.0。
- sigma!: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 标准差，默认值 1.0。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 一个 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型的随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Float16 = m.nextGaussianFloat16(mean: 0.0, sigma: 1.0)
    if (n is Float16) {
        println("n is Float16")
    }
    return 0
}
```

运行结果：

```text
n is Float16
```