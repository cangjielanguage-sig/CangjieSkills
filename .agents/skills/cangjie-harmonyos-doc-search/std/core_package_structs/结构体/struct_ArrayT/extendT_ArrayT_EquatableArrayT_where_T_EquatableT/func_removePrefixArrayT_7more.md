#### func removePrefix(Array\<T>)

```cangjie
public func removePrefix(prefix: Array<T>): Array<T>
```

功能：删除前缀。

如果当前数组开头与 prefix 完全匹配，删除其前缀。返回值为当前数组删除前缀后得到的切片。

参数：

- prefix: [Array](./core_package_structs.md#struct-arrayt)\<T> - 待删除的前缀。

返回值：

- [Array](./core_package_structs.md#struct-arrayt)\<T> - 删除前缀后得到的原数组切片。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 1, 2, 3].removePrefix([1, 2])
    println(arr)
    return 0
}
```

运行结果：

```text
[1, 2, 3]
```

#### func removeSuffix(Array\<T>)

```cangjie
public func removeSuffix(suffix: Array<T>): Array<T>
```

功能：删除后缀。

如果当前数组结尾与 suffix 完全匹配，删除其后缀。返回值为当前数组删除后缀后得到的切片。

参数：

- suffix: [Array](./core_package_structs.md#struct-arrayt)\<T> - 待删除的后缀。

返回值：

- [Array](./core_package_structs.md#struct-arrayt)\<T> - 删除后缀后得到的原数组切片。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 3, 2, 3].removeSuffix([2, 3])
    println(arr)
    return 0
}
```

运行结果：

```text
[1, 2, 3]
```

#### func trimEnd((T)->Bool)

```cangjie
public func trimEnd(predicate: (T)->Bool): Array<T>
```

功能：修剪当前数组，从尾开始删除符合过滤条件的函数，直到第一个不符合的元素为止，并返回当前数组的切片。

参数：

- predicate: (T)->[Bool](./core_package_intrinsics.md#bool) - 过滤条件。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 修剪后的数组切片。

#### func trimEnd(Array\<T>)

```cangjie
public func trimEnd(set: Array<T>): Array<T>
```

功能：修剪当前数组，从尾开始删除在指定集合 set 中的元素，直到第一个不在 set 中的元素为止，并返回当前数组的切片。

参数：

- set: [Array](core_package_structs.md#struct-arrayt)\<T> - 待删除的元素的集合。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 修剪后的数组切片。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [2, 1, 2, 2, 3].trimEnd([2, 3])
    println(arr)
    return 0
}
```

运行结果：

```text
[2, 1]
```

#### func trimStart((T)->Bool)

```cangjie
public func trimStart(predicate: (T)->Bool): Array<T>
```

功能：修剪当前数组，从头开始删除符合过滤条件的函数，直到第一个不符合的元素为止，并返回当前数组的切片。

参数：

- predicate: (T)->[Bool](./core_package_intrinsics.md#bool) - 过滤条件。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 修剪后的数组切片。

#### func trimStart(Array\<T>)

```cangjie
public func trimStart(set: Array<T>): Array<T>
```

功能：修剪当前数组，从头开始删除在指定集合 set 中的元素，直到第一个不在 set 中的元素为止，并返回当前数组的切片。

参数：

- set: [Array](core_package_structs.md#struct-arrayt)\<T> - 待删除的元素的集合。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<T> - 修剪后的数组切片。

示例：

<!-- verify -->
```cangjie
main(): Int64 {
    let arr = [1, 2, 1, 3, 1].trimStart([1, 2])
    println(arr)
    return 0
}
```

运行结果：

```text
[3, 1]
```

#### operator func !=(Array\<T>)

```cangjie
public operator const func !=(that: Array<T>): Bool
```

功能：判断当前实例与指定 [Array](core_package_structs.md#struct-arrayt)\<T> 实例是否不等。

参数：

- that: [Array](core_package_structs.md#struct-arrayt)\<T> - 用于与当前实例比较的另一个 [Array](core_package_structs.md#struct-arrayt)\<T> 实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果不相等，则返回 true；相等则返回 false。