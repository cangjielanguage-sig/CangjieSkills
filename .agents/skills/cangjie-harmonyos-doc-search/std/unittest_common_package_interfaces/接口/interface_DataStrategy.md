## interface DataStrategy

```cangjie
public interface DataStrategy<T> {
    func provider(configuration: Configuration): DataProvider<T>
    func shrinker(configuration: Configuration): DataShrinker<T>
    prop isInfinite: Bool
}
```

功能：为参数化测试提供数据的策略，T 指定该策略操作的数据类型。

### prop isInfinite

```cangjie
prop isInfinite: Bool
```

功能：是否无法穷尽。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### func provider(Configuration)

```cangjie
func provider(configuration: Configuration): DataProvider<T>
```

功能：获取提供测试数据组件。

参数：

- configuration: [Configuration](unittest_common_package_classes.md#class-configuration) - 配置信息。

返回值：

- [DataProvider](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-dataprovider)\<T> - 提供测试数据的组件对象。

### func shrinker(Configuration)

```cangjie
func shrinker(configuration: Configuration): DataShrinker<T>
```

功能：获取缩减测试数据的组件。

参数：

- configuration: [Configuration](unittest_common_package_classes.md#class-configuration) - 配置信息。

返回值：

- [DataShrinker](#interface-datashrinkert)\<T> - 缩减测试数据的组件对象。

### extend\<T> Array\<T> <: DataStrategy\<T>

```cangjie
extend<T> Array<T> <: DataStrategy<T>
```

功能：对 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> 进行扩展。

#### prop isInfinite

```cangjie
public prop isInfinite: Bool
```

功能：是否无法穷尽。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

#### func provider(Configuration)

```cangjie
public func provider(configuration: Configuration): DataProvider<T>
```

功能：获取提供测试数据组件。

参数：

- configuration: [Configuration](unittest_common_package_classes.md#class-configuration) - 配置信息。

返回值：

- [DataProvider](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-dataprovider)\<T> - 提供测试数据的组件对象。

#### func shrinker(Configuration)

```cangjie
func shrinker(configuration: Configuration): DataShrinker<T>
```

功能：获取缩减测试数据的组件。

参数：

- configuration: [Configuration](unittest_common_package_classes.md#class-configuration) - 配置信息。

返回值：

- [DataShrinker](#interface-datashrinkert)\<T> - 缩减测试数据的组件对象。

### extend\<T> Range\<T> <: DataStrategy\<T>

```cangjie
extend<T> Range<T> <: DataStrategy<T>
```

功能：对 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<T> 进行扩展。

#### prop isInfinite

```cangjie
public prop isInfinite: Bool
```

功能：是否无法穷尽。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

#### func provider(Configuration)

```cangjie
public func provider(configuration: Configuration): DataProvider<T>
```

功能：获取提供测试数据组件。

参数：

- configuration: [Configuration](unittest_common_package_classes.md#class-configuration) - 配置信息。

返回值：

- [DataProvider](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-dataprovider)\<T> - 提供测试数据的组件对象。

#### func shrinker(Configuration)

```cangjie
func shrinker(configuration: Configuration): DataShrinker<T>
```

功能：获取缩减测试数据的组件。

参数：

- configuration: [Configuration](unittest_common_package_classes.md#class-configuration) - 配置信息。

返回值：

- [DataShrinker](#interface-datashrinkert)\<T> - 缩减测试数据的组件对象。