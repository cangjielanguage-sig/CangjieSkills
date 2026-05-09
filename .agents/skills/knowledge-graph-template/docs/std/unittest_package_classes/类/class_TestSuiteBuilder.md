## class TestSuiteBuilder

```cangjie
public class TestSuiteBuilder {}
```

功能：提供配置测试套方法的测试套构造器。

### func add(Benchmark)

```cangjie
public func add(benchmark: Benchmark): TestSuiteBuilder
```

功能：为测试套添加性能用例。

参数：

- benchmark: [Benchmark](#class-benchmark) - 性能测试用例。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func add(UnitTestCase)

```cangjie
public func add(test: UnitTestCase): TestSuiteBuilder
```

功能：为测试套添加单元测试用例。

参数：

- test: [UnitTestCase](#class-unittestcase) - 单元测试用例。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func afterAll(() -> Unit)

```cangjie
public func afterAll(body: () -> Unit): TestSuiteBuilder
```

功能：为测试套添加在所有用例执行完成后执行的生命周期管理闭包。

参数：

- body: () -> Unit - 执行体。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func afterEach(() -> Unit)

```cangjie
public func afterEach(body: () -> Unit): TestSuiteBuilder
```

功能：为测试套添加在每个用例执行完成后执行的生命周期管理闭包。

参数：

- body: () -> Unit - 执行体。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func afterEach((String) -> Unit)

```cangjie
public func afterEach(body: (String) -> Unit): TestSuiteBuilder
```

功能：为测试套添加在每个用例执行完成后执行的生命周期管理闭包。

参数：

- body: (String) -> Unit - 执行体。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func beforeAll(() -> Unit)

```cangjie
public func beforeAll(body: () -> Unit): TestSuiteBuilder
```

功能：为测试套添加在所有用例执行前执行的生命周期管理闭包。

参数：

- body: () -> Unit - 执行体。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func beforeEach(() -> Unit)

```cangjie
public func beforeEach(body: () -> Unit): TestSuiteBuilder
```

功能：为测试套添加在每个用例执行前执行的生命周期管理闭包。

参数：

- body: () -> Unit - 执行体。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func beforeEach((String) -> Unit)

```cangjie
public func beforeEach(body: (String) -> Unit): TestSuiteBuilder
```

功能：为测试套添加在每个用例执行前执行的生命周期管理闭包。

参数：

- body: (String) -> Unit - 执行体。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func template(TestSuite)

```cangjie
public func template(template: TestSuite): TestSuiteBuilder
```

功能：执行此方法可为测试套件设置模板。

参数

- template: TestSuite - 将作为模板的测试套件。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func build()

```cangjie
public func build(): TestSuite
```

功能：配置完成后构造测试套。

返回值：

- [TestSuite](#class-testsuite) - 测试套。

### func configure(Configuration)

```cangjie
public func configure(configuration: Configuration): TestSuiteBuilder
```

功能：为测试套添加配置信息。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 测试配置信息。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。

### func setName(String)

```cangjie
public func setName(name: String): TestSuiteBuilder
```

功能：为测试套设置名称。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 测试套名称。

返回值：

- [TestSuiteBuilder](#class-testsuitebuilder) - 测试组合构造器。