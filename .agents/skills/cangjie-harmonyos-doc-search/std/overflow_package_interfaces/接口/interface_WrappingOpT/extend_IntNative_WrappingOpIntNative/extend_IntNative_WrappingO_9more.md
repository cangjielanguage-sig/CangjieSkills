### extend IntNative <: WrappingOp\<IntNative>

```cangjie
extend IntNative <: WrappingOp<IntNative>
```

功能：为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 实现 [WrappingOp](#interface-wrappingopt) 接口。

父类型：

- [WrappingOp](#interface-wrappingopt)\<[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)>

#### func wrappingAdd(IntNative)

```cangjie
public func wrappingAdd(y: IntNative): IntNative
```

功能：使用高位截断策略的加法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 加数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 加法运算结果。

#### func wrappingDec()

```cangjie
public func wrappingDec(): IntNative
```

功能：使用高位截断策略的自减运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 自减运算结果。

#### func wrappingDiv(IntNative)

```cangjie
public func wrappingDiv(y: IntNative): IntNative
```

功能：使用高位截断策略的除法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除法运算结果。

#### func wrappingInc()

```cangjie
public func wrappingInc(): IntNative
```

功能：使用高位截断策略的自增运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 自增运算结果。

#### func wrappingMod(IntNative)

```cangjie
public func wrappingMod(y: IntNative): IntNative
```

功能：使用高位截断策略的取余运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 取余运算结果。

#### func wrappingMul(IntNative)

```cangjie
public func wrappingMul(y: IntNative): IntNative
```

功能：使用高位截断策略的乘法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 乘数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 乘法运算结果。

#### func wrappingNeg()

```cangjie
public func wrappingNeg(): IntNative
```

功能：使用高位截断策略的负号运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 负号运算结果。

#### func wrappingShl(UInt64)

```cangjie
public func wrappingShl(y: UInt64): IntNative
```

功能：使用高位截断策略的左移运算。

当右操作数大于等于左操作数位数时，取右操作数的低位作为移位位数，具体取的位数取决于当前系统下 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 的位数。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 左移运算结果。