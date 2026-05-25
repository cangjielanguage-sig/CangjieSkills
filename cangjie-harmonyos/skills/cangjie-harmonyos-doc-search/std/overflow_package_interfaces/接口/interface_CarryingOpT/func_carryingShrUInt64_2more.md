### func carryingShr(UInt64)

```cangjie
func carryingShr(y: UInt64): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示右移运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 右移运算是否发生截断以及运算的结果。

### func carryingSub(T)

```cangjie
func carryingSub(y: T): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示减法运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

参数：

- y: T - 减数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 减法运算是否发生截断以及运算的结果。