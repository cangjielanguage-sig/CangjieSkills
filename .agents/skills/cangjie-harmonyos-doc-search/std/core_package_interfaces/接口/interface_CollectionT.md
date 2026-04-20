## interface Collection\<T>

```cangjie
public interface Collection<T> <: Iterable<T> {
    prop size: Int64
    func isEmpty(): Bool
    func toArray(): Array<T>
}
```

功能：该接口用来表示集合，通常容器类型应该实现该接口。

父类型：

- [Iterable](#interface-iterablee)\<T>

### prop size

```cangjie
prop size: Int64
```

功能：获取当前集合的大小，即集合中元素的个数。

类型：[Int64](core_package_intrinsics.md#int64)

### func isEmpty()

```cangjie
func isEmpty(): Bool
```

功能：判断当前集合是否为空。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果为空返回 true，否则返回 false。

### func toArray()

```cangjie
func toArray(): Array<T>
```

功能：将当前集合转为数组类型。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 转换得到的数组。