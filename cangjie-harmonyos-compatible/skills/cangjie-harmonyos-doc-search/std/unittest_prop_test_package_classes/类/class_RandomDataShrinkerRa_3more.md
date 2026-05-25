## class RandomDataShrinkerRange\<T>

```cangjie
public class RandomDataShrinkerRange<T> <: DataShrinker<T> where T <: Comparable<T> {}
```

功能：可按照给定范围生成的数据缩减器。

父类型：

- [DataShrinker\<T>](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datashrinkert)

### func shrink(T)

```cangjie
public override func shrink(value: T): Iterable<T>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 数据迭代器。

## class RandomDataStrategy\<T>

```cangjie
public class RandomDataStrategy<T> <: DataStrategy<T> where T <: Arbitrary<T>{}
```

功能：使用随机数据生成的 [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 接口的实现。

父类型：

- [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)\<T>

### prop isInfinite

```cangjie
public override prop isInfinite: Bool
```

功能：当该策略为无穷尽时，值为 true, 否则为 false。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)。

### func provider(Configuration)

```cangjie
public override func provider(configuration: Configuration): RandomDataProvider<T>
```

功能：获取随机数据的提供者。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 参数配置信息。

返回值：

- [RandomDataProvider](#class-randomdataprovidert)\<T> - 随机数提供者。

### func shrinker(Configuration)

```cangjie
public override func shrinker(_: Configuration): RandomDataShrinker<T>
```

功能：获取随机数据的缩减器。

参数：

- _: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 参数配置信息。

返回值：

- [RandomDataShrinker](#class-randomdatashrinkert)\<T> - 随机数据的缩减器。

## class RandomDataStrategyRange\<T>

```cangjie
public class RandomDataStrategyRange<T> <: DataStrategy<T> where T <: ArbitraryRange<T> {}
```

功能：可按照给定范围生成的数据策略器。

父类型：

- [DataStrategy\<T>](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy)

### func provider(Configuration)

```cangjie
public override func provider(configuration: Configuration): RandomDataProviderRange<T>
```

功能：获取随机数据的提供者。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 参数配置信息。

返回值：

- [RandomDataProviderRange](unittest_prop_test_package_classes.md#class-randomdataproviderranget)\<T> - 随机数提供者。

### func shrinker(Configuration)

```cangjie
public override func shrinker(_: Configuration): RandomDataShrinkerRange<T>
```

功能：获取随机数据的缩减器。

参数：

- _: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 参数配置信息。

返回值：

- [RandomDataShrinkerRange](#class-randomdatashrinkerranget)\<T> - 随机数据的缩减器。

### prop isInfinite

```cangjie
public prop isInfinite: Bool 
```

功能：当该策略为无穷尽时，值为 true, 否则为 false。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)。