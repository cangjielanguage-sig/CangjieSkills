### func seek(SeekPosition)

```cangjie
public func seek(sp: SeekPosition): Int64
```

功能：将光标跳转到指定位置。

指定的位置不能位于文件头部之前，指定位置可以超过文件末尾，但指定位置到文件头部的最大偏移量不能超过当前文件系统允许的最大值，这个最大值接近当前文件系统的所允许的最大文件大小，一般为最大文件大小减去 4096 个字节。

参数：

- sp: [SeekPosition](../../io/io_package_api/io_package_enums.md#enum-seekposition) - 指定光标跳转后的位置。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回文件头部到跳转后位置的偏移量（以字节为单位）。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 指定位置不满足以上情况时或文件不能 seek 时均会抛出异常。

### func setLength(Int64)

```cangjie
public func setLength(length: Int64): Unit
```

功能：将当前文件截断为指定长度。当 length 大于当前文件长度时，则将使用 0 填充文件直到目标长度。此方法不会改变文件光标的位置。

参数：

- length: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定截断的长度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 指定的长度为负数时抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 文件截断操作失败时，抛出异常。

### func write(Array\<Byte>)

```cangjie
public func write(buffer: Array<Byte>): Unit
```

功能：将 buffer 中的数据写入到文件中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 待写入数据的缓冲区，若 buffer 为空则直接返回。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果写入失败、只写入了部分数据、文件已关闭或文件不可写则抛出异常。