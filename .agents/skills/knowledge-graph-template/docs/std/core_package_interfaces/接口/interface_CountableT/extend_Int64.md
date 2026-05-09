### extend Int64

```cangjie
extend Int64
```

功能：拓展了 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型作为左操作数和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型作为右操作数的乘法运算。

#### operator func *(Duration)

```cangjie
public operator func *(r: Duration): Duration
```

功能：实现 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型的乘法，即 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) * [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 运算。

例如 2 * [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).second 返回表示时间间隔为 2 秒的 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 实例。

参数：

- r: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 乘法的右操作数。

返回值：

- [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型实例和 `r` 的乘积。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相乘后的结果超出 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 的表示范围时，抛出异常。