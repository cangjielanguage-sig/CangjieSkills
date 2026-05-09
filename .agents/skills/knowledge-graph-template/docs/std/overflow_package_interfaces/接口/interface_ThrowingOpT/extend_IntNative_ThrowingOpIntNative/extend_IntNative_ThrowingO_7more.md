### extend IntNative <: ThrowingOp\<IntNative>

```cangjie
extend IntNative <: ThrowingOp<IntNative>
```

功能：为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 实现 [ThrowingOp](#interface-throwingopt) 接口。

父类型：

- [ThrowingOp](#interface-throwingopt)\<[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)>

#### func throwingAdd(IntNative)

```cangjie
public func throwingAdd(y: IntNative): IntNative
```

功能：使用抛出异常策略的加法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 加数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 加法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当加法运算出现溢出时，抛出异常。

#### func throwingDec()

```cangjie
public func throwingDec(): IntNative
```

功能：使用抛出异常策略的自减运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 自减运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自减运算出现溢出时，抛出异常。

#### func throwingDiv(IntNative)

```cangjie
public func throwingDiv(y: IntNative): IntNative
```

功能：使用抛出异常策略的除法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法运算出现溢出时，抛出异常。

#### func throwingInc()

```cangjie
public func throwingInc(): IntNative
```

功能：使用抛出异常策略的自增运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 自增运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当自增运算出现溢出时，抛出异常。

#### func throwingMod(IntNative)

```cangjie
public func throwingMod(y: IntNative): IntNative
```

功能：使用抛出异常策略的取余运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 取余运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当取余运算出现溢出时，抛出异常。

#### func throwingMul(IntNative)

```cangjie
public func throwingMul(y: IntNative): IntNative
```

功能：使用抛出异常策略的乘法运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 乘数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 乘法运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当乘法运算出现溢出时，抛出异常。