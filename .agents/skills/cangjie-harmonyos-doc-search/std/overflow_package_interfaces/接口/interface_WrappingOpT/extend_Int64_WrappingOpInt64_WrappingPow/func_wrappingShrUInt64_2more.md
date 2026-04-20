#### func wrappingShr(UInt64)

```cangjie
public func wrappingShr(y: UInt64): Int64
```

功能：使用高位截断策略的右移运算。

当右操作数大于等于左操作数位数时，取右操作数的低 6 位作为移位位数。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 右移运算结果。

#### func wrappingSub(Int64)

```cangjie
public func wrappingSub(y: Int64): Int64
```

功能：使用高位截断策略的减法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 减数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 减法运算结果。