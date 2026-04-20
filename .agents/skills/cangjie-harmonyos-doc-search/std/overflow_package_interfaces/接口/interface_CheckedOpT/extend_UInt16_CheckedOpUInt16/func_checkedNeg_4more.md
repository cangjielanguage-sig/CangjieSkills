#### func checkedNeg()

```cangjie
public func checkedNeg(): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的负号运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 负号运算结果。

#### func checkedShl(UInt64)

```cangjie
public func checkedShl(y: UInt64): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的左移运算。

当移位位数大于等于操作数位数时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 左移运算结果。

#### func checkedShr(UInt64)

```cangjie
public func checkedShr(y: UInt64): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的右移运算。

当移位位数大于等于操作数位数时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 右移运算结果。

#### func checkedSub(UInt16)

```cangjie
public func checkedSub(y: UInt16): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的减法运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 减数。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 减法运算结果。