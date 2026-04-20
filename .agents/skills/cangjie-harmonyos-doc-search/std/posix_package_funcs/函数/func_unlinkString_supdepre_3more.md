## func unlink(String) <sup>(deprecated)</sup>

```cangjie
public func unlink(path: String): Int32
```

功能：从文件系统中删除文件。

- 如果 `path` 是指向文件的最后一个链接，并且没有进程打开该文件，则该文件将被删除，它使用的空间可供重复使用。
- 如果 `path` 是指向文件的最后一个链接，但仍然有进程打开该文件，该文件将一直存在，直到引用它的最后一个文件描述符关闭。
- 如果 `path` 引用了符号链接，则该链接将被删除。
- 如果 `path` 引用了套接字、FIFO 或设备，则该文件将被删除，但打开对象的进程可能会继续使用它。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func unlinkat(Int32, String, Int32) <sup>(deprecated)</sup>

```cangjie
public func unlinkat(fd: Int32, path: String, ulflag: Int32): Int32
```

功能：从文件系统中删除文件。

该函数系统调用的操作方式与 [unlink](posix_package_funcs.md#func-unlinkstring-deprecated) 函数完全相同，但此处描述的差异除外：

- `path` 为相对路径且 `fd` 为特殊值 `AT_FDCWD` 时，则路径将相对于调用进程的当前工作目录。
- `path` 为相对路径且 `fd` 非 `AT_FDCWD` 时，则路径将相对于 `fd` 引用的文件所属目录。
- `path` 为绝对路径时 `fd` 参数将被忽略。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- ulflag: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 可以指定为 `0`，或者可以设置为控制 [unlinkat](posix_package_funcs.md#func-unlinkatint32-string-int32-deprecated)() 操作的标志值按位或运算。标志值当前取值仅支持 [AT_REMOVEDIR](posix_package_constants_vars.md#const-at_removedir-deprecated)。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func write(Int32, CPointer\<UInt8>, UIntNative) <sup>(deprecated)</sup>

```cangjie
public unsafe func write(fd: Int32, buffer: CPointer<UInt8>, nbyte: UIntNative): IntNative
```

功能：将 `buffer` 指向的内存中 `nbyte` 字节写入到 `fd` 指向的文件。指定文件的读写位置会随之移动。

建议 `nbyte` 的大小与 `buffer` 的大小相同，且 `buffer` 的大小小于或等于 `150000` 字节。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 待写入文件的文件描述符。
- buffer: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区容器。
- nbyte: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 读取字节数，建议采用 `buffer.size`。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 返回实际读取字节数，读取无效时返回 `-1`。