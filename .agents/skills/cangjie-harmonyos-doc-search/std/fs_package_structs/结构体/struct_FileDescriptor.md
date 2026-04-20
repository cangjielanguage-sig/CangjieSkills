## struct FileDescriptor

```cangjie
public struct FileDescriptor {}
```

功能：用于获取文件句柄信息。

> **说明：**
>
> 文件句柄（File Handle）是操作系统为了跟踪文件而分配的一种数据结构，用于标识一个打开文件的实例。文件句柄包含了文件的元数据信息（如文件名、路径、大小、修改时间等）以及文件数据在磁盘上的物理位置等信息。
> 在不同的操作系统中，文件句柄的形式可能会有所不同。在 Unix 和 Linux 系统中，文件句柄通常是一个非负整数，由操作系统内核分配，并在打开文件时返回给应用程序。在 Windows 系统中，文件句柄通常是一个指向文件对象的指针，由操作系统内核分配，并在打开文件时返回给应用程序。无论文件句柄的形式是什么，应用程序都可以使用它来执行文件的读取、写入、修改等操作。

### prop fileHandle

```cangjie
public prop fileHandle: IntNative
```

功能：获取文件句柄信息。

类型：[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)