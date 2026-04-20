### extend Int32 <: SaturatingOp\<Int32>

```cangjie
extend Int32 <: SaturatingOp<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 实现 [SaturatingOp](#interface-saturatingopt) 接口。

父类型：

- [SaturatingOp](#interface-saturatingopt)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### func saturatingAdd(Int32)

```cangjie
public func saturatingAdd(y: Int32): Int32
```

功能：使用饱和策略的加法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 加数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 加法运算结果。

#### func saturatingDec()

```cangjie
public func saturatingDec(): Int32
```

功能：使用饱和策略的自减运算。

当运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 自减运算结果。

#### func saturatingDiv(Int32)

```cangjie
public func saturatingDiv(y: Int32): Int32
```

功能：使用饱和策略的除法运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除法运算结果。

#### func saturatingInc()

```cangjie
public func saturatingInc(): Int32
```

功能：使用饱和策略的自增运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 自增运算结果。

#### func saturatingMod(Int32)

```cangjie
public func saturatingMod(y: Int32): Int32
```

功能：使用饱和策略的取余运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 取余运算结果。

#### func saturatingMul(Int32)

```cangjie
public func saturatingMul(y: Int32): Int32
```

功能：使用饱和策略的乘法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 乘数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 乘法运算结果。

#### func saturatingNeg()

```cangjie
public func saturatingNeg(): Int32
```

功能：使用饱和策略的负号运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 负号运算结果。

#### func saturatingShl(UInt64)

```cangjie
public func saturatingShl(y: UInt64): Int32
```

功能：使用饱和策略的左移运算。

当移位位数大于等于操作数位数时，将移位位数置为操作数位数 - 1，返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 左移运算结果。