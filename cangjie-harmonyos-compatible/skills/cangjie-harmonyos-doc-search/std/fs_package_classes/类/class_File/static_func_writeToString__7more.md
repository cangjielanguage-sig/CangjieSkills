### static func writeTo(String, Array\<Byte>)

```cangjie
public static func writeTo(path: String, buffer: Array<Byte>): Unit
```

功能：打开指定路径的文件并将 buffer 以覆盖的方式写入，即文件存在时会将该文件截断为零字节大小，文件不存在则将创建文件。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径字符串。
- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 待写入的 bytes。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 文件打开失败或写入失败，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空字符串或包含空字符，则抛出异常。

### func canRead()

```cangjie
public func canRead(): Bool
```

功能：判断当前 [File](fs_package_classes.md#class-file) 对象是否可读。

该函数返回值由创建文件对象的 openMode 所决定，文件对象关闭后返回 false。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示可读，返回 false 表示不可读或文件对象已关闭。

### func canWrite()

```cangjie
public func canWrite(): Bool
```

功能：判断当前 [File](fs_package_classes.md#class-file) 对象是否可写。

该函数返回值由创建文件对象的 openMode 所决定，文件对象关闭后返回 false。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回 true 表示可写，false 表示不可写或文件对象已关闭。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭当前 [File](fs_package_classes.md#class-file) 对象。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果关闭失败，则抛出异常。

### func flush()

```cangjie
public func flush(): Unit
```

功能：将缓冲区数据写入流。由于 [File](fs_package_classes.md#class-file) 不存在缓冲区，所以该函数没有具体作用。

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：判断当前 [File](fs_package_classes.md#class-file) 对象是否已关闭。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - true 表示已关闭，false 表示未关闭。

### func read(Array\<Byte>)

```cangjie
public func read(buffer: Array<Byte>): Int64
```

功能：从文件中读出数据到 buffer 中。

参数：

- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 读取数据存放的缓冲区。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 读取成功，返回读取字节数，如果文件被读完，返回 0。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 buffer 为空，则抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 读取失败、文件已关闭或文件不可读，则抛出异常。