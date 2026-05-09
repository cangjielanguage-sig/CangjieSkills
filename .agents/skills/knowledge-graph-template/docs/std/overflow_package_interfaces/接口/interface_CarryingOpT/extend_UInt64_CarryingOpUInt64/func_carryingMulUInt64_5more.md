#### func carryingMul(UInt64)

```cangjie
public func carryingMul(y: UInt64): (Bool, UInt64)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的乘法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 乘数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingNeg()

```cangjie
public func carryingNeg(): (Bool, UInt64)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的负号运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingShl(UInt64)

```cangjie
public func carryingShl(y: UInt64): (Bool, UInt64)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的左移运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingShr(UInt64)

```cangjie
public func carryingShr(y: UInt64): (Bool, UInt64)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的右移运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

#### func carryingSub(UInt64)

```cangjie
public func carryingSub(y: UInt64): (Bool, UInt64)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的减法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 减数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。