### static func createTemp(String)

```cangjie
public static func createTemp(directoryPath: String): File
```

功能：在指定目录下创建临时文件。

创建的文件名称是 tmpFileXXXXXX 形式，不使用的临时文件应手动删除。

参数：

- directoryPath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 目录路径字符串。

返回值：

- [File](fs_package_classes.md#class-file) - 临时文件 [File](fs_package_classes.md#class-file) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 创建文件失败或路径不存在则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空字符串或包含空字符，则抛出异常。

### static func readFrom(Path)

```cangjie
public static func readFrom(path: Path): Array<Byte>
```

功能：根据指定路径读取文件全部内容，以字节数组的形式返回其内容。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 文件路径。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 字节数组形式的文件全部内容。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 文件路径为空、文件不可读、文件读取失败，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 文件路径包含空字符则抛出异常。

### static func readFrom(String)

```cangjie
public static func readFrom(path: String): Array<Byte>
```

功能：根据指定路径读取文件全部内容，以字节数组的形式返回其内容。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径字符串。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 字节数组形式的文件全部内容。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 文件读取失败、文件关闭失败、文件路径为空、文件不可读，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 文件路径包含空字符则抛出异常。

### static func writeTo(Path, Array\<Byte>)

```cangjie
public static func writeTo(path: Path, buffer: Array<Byte>): Unit
```

功能：打开指定路径的文件并将 buffer 以覆盖的方式写入，即文件存在时会将该文件截断为零字节大小，文件不存在则将创建文件。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 文件路径。
- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 待写入的 bytes。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 文件打开失败或写入失败，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空或包含空字符，则抛出异常。