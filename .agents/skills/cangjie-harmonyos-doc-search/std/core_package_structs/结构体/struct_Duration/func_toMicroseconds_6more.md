### func toMicroseconds()

```cangjie
public func toMicroseconds(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例以微秒为单位的整数大小。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例以微秒为单位的大小。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当 [Duration](core_package_structs.md#struct-duration) 实例以微秒为单位的大小超过 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 表示范围时，抛出异常。

### func toMilliseconds()

```cangjie
public func toMilliseconds(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例以毫秒为单位的整数大小。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例以毫秒为单位的大小。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当 [Duration](core_package_structs.md#struct-duration) 实例以毫秒为单位的大小超过 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 表示范围时，抛出异常。

### func toMinutes()

```cangjie
public func toMinutes(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例以分钟为单位的整数大小。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例以分钟为单位的大小。

### func toNanoseconds()

```cangjie
public func toNanoseconds(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例以纳秒为单位的整数大小，向绝对值小的方向取整。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例以纳秒为单位的大小。

异常：

- [ArithmeticException](../../core/core_package_api/core_package_exceptions.md#class-arithmeticexception) - 当 [Duration](core_package_structs.md#struct-duration) 实例以“纳秒”为单位的大小超过 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 表示范围时，抛出异常。

### func toSeconds()

```cangjie
public func toSeconds(): Int64
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例以秒为单位的整数大小。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前 [Duration](core_package_structs.md#struct-duration) 实例以秒为单位的大小。

### func toString()

```cangjie
public func toString(): String
```

功能：获得当前 [Duration](core_package_structs.md#struct-duration) 实例的字符串表示，格式形如："1d2h3m4s5ms6us7ns"，表示“1 天 2 小时 3 分钟 4 秒 5 毫秒 6 微秒 7 纳秒”。某个单位下数值为 0 时此项会被省略，特别地，当所有单位下数值都为 0 时，返回 "0s"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 当前 [Duration](core_package_structs.md#struct-duration) 实例的字符串表示。