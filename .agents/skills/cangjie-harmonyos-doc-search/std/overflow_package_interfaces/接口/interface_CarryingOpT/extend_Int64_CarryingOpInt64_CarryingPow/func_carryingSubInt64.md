#### func carryingSub(Int64)

```cangjie
public func carryingSub(y: Int64): (Bool, Int64)
```

功能：使用 [wrapping](./overflow_package_interfaces.md#interface-wrappingopt) 策略的减法运算。

当运算出现溢出时，返回 `true` 和运算结果，否则返回 `false` 和运算结果。

参数：

- y: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 减数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) - 返回一个元组，元组的第一个元素表示运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。