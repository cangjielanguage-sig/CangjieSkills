### extend UInt16 <: ThrowingOp\<UInt16>

```cangjie
extend UInt16 <: ThrowingOp<UInt16>
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 实现 [ThrowingOp](#interface-throwingopt) 接口。

父类型：

- [ThrowingOp](#interface-throwingopt)\<[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)>

#### func throwingAdd(UInt16)

```cangjie
public func throwingAdd(y: UInt16): UInt16
```

功能：使用抛出异常策略的加法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 加数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 加法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当加法运算出现溢出时，抛出异常。

#### func throwingDec()

```cangjie
public func throwingDec(): UInt16
```

功能：使用抛出异常策略的自减运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 自减运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自减运算出现溢出时，抛出异常。

#### func throwingDiv(UInt16)

```cangjie
public func throwingDiv(y: UInt16): UInt16
```

功能：使用抛出异常策略的除法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法运算出现溢出时，抛出异常。

#### func throwingInc()

```cangjie
public func throwingInc(): UInt16
```

功能：使用抛出异常策略的自增运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 自增运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自增运算出现溢出时，抛出异常。

#### func throwingMod(UInt16)

```cangjie
public func throwingMod(y: UInt16): UInt16
```

功能：使用抛出异常策略的取余运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 除数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 取余运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当取余运算出现溢出时，抛出异常。

#### func throwingMul(UInt16)

```cangjie
public func throwingMul(y: UInt16): UInt16
```

功能：使用抛出异常策略的乘法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 乘数。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 乘法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当乘法运算出现溢出时，抛出异常。