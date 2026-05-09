## struct CpuCycles

```cangjie
public struct CpuCycles <: Measurement {}
```

功能：使用本机 `rdtscp` 指令测量 CPU 周期数。仅适用于 x86 平台。

父类型：

- [Measurement](unittest_package_interfaces.md#interface-measurement)

### prop conversionTable

```cangjie
prop conversionTable: MeasurementUnitTable
```

功能：提供当前时间的单位换算表。
例如 `[(1.0, "cycles")]`。

类型：[MeasurementUnitTable](../unittest_package_api/unittest_package_types.md#type-measurementunittable)。

### prop name

```cangjie
prop name: String
```

功能：提供当前时间单位唯一的显示名称，例如：`CpuCycles`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### prop textDescription

```cangjie
prop textDescription: String
```

功能：描述此测量的简单文本将显示在某些报告中。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### func measure()

```cangjie
public func measure(): Float64
```

功能：返回执行了多少个 CPU 周期。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 计算得到的数据，用于统计分析。

### func setup()

```cangjie
public func setup()
```

功能：在测量前执行的配置动作。

## struct GenerateEachInputProvider\<T>

```cangjie
public struct GenerateEachInputProvider<T> <: BenchInputProvider<T>{
    public GenerateEachInputProvider(let builder: () -> T)
}
```

功能：基准输入提供程序，在每次执行基准之前生成输入。
生成时间包含在基准测量中，然后作为框架开销计算的一部分从最终结果中排除。

父类型：

- [BenchInputProvider](unittest_package_interfaces.md#interface-benchinputprovider)\<T>

### GenerateEachInputProvider(() -> T)

```cangjie
public GenerateEachInputProvider(let builder: () -> T)
```

功能：GenerateEachInputProvider 构造函数。

参数：

- builder: () -> T - 用于生成基准测试输入的闭包。

### func get(Int64)

```cangjie
public mut func get(idx: Int64): T
```

功能：获取元素，该函数的执行时间包含在基准测量中，然后作为框架开销计算的一部分从结果中排除。

参数：

- idx: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 元素索引值。

返回值：

- T - 元素值。

### func reset(Int64)

```cangjie
public mut func reset(max: Int64)
```

功能：在基准测量之前调用。调用此函数后，后续的 `get(i)` 调用必须成功获取 [0, max) 中的 `i` 。

参数：

- max: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 最大值。