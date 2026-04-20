## class DataStrategyProcessor\<T>

```cangjie
abstract sealed class DataStrategyProcessor<T> {}
```

功能：所有 [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 组件的基类。该类的实例由 [@Strategy](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#strategy-宏) 宏或成员函数创建。

### prop isInfinite

```cangjie
protected prop isInfinite: Bool
```

功能：获取该策略是否为无限。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)。

### func intoBenchmark(String, Configuration, (T, Int64, Int64) -> Float64)

```cangjie
public func intoBenchmark(
    caseName!: String,
    configuration!: Configuration,
    doRun!: (T, Int64, Int64) -> Float64
): Benchmark
```

功能：宏生成的代码使用的辅助函数。用于创建使用该策略的性能测试用例。

参数：

- caseName!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- configuration!: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 配置信息。
- doRun!: (T, Int64, Int64) -> Float64 - 性能测试用例执行体。

返回值：

- [Benchmark](#class-benchmark) - 性能测试用例对象。

### func intoUnitTestCase(String, Configuration, (T) -> Unit)

```cangjie
public func intoUnitTestCase(
    caseName!: String,
    configuration!: Configuration,
    doRun!: (T) -> Unit
): UnitTestCase
```

功能：宏生成的代码使用的辅助函数。用于创建使用该策略的测试用例。

参数：

- caseName!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- configuration!: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 配置信息。
- doRun!: (T) -> Unit - 性能测试用例执行体。

返回值：

- [UnitTestCase](#class-unittestcase) - 测试用例对象。

### func lastItemInfo()

```cangjie
protected func lastItemInfo(): Array<InputParameter>
```

功能：获取上一个处理条目的信息。

返回值：

- Array\<[InputParameter](./unittest_package_classes.md#class-inputparameter)> - 上一个处理条目的信息。

### func lastItem(Configuration)

```cangjie
protected func lastItem(configuration: Configuration): T
```

功能：获取上一个处理条目。

参数：

- configuration: [Configuration](./../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 处理策略配置信息。

返回值：

- T - 上一个处理条目。

### func provide(Configuration)

```cangjie
protected func provide(configuration: Configuration): Iterable<T>
```

功能：生成依据配置信息和数据策略生成的数据迭代器。

参数：

- configuration: [Configuration](./../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 处理策略配置信息。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 数据迭代器。

### func shrinkLastItem(Configuration, LazyCyclicNode)

```cangjie
protected func shrinkLastItem(configuration: Configuration, engine: LazyCyclicNode): Iterable<T>
```

功能：收缩上一个条目。

参数：

- configuration: [Configuration](./../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 配置信息。
- engine: [LazyCyclicNode](./unittest_package_classes.md#class-lazycyclicnode) - 惰性节点。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 收缩后的数据迭代器。