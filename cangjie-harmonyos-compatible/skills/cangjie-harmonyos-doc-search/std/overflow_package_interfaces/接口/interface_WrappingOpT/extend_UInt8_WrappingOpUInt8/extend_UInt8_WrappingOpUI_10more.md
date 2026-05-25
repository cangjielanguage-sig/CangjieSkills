### extend UInt8 <: WrappingOp\<UInt8>

```cangjie
extend UInt8 <: WrappingOp<UInt8>
```

功能：为 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 实现 [WrappingOp](#interface-wrappingopt) 接口。

父类型：

- [WrappingOp](#interface-wrappingopt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)>

#### func wrappingAdd(UInt8)

```cangjie
public func wrappingAdd(y: UInt8): UInt8
```

功能：使用高位截断策略的加法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 加数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 加法运算结果。

#### func wrappingDec()

```cangjie
public func wrappingDec(): UInt8
```

功能：使用高位截断策略的自减运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 自减运算结果。

#### func wrappingDiv(UInt8)

```cangjie
public func wrappingDiv(y: UInt8): UInt8
```

功能：使用高位截断策略的除法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除法运算结果。

#### func wrappingInc()

```cangjie
public func wrappingInc(): UInt8
```

功能：使用高位截断策略的自增运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 自增运算结果。

#### func wrappingMod(UInt8)

```cangjie
public func wrappingMod(y: UInt8): UInt8
```

功能：使用高位截断策略的取余运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 取余运算结果。

#### func wrappingMul(UInt8)

```cangjie
public func wrappingMul(y: UInt8): UInt8
```

功能：使用高位截断策略的乘法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 乘数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 乘法运算结果。

#### func wrappingNeg()

```cangjie
public func wrappingNeg(): UInt8
```

功能：使用高位截断策略的负号运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 负号运算结果。

#### func wrappingShl(UInt64)

```cangjie
public func wrappingShl(y: UInt64): UInt8
```

功能：使用高位截断策略的左移运算。

当右操作数大于等于左操作数位数时，取右操作数的低 3 位作为移位位数。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 左移运算结果。

#### func wrappingShr(UInt64)

```cangjie
public func wrappingShr(y: UInt64): UInt8
```

功能：使用高位截断策略的右移运算。

当右操作数大于等于左操作数位数时，取右操作数的低 3 位作为移位位数。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 右移运算结果。