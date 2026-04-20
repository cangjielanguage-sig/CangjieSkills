## struct Perf

```cangjie
public struct Perf <: Measurement {
    public init()
    public Perf(counter: PerfCounter)
}
```

功能：使用 Linux 系统调用 `perf_event_open` 测量各种硬件和软件 CPU 计数器。仅在 Linux 上可用。

父类型：

- [Measurement](unittest_package_interfaces.md#interface-measurement)

### prop conversionTable

```cangjie
prop conversionTable: MeasurementUnitTable
```

功能：提供对应 CPU 计数器的换算表。

类型：[MeasurementUnitTable](../unittest_package_api/unittest_package_types.md#type-measurementunittable)。

### prop name

```cangjie
prop name: String
```

功能：为当前 CPU 计数器提供唯一的显示名称，例如：`Perf(cycles)`。

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

功能：使用 CPU 周期计数器的默认构造函数。

### Perf(PerfCounter)

```cangjie
public Perf(counter: PerfCounter)
```

功能：指定要测量的 CPU 计数器的构造函数。

参数：

- counter: [PerfCounter](../unittest_package_api/unittest_package_enums.md#enum-perfcounter) - 指定计数器。

### func measure()

```cangjie
public func measure(): Float64
```

功能：返回指定 CPU 计数器的值。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 计算得到的数据，用于统计分析。

### func setup()

```cangjie
func setup()
```

功能：此 CPU 计数器的初始化例程。在每个基准步骤之前调用。

## struct RelativeDelta\<T>

```cangjie
public struct RelativeDelta<T> {
    public RelativeDelta(let absolute!: T, let relative!: T) {}
}
```

功能：对于浮点类型，提供相对的 delta 数据类型来做近似相等的计算。计算公式如下。

$$|x - y| \le absolute + relative * max(abs(x), abs(y))$$

### RelativeDelta(T, T)

```cangjie
public RelativeDelta(let absolute!: T, let relative!: T)
```

功能：RelativeDelta 的主构造函数。

参数：

- absolute!: T - 绝对比较部分的 delta 值。
- relative!: T - 相对比较部分的 delta 值。

## struct TestCaseInfo

```cangjie
public struct TestCaseInfo {
    public let groupName: String
    public let suiteName: String
    public let caseName: String
}
```

功能：当前正在运行的测试用例的信息。通常在动态 API 的超时处理句柄中被使用。

### let caseName

```cangjie
public let caseName: String
```

功能：用例名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### let groupName

```cangjie
public let groupName: String
```

功能：用例的测试组名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### let suiteName

```cangjie
public let suiteName: String
```

功能：用例的测试套名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。