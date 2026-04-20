#### func saturatingShr(UInt64)

```cangjie
public func saturatingShr(y: UInt64): Int8
```

功能：使用饱和策略的右移运算。

当移位位数大于等于操作数位数时，将移位位数置为操作数位数 - 1，返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 右移运算结果。

#### func saturatingSub(Int8)

```cangjie
public func saturatingSub(y: Int8): Int8
```

功能：使用饱和策略的减法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 减数。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - 减法运算结果。