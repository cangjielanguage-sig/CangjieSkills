### extend Int8 <: CheckedOp\<Int8>

```cangjie
extend Int8 <: CheckedOp<Int8>
```

功能：为 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)>

#### func checkedAdd(Int8)

```cangjie
public func checkedAdd(y: Int8): ?Int8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8).None，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 加数。

返回值：

- ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?Int8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8).None，否则返回运算结果。

返回值：

- ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 自减运算结果。

#### func checkedDiv(Int8)

```cangjie
public func checkedDiv(y: Int8): ?Int8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8).None，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 除数。

返回值：

- ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?Int8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8).None，否则返回运算结果。

返回值：

- ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 自增运算结果。

#### func checkedMod(Int8)

```cangjie
public func checkedMod(y: Int8): ?Int8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8).None，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 除数。

返回值：

- ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 取余运算结果。

#### func checkedMul(Int8)

```cangjie
public func checkedMul(y: Int8): ?Int8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8).None，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 乘数。

返回值：

- ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 乘法运算结果。

#### func checkedNeg()

```cangjie
public func checkedNeg(): ?Int8
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的负号运算。

当运算出现溢出时，返回 ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8).None，否则返回运算结果。

返回值：

- ?[Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 负号运算结果。