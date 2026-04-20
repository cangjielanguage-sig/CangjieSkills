### func isDirectory()

```cangjie
public func isDirectory(): Bool
```

功能：判断当前文件是否是目录。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示是目录；false 表示不是目录。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### func isHidden()

```cangjie
public func isHidden(): Bool
```

功能：判断当前文件是否隐藏。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示隐藏；false 表示未隐藏。

### func isReadOnly()

```cangjie
public func isReadOnly(): Bool
```

功能：判断当前文件是否只读。

- 在 Windows 环境下，用户对于文件的只读权限正常使用；用户始终拥有对于目录的删除修改权限，该函数不生效，返回 false。
- 在 Linux 和 macOS 环境下，该函数正常使用。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示是只读；false 表示不是只读。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### func isRegular()

```cangjie
public func isRegular(): Bool
```

功能：判断当前文件是否是普通文件。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示是文件；false 表示不是文件。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### func isSymbolicLink()

```cangjie
public func isSymbolicLink(): Bool
```

功能：判断当前文件是否是软链接。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示是软链接；false 表示不是软链接。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### func setExecutable(Bool)

```cangjie
public func setExecutable(executable: Bool): Bool
```

功能：对当前实例对应的文件设置文件所有者是否可执行的权限，当前用户没有权限修改则抛出异常。

- 对文件而言，设置用户是否有执行文件的权限，对目录而言，设置用户是否有进入目录的权限。
- 在 Windows 环境下，用户对于文件的执行权限由文件扩展名决定，用户始终拥有对于目录的执行权限该函数不生效，返回 false。
- 在 Linux 和 macOS 环境下，该函数正常使用如果在此函数调用期间，该 [FileInfo](fs_package_structs.md#struct-fileinfo) 对应的文件实体被其他用户或者进程修改，有可能因为竞争条件(Race Condition)导致其他修改不能生效。

参数：

- executable: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否设置可执行。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，操作成功；false，操作失败。

### func setReadable(Bool)

```cangjie
public func setReadable(readable: Bool): Bool
```

功能：对当前实例对应的文件设置文件所有者是否可读取的权限，当前用户没有权限修改则抛出异常。

- 对文件而言，设置用户是否有读取文件的权限。
- 对目录而言，设置用户是否有浏览目录的权限。
- 在 Windows 环境下，用户始终拥有对于文件以及目录的可读权限，不可更改，该函数不生效当 readable 为 true 时，函数返回 true，当 readable 为 false 时，函数返回 false。
- 在 Linux 和 macOS 环境下，该函数正常使用如果在此函数调用期间，该 [FileInfo](fs_package_structs.md#struct-fileinfo) 对应的文件实体被其他用户或者进程修改，有可能因为竞争条件(Race Condition)导致其他修改不能生效。

参数：

- readable: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否设置可读。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，操作成功；false，操作失败。