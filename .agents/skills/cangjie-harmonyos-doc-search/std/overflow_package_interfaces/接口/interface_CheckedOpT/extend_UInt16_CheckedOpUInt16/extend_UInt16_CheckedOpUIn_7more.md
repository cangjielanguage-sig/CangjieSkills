### extend UInt16 <: CheckedOp\<UInt16>

```cangjie
extend UInt16 <: CheckedOp<UInt16>
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)>

#### func checkedAdd(UInt16)

```cangjie
public func checkedAdd(y: UInt16): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 加数。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 自减运算结果。

#### func checkedDiv(UInt16)

```cangjie
public func checkedDiv(y: UInt16): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除数。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 自增运算结果。

#### func checkedMod(UInt16)

```cangjie
public func checkedMod(y: UInt16): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除数。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 取余运算结果。

#### func checkedMul(UInt16)

```cangjie
public func checkedMul(y: UInt16): ?UInt16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16).None，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 乘数。

返回值：

- ?[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 乘法运算结果。