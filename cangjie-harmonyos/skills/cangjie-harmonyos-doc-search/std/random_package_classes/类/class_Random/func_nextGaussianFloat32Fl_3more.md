### func nextGaussianFloat32(Float32, Float32)

```cangjie
public func nextGaussianFloat32(mean!: Float32 = 0.0, sigma!: Float32 = 1.0): Float32
```

功能：获取一个 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型的符合指定均值与标准差的高斯分布的随机数。

默认获取一个 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型且符合均值为 0.0 标准差为 1.0 的高斯分布的随机数。其中均值是期望值，可解释为位置参数，决定了分布的位置，标准差可解释为尺度参数，决定了分布的幅度。

参数：

- mean!: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 均值，默认值 0.0。
- sigma!: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 标准差，默认值 1.0。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 一个 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型的随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Float32 = m.nextGaussianFloat32(mean: 0.0, sigma: 1.0)
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

### func nextGaussianFloat64(Float64, Float64)

```cangjie
public func nextGaussianFloat64(mean!: Float64 = 0.0, sigma!: Float64 = 1.0): Float64
```

功能：获取一个 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的符合指定均值与标准差的高斯分布的随机数。

默认获取一个 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型且符合均值为 0.0 标准差为 1.0 的高斯分布的随机数。其中均值是期望值，可解释为位置参数，决定了分布的位置，标准差可解释为尺度参数，决定了分布的幅度。

参数：

- mean!: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 均值，默认值 0.0。
- sigma!: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 标准差，默认值 1.0。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 一个 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Float64 = m.nextGaussianFloat64(mean: 0.0, sigma: 1.0)
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

### func nextInt16()

```cangjie
public func nextInt16(): Int16
```

功能：获取一个 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型的伪随机数。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 一个 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型的伪随机数。

示例：
<!-- verify -->
```cangjie
import std.random.*

main() {
    let m: Random = Random()
    let n: Int16 = m.nextInt16()
    if (n is Int16) {
        println("n is Int16")
    }
    return 0
}
```

运行结果：

```text
n is Int16
```