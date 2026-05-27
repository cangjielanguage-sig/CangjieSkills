## interface SaturatingPow

```cangjie
public interface SaturatingPow {
    func saturatingPow(y: UInt64): Int64
}
```

功能：提供饱和策略的幂运算接口。

### func saturatingPow(UInt64)

```cangjie
func saturatingPow(y: UInt64): Int64
```

功能：使用饱和策略的幂运算。

当运算出现上溢时，返回操作数类型的最大值，运算出现下溢时，返回操作数类型的最小值，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 指数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 幂运算结果。