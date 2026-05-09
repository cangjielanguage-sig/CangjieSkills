### func trimEnd((Rune)->Bool)

```cangjie
public func trimEnd(predicate: (Rune)->Bool): String
```

功能：修剪当前字符串，从尾开始删除符合过滤条件的 [Rune](./core_package_intrinsics.md#rune) 字符，直到第一个不符合过滤条件的 [Rune](./core_package_intrinsics.md#rune) 字符为止。

参数：

- predicate: ([Rune](./core_package_intrinsics.md#rune))->[Bool](./core_package_intrinsics.md#bool) - 过滤条件。

返回值：

- [String](./core_package_structs.md#struct-string) - 修剪后得到的新字符串。

示例：

<!-- verify -->
```cangjie
main() {
    var str = "14122"
    var subStr = str.trimEnd({c => c == r'2'})
    println(subStr)
}
```

运行结果：

```text
141
```

### func trimEnd(Array\<Rune>)

```cangjie
public func trimEnd(set: Array<Rune>): String
```

功能：修剪当前字符串，从尾开始删除在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符，直到第一个不在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符为止。

参数：

- set: [Array](./core_package_structs.md#struct-arrayt)\<[Rune](./core_package_intrinsics.md#rune)> - 待删除的字符的集合。

返回值：

- [String](./core_package_structs.md#struct-string) - 修剪后得到的新字符串。

示例：

<!-- verify -->
```cangjie
main() {
    var str = "14122"
    var subStr = str.trimEnd([r'1', r'2'])
    println(subStr)
}
```

运行结果：

```text
14
```

### func trimEnd(String)

```cangjie
public func trimEnd(set: String): String
```

功能：修剪当前字符串，从尾开始删除在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符，直到第一个不在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符为止。

参数：

- set: [String](./core_package_structs.md#struct-string) - 待删除的字符的集合。

返回值：

- [String](./core_package_structs.md#struct-string) - 修剪后得到的新字符串。

示例：

<!-- verify -->
```cangjie
main() {
    var str = "14122"
    var subStr = str.trimEnd("12")
    println(subStr)
}
```

运行结果：

```text
14
```

### func trimStart((Rune)->Bool)

```cangjie
public func trimStart(predicate: (Rune)->Bool): String
```

功能：修剪当前字符串，从头开始删除符合过滤条件的 [Rune](./core_package_intrinsics.md#rune) 字符，直到第一个不符合过滤条件的 [Rune](./core_package_intrinsics.md#rune) 字符为止。

参数：

- predicate: ([Rune](./core_package_intrinsics.md#rune))->[Bool](./core_package_intrinsics.md#bool) - 过滤条件。

返回值：

- [String](./core_package_structs.md#struct-string) - 修剪后得到的新字符串。

### func trimStart(Array\<Rune>)

```cangjie
public func trimStart(set: Array<Rune>): String
```

功能：修剪当前字符串，从头开始删除在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符，直到第一个不在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符为止。

例如 "12241".trimStart([r'1', r'2']) = "41"。

参数：

- set: [Array](./core_package_structs.md#struct-arrayt)\<[Rune](./core_package_intrinsics.md#rune)> - 待删除的字符的集合。

返回值：

- [String](./core_package_structs.md#struct-string) - 修剪后得到的新字符串。

### func trimStart(String)

```cangjie
public func trimStart(set: String): String
```

功能：修剪当前字符串，从头开始删除在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符，直到第一个不在 set 中的 [Rune](./core_package_intrinsics.md#rune) 字符为止。

例如 "12241".trimStart("12") = "41"。

参数：

- set: [String](./core_package_structs.md#struct-string) - 待删除的字符的集合。

返回值：

- [String](./core_package_structs.md#struct-string) - 修剪后得到的新字符串。