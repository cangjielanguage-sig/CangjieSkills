## class Benchmark

```cangjie
public class Benchmark {}
```

功能：该类提供创建和运行单个性能测试用例的方法。

### prop name

```cangjie
public prop name: String
```

功能：获取用例名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### func run()

```cangjie
public func run(): BenchReport
```

功能：运行该性能用例。

返回值：

- [BenchReport](#class-benchreport) - 运行结果报告。

### static func create(String, Configuration, Measurement, () -> Unit)

```cangjie
public static func create(
    name: String,
    configuration!: Configuration = Configuration(),
    measurement!: Measurement = TimeNow(),
    body!: () -> Unit
): Benchmark
```

功能：创建一个性能测试用例对象。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- configuration!: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 用例配置信息。
- measurement: [Measurement](unittest_package_interfaces.md#interface-measurement) - 测量方法信息。
- body: () -> Unit - 用例执行体。

返回值：

- [Benchmark](#class-benchmark) - 性能测试用例对象。

### static func createParameterized\<T>(String, DataStrategy\<T>, Configuration, Measurement, (T) -> Unit)

```cangjie
public static func createParameterized<T>(
    name: String,
    strategy: DataStrategy<T>,
    configuration!: Configuration = Configuration(),
    measurement!: Measurement = TimeNow(),
    body!: (T) -> Unit
): Benchmark
```

功能：创建一个参数化的性能测试用例对象。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- strategy: [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) - 参数数据策略。
- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 用例配置信息。
- measurement!: [Measurement](unittest_package_interfaces.md#interface-measurement) 测量方法信息。
- body: () -> Unit - 用例执行体。

返回值：

- [Benchmark](#class-benchmark) - 性能测试用例对象。

### static func createParameterized\<T>(String, DataStrategyProcessor\<T>, Configuration, Measurement, (T) -> Unit)

```cangjie
public static func createParameterized<T>(
    name: String,
    strategy: DataStrategyProcessor<T>,
    configuration!: Configuration = Configuration(),
    measurement!: Measurement = TimeNow(),
    body!: (T) -> Unit
): Benchmark
```

功能：创建一个参数化的性能测试用例对象。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- strategy: [DataStrategyProcessor](#class-datastrategyprocessort) - 参数数据处理器。
- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 用例配置信息。
- measurement: [Measurement](unittest_package_interfaces.md#interface-measurement) - 测量方法信息。
- body: () -> Unit - 用例执行体。

返回值：

- [Benchmark](#class-benchmark) - 性能测试用例对象。