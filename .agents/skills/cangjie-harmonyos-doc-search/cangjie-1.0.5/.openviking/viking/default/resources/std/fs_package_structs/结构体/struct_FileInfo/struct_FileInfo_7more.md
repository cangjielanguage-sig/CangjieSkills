## struct FileInfo

```cangjie
public struct FileInfo <: Equatable<FileInfo> {
    public init(path: Path)
    public init(path: String)
}
```

功能：对应文件系统中的文件元数据。

> **说明：**
>
> 文件元数据是指文件系统中与文件相关的信息，包括文件名、文件大小、创建时间、修改时间、访问时间、文件权限、文件所有者等。
>
> [FileInfo](fs_package_structs.md#struct-fileinfo) 的底层实现是没有直接缓存文件属性的，每次通过 [FileInfo](fs_package_structs.md#struct-fileinfo) 的 API 都是现场获取的最新的文件属性。
>
> 因此这里有需要注意的情况，对于创建的同一 [FileInfo](fs_package_structs.md#struct-fileinfo) 实例，如果在两次获取其文件属性操作期间，对应的文件实体可能会被其他用户或进程做了修改或者替换等不期望的操作，就会导致后一次获取的可能不是期望的文件属性。
> 如果有特殊文件操作需求需要避免上述情况的产生，可以采用设置文件权限或者给关键文件操作加锁的方式来保证。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[FileInfo](#struct-fileinfo)>

### prop creationTime

```cangjie
public prop creationTime: DateTime
```

功能：获取创建时间。

类型：[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime)

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### prop lastAccessTime

```cangjie
public prop lastAccessTime: DateTime
```

功能：获取最后访问时间。

类型：[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime)

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### prop lastModificationTime

```cangjie
public prop lastModificationTime: DateTime
```

功能：获取最后修改时间。

类型：[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime)

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果判断过程中底层接口发生错误，则抛出异常。

### prop name

```cangjie
public prop name: String
```

功能：获取当前实例对应的文件名或目录名。

该属性与 this.path.fileName 等价，路径解析规则详见 [Path](./fs_package_structs.md#struct-path) 结构体的 [fileName](./fs_package_structs.md#prop-filename) 属性。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop parentDirectory

```cangjie
public prop parentDirectory: Option<FileInfo>
```

功能：获得父级目录元数据，以 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[FileInfo](fs_package_structs.md#struct-fileinfo)> 形式返回，有父级返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[FileInfo](fs_package_structs.md#struct-fileinfo)>.Some(v)；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[FileInfo](fs_package_structs.md#struct-fileinfo)>.None。

类型：[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[FileInfo](fs_package_structs.md#struct-fileinfo)>

### prop path

```cangjie
public prop path: Path
```

功能：获得当前文件路径，以 [Path](fs_package_structs.md#struct-path) 形式返回。

类型：[Path](fs_package_structs.md#struct-path)