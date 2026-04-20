### extend UInt64 <: CheckedOp\<UInt64>

```cangjie
extend UInt64 <: CheckedOp<UInt64>
```

功能：为 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)>

#### func checkedAdd(UInt64)

```cangjie
public func checkedAdd(y: UInt64): ?UInt64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64).None，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 加数。

返回值：

- ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?UInt64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64).None，否则返回运算结果。

返回值：

- ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 自减运算结果。

#### func checkedDiv(UInt64)

```cangjie
public func checkedDiv(y: UInt64): ?UInt64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64).None，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 除数。

返回值：

- ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?UInt64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64).None，否则返回运算结果。

返回值：

- ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 自增运算结果。

#### func checkedMod(UInt64)

```cangjie
public func checkedMod(y: UInt64): ?UInt64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64).None，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 除数。

返回值：

- ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 取余运算结果。

#### func checkedMul(UInt64)

```cangjie
public func checkedMul(y: UInt64): ?UInt64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64).None，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 乘数。

返回值：

- ?[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 乘法运算结果。