### extend Int64 <: CheckedOp\<Int64> & CheckedPow

```cangjie
extend Int64 <: CheckedOp<Int64> & CheckedPow
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 实现 [CheckedOp](#interface-checkedopt) 和 [CheckedPow](#interface-checkedpow) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>
- [CheckedPow](#interface-checkedpow)

#### func checkedAdd(Int64)

```cangjie
public func checkedAdd(y: Int64): ?Int64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).None，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 加数。

返回值：

- ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?Int64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).None，否则返回运算结果。

返回值：

- ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自减运算结果。

#### func checkedDiv(Int64)

```cangjie
public func checkedDiv(y: Int64): ?Int64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).None，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除数。

返回值：

- ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?Int64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).None，否则返回运算结果。

返回值：

- ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自增运算结果。

#### func checkedMod(Int64)

```cangjie
public func checkedMod(y: Int64): ?Int64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).None，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除数。

返回值：

- ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 取余运算结果。

#### func checkedMul(Int64)

```cangjie
public func checkedMul(y: Int64): ?Int64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).None，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘数。

返回值：

- ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘法运算结果。