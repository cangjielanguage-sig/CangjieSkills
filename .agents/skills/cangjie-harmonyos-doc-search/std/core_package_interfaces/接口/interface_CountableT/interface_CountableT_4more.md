## interface Countable\<T>

```cangjie
public interface Countable<T> {
    func next(right: Int64): T
    func position(): Int64
}
```

功能：该接口表示类型可数。

可数类型的每一个实例都对应一个位置信息（[Int64](core_package_intrinsics.md#int64) 值），可以通过往后数数得到其他的该类型实例。

### func next(Int64)

```cangjie
func next(right: Int64): T
```

功能：获取当前实例向右移动 `right` 后对应位置的 `T` 类型实例。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- T - 向右移动 `right` 后对应位置的 `T` 类型实例。

### func position()

```cangjie
func position(): Int64
```

功能：获取当前可数实例的位置信息，即将当前实例转为 [Int64](core_package_intrinsics.md#int64) 类型。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 转换后的 [Int64](core_package_intrinsics.md#int64) 值。

### extend Float64

```cangjie
extend Float64
```

功能：拓展了 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型作为左操作数和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型作为右操作数的乘法运算。

#### operator func *(Duration)

```cangjie
public operator func *(r: Duration): Duration
```

功能：实现 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型的乘法，即 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) * [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 实例。

返回值：

- [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型实例和 `r` 的乘积。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相乘后的结果超出 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 的表示范围时，抛出异常。