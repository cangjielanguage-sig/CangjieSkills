## class BenchReport

```cangjie
public class BenchReport <: Report {}
```

功能：提供性能用例执行结果报告处理能力。

父类型：

- [Report](#class-report)

### func reportTo\<T>(Reporter\<BenchReport, T>)

```cangjie
public func reportTo<T>(reporter: Reporter<BenchReport, T>): T
```

功能：打印性能用例结果报告。

参数：

- reporter: [Reporter](#class-report)\<[BenchReport](#class-benchreport), T> - 性能用例结果报告。

返回值：

- T - 打印结果返回值。一般为 Unit 类型。

## class CartesianProductProcessor\<T0,T1>

```cangjie
public class CartesianProductProcessor<T0, T1> <: DataStrategyProcessor<(T0, T1)> {
    public CartesianProductProcessor(let left: DataStrategyProcessor<T0>, let right: DataStrategyProcessor<T1>)
}
```

功能：笛卡尔积处理器。

父类型：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<(T0, T1)>

### CartesianProductProcessor(DataStrategyProcessor\<T0>, DataStrategyProcessor\<T1>)

```cangjie
public CartesianProductProcessor(let left: DataStrategyProcessor<T0>, let right: DataStrategyProcessor<T1>)
```

功能：CartesianProductProcessor 构造函数。

参数：

- left: [DataStrategyProcessor](#class-datastrategyprocessort)\<T0> - 数据策略处理器。
- right: [DataStrategyProcessor](#class-datastrategyprocessort)\<T1> - 数据策略处理器。

## class ConsoleReporter

```cangjie
public class ConsoleReporter <: Reporter<TestReport, Unit> & Reporter<BenchReport, Unit>{
    public ConsoleReporter(let colored!: Bool = true)
}
```

功能：打印单元测试用例结果或者性能测试用例结果到控制台。

父类型：

- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[TestReport](#class-testreport), [Unit](../../core/core_package_api/core_package_intrinsics.md#unit)>
- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[BenchReport](#class-benchreport), [Unit](../../core/core_package_api/core_package_intrinsics.md#unit)>

### ConsoleReporter(Bool)

```cangjie
public ConsoleReporter(let colored!: Bool = true)
```

功能：ConsoleReporter 构造函数。

参数：

- colored!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用带颜色的打印，默认带颜色。

## class TextReporter\<PP>

```cangjie
public class TextReporter<PP> <: Reporter<TestReport, PP> & Reporter<BenchReport, PP> where PP <: PrettyPrinter {
    public TextReporter(let into!: PP)
}
```

功能：将单元测试用例结果或性能测试结果打印到 [PrettyPrinter](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-prettyprinter) 的子类。格式与 [ConsoleReporter](#class-consolereporter) 相同。

父类型：

- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[TestReport](#class-testreport), PP>
- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[BenchReport](#class-benchreport), PP>

### TextReporter(PP)

```cangjie
public TextReporter(let into!: PP)
```

功能：TextReporter 构造函数。

参数：

- into!: PP - [PrettyPrinter](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-prettyprinter) 的子类。打印报告。