## class RandomDataProvider\<T>

```cangjie
public class RandomDataProvider<T> <: DataProvider<T> where T <: Arbitrary<T> {
    public RandomDataProvider(private let configuration: Configuration)
}
```

功能：使用随机数据生成的 [DataProvider](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-dataprovider) 接口的实现。

父类型：

- [DataProvider](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-dataprovider)\<T>

### RandomDataProvider(Configuration)

```cangjie
public RandomDataProvider(private let configuration: Configuration)
```

功能：构造一个随机数据提供者 RandomDataProvider 的对象。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 配置对象，必须包含一个随机生成器，名称为 `random` ，类型为 random.[Random](../../random/random_package_api/random_package_classes.md#class-random)。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 configuration 不包含 random 实例时，抛出异常。

### func provide()

```cangjie
public override func provide(): Iterable<T>
```

功能：提供随机化生成的数据。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 从 T 的任意实例创建的无限迭代器。

## class RandomDataProviderRange\<T>

```cangjie
public class RandomDataProviderRange<T> <: DataProvider<T> where T <: ArbitraryRange<T> {
    public RandomDataProviderRange(configuration: Configuration, min: T, max: T)
}
```

功能：可按照给定范围生成的数据提供器。

父类型：

- [DataProvider\<T>](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-dataprovider)

### RandomDataProviderRange(Configuration, T, T)

```cangjie
RandomDataProviderRange(configuration: Configuration, min: T, max: T)
```

功能：构造器。

参数：

- configuration: [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 参数配置信息。
- min: T - 最小值（包含）。
- max: T - 最大值（不包含）。

### func provide()

```cangjie
override func provide(): Iterable<T>
```

功能：提供随机化生成的数据。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 数据迭代器。

## class RandomDataShrinker\<T>

```cangjie
public class RandomDataShrinker<T> <: DataShrinker<T> {}
```

功能：使用随机数据生成的 [DataShrinker](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datashrinkert) 接口的实现。

父类型：

- [DataShrinker](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datashrinkert)\<T>

### func shrink(T)

```cangjie
public override func shrink(value: T): Iterable<T>
```

功能：获取值的缩减器。

参数：

- value: T - 参数值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 如果参数实现了 [Shrink](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-shrinkt) 接口，则返回缩减后的迭代器，如果未实现，则返回空的数组。