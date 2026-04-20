## func pread(Int32, CPointer\<UInt8>, UIntNative, Int32) <sup>(deprecated)</sup>

```cangjie
public unsafe func pread(fd: Int32, buffer: CPointer<UInt8>, nbyte: UIntNative, offset: Int32): IntNative
```

功能：将 `fd` 指向的文件的 `nbyte` 字节传输到 `buffer` 指向的内存中。如果 `nbyte` 为 `0`，则函数无效果，并返回 `0`。返回值是实际读取的字节数。返回值为 `0` 表示到达文件末尾或无法读取数据。此外，文件的读写位置随着读取字节的变化而变化。

建议 `nbyte` 的大小与 `buffer` 的大小相同，且 `buffer` 的大小小于或等于 `150000` 字节。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 待读取文件的文件描述符。
- buffer: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区容器。
- nbyte: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 读取字节数，建议采用 `buffer.size`。
- offset: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 读取位置的偏移量。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 返回实际读取字节数，读取无效时返回 `-1`。

## func pwrite(Int32, CPointer\<UInt8>, UIntNative, Int32) <sup>(deprecated)</sup>

```cangjie
public unsafe func pwrite(fd: Int32, buffer: CPointer<UInt8>, nbyte: UIntNative, offset: Int32): IntNative
```

功能：将 `buffer` 指向的内存中 `nbyte` 字节从指定偏移位置开始写入到 `fd` 指向的文件。指定文件的读写位置会随之移动。

建议 `nbyte` 的大小与 `buffer` 的大小相同，且 `buffer` 的大小小于或等于 `150000` 字节。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 待读取文件的文件描述符。
- buffer: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区容器。
- nbyte: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 读取字节数，建议采用 `buffer.size`。
- offset: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 读取位置的偏移量。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 返回实际写入数，执行失败时返回 `-1`。

## func read(Int32, CPointer\<UInt8>, UIntNative) <sup>(deprecated)</sup>

```cangjie
public unsafe func read(fd: Int32, buffer: CPointer<UInt8>, nbyte: UIntNative): IntNative
```

功能：将 `fd` 指向的文件的 `nbyte` 字节传输到 `buffer` 指向的内存中。如果 `nbyte` 为 `0`，则函数无效果，并返回 `0`。返回值是实际读取的字节数。返回值为 `0` 表示到达文件末尾或无法读取数据。此外，文件的读写位置随着读取字节的变化而变化。

建议 `nbyte` 的大小与 `buffer` 的大小相同，且 `buffer` 的大小小于或等于 `150000` 字节。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 待读取文件的文件描述符。
- buffer: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 缓冲区容器。
- nbyte: [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) - 读取字节数，建议采用 `buffer.size`。

返回值：

- [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) - 返回实际读取字节数，读取无效时返回 `-1`。