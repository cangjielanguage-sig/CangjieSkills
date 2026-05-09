## interface BenchmarkInputMarker

```cangjie
public interface BenchmarkInputMarker
```

功能：当我们不知道 `T` 时，该接口能够检测 `BenchInputProvider<T>` 。

## interface Measurement

```cangjie
public interface Measurement {
    prop conversionTable: MeasurementUnitTable
    prop name: String
    prop textDescription: String
    func setup(): Unit
    func measure(): Float64
    prop info: MeasurementInfo
}
```

功能：该接口指定如何在性能测试期间测量数据以及如何在报告中显示数据。
实现接口的实例可以作为宏 `@Measure` 的属性传递。

### prop conversionTable

```cangjie
prop conversionTable: MeasurementUnitTable
```

功能：用于在性能测试报告中构建测量值的表示。
包含测量单位的边界对。
根据值的边界，使用最合适的单位。
对于 CSV 格式报告，始终选择下限以简化结果处理。
默认值为 `[(1.0, "")]`。

类型：[MeasurementUnitTable](../unittest_package_api/unittest_package_types.md#type-measurementunittable)。

### prop name

```cangjie
prop name: String
```

功能：当前 `Measurement` 类型的唯一显示名称。
有助于区分报告表中的不同测量类型。
默认值为 `Measurement`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### prop textDescription

```cangjie
prop textDescription: String
```

功能：描述此测量的简单文本将显示在某些报告中。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### func measure()

```cangjie
func measure(): Float64
```

功能：将用于统计分析的测量运行时间的方法。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 测量得到的数据。

### func setup()

```cangjie
func setup()
```

功能：此测量的初始化例程。在每个基准步骤之前调用。

### prop info

功能：具体测量的汇总信息。

类型: [MeasurementInfo](../unittest_package_api/unittest_package_structs.md#struct-measurementinfo)