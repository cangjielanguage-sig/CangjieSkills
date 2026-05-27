## interface BenchmarkConfig

```cangjie
public interface BenchmarkConfig {
    func batchSize(b: Int64): Unit
    func batchSize(x: Range<Int64>): Unit
    func warmup(x: Int64): Unit
    func warmup(x: Duration): Unit
    func minDuration(x: Duration): Unit
    func explicitGC(x: ExplicitGcType): Unit
    func minBatches(x: Int64): Unit
}
```

功能：该接口提供为 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 宏配置性能测试相关信息的函数签名。

### func batchSize(Int64)

```cangjie
func batchSize(b: Int64): Unit
```

功能：可实现该函数，为 `@Configuration` 宏配置批次的大小。

参数：

- b: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需配置的批次大小值。

### func batchSize(Range\<Int64>): Unit

```cangjie
func batchSize(x: Range<Int64>): Unit
```

功能：可实现该函数，为 `@Configuration` 宏配置批次的大小。

参数：

- x: [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 需配置的批次大小范围值。

### func explicitGC(ExplicitGcType)

```cangjie
func explicitGC(x: ExplicitGcType): Unit
```

功能：可实现该函数，为 `@Configuration` 宏配置 GC 的类型。

参数：

- x: [ExplicitGcType](../unittest_package_api/unittest_package_enums.md#enum-explicitgctype) - 需配置的 GC 类型值。

### func minBatches(Int64)

```cangjie
func minBatches(x: Int64): Unit
```

功能：可实现该函数，为 `@Configuration` 宏配置最小批次个数。

参数：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需配置的最小批次个数。

### func minDuration(Duration)

```cangjie
func minDuration(x: Duration): Unit
```

功能：可实现该函数，为 `@Configuration` 宏配置性能测试最小执行时间。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需配置的性能测试最小执行时间。

### func warmup(Int64)

```cangjie
func warmup(x: Int64): Unit
```

功能：可实现该函数，为 `@Configuration` 宏配置预热期的执行次数。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需配置的预热期的执行次数。

### func warmup(Duration)

```cangjie
func warmup(x: Duration): Unit
```

功能：可实现该函数，为 `@Configuration` 宏配置预热期的执行时间。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 需配置的预热期的执行时间。