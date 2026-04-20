## class UnitTestCase

```cangjie
public class UnitTestCase {}
```

功能：提供创建和执行单元测试用例的方法的类。

### prop name

```cangjie
public prop name: String
```

功能：获取单元测试名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### func run()

```cangjie
public func run(): TestReport
```

功能：运行单元测试用例。

返回值：

- [TestReport](#class-testreport) - 单元测试执行结果报告。

### static func create(String, Configuration, () -> Unit)

```cangjie
public static func create(
    name: String,
    configuration!: Configuration = Configuration(),
    body!: () -> Unit
): UnitTestCase
```

功能：创建单元测试用例。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- configuration!: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 用例配置信息。
- body!: () -> Unit - 用例执行体。

返回值：

- [UnitTestCase](#class-unittestcase) - 单元测试用例对象。

### static func createParameterized\<T>(String, DataStrategy\<T>, Configuration, (T) -> Unit)

```cangjie
public static func createParameterized<T>(
    name: String,
    strategy: DataStrategy<T>,
    configuration!: Configuration = Configuration(),
    body!: (T) -> Unit
): UnitTestCase
```

功能：创建参数化的单元测试用例。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- strategy: [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) - 参数数据策略。
- configuration!: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 用例配置信息。
- body!: () -> Unit - 用例执行体。

返回值：

- [UnitTestCase](#class-unittestcase) - 单元测试用例对象。

### static func createParameterized\<T>(String, DataStrategyProcessor\<T>, Configuration, (T) -> Unit)

```cangjie
public static func createParameterized<T>(
    name: String,
    strategy: DataStrategyProcessor<T>,
    configuration!: Configuration = Configuration(),
    body!: (T) -> Unit
): UnitTestCase
```

功能：创建参数化的单元测试用例。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- strategy: [DataStrategyProcessor](#class-datastrategyprocessort) - 参数数据处理器。
- configuration!: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 用例配置信息。
- body!: () -> Unit - 用例执行体。

返回值：

- [UnitTestCase](#class-unittestcase) - 单元测试用例对象。