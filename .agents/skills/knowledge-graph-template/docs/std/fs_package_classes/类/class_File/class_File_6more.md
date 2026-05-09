## class File

```cangjie
public class File <: Resource & IOStream & Seekable {
    public init(path: String, mode: OpenMode)
    public init(path: Path, mode: OpenMode)
}
```

功能：提供一些对文件进行操作的函数，包括文件的打开、创建、关闭、移动、复制、删除，文件的流式读写操作，查询属性以及一些其他函数。

> **说明：**
>
> 非法路径指的是以下情况之一：
>
> - 路径中包含非法字符，例如空格、制表符、换行符等；
> - 路径中包含不合法的字符，例如特殊字符、控制字符等；
> - 路径中包含不存在的目录或文件；
> - 路径中包含无法访问的目录或文件，例如权限不足或被锁定等。

在输入路径时，应该避免使用非法字符，确保路径的合法性，以便正确地访问目标文件或目录。

> **注意：**
>
> 创建的 [File](fs_package_classes.md#class-file) 对象会默认打开对应的文件，当使用结束后需要及时调用 [close](fs_package_classes.md#func-close) 函数关闭文件，否则会造成资源泄露。

父类型：

- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)
- [IOStream](../../io/io_package_api/io_package_interfaces.md#interface-iostream)
- [Seekable](../../io/io_package_api/io_package_interfaces.md#interface-seekable)

### prop fileDescriptor

```cangjie
public prop fileDescriptor: FileDescriptor
```

功能：获取文件描述符信息。

类型：[FileDescriptor](fs_package_structs.md#struct-filedescriptor)

### prop info

```cangjie
public prop info: FileInfo
```

功能：获取文件元数据信息。

类型：[FileInfo](fs_package_structs.md#struct-fileinfo)

### prop length

```cangjie
public prop length: Int64
```

功能：获取文件头至文件尾的数据字节数。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Path, OpenMode)

```cangjie
public init(path: Path, mode: OpenMode)
```

功能：创建一个 [File](fs_package_classes.md#class-file) 对象。

需指定文件路径和文件打开方式（读写权限），路径支持相对路径和绝对路径。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 文件路径。
- mode: [OpenMode](fs_package_enums.md#enum-openmode) - 文件打开模式。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果以只读方式打开文件但文件不存在、文件的父目录不存在或其他原因导致无法打开文件，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 path 为空路径或者 path 路径中包含空字符，则抛出异常。

### init(String, OpenMode)

```cangjie
public init(path: String, mode: OpenMode)
```

功能：创建 [File](fs_package_classes.md#class-file) 对象。

需指定文件路径和文件打开方式（读写权限），路径支持相对路径和绝对路径。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径字符串。
- mode: [OpenMode](fs_package_enums.md#enum-openmode) - 文件打开模式。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果以只读方式打开文件但文件不存在、文件的父目录不存在或其他原因导致无法打开文件，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 path 是空字符串或者 path 包含空字符，则抛出异常。