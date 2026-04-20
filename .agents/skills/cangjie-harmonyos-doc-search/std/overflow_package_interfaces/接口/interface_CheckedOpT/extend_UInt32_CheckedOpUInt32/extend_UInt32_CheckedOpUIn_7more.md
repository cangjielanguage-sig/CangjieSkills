### extend UInt32 <: CheckedOp\<UInt32>

```cangjie
extend UInt32 <: CheckedOp<UInt32>
```

功能：为 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)>

#### func checkedAdd(UInt32)

```cangjie
public func checkedAdd(y: UInt32): ?UInt32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32).None，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 加数。

返回值：

- ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?UInt32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32).None，否则返回运算结果。

返回值：

- ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 自减运算结果。

#### func checkedDiv(UInt32)

```cangjie
public func checkedDiv(y: UInt32): ?UInt32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32).None，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 除数。

返回值：

- ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?UInt32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32).None，否则返回运算结果。

返回值：

- ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 自增运算结果。

#### func checkedMod(UInt32)

```cangjie
public func checkedMod(y: UInt32): ?UInt32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32).None，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 除数。

返回值：

- ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 取余运算结果。

#### func checkedMul(UInt32)

```cangjie
public func checkedMul(y: UInt32): ?UInt32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32).None，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 乘数。

返回值：

- ?[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 乘法运算结果。