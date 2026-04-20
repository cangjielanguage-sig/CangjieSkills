### prop parent

```cangjie
public prop parent: Path
```

功能：获得该 [Path](fs_package_structs.md#struct-path) 实例的父路径。

整个路径字符串被划分为 parent 和 fileName，以最后一个有效文件分隔符（末尾的分隔符会被忽略）作为分界。如果 parent 不存在，就返回空字符串构造的 Path 实例。parent 和 fileName 部分都不包含末尾分隔符，parent 保留表示根目录的分隔符。无父目录时返回空的 [Path](./fs_package_structs.md#struct-path) 实例。

该属性不会访问文件系统，也不会消除特殊名称。如果有需要可以跟规范化搭配使用。

该属性在不同操作系统行为有差异，在 Windows 系统中，文件分隔符为 "\\" 或 "/"（规范化时会统一转换为 "\\"），在 Linux、macOS 系统中，文件分隔符为 "/"。

以下示例适用于所有系统：

- 对于路径 "/a/b/c"，此属性返回 Path("/a/b")；
- 对于路径 "/a/b/"，此属性返回 Path("/a")；
- 对于路径 "/a"，此属性返回 Path("/")；
- 对于路径 "/"，此属性返回 Path("/")；
- 对于路径 "./a/b"，此属性返回 Path("./a")；
- 对于路径 "./"，此属性返回 Path("")；
- 对于路径 ".gitignore"，此属性返回 Path("")；
- 对于路径 "/a/./../b"，此属性返回 Path("/a/./..")。

此外，在 Windows 系统中，path 被分为卷名、目录名和文件名，详情请参见微软官方文档。属性 parent 包含卷名和目录名。

以下示例仅适用于 Windows 系统：

- 对于路径 "C:"，此属性返回 Path("C:")；
- 对于路径 "C:\\a\\b"，此属性返回 Path("C:\\a")；
- 对于路径 "\\\\Server\\Share\\xx\\yy"，此属性返回 Path("\\\\Server\\Share\\xx")；
- 对于路径 "\\\\?\\UNC\\Server\\Share\\xx\\yy"，此属性返回 Path("\\\\?\\UNC\\Server\\Share\\xx")；
- 对于路径 "\\\\?\\c:\\xx\\yy"，此属性返回 Path("\\\\?\\c:\\xx")。

类型：[Path](fs_package_structs.md#struct-path)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当路径为空或包含字符串结束符则抛出异常。

### init(String)

```cangjie
public init(rawPath: String)
```

功能：创建 [Path](fs_package_structs.md#struct-path) 实例时不检查路径字符串是否合法，支持绝对路径和相对路径。

参数：

- rawPath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 路径的字符串。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获得 [Path](fs_package_structs.md#struct-path) 的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - [Path](fs_package_structs.md#struct-path) 的哈希值。

### func isAbsolute()

```cangjie
public func isAbsolute(): Bool
```

功能：判断 [Path](fs_package_structs.md#struct-path) 是否是绝对路径。在 Unix 中，以 `/` 开头的路径为绝对路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，是绝对路径；false，不是绝对路径。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当路径为空或包含字符串结束符则抛出异常。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断当前实例是否为空路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果当前实例为空路径，返回 true，否则返回 false。