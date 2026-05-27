### extend \<T> DataStrategyProcessor\<T>

```cangjie
extend <T> DataStrategyProcessor<T> {}
```

#### func map\<R>((T) -> R)

```cangjie
public func map<R>(f: (T) -> R): MapProcessor<T, R>
```

功能：简单地将 `f` 应用于原始数据策略的每个项目。 [Shrink](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-shrinkt) 也会发生在原始输入上，然后进行映射。

参数：

- f: (T) -> R - 需要增加的处理逻辑函数。

返回值：

- [MapProcessor\<T, R>](#class-mapprocessortr) - 应用 `f` 后的处理器。

#### func mapWithConfig\<R>((T, Configuration) -> R)

```cangjie
public func mapWithConfig<R>(f: (T, Configuration) -> R): MapProcessor<T, R>
```

功能：可以访问当前的 [Configuration](./../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) ，只需将 `f` 应用于原始数据策略的每个项目。 [Shrink](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-shrinkt) 也会发生在原始输入上，然后进行映射。

参数：

- f: (T, Configuration) -> R - 需要增加的处理逻辑函数。

返回值：

- [MapProcessor\<T, R>](#class-mapprocessortr) - 应用 `f` 后的处理器。

#### func flatMap\<R>((T) -> DataProvider\<R>)

```cangjie
public func flatMap<R>(f: (T) -> DataProvider<R>): FlatMapProcessor<T, R>
```

功能：简单地将 `f` 应用于原始数据策略的每个项目，然后展平结果。 [Shrink](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-shrinkt)  也会发生在原始输入上，然后进行 [flatMap](../../collection/collection_package_api/collection_package_function.md#func-flatmapt-rt---iterabler) 。

参数：

- f: (T) -> [DataProvider](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)\<R> - 需要增加的处理逻辑函数。

返回值：

- [FlatMapProcessor\<T, R>](#class-flatmapprocessortr) - 应用 `f` 后的处理器。

#### func flatMapStrategy((T) -> DataStrategy\<R>)

```cangjie
public func flatMapStrategy<R>(f: (T) -> DataStrategy<R>): FlatMapStrategyProcessor<T, R>
```

功能：简单地将 `f` 应用于原始数据策略的每个项目，然后展平结果。 [Shrink](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-shrinkt) 是通过返回的策略而不是原始输入来完成的。

参数：

- f: (T) -> [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)\<R> - 需要增加的处理逻辑函数。

返回值：

- [FlatMapStrategyProcessor\<T, R>](#class-flatmapstrategyprocessortr) - 应用 `f` 后的处理器。

#### func product(DataStrategyProcessor\<R>)

```cangjie
public func product<R>(p: DataStrategyProcessor<R>): CartesianProductProcessor<T, R>
```

功能：笛卡尔积组合器创建包含原始策略中元素的所有可能排列的数据策略。
对于无限策略，它首先迭代所有有限的子策略，然后才推进无限的子策略。
[Shrink](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-shrinkt)  独立且统一地发生在原始策略的每个元素上。

参数：

- p: [DataStrategyProcessor](#class-datastrategyprocessort)\<R> - 数据策略处理器。

返回值：

- [CartesianProductProcessor\<T, R>](#class-cartesianproductprocessort0t1) - 笛卡尔积处理器。