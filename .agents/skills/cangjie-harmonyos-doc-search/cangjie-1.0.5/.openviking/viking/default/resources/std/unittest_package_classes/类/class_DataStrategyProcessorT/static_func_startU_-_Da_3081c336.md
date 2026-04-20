### static func start\<U>(() -> DataStrategyProcessor\<U>, String, Int64)

```cangjie
public static func start<U>(
    f: () -> DataStrategyProcessor<U>,
    name: String,
    x!: Int64 = 0
): DataStrategyProcessor<U> where U <: BenchInputProvider<T>
```

功能：[DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 的组合和映射的起点。

参数：

- s: () -> [DataStrategyProcessor](#class-datastrategyprocessort)\<U> - 生成数据策略处理器的闭包。
- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用例名称。
- x!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 为实现不同返回值的重构增加的参数。

返回值：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<U> where U <: [BenchInputProvider](./unittest_package_interfaces.md#interface-benchinputprovider)\<T> - 数据策略处理器。