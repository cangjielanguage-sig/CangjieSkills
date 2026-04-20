### extend Int32 <: WrappingOp\<Int32>

```cangjie
extend Int32 <: WrappingOp<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 实现 [WrappingOp](#interface-wrappingopt) 接口。

父类型：

- [WrappingOp](#interface-wrappingopt)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### func wrappingAdd(Int32)

```cangjie
public func wrappingAdd(y: Int32): Int32
```

功能：使用高位截断策略的加法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 加数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 加法运算结果。

#### func wrappingDec()

```cangjie
public func wrappingDec(): Int32
```

功能：使用高位截断策略的自减运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 自减运算结果。

#### func wrappingDiv(Int32)

```cangjie
public func wrappingDiv(y: Int32): Int32
```

功能：使用高位截断策略的除法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除法运算结果。

#### func wrappingInc()

```cangjie
public func wrappingInc(): Int32
```

功能：使用高位截断策略的自增运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 自增运算结果。

#### func wrappingMod(Int32)

```cangjie
public func wrappingMod(y: Int32): Int32
```

功能：使用高位截断策略的取余运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 取余运算结果。

#### func wrappingMul(Int32)

```cangjie
public func wrappingMul(y: Int32): Int32
```

功能：使用高位截断策略的乘法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 乘数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 乘法运算结果。

#### func wrappingNeg()

```cangjie
public func wrappingNeg(): Int32
```

功能：使用高位截断策略的负号运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 负号运算结果。

#### func wrappingShl(UInt64)

```cangjie
public func wrappingShl(y: UInt64): Int32
```

功能：使用高位截断策略的左移运算。

当右操作数大于等于左操作数位数时，取右操作数的低 5 位作为移位位数。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 左移运算结果。

#### func wrappingShr(UInt64)

```cangjie
public func wrappingShr(y: UInt64): Int32
```

功能：使用高位截断策略的右移运算。

当右操作数大于等于左操作数位数时，取右操作数的低 5 位作为移位位数。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 右移运算结果。