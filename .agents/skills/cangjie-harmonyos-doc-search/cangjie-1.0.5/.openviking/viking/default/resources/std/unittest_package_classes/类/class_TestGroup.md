## class TestGroup

```cangjie
public class TestGroup {}
```

功能：提供构建和运行测试组合方法的类。

### prop name

```cangjie
public prop name: String
```

功能：获取测试组合名称。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### func runBenchmarks()

```cangjie
public func runBenchmarks(): BenchReport
```

功能：运行所有性能测试用例。

返回值：

- [BenchReport](#class-benchreport) - 性能测试用例报告。

### func runBenchmarks(Configuration)

```cangjie
public func runBenchmarks(Configuration): BenchReport
```

功能：带运行配置得执行所有性能测试用例。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 运行配置。

返回值：

- [BenchReport](#class-benchreport) - 性能测试用例报告。

### func runTests()

```cangjie
public func runTests(): TestReport
```

功能：执行所有单元测试用例。

返回值：

- [TestReport](#class-testreport) - 单元测试用例报告。

### func runTests(Configuration)

```cangjie
public func runTests(configuration: Configuration): TestReport
```

功能：带运行配置得执行所有单元测试用例。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 运行配置。

返回值：

- [TestReport](#class-testreport) - 单元测试用例报告。

### static func builder(String)

```cangjie
public static func builder(name: String): TestGroupBuilder
```

功能：创建测试组合构造器。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 测试组合名称。

返回值：

- [TestGroupBuilder](#class-testgroupbuilder) - 测试组合构造器。

### static func builder(TestGroup)

```cangjie
public static func builder(group: TestGroup): TestGroupBuilder
```

功能：创建测试组合构造器。

参数：

- group: [TestGroup](#class-testgroup) - 测试组合。

返回值：

- [TestGroupBuilder](#class-testgroupbuilder) - 测试组合构造器。