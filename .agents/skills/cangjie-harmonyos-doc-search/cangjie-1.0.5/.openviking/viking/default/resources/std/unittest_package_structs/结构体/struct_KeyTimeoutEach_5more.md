## struct KeyTimeoutEach

```cangjie
public struct KeyTimeoutEach <: KeyFor<String> {}
```

功能：用于在 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中作为对应配置项的键值。

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)

### prop timeoutEach

```cangjie
public static prop timeoutEach: TimeoutEach
```

功能：配置项的键值。

### prop name

```cangjie
public prop name: String
```

功能：配置项的键值的名称。

## struct KeyTimeoutHandler

```cangjie
public struct KeyTimeoutHandler <: KeyFor<(TestCaseInfo) -> Unit> {}
```

功能：支持在配置信息中指定超时处理的句柄。

例如：

<!-- compile -->
```cangjie
let conf = Configuration()
conf.set(KeyTimeoutHandler.timeoutHandler, { info => /*...*/ })
```

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)

### prop timeoutHandler

```cangjie
public static prop timeoutHandler: KeyTimeoutHandler
```

功能：超时处理句柄。

类型：[KeyTimeoutHandler](#struct-keytimeouthandler)。

### prop name

```cangjie
public prop name: String
```

功能：超时处理句柄的名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

## struct KeyVerbose

```cangjie
public struct KeyVerbose <: KeyFor<Bool> {}
```

功能：用于在 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中作为对应配置项的键值。

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)

### prop verbose

```cangjie
public static prop verbose: Verbose
```

功能：配置项的键值。

### prop name

```cangjie
public prop name: String
```

功能：配置项的键值的名称。

## struct KeyWarmup

```cangjie
public struct KeyWarmup <: KeyFor<Int64> & KeyFor<Duration> {}
```

功能：用于在 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中作为对应配置项的键值。

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)

### prop warmup

```cangjie
public static prop warmup: Warmup
```

功能：配置项的键值。

### prop name

```cangjie
public prop name: String
```

功能：配置项的键值的名称。

## struct MeasurementInfo

```cangjie
public struct MeasurementInfo {
    public let conversionTable: MeasurementUnitTable,
    public let name: String,
    public let textDescription: String
}
```

功能：存储测量信息的结构体。

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