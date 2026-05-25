### operator func +(Duration)

```cangjie
public operator func +(r: Duration): MonoTime
```

功能：实现 [MonoTime](time_package_structs.md#struct-monotime) 类型和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型加法，即 [MonoTime](time_package_structs.md#struct-monotime) + [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 时间间隔。

返回值：

- [MonoTime](time_package_structs.md#struct-monotime) - 参数 `r` 表示时间间隔后的单调时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当结果超过单调时间的表示范围时，抛出异常。

### operator func -(Duration)

```cangjie
public operator func -(r: Duration): MonoTime
```

功能：实现 [MonoTime](time_package_structs.md#struct-monotime) 类型和 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 类型减法，即 [MonoTime](time_package_structs.md#struct-monotime) - [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 运算。

参数：

- r: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 时间间隔。

返回值：

- [MonoTime](time_package_structs.md#struct-monotime) - 参数 `r` 表示时间间隔前的单调时间。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当结果超过单调时间的表示范围时，抛出异常。

### operator func -(MonoTime)

```cangjie
public operator func -(r: MonoTime): Duration
```

功能：实现 [MonoTime](time_package_structs.md#struct-monotime) 类型之间的减法，即 [MonoTime](time_package_structs.md#struct-monotime) - [MonoTime](time_package_structs.md#struct-monotime) 运算。

参数：

- r: [MonoTime](time_package_structs.md#struct-monotime) - 单调时间。

返回值：

- [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 当前实例距 `r` 经过的时间间隔。

### operator func <(MonoTime)

```cangjie
public operator func <(r: MonoTime): Bool
```

功能：判断当前 [MonoTime](time_package_structs.md#struct-monotime) 实例是否早于 `r`。

参数：

- r: [MonoTime](time_package_structs.md#struct-monotime) - 单调时间。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [MonoTime](time_package_structs.md#struct-monotime) 实例早于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func <=(MonoTime)

```cangjie
public operator func <=(r: MonoTime): Bool
```

功能：判断当前 [MonoTime](time_package_structs.md#struct-monotime) 实例是否早于或等于 `r`。

参数：

- r: [MonoTime](time_package_structs.md#struct-monotime) - 单调时间。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [MonoTime](time_package_structs.md#struct-monotime) 实例早于或等于 `r` 时，返回 `true`；否则，返回 `false`。

### operator func ==(MonoTime)

```cangjie
public operator func ==(r: MonoTime): Bool
```

功能：判断当前 [MonoTime](time_package_structs.md#struct-monotime) 实例是否等于 `r`。

参数：

- r: [MonoTime](time_package_structs.md#struct-monotime) - 单调时间。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - `true` 或 `false`。当前 [MonoTime](time_package_structs.md#struct-monotime) 实例等于 `r` 时，返回 `true`；否则，返回 `false`。