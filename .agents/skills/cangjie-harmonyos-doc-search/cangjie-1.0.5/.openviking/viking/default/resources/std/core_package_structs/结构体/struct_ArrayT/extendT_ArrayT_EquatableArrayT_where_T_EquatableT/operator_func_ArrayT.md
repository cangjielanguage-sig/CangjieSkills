#### operator func ==(Array\<T>)

```cangjie
public operator const func ==(that: Array<T>): Bool
```

功能：判断当前实例与指定 [Array](core_package_structs.md#struct-arrayt)\<T> 实例是否相等。

两个 [Array](core_package_structs.md#struct-arrayt)\<T> 相等指的是其中的每个元素都相等。

参数：

- that: [Array](core_package_structs.md#struct-arrayt)\<T> - 用于与当前实例比较的另一个 [Array](core_package_structs.md#struct-arrayt)\<T> 实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果相等，则返回 true，否则返回 false。