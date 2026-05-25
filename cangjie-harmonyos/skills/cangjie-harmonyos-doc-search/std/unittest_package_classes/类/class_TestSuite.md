## class TestSuite

```cangjie
public class TestSuite {}
```

功能：提供构建和执行测试套方法的类。

### prop name

```cangjie
public prop name: String
```

功能：获取测试套名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### func runBenchmarks()

```cangjie
public func runBenchmarks(): BenchReport
```

功能：运行所有性能测试用例。

返回值：

- [BenchReport](#class-benchreport) - 性能测试运行结果。

### func runBenchmarks(Configuration)

```cangjie
public func runBenchmarks(configuration: Configuration): BenchReport
```

功能：带配置信息得运行所有性能测试用例。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 运行配置信息。

返回值：

- [BenchReport](#class-benchreport) - 性能测试用例运行结果。

### func runTests()

```cangjie
public func runTests(): TestReport
```

功能：运行测试套。

返回值：

- [TestReport](#class-testreport) - 测试套运行结果。

### func runTests(Configuration)

```cangjie
public func runTests(configuration: Configuration): TestReport
```

功能：带配置信息得运行测试套。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 运行配置信息。

返回值：

- [TestReport](#class-testreport) - 测试套运行结果。

### static func builder(String)

```cangjie
public static func builder(name: String): TestSuiteBuilder
```

功能：创建测试套构建器。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 测试套名称。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试套构造器。

### static func builder(TestSuite)

```cangjie
public static func builder(suite: TestSuite): TestSuiteBuilder
```

功能：创建测试套构建器。

参数：

- suite: [TestSuite](#class-testsuite) - 测试套。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试套构造器。