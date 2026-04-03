### operator func -(Duration)

```cangjie
public operator func -(r: Duration): Duration
```

功能：实现 [Duration](core_package_structs.md#struct-duration) 类型之间的减法，即 [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](core_package_structs.md#struct-duration) - 减法的右操作数。

返回值：

- [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 类型实例和 `r` 的差。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相减后的结果超出 [Duration](core_package_structs.md#struct-duration) 的表示范围时，抛出异常。

### operator func /(Duration)

```cangjie
public operator func /(r: Duration): Float64
```

功能：实现 [Duration](core_package_structs.md#struct-duration) 类型与 [Duration](core_package_structs.md#struct-duration) 类型的除法，即 [Duration](core_package_structs.md#struct-duration) / [Duration](core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](core_package_structs.md#struct-duration) - 除数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - [Duration](core_package_structs.md#struct-duration) 类型实例和 `r` 的商。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `r` 等于 [Duration](core_package_structs.md#struct-duration).Zero 时，抛出异常。

### operator func /(Float64)

```cangjie
public operator func /(r: Float64): Duration
```

功能：实现 [Duration](core_package_structs.md#struct-duration) 类型与 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的除法，即 [Duration](core_package_structs.md#struct-duration) / [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 运算。

参数：

- r: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 除数。

返回值：

- [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 类型实例和 `r` 的商。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `r` 等于 0 时，抛出异常。
- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相除后的结果超出 [Duration](core_package_structs.md#struct-duration) 的表示范围时，抛出异常。

### operator func /(Int64)

```cangjie
public operator func /(r: Int64): Duration
```

功能：实现 [Duration](core_package_structs.md#struct-duration) 类型与 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的除法，即 [Duration](core_package_structs.md#struct-duration) / [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 运算。

参数：

- r: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除数。

返回值：

- [Duration](core_package_structs.md#struct-duration) - [Duration](core_package_structs.md#struct-duration) 类型实例和 `r` 的商。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `r` 等于 0 时，抛出异常。
- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当相除后的结果超出 [Duration](core_package_structs.md#struct-duration) 的表示范围时，抛出异常。