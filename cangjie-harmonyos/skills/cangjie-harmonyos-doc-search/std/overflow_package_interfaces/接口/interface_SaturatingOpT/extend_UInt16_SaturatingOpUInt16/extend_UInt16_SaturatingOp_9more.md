### extend UInt16 <: SaturatingOp\<UInt16>

```cangjie
extend UInt16 <: SaturatingOp<UInt16>
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 实现 [SaturatingOp](#interface-saturatingopt) 接口。

父类型：

- [SaturatingOp](#interface-saturatingopt)\<[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)>

#### func saturatingAdd(UInt16)

```cangjie
public func saturatingAdd(y: UInt16): UInt16
```

功能：使用饱和策略的加法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 加数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 加法运算结果。

#### func saturatingDec()

```cangjie
public func saturatingDec(): UInt16
```

功能：使用饱和策略的自减运算。

当运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 自减运算结果。

#### func saturatingDiv(UInt16)

```cangjie
public func saturatingDiv(y: UInt16): UInt16
```

功能：使用饱和策略的除法运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除法运算结果。

#### func saturatingInc()

```cangjie
public func saturatingInc(): UInt16
```

功能：使用饱和策略的自增运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 自增运算结果。

#### func saturatingMod(UInt16)

```cangjie
public func saturatingMod(y: UInt16): UInt16
```

功能：使用饱和策略的取余运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 取余运算结果。

#### func saturatingMul(UInt16)

```cangjie
public func saturatingMul(y: UInt16): UInt16
```

功能：使用饱和策略的乘法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 乘数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 乘法运算结果。

#### func saturatingNeg()

```cangjie
public func saturatingNeg(): UInt16
```

功能：使用饱和策略的负号运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 负号运算结果。

#### func saturatingShl(UInt64)

```cangjie
public func saturatingShl(y: UInt64): UInt16
```

功能：使用饱和策略的左移运算。

当移位位数大于等于操作数位数时，将移位位数置为操作数位数 - 1，返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 左移运算结果。