### func setWritable(Bool)

```cangjie
public func setWritable(writable: Bool): Bool
```

功能：对当前实例对应的文件设置文件所有者是否可写入的权限，当前用户没有权限修改则抛出异常。

- 对文件而言，设置用户是否有写入文件的权限。
- 对目录而言，设置用户是否有删除、移动、创建目录内文件的权限。
- 在 Windows 环境下，用户对于文件的可写权限正常使用；用户始终拥有对于目录的可写权限，不可更改，该函数不生效，返回 false。
- 在 Linux 和 macOS 环境下，该函数正常使用如果在此函数调用期间，该 [FileInfo](fs_package_structs.md#struct-fileinfo) 对应的文件实体被其他用户或者进程修改，有可能因为竞争条件(Race Condition)导致其他修改不能生效。

参数：

- writable: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否设置可写。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，操作成功；false，操作失败。

### operator func ==(FileInfo)

```cangjie
public operator func ==(that: FileInfo): Bool
```

功能：判断当前 [FileInfo](fs_package_structs.md#struct-fileinfo) 和另一个 [FileInfo](fs_package_structs.md#struct-fileinfo) 是否对应同一文件。

参数：

- that: [FileInfo](fs_package_structs.md#struct-fileinfo) - 另一个 [FileInfo](fs_package_structs.md#struct-fileinfo)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true，是同一文件；false，不是同一文件。