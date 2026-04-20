### extend UInt8 <: CheckedOp\<UInt8>

```cangjie
extend UInt8 <: CheckedOp<UInt8>
```

功能：为 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)>

#### func checkedAdd(UInt8)

```cangjie
public func checkedAdd(y: UInt8): ?UInt8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8).None，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 加数。

返回值：

- ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?UInt8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8).None，否则返回运算结果。

返回值：

- ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 自减运算结果。

#### func checkedDiv(UInt8)

```cangjie
public func checkedDiv(y: UInt8): ?UInt8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8).None，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除数。

返回值：

- ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?UInt8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8).None，否则返回运算结果。

返回值：

- ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 自增运算结果。

#### func checkedMod(UInt8)

```cangjie
public func checkedMod(y: UInt8): ?UInt8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8).None，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除数。

返回值：

- ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 取余运算结果。

#### func checkedMul(UInt8)

```cangjie
public func checkedMul(y: UInt8): ?UInt8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8).None，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 乘数。

返回值：

- ?[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 乘法运算结果。