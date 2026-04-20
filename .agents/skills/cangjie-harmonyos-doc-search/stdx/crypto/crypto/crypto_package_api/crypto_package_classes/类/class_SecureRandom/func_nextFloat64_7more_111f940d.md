### func nextFloat64()

```cangjie
public func nextFloat64(): Float64
```

功能：获取一个 Float64 类型且在区间 [0.0, 1.0) 内的随机数。

返回值：

- Float64 - 一个 Float64 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextGaussianFloat16(Float16, Float16)

```cangjie
public func nextGaussianFloat16(mean!: Float16 = 0.0, sigma!: Float16 = 1.0): Float16
```

功能：默认获取一个 Float16 类型且符合均值为 0.0 标准差为 1.0 的高斯分布的随机数，其中均值是期望值，可解释为位置参数，决定了分布的位置，标准差可解释为尺度参数，决定了分布的幅度。

参数：

- mean!: Float16 - 均值。
- sigma!: Float16 - 标准差。

返回值：

- Float16 - 一个 Float16 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextGaussianFloat32(Float32, Float32)

```cangjie
public func nextGaussianFloat32(mean!: Float32 = 0.0, sigma!: Float32 = 1.0): Float32
```

功能：默认获取一个 Float32 类型且符合均值为 0.0 标准差为 1.0 的高斯分布的随机数，其中均值是期望值，可解释为位置参数，决定了分布的位置，标准差可解释为尺度参数，决定了分布的幅度。

参数：

- mean!: Float32 - 均值。
- sigma!: Float32 - 标准差。

返回值：

- Float32 - 一个 Float32 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextGaussianFloat64(Float64, Float64)

```cangjie
public func nextGaussianFloat64(mean!: Float64 = 0.0, sigma!: Float64 = 1.0): Float64
```

功能：默认获取一个 Float64 类型且符合均值为 0.0 标准差为 1.0 的高斯分布的随机数，其中均值是期望值，可解释为位置参数，决定了分布的位置，标准差可解释为尺度参数，决定了分布的幅度。

参数：

- mean!: Float64 - 均值。
- sigma!: Float64 - 标准差。

返回值：

- Float64 - 一个 Float64 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextInt16()

```cangjie
public func nextInt16(): Int16
```

功能：获取一个 Int16 类型的随机数。

返回值：

- Int16 - 一个 Int16 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextInt32()

```cangjie
public func nextInt32(): Int32
```

功能：获取一个 Int32 类型的随机数。

返回值：

- Int32 - 一个 Int32 类型的随机数。

异常：

- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。

### func nextInt16(Int16)

```cangjie
public func nextInt16(max: Int16): Int16
```

功能：获取一个 Int16 类型且在区间 [0, max) 内的随机数。

参数：

- max: Int16 - 区间最大值。

返回值：

- Int16 - 一个 Int16 类型的随机数。

异常：

- IllegalArgumentException - 当 max 为非正数时，抛出异常。
- [SecureRandomException](crypto_package_exceptions.md#class-securerandomexception) - 当生成器不能正确生成随机数或生成随机数失败时，抛出异常。