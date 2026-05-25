### extend UInt8 <: ThrowingOp\<UInt8>

```cangjie
extend UInt8 <: ThrowingOp<UInt8>
```

功能：为 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 实现 [ThrowingOp](#interface-throwingopt) 接口。

父类型：

- [ThrowingOp](#interface-throwingopt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)>

#### func throwingAdd(UInt8)

```cangjie
public func throwingAdd(y: UInt8): UInt8
```

功能：使用抛出异常策略的加法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 加数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 加法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当加法运算出现溢出时，抛出异常。

#### func throwingDec()

```cangjie
public func throwingDec(): UInt8
```

功能：使用抛出异常策略的自减运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 自减运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自减运算出现溢出时，抛出异常。

#### func throwingDiv(UInt8)

```cangjie
public func throwingDiv(y: UInt8): UInt8
```

功能：使用抛出异常策略的除法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法运算出现溢出时，抛出异常。

#### func throwingInc()

```cangjie
public func throwingInc(): UInt8
```

功能：使用抛出异常策略的自增运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 自增运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自增运算出现溢出时，抛出异常。

#### func throwingMod(UInt8)

```cangjie
public func throwingMod(y: UInt8): UInt8
```

功能：使用抛出异常策略的取余运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 除数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 取余运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当取余运算出现溢出时，抛出异常。

#### func throwingMul(UInt8)

```cangjie
public func throwingMul(y: UInt8): UInt8
```

功能：使用抛出异常策略的乘法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 乘数。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - 乘法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当乘法运算出现溢出时，抛出异常。