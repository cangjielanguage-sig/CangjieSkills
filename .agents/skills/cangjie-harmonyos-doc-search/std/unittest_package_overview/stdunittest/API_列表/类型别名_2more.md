### 类型别名

|  类型别名 | 功能  |
| ------------ | ------------ |
| [MeasurementUnitTable](./unittest_package_api/unittest_package_types.md#type-measurementunittable) | 用于为性能测试指定 [Measurement](./unittest_package_api/unittest_package_interfaces.md#interface-measurement) 实例。|

### 接口

|              接口名          |           功能           |
| --------------------------- | ------------------------ |
| [BenchInputProvider](./unittest_package_api/unittest_package_interfaces.md#interface-benchinputprovider) | 用于处理性能测试的接口，其中需要在每次性能测试调用之前执行一些代码或者性能测试的输入发生了变化，并且每次都必须从头开始生成。|
| [BenchmarkConfig](./unittest_package_api/unittest_package_interfaces.md#interface-benchmarkconfig) | 空接口，区分部分 [Configuration](../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 函数为性能相关配置。|
| [BenchmarkInputMarker](./unittest_package_api/unittest_package_interfaces.md#interface-benchmarkinputmarker) | 当我们不知道 `T` 时，该接口能够检测 `BenchInputProvider<T>` 。|
| [Measurement](./unittest_package_api/unittest_package_interfaces.md#interface-measurement) | 在性能测试过程中可以收集和分析各种数据的接口。性能测试期间使用的 `Measurement` 的具体实例在 `@Measure` 宏中指定（例如在类声明中）。|
| [NearEquatable\<CT, D>](./unittest_package_api/unittest_package_interfaces.md#interface-nearequatablect-d) | 判断某个对象是否基于这个 delta 近似相等。|
| [TestClass](./unittest_package_api/unittest_package_interfaces.md#interface-testclass) | 提供创建 [TestSuite](./unittest_package_api/unittest_package_classes.md#class-testsuite) 的方法。|