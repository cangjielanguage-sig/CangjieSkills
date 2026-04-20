### extend UIntNative <: CarryingOp\<UIntNative>

```cangjie
extend UIntNative <: CarryingOp<UIntNative>
```

功能：为 [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) 实现 [CarryingOp](#interface-carryingopt) 接口。

父类型：

- [CarryingOp](#interface-carryingopt)\<[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)>

#### func carryingAdd(UIntNative)

```cangjie
public func carryingAdd(y: UIntNative): (Bool, UIntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的加法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 加数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingDec()

```cangjie
public func carryingDec(): (Bool, UIntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的自减运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingDiv(UIntNative)

```cangjie
public func carryingDiv(y: UIntNative): (Bool, UIntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的除法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingInc()

```cangjie
public func carryingInc(): (Bool, UIntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的自增运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingMod(UIntNative)

```cangjie
public func carryingMod(y: UIntNative): (Bool, UIntNative)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的取余运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。