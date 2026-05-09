#### func productWithUnit\<P>(P): MapProcessor\<(T, Unit), T>

```cangjie
public func productWithUnit<P>(p: P): MapProcessor<(T, Unit), T> where P <: DataStrategyProcessor<Unit>
```

功能：[DataStrategyProcessor](#class-datastrategyprocessort) 的便捷适配器。

参数：

- p: [P](#class-datastrategyprocessort) -  数据策略处理器。

返回值：

- | [MapProcessor\<(T, Unit),R>](../unittest_package_api/unittest_package_classes.md#class-mapprocessortr) - 处理器。