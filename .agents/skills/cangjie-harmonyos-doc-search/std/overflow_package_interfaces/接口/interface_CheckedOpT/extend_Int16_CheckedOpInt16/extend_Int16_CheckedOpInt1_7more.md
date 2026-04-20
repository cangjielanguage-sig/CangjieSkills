### extend Int16 <: CheckedOp\<Int16>

```cangjie
extend Int16 <: CheckedOp<Int16>
```

功能：为 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)>

#### func checkedAdd(Int16)

```cangjie
public func checkedAdd(y: Int16): ?Int16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16).None，否则返回运算结果。

参数：

- y: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 加数。

返回值：

- ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?Int16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16).None，否则返回运算结果。

返回值：

- ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 自减运算结果。

#### func checkedDiv(Int16)

```cangjie
public func checkedDiv(y: Int16): ?Int16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16).None，否则返回运算结果。

参数：

- y: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 除数。

返回值：

- ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?Int16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16).None，否则返回运算结果。

返回值：

- ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 自增运算结果。

#### func checkedMod(Int16)

```cangjie
public func checkedMod(y: Int16): ?Int16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16).None，否则返回运算结果。

参数：

- y: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 除数。

返回值：

- ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 取余运算结果。

#### func checkedMul(Int16)

```cangjie
public func checkedMul(y: Int16): ?Int16
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16).None，否则返回运算结果。

参数：

- y: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 乘数。

返回值：

- ?[Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - 乘法运算结果。