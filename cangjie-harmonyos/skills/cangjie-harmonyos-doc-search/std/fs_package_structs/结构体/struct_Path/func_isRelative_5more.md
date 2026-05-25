### func isRelative()

```cangjie
public func isRelative(): Bool
```

功能：判断 [Path](fs_package_structs.md#struct-path) 是否是相对路径，其结果与函数 [isAbsolute](fs_package_structs.md#func-isabsolute) 结果相反。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，是相对路径；false，不是相对路径。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当路径为空或包含字符串结束符则抛出异常。

### func join(Path)

```cangjie
public func join(path: Path): Path
```

功能：在当前路径后拼接另一个路径字符串形成新路径。

- 对于路径 "a/b"，"c"，返回 "a/b/c"。
- 对于路径 "a"，"b/c"，返回 "a/b/c"。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 另一个 [Path](fs_package_structs.md#struct-path)。

返回值：

- [Path](fs_package_structs.md#struct-path) - 新路径的 [Path](fs_package_structs.md#struct-path) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果参数 path 是绝对路径则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当前路径为空或当前路径、入参路径非法时抛出异常。

### func join(String)

```cangjie
public func join(path: String): Path
```

功能：在当前路径后拼接另一个路径字符串形成新路径。

- 对于路径 "a/b"，"c"，返回 "a/b/c"。
- 对于路径 "a"，"b/c"，返回 "a/b/c"。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 另一个路径的字符串。

返回值：

- [Path](fs_package_structs.md#struct-path) - 新路径的 [Path](fs_package_structs.md#struct-path) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果参数 path 是绝对路径则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当前路径为空或当前路径、入参路径非法时抛出异常。

### func normalize()

```cangjie
public func normalize(): Path
```

功能：将路径字符串进行规范化处理，并用规范化后的字符串构造新的 [Path](./fs_package_structs.md#struct-path) 实例。该函数仅做字符串解析，不会进行 io 操作。

规范化规则：

- 将连续的多个路径分隔符替换为单个路径分隔符；
- 删除末尾的路径分隔符（不删除作为根目录的路径分隔符或卷名中的字符）；
- 删除每一个 "." 路径名元素（代表当前目录）；
- 删除每一个路径内的 ".." 路径名元素（代表父目录）和它前面的非 ".." 路径名元素；
- 删除开始于根路径的 ".." 路径名元素，即将路径开始处的 "/.." 替换为 "/"（Windows 系统中还会将 "\\.." 替换为 "\\"）；
- 相对路径保留开头的 "../"（Windows 系统中还将保留 "..\\"）;
- 最后如果得到空路径，返回 Path(".")。

特别地，Windows 文件系统中，卷名部分仅做分隔符转换，即 "/" 转换为 "\\"。

返回值：

- [Path](./fs_package_structs.md#struct-path) - 规范化后的 [Path](./fs_package_structs.md#struct-path) 实例。

### func toString()

```cangjie
public func toString(): String
```

功能：获得 [Path](fs_package_structs.md#struct-path) 的路径字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - [Path](fs_package_structs.md#struct-path) 的路径字符串。