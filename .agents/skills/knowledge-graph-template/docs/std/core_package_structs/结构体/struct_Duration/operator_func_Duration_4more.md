### operator func !=(Duration)

```cangjie
public operator func !=(r: Duration): Bool
```

功能：判断当前 [Duration](core_package_structs.md#struct-duration) 实例是否不等于 `r`。

参数：

- r: [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [Duration](core_package_structs.md#struct-duration) 实例不等于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func *(Float64)

```cangjie
public operator func *(r: Float64): Duration
```

功能：实现 [Duration](core_package_structs.md#struct-duration) 类型与 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的乘法，即 [Duration](core_package_structs.md#struct-duration) * [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 运算。

参数：

- r: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 乘法的右操作数。

返回值：

- [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 类型实例和 `r` 的乘积。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相乘后的结果超出 [Duration](core_package_structs.md#struct-duration) 的表示范围时，抛出异常。

### operator func *(Int64)

```cangjie
public operator func *(r: Int64): Duration
```

功能：实现 [Duration](core_package_structs.md#struct-duration) 类型与 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的乘法，即 [Duration](core_package_structs.md#struct-duration) * [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 运算。

参数：

- r: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘法的右操作数。

返回值：

- [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 类型实例和 `r` 的乘积。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相乘后的结果超出 [Duration](core_package_structs.md#struct-duration) 的表示范围时，抛出异常。

### operator func +(Duration)

```cangjie
public operator func +(r: Duration): Duration
```

功能：实现 [Duration](core_package_structs.md#struct-duration) 类型之间的加法，即 [Duration](core_package_structs.md#struct-duration) + [Duration](core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](core_package_structs.md#struct-duration) - 加法的右操作数。

返回值：

- [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 类型实例和 `r` 的和。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相加后的结果超出 [Duration](core_package_structs.md#struct-duration) 的表示范围时，抛出异常。