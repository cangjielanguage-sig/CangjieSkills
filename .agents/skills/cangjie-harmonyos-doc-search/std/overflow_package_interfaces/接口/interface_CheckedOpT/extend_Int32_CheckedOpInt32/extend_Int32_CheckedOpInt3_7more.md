### extend Int32 <: CheckedOp\<Int32>

```cangjie
extend Int32 <: CheckedOp<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### func checkedAdd(Int32)

```cangjie
public func checkedAdd(y: Int32): ?Int32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).None，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 加数。

返回值：

- ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?Int32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).None，否则返回运算结果。

返回值：

- ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 自减运算结果。

#### func checkedDiv(Int32)

```cangjie
public func checkedDiv(y: Int32): ?Int32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).None，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?Int32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).None，否则返回运算结果。

返回值：

- ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 自增运算结果。

#### func checkedMod(Int32)

```cangjie
public func checkedMod(y: Int32): ?Int32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).None，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 取余运算结果。

#### func checkedMul(Int32)

```cangjie
public func checkedMul(y: Int32): ?Int32
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).None，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 乘数。

返回值：

- ?[Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 乘法运算结果。