### extend Int32 <: CarryingOp\<Int32>

```cangjie
extend Int32 <: CarryingOp<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 实现 [CarryingOp](#interface-carryingopt) 接口。

父类型：

- [CarryingOp](#interface-carryingopt)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### func carryingAdd(Int32)

```cangjie
public func carryingAdd(y: Int32): (Bool, Int32)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的加法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 加数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [Int32](../../core/core_package_api/core_package_intrinsics.md#int32)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingDec()

```cangjie
public func carryingDec(): (Bool, Int32)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的自减运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [Int32](../../core/core_package_api/core_package_intrinsics.md#int32)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingDiv(Int32)

```cangjie
public func carryingDiv(y: Int32): (Bool, Int32)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的除法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [Int32](../../core/core_package_api/core_package_intrinsics.md#int32)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingInc()

```cangjie
public func carryingInc(): (Bool, Int32)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的自增运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [Int32](../../core/core_package_api/core_package_intrinsics.md#int32)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingMod(Int32)

```cangjie
public func carryingMod(y: Int32): (Bool, Int32)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的取余运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [Int32](../../core/core_package_api/core_package_intrinsics.md#int32)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。