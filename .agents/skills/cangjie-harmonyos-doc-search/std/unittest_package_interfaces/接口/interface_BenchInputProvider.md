## interface BenchInputProvider

```cangjie
public interface BenchInputProvider<T> <: BenchmarkInputMarker  {
    mut func get(idx: Int64): T
    mut func reset(max: Int64)
}
```

功能：当某些代码需要在性能测试执行前执行，或当输入变化就需要重新执行一段代码时，可实现本接口。同时 [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 的实现类型应返回此接口的实现类型。

用户一般不需要自行实现该接口，可直接使用 [@Strategy](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#strategy-宏) 宏。

父类型：

- [BenchmarkInputMarker](#interface-benchmarkinputmarker)

### func get(Int64)

```cangjie
mut func get(idx: Int64): T
```

功能：获取元素。该函数的执行时间包含在基准测量中，然后作为框架开销计算的一部分从结果中排除。

参数：

- idx: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 元素索引值。

返回值：

- T - 元素值。

### func reset(Int64)

```cangjie
mut func reset(max: Int64)
```

功能：在基准测量之前调用。调用此函数后，后续的 `get(i)` 调用必须成功获取 [0, max) 中的 `i` 。

参数：

- max: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 最大值。