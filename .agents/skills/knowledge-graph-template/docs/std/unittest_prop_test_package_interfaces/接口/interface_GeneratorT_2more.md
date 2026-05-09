## interface Generator\<T>

```cangjie
public interface Generator<T> {
    func next(): T
}
```

功能：生成器生成 T 类型的值。

### func next()

```cangjie
func next(): T
```

功能：获取生成出来的 T 类型的值。

返回值：

- T - 生成的 T 类型的值。

## interface IndexAccess

```cangjie
public interface IndexAccess {
    func getElementAsAny(index: Int64): ?Any
}
```

功能：通过索引访问元组元素的实用程序接口。

### func getElementAsAny(Int64)

```cangjie
func getElementAsAny(index: Int64): ?Any
```

功能：通过索引访问元组元素。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 索引值。

返回值：

- ?[Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 元素值。若未获取到则为 `None` 。