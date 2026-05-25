### extend UIntNative <: SaturatingOp\<UIntNative>

```cangjie
extend UIntNative <: SaturatingOp<UIntNative>
```

功能：为 [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) 实现 [SaturatingOp](#interface-saturatingopt) 接口。

父类型：

- [SaturatingOp](#interface-saturatingopt)\<[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)>

#### func saturatingAdd(UIntNative)

```cangjie
public func saturatingAdd(y: UIntNative): UIntNative
```

功能：使用饱和策略的加法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 加数。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 加法运算结果。

#### func saturatingDec()

```cangjie
public func saturatingDec(): UIntNative
```

功能：使用饱和策略的自减运算。

当运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 自减运算结果。

#### func saturatingDiv(UIntNative)

```cangjie
public func saturatingDiv(y: UIntNative): UIntNative
```

功能：使用饱和策略的除法运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除数。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除法运算结果。

#### func saturatingInc()

```cangjie
public func saturatingInc(): UIntNative
```

功能：使用饱和策略的自增运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 自增运算结果。

#### func saturatingMod(UIntNative)

```cangjie
public func saturatingMod(y: UIntNative): UIntNative
```

功能：使用饱和策略的取余运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除数。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 取余运算结果。

#### func saturatingMul(UIntNative)

```cangjie
public func saturatingMul(y: UIntNative): UIntNative
```

功能：使用饱和策略的乘法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 乘数。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 乘法运算结果。

#### func saturatingNeg()

```cangjie
public func saturatingNeg(): UIntNative
```

功能：使用饱和策略的负号运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 负号运算结果。

#### func saturatingShl(UInt64)

```cangjie
public func saturatingShl(y: UInt64): UIntNative
```

功能：使用饱和策略的左移运算。

当移位位数大于等于操作数位数时，将移位位数置为操作数位数 - 1，返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 左移运算结果。