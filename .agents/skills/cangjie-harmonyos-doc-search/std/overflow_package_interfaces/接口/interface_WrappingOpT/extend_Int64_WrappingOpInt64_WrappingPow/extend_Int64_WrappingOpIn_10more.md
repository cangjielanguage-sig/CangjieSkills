### extend Int64 <: WrappingOp\<Int64> & WrappingPow

```cangjie
extend Int64 <: WrappingOp<Int64> & WrappingPow
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 实现 [WrappingOp](#interface-wrappingopt) 和 [WrappingPow](#interface-wrappingpow) 接口。

父类型：

- [WrappingOp](#interface-wrappingopt)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>
- [WrappingPow](#interface-wrappingpow)

#### func wrappingAdd(Int64)

```cangjie
public func wrappingAdd(y: Int64): Int64
```

功能：使用高位截断策略的加法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 加数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 加法运算结果。

#### func wrappingDec()

```cangjie
public func wrappingDec(): Int64
```

功能：使用高位截断策略的自减运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自减运算结果。

#### func wrappingDiv(Int64)

```cangjie
public func wrappingDiv(y: Int64): Int64
```

功能：使用高位截断策略的除法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除法运算结果。

#### func wrappingInc()

```cangjie
public func wrappingInc(): Int64
```

功能：使用高位截断策略的自增运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 自增运算结果。

#### func wrappingMod(Int64)

```cangjie
public func wrappingMod(y: Int64): Int64
```

功能：使用高位截断策略的取余运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 除数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 取余运算结果。

#### func wrappingMul(Int64)

```cangjie
public func wrappingMul(y: Int64): Int64
```

功能：使用高位截断策略的乘法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 乘法运算结果。

#### func wrappingNeg()

```cangjie
public func wrappingNeg(): Int64
```

功能：使用高位截断策略的负号运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 负号运算结果。

#### func wrappingPow(UInt64)

```cangjie
public func wrappingPow(y: UInt64): Int64
```

功能：使用高位截断策略的幂运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 指数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 幂运算结果。

#### func wrappingShl(UInt64)

```cangjie
public func wrappingShl(y: UInt64): Int64
```

功能：使用高位截断策略的左移运算。

当右操作数大于等于左操作数位数时，取右操作数的低 6 位作为移位位数。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 左移运算结果。