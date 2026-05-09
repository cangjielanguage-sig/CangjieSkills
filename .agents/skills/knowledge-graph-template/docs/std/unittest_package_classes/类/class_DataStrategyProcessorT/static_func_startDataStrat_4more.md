### static func start(DataStrategy\<T>, String)

```cangjie
public static func start(s: DataStrategy<T>, name: String): SimpleProcessor<T>
```

功能：[DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 的组合和映射的起点。

参数：

- s: [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)\<T> - 数据策略。
- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。

返回值：

- [SimpleProcessor\<T>](#class-simpleprocessort) - 测试用例处理器。

### static func start\<U>(() -> DataStrategy\<U>, String)

```cangjie
public static func start<U>(
    f: () -> DataStrategy<U>,
    name: String
): DataStrategyProcessor<U> where U <: BenchInputProvider < T >
```

功能：[DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 的组合和映射的起点。

参数：

- s: () -> [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)\<U> - 生成数据策略的闭包。
- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。

返回值：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<T> - 数据策略处理器。

### static func start(() -> DataStrategy\<T>, String, Int64)

```cangjie
public static func start(
    f: () -> DataStrategy<T>,
    name: String,
    x!: Int64 = 0
): SimpleProcessor<T>
```

功能：[DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 的组合和映射的起点。

参数：

- s: () -> [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)\<T> - 生成数据策略的闭包。
- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- x!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 为实现不同返回值的重构增加的参数。

返回值：

- [SimpleProcessor\<T>](#class-simpleprocessort) - 测试用例处理器。

### static func start(() -> DataStrategyProcessor\<T>, String)

```cangjie
public static func start(f: () -> DataStrategyProcessor<T>, name: String): DataStrategyProcessor<T>
```

功能：[DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 的组合和映射的起点。

参数：

- s: () -> [DataStrategyProcessor](#class-datastrategyprocessort)\<T> - 生成数据策略处理器的闭包。
- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。

返回值：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<T> - 数据策略处理器。