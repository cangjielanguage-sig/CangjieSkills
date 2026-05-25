### extend IntNative <: CheckedOp\<IntNative>

```cangjie
extend IntNative <: CheckedOp<IntNative>
```

功能：为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 实现 [CheckedOp](#interface-checkedopt) 接口。

父类型：

- [CheckedOp](#interface-checkedopt)\<[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)>

#### func checkedAdd(IntNative)

```cangjie
public func checkedAdd(y: IntNative): ?IntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative).None，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 加数。

返回值：

- ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 加法运算结果。

#### func checkedDec()

```cangjie
public func checkedDec(): ?IntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative).None，否则返回运算结果。

返回值：

- ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 自减运算结果。

#### func checkedDiv(IntNative)

```cangjie
public func checkedDiv(y: IntNative): ?IntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative).None，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除法运算结果。

#### func checkedInc()

```cangjie
public func checkedInc(): ?IntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative).None，否则返回运算结果。

返回值：

- ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 自增运算结果。

#### func checkedMod(IntNative)

```cangjie
public func checkedMod(y: IntNative): ?IntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative).None，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 取余运算结果。

#### func checkedMul(IntNative)

```cangjie
public func checkedMul(y: IntNative): ?IntNative
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative).None，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 乘数。

返回值：

- ?[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 乘法运算结果。