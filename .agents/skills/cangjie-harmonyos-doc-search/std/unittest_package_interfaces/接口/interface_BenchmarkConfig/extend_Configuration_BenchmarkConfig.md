### extend Configuration <: BenchmarkConfig

```cangjie
extend Configuration <: BenchmarkConfig {}
```

功能：为 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 扩展 [BenchmarkConfig](../../unittest/unittest_package_api/unittest_package_interfaces.md#interface-benchmarkconfig) 接口。

父类型：

- [BenchmarkConfig](../../unittest/unittest_package_api/unittest_package_interfaces.md#interface-benchmarkconfig)

#### func batchSize(Int64)

```cangjie
public func batchSize(b: Int64)
```

功能：配置性能测试时一个批次的执行次数。

参数：

- b: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行次数。

#### func batchSize(Range\<Int64>)

```cangjie
public func batchSize(x: Range<Int64>)
```

功能：配置性能测试时一个批次的执行次数范围。

参数：

- b: [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<Int64> - 执行次数范围。

#### func explicitGC(ExplicitGcType)

```cangjie
public func explicitGC(x: ExplicitGcType)
```

功能：配置性能测试时执行 GC 的方式。

参数：

- x: [ExplicitGcType](../../unittest/unittest_package_api/unittest_package_enums.md#enum-explicitgctype) - GC 执行的方式。

#### func minBatches(Int64)

```cangjie
public func minBatches(x: Int64)
```

功能：配置性能测试时最少的批次数。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 最少的批次数。

#### func minDuration(Duration)

```cangjie
public func minDuration(x: Duration)
```

功能：配置性能测试时最短的执行时长。

参数：

- x: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 最短的执行时长。

#### func warmup(Int64)

```cangjie
public func warmup(x: Int64)
```

功能：配置性能测试时预热的秒数。

参数：

- x: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预热的秒数。

#### func warmup(Duration)

```cangjie
public func warmup(x: Duration)
```

功能：配置性能测试时预热的时长。

参数：

- x: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 预热的时长。