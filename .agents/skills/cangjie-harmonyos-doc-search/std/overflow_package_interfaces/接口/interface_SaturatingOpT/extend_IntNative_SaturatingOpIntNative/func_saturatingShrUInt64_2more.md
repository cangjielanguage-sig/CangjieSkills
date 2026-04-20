#### func saturatingShr(UInt64)

```cangjie
public func saturatingShr(y: UInt64): IntNative
```

功能：使用饱和策略的右移运算。

当移位位数大于等于操作数位数时，将移位位数置为操作数位数 - 1，返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 右移运算结果。

#### func saturatingSub(IntNative)

```cangjie
public func saturatingSub(y: IntNative): IntNative
```

功能：使用饱和策略的减法运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 减数。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 减法运算结果。