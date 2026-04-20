## class TestGroupBuilder

```cangjie
public class TestGroupBuilder {}
```

功能：提供配置测试组合的方法的构造器。

### func add(Benchmark)

```cangjie
public func add(benchmark: Benchmark): TestGroupBuilder
```

功能：为测试组合增加性能测试用例。

参数：

- benchmark: [Benchmark](#class-benchmark) - 性能测试用例。

返回值：

- [TestGroupBuilder](#class-testgroupbuilder)  - 测试组合构造器。

### func add(TestSuite)

```cangjie
public func add(suite: TestSuite): TestGroupBuilder
```

功能：为测试组合增加单元测试套。

参数：

- suite: [TestSuite](#class-testsuite) - 单元测试套。

返回值：

- [TestGroupBuilder](#class-testgroupbuilder)  - 测试组合构造器。

### func add(UnitTestCase)

```cangjie
public func add(test: UnitTestCase): TestGroupBuilder
```

功能：为测试组合增加单元测试用例。

参数：

- test: [UnitTestCase](#class-unittestcase) - 单元测试用例。

返回值：

- [TestGroupBuilder](#class-testgroupbuilder) - 测试组合构造器。

### func build()

```cangjie
public func build(): TestGroup
```

功能：配置完成后，构建测试组合对象。

返回值：

- [TestGroup](#class-testgroup) - 测试组合。

### func configure(Configuration)

```cangjie
public func configure(configuration: Configuration): TestGroupBuilder
```

功能：为测试组合配置配置信息。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 配置信息。

返回值：

- [TestGroupBuilder](#class-testgroupbuilder) - 测试组合构造器。

### func setName(String)

```cangjie
public func setName(name: String): TestGroupBuilder
```

功能：为测试组合设置名称。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 名称。

返回值：

- [TestGroupBuilder](#class-testgroupbuilder) - 测试组合构造器。

## class TestPackage

```cangjie
public class TestPackage {
    public TestPackage(let name: String)
}
```

功能：用例包对象。

### TestPackage(String)

```cangjie
public TestPackage(let name: String)
```

功能：TestPackage 构造函数。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例包名称。

### func registerCase(() -> UnitTestCase)

```cangjie
public func registerCase(testCase: () -> UnitTestCase): Unit
```

功能：注册单元测试用例。

参数：

- testCase: () -> [UnitTestCase](#class-unittestcase) - 单元测试用例生成闭包。

### func registerSuite(() -> TestSuite)

```cangjie
public func registerSuite(suite: () -> TestSuite): Unit
```

功能：注册测试套。

参数：

- suite: () -> [TestSuite](#class-testsuite) - 测试套生成闭包。

### func registerBench(() -> Benchmark)

```cangjie
public func registerBench(bench: () -> Benchmark): Unit
```

功能：注册性能用例。

参数：

- bench: () -> [Benchmark](#class-benchmark) - 性能用例生成闭包。

### func enableOptimizedMockForBench()

```cangjie
public func enableOptimizedMockForBench(): Unit
```

功能：启用优化以在测试中同时使用模拟和基准测试。

## class TestReport

```cangjie
public class TestReport <: Report {}
```

功能：单元测试执行结果报告。

父类型：

- [Report](#class-report)

### func reportTo\<T>(Reporter\<TestReport, T>)

```cangjie
public func reportTo<T>(reporter: Reporter<TestReport, T>): T
```

功能：打印单元测试执行报告。

参数：

- reporter: [Reporter](#class-report)\<[TestReport](#class-testreport), T> - 单元测试报告打印器。

返回值：

- T - 打印返回值，一般为 Unit 。