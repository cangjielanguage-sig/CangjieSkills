## class Report

```cangjie
sealed abstract class Report {}
```

功能：打印测试用例结果报告的基类。

### prop errorCount

```cangjie
public prop errorCount: Int64
```

功能：获取错误的用例个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)。

### prop caseCount

```cangjie
public prop caseCount: Int64
```

功能：获取用例个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)。

### prop passedCount

```cangjie
public prop passedCount:   Int64
```

功能：获取通过的用例个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)。

### prop failedCount

```cangjie
public prop failedCount:   Int64
```

功能：获取失败的用例个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)。

### prop skippedCount

```cangjie
public prop skippedCount:   Int64
```

功能：获取跳过的用例个数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)。

## class RawStatsReporter

```cangjie
public class RawStatsReporter <: Reporter<BenchReport, HashMap<String, (Float64, Float64)>> {
    public RawStatsReporter()
}
```

功能：未处理的性能测试数据报告器。仅给框架内部使用。

父类型：

- [Reporter](unittest_package_interfaces.md#interface-reporter)\<[BenchReport](#class-benchreport), [HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<[String](../../core/core_package_api/core_package_structs.md#struct-string), ([Float64](../../core/core_package_api/core_package_intrinsics.md#float64), [Float64](../../core/core_package_api/core_package_intrinsics.md#float64))>>

### RawStatsReporter()

```cangjie
public RawStatsReporter()
```

功能：RawStatsReporter 构造函数。

## class SimpleProcessor\<T>

```cangjie
public class SimpleProcessor<T> <: DataStrategyProcessor<T> {
    public SimpleProcessor(let buildDelegate:() -> DataStrategy<T>, let name: String)
}
```

功能：简单的数据策略处理器。对 [DataStrategyProcessor](#class-datastrategyprocessort) 的一种实现。

父类型：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<T>

### SimpleProcessor(() -> DataStrategy\<T>, String)

```cangjie
public SimpleProcessor(let buildDelegate:() -> DataStrategy<T>, let name: String)
```

功能：SimpleProcessor 构造函数。

参数：

- buildDelegate: () -> [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)\<T> - 生成数据策略的闭包。
- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 处理器名称。