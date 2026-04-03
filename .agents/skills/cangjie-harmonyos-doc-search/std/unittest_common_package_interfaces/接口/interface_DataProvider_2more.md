## interface DataProvider

```cangjie
public interface DataProvider<T> {
    func provide(): Iterable<T>
}
```

功能：[DataStrategy](#interface-datastrategy) 的组件，用于提供测试数据，T 指定提供者提供的数据类型。

### func provide()

```cangjie
func provide(): Iterable<T>
```

功能：获取数据迭代器。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 数据迭代器。

### extend\<T> Array\<T> <: DataProvider\<T>

```cangjie
extend<T> Array<T> <: DataProvider<T>
```

功能：对 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> 进行扩展。

#### func provide()

```cangjie
public func provide(): Iterable<T>
```

功能：获取数据迭代器。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 数据迭代器。

### extend\<T> Range\<T> <: DataProvider\<T>

```cangjie
extend<T> Range<T> <: DataProvider<T>
```

功能：对 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<T> 进行扩展。

#### func provide()

```cangjie
public func provide(): Iterable<T>
```

功能：获取数据迭代器。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 数据迭代器。

## interface DataShrinker\<T>

```cangjie
public interface DataShrinker<T> {
    func shrink(value: T): Iterable<T>
}
```

功能：[DataStrategy](#interface-datastrategy) 的组件，用于在测试期间缩减数据，T 指定该收缩器处理的数据类型。

### func shrink(T)

```cangjie
func shrink(value: T): Iterable<T>
```

功能：获取类型 T 的值并生成较小值的集合。什么被认为是“较小”取决于数据的类型。

参数：

- value: T - 被缩减的值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 较小值的集合，当数据无法再被缩减时返回空集合。