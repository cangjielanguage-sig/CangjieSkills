### extend UIntNative <: CheckedOp\<UIntNative>

```cangjie
extend UIntNative <: CheckedOp<UIntNative>
```

功能：为 [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)>

#### func checkedAdd(UIntNative)

```cangjie
public func checkedAdd(y: UIntNative): ?UIntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative).None，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 加数。

返回值：

- ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?UIntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative).None，否则返回运算结果。

返回值：

- ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 自减运算结果。

#### func checkedDiv(UIntNative)

```cangjie
public func checkedDiv(y: UIntNative): ?UIntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative).None，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除数。

返回值：

- ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?UIntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative).None，否则返回运算结果。

返回值：

- ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 自增运算结果。

#### func checkedMod(UIntNative)

```cangjie
public func checkedMod(y: UIntNative): ?UIntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative).None，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除数。

返回值：

- ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 取余运算结果。

#### func checkedMul(UIntNative)

```cangjie
public func checkedMul(y: UIntNative): ?UIntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative).None，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 乘数。

返回值：

- ?[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 乘法运算结果。