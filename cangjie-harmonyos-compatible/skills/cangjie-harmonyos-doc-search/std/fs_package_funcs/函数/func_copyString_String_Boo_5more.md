## func copy(String, String, Bool)

```cangjie
public func copy(sourcePath: String, to!: String, overwrite!: Bool = false): Unit
```

功能：实现文件系统的拷贝功能，用于复制文件或目录。

当目标位置存在且 `overwrite` 为 `true` 时，该函数要求 `sourcePath` 的类型与 `to` 的类型一致，比如，`sourcePath` 的类型是 `Directory`，`to` 的类型也应该是 `Directory`，否则函数会抛出异常 FSException。当前支持的文件类型有文件夹（Directory），常规文件（Regular file），符号链接（SymbolicLink）。

参数：

- sourcePath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待拷贝的文件地址。
- to!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 目标地址。
- overwrite!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否覆盖目标地址，默认值为 `false`。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果源文件类型和目标文件类型不一致会抛出异常或者 `overwrite` 为 `false` 并且目标地址存在时抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。

## func exists(Path)

```cangjie
public func exists(path: Path): Bool
```

功能：判断目标地址是否存在。

参数：

- path: [Path](./fs_package_structs.md#struct-path) - 待判断的目标地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 目标地址是否存在。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。

## func exists(String)

```cangjie
public func exists(path: String): Bool
```

功能：判断目标地址是否存在。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待判断的目标地址。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 目标地址是否存在。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。

## func remove(Path, Bool)

```cangjie
public func remove(path: Path, recursive!: Bool = false): Unit
```

功能：删除文件或目录。

当目标是文件夹时，可选择是否递归删除文件夹。

参数：

- path: [Path](./fs_package_structs.md#struct-path) - 目标路径。
- recursive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否递归删除文件夹，默认值为 `false`。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果指定目录不存在或删除失败，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。

## func remove(String, Bool)

```cangjie
public func remove(path: String, recursive!: Bool = false): Unit
```

功能：删除文件或目录。

当目标是文件夹时，可选择是否递归删除文件夹。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 目标路径。
- recursive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否递归删除文件夹，默认值为 `false`。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果指定目录不存在或删除失败，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 路径为空或包含字符串结束符时抛出异常。