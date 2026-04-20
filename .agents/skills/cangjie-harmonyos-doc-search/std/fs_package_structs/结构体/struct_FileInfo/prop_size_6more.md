### prop size

```cangjie
public prop size: Int64
```

功能：返回当前文件大小。

- 当前是文件时，表示单个文件占用磁盘空间的大小。
- 当前是目录时，表示当前目录的所有文件占用磁盘空间的大小。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### init(Path)

```cangjie
public init(path: Path)
```

功能：创建 [FileInfo](fs_package_structs.md#struct-fileinfo) 实例。

参数：

- path: [Path](fs_package_structs.md#struct-path) - [Path](fs_package_structs.md#struct-path) 形式的目录路径。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 当路径非法时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当路径为空，或包含字符串结束符则抛出异常。

### init(String)

```cangjie
public init(path: String)
```

功能：创建 [FileInfo](fs_package_structs.md#struct-fileinfo) 实例。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - [String](../../core/core_package_api/core_package_structs.md#struct-string) 形式的目录路径。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 当路径非法时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当路径为空，或包含字符串结束符则抛出异常。

### func canExecute()

```cangjie
public func canExecute(): Bool
```

功能：判断当前用户是否有权限执行该实例对应的文件。

- 对文件而言，判断用户是否有执行文件的权限。
- 对目录而言，判断用户是否有进入目录的权限。
- 在 Windows 环境下，用户对于文件的执行权限由文件扩展名决定；用户始终拥有对于目录的执行权限，该函数不生效，返回 true。
- 在 Linux 和 macOS 环境下，该函数正常使用。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示有权限；false 表示无权限。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### func canRead()

```cangjie
public func canRead(): Bool
```

功能：判断当前用户是否有权限读取该实例对应的文件。

- 对文件而言，判断用户是否有读取文件的权限。
- 对目录而言，判断用户是否有浏览目录的权限。
- 在 Windows 环境下，用户始终拥有对于文件和目录的可读权限，该函数不生效，返回 true。
- 在 Linux 和 macOS 环境下，该函数正常使用。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示有权限；false 表示无权限。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### func canWrite()

```cangjie
public func canWrite(): Bool
```

功能：判断当前用户是否有权限写入该实例对应的文件。

- 对文件而言，判断用户是否有写入文件的权限。
- 对目录而言，判断用户是否有删除、移动、创建目录内文件的权限。
- 在 Windows 环境下，用户对于文件的可写权限正常使用，用户始终拥有对于目录的可写权限，该函数不生效，返回 true。
- 在 Linux 和 macOS 环境下，该函数正常使用。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示有权限；false 表示无权限。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。