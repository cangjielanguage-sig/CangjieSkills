## interface Iterable\<E>

```cangjie
public interface Iterable<E> {
    func iterator(): Iterator<E>
}
```

功能：该接口表示可迭代，实现了该接口的类型（通常为容器类型）可以在 `for-in` 语句中实现迭代，也可以获取其对应的迭代器类型实例，调用 `next` 函数实现迭代。

本包已经为 [Array](core_package_structs.md#struct-arrayt)、[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)、[HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 等基础容器类型实现了该接口，用户可以为其他类型实现该接口，使之支持迭代遍历的功能。

### func iterator()

```cangjie
func iterator(): Iterator<E>
```

功能：获取迭代器。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<E> - 迭代器。

## interface Less\<T>

```cangjie
public interface Less<T> {
    operator func <(rhs: T): Bool
}
```

功能：该接口表示小于计算。

### operator func <(T)

```cangjie
operator func <(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否小于参数指向的 `T` 类型实例。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果小于，返回 true，否则返回 false。

## interface LessOrEqual\<T>

```cangjie
public interface LessOrEqual<T> {
    operator func <=(rhs: T): Bool
}
```

功能：该接口表示小于等于计算。

### operator func <=(T)

```cangjie
operator func <=(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否小于等于参数指向的 `T` 类型实例。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果小于等于，返回 true，否则返回 false。

## interface NotEqual\<T>

```cangjie
public interface NotEqual<T> {
    operator func !=(rhs: T): Bool
}
```

功能：该接口用于支持判不等操作。

### operator func !=(T)

```cangjie
operator func !=(rhs: T): Bool
```

功能：判断两个实例是否不相等。

参数：

- rhs: T - 待比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果不相等，返回 true，否则返回 false。

## interface Resource

```cangjie
public interface Resource {
    func close(): Unit
    func isClosed(): Bool
}
```

功能：该接口用于资源管理，通常用于内存、句柄等资源的关闭和释放。

实现了该接口的类型可以在 `try-with-resource` 语法上下文中实现自动资源释放。

### func close()

```cangjie
func close(): Unit
```

功能：关闭资源。

### func isClosed()

```cangjie
func isClosed(): Bool
```

功能：判断资源是否已经关闭。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果已经关闭返回 true，否则返回 false。

## interface ThreadContext

```cangjie
public interface ThreadContext {
    func end(): Unit
    func hasEnded(): Bool
}
```

功能：仓颉线程上下文接口。

用户创建 `thread` 时，除了缺省 `spawn` 表达式入参，也可以通过传入不同 [ThreadContext](core_package_interfaces.md#interface-threadcontext) 类型的实例，选择不同的线程上下文，然后一定程度上控制并发行为。

目前不允许用户自行实现 [ThreadContext](core_package_interfaces.md#interface-threadcontext) 接口，仓颉语言根据使用场景，提供了 `MainThreadContext`, 具体定义可在终端框架库中查阅。

### func end()

```cangjie
func end(): Unit
```

功能：结束方法，用于向当前 context 发送结束请求。

### func hasEnded()

```cangjie
func hasEnded(): Bool
```

功能：检查方法，用于检查当前 context 是否已结束。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果结束返回 true，否则返回 false。