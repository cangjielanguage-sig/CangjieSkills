## func canonicalize(Path)

```cangjie
public func canonicalize(path: Path): Path
```

功能：将 [Path](fs_package_structs.md#struct-path) 实例规范化，获取绝对路径形式的规范化路径。

所有的中间引用和软链接都会处理（UNC 路径下的软链接无法被规范化），例如，对于路径 "/foo/test/../test/bar.txt"，该函数会返回 "/foo/test/bar.txt"。

参数：

- path: [Path](./fs_package_structs.md#struct-path) - 待规范化的 [Path](fs_package_structs.md#struct-path) 实例。

返回值：

- [Path](fs_package_structs.md#struct-path) - 规范化后的 [Path](fs_package_structs.md#struct-path) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 路径不存在或无法规范化时抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。

## func canonicalize(String)

```cangjie
public func canonicalize(path: String): Path
```

功能：用 path 字符串构造 [Path](fs_package_structs.md#struct-path) 实例，并进行规范化，获取绝对路径形式的规范化路径。

所有的中间引用和软链接都会处理 （UNC 路径下的软链接无法被规范化），例如，对于路径 "/foo/test/../test/bar.txt"，该函数会返回 "/foo/test/bar.txt"。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待规范化的路径字符串。

返回值：

- [Path](fs_package_structs.md#struct-path) - 规范化后的 [Path](fs_package_structs.md#struct-path) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 路径不存在或无法规范化时抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。

## func copy(Path, Path, Bool)

```cangjie
public func copy(sourcePath: Path, to!: Path, overwrite!: Bool = false): Unit
```

功能：实现文件系统的拷贝功能，用于复制文件或目录。

当目标位置存在且 `overwrite` 为 `true` 时，该函数要求 `sourcePath` 的类型与 `to` 的类型一致，比如，`sourcePath` 的类型是 `Directory`，`to` 的类型也应该是 `Directory`，否则函数会抛出异常 FSException。当前支持的文件类型有文件夹（Directory），常规文件（Regular file），符号链接（SymbolicLink）。

参数：

- sourcePath: [Path](./fs_package_structs.md#struct-path) - 待拷贝的文件地址。
- to!: [Path](./fs_package_structs.md#struct-path) - 目标地址。
- overwrite!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否覆盖目标地址，默认值为 `false`。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果源文件类型和目标文件类型不一致会抛出异常或者 `overwrite` 为 `false` 并且目标地址存在时抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。