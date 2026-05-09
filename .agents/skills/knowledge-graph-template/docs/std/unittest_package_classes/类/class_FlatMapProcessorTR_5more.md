## class FlatMapProcessor\<T,R>

```cangjie
public class FlatMapProcessor<T,R> <: DataStrategyProcessor<R> {}
```

功能：对参数数据进行 [FlatMap](../../collection/collection_package_api/collection_package_function.md#func-flatmapt-rt---iterabler) 的处理器。

父类型：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<R>

## class FlatMapStrategyProcessor\<T,R>

```cangjie
public class FlatMapStrategyProcessor<T,R> <: DataStrategyProcessor<R> {}
```

功能：对参数数据进行 [FlatMap](../../collection/collection_package_api/collection_package_function.md#func-flatmapt-rt---iterabler) 的处理器。

父类型：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<R>

## class InputParameter

```cangjie
public class InputParameter {}
```

功能：入参对象类型。

## class LazyCyclicNode

```cangjie
public open class LazyCyclicNode {}
```

功能：用于在一个循环中一个接一个地推进类型擦除的内部惰性迭代器。

### func advance()

```cangjie
protected open func advance(): ?Unit
```

功能：前进一个值。

返回值：

- ?Unit - 当无法前进时返回 None ，否则返回 Unit 。

### func recover()

```cangjie
protected open func recover(): Unit
```

功能：恢复或后退一个值。

## class MapProcessor\<T,R>

```cangjie
public class MapProcessor<T,R> <: DataStrategyProcessor<R> {}
```

功能：对参数数据进行 [Map](../../collection/collection_package_api/collection_package_function.md#func-mapt-rt---r) 的处理器。

父类型：

- [DataStrategyProcessor](#class-datastrategyprocessort)\<R>