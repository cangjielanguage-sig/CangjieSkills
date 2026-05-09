#### func wrappingSub(UInt8)

```cangjie
public func wrappingSub(y: UInt8): UInt8
```

功能：使用高位截断策略的减法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 减数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 减法运算结果。