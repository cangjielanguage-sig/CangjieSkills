### extend Int8 <: ThrowingOp\<Int8>

```cangjie
extend Int8 <: ThrowingOp<Int8>
```

功能：为 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 实现 [ThrowingOp](#interface-throwingopt) 接口。

父类型：

- [ThrowingOp](#interface-throwingopt)\<[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)>

#### func throwingAdd(Int8)

```cangjie
public func throwingAdd(y: Int8): Int8
```

功能：使用抛出异常策略的加法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 加数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 加法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当加法运算出现溢出时，抛出异常。

#### func throwingDec()

```cangjie
public func throwingDec(): Int8
```

功能：使用抛出异常策略的自减运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 自减运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自减运算出现溢出时，抛出异常。

#### func throwingDiv(Int8)

```cangjie
public func throwingDiv(y: Int8): Int8
```

功能：使用抛出异常策略的除法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 除数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 除法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法运算出现溢出时，抛出异常。

#### func throwingInc()

```cangjie
public func throwingInc(): Int8
```

功能：使用抛出异常策略的自增运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 自增运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自增运算出现溢出时，抛出异常。

#### func throwingMod(Int8)

```cangjie
public func throwingMod(y: Int8): Int8
```

功能：使用抛出异常策略的取余运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 除数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 取余运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当取余运算出现溢出时，抛出异常。

#### func throwingMul(Int8)

```cangjie
public func throwingMul(y: Int8): Int8
```

功能：使用抛出异常策略的乘法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 乘数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 乘法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当乘法运算出现溢出时，抛出异常。