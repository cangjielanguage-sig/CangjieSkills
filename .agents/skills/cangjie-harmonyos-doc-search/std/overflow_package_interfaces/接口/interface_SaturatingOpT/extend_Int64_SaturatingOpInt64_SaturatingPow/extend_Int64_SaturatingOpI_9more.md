### extend Int64 <: SaturatingOp\<Int64> & SaturatingPow

```cangjie
extend Int64 <: SaturatingOp<Int64> & SaturatingPow
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 实现 [SaturatingOp](#interface-saturatingopt) 和 [SaturatingPow](#interface-saturatingpow) 接口。

父类型：

- [SaturatingOp](#interface-saturatingopt)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>
- [SaturatingPow](#interface-saturatingpow)

#### func saturatingAdd(Int64)

```cangjie
public func saturatingAdd(y: Int64): Int64
```

功能：使用饱和策略的加法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 加数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 加法运算结果。

#### func saturatingDec()

```cangjie
public func saturatingDec(): Int64
```

功能：使用饱和策略的自减运算。

当运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自减运算结果。

#### func saturatingDiv(Int64)

```cangjie
public func saturatingDiv(y: Int64): Int64
```

功能：使用饱和策略的除法运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除法运算结果。

#### func saturatingInc()

```cangjie
public func saturatingInc(): Int64
```

功能：使用饱和策略的自增运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自增运算结果。

#### func saturatingMod(Int64)

```cangjie
public func saturatingMod(y: Int64): Int64
```

功能：使用饱和策略的取余运算。

当运算出现上溢时，返回操作数类型的最大值，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 取余运算结果。

#### func saturatingMul(Int64)

```cangjie
public func saturatingMul(y: Int64): Int64
```

功能：使用饱和策略的乘法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘法运算结果。

#### func saturatingNeg()

```cangjie
public func saturatingNeg(): Int64
```

功能：使用饱和策略的负号运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 负号运算结果。

#### func saturatingPow(UInt64)

```cangjie
public func saturatingPow(y: UInt64): Int64
```

功能：使用饱和策略的幂运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 指数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 幂运算结果。