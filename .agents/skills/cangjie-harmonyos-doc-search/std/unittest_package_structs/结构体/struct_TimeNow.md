## struct TimeNow

```cangjie
public struct TimeNow <: Measurement {
    public init()
    public init(unit: ?TimeUnit)
}
```

功能：[Measurement](../../unittest/unittest_package_api/unittest_package_interfaces.md#interface-measurement) 的实现，用于测量执行一个函数所花费的时间。

父类型：

- [Measurement](unittest_package_interfaces.md#interface-measurement)

### prop conversionTable

```cangjie
prop conversionTable: MeasurementUnitTable
```

功能：提供当前时间的单位换算表。
例如 `[(1.0, "ns"), (1e3, "us"), (1e6, "ms"), (1e9, "s")]`。

类型：[MeasurementUnitTable](../unittest_package_api/unittest_package_types.md#type-measurementunittable)。

### prop name

```cangjie
prop name: String
```

功能：提供当前时间单位唯一的显示名称，例如：`Duration(ns)` 或 `Duration(s)`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### prop textDescription

```cangjie
prop textDescription: String
```

功能：描述此测量的简单文本将显示在某些报告中。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### init()

```cangjie
public init()
```

功能：自动选择输出格式的默认构造函数。

### init(?TimeUnit)

```cangjie
public init(unit: ?TimeUnit)
```

功能： `unit` 参数用于指定打印结果时将使用的时间单位。

参数：

- unit: ?[TimeUnit](unittest_package_enums.md#enum-timeunit) - 指定的时间单位。

### func measure()

```cangjie
public func measure(): Float64
```

功能：获取当前时间用于统计分析。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 计算得到的数据，用于统计分析。