### extend IntNative <: CarryingOp\<IntNative>

```cangjie
extend IntNative <: CarryingOp<IntNative>
```

功能：为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 实现 [CarryingOp](#interface-carryingopt) 接口。

父类型：

- [CarryingOp](#interface-carryingopt)\<[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)>

#### func carryingAdd(IntNative)

```cangjie
public func carryingAdd(y: IntNative): (Bool, IntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的加法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 加数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingDec()

```cangjie
public func carryingDec(): (Bool, IntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的自减运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingDiv(IntNative)

```cangjie
public func carryingDiv(y: IntNative): (Bool, IntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的除法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingInc()

```cangjie
public func carryingInc(): (Bool, IntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的自增运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingMod(IntNative)

```cangjie
public func carryingMod(y: IntNative): (Bool, IntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的取余运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。