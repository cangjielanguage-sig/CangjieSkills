#### func throwingNeg()

```cangjie
public func throwingNeg(): UInt32
```

功能：使用抛出异常策略的负号运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 负号运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当负号运算出现溢出时，抛出异常。

#### func throwingShl(UInt64)

```cangjie
public func throwingShl(y: UInt64): UInt32
```

功能：使用抛出异常策略的左移运算。

当移位位数大于等于操作数位数时，抛出异常，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 左移运算结果。

异常：

- [OvershiftException](overflow_package_exceptions.md#class-overshiftexception) - 当移位位数大于等于操作数位数时，抛出异常。

#### func throwingShr(UInt64)

```cangjie
public func throwingShr(y: UInt64): UInt32
```

功能：右移运算。

当移位位数大于等于操作数位数时，抛出异常，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 右移运算结果。

异常：

- [OvershiftException](overflow_package_exceptions.md#class-overshiftexception) - 当移位位数大于等于操作数位数时，抛出异常。

#### func throwingSub(UInt32)

```cangjie
public func throwingSub(y: UInt32): UInt32
```

功能：使用抛出异常策略的减法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 减数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 减法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当减法运算出现溢出时，抛出异常。