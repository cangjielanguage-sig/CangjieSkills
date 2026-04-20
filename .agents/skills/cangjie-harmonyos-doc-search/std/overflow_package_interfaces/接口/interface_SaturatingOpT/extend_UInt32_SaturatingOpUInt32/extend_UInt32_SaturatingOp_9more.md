### extend UInt32 <: SaturatingOp\<UInt32>

```cangjie
extend UInt32 <: SaturatingOp<UInt32>
```

功能：为 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 实现 [SaturatingOp](#interface-saturatingopt) 接口。

父类型：

- [SaturatingOp](#interface-saturatingopt)\<[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)>

#### func saturatingAdd(UInt32)

```cangjie
public func saturatingAdd(y: UInt32): UInt32
```

功能：使用饱和策略的加法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 加数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 加法运算结果。

#### func saturatingDec()

```cangjie
public func saturatingDec(): UInt32
```

功能：使用饱和策略的自减运算。

当运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 自减运算结果。

#### func saturatingDiv(UInt32)

```cangjie
public func saturatingDiv(y: UInt32): UInt32
```

功能：使用饱和策略的除法运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 除数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 除法运算结果。

#### func saturatingInc()

```cangjie
public func saturatingInc(): UInt32
```

功能：使用饱和策略的自增运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 自增运算结果。

#### func saturatingMod(UInt32)

```cangjie
public func saturatingMod(y: UInt32): UInt32
```

功能：使用饱和策略的取余运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 除数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 取余运算结果。

#### func saturatingMul(UInt32)

```cangjie
public func saturatingMul(y: UInt32): UInt32
```

功能：使用饱和策略的乘法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 乘数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 乘法运算结果。

#### func saturatingNeg()

```cangjie
public func saturatingNeg(): UInt32
```

功能：使用饱和策略的负号运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 负号运算结果。

#### func saturatingShl(UInt64)

```cangjie
public func saturatingShl(y: UInt64): UInt32
```

功能：使用饱和策略的左移运算。

当移位位数大于等于操作数位数时，将移位位数置为操作数位数 - 1，返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 左移运算结果。