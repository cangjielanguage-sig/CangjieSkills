### static func appendTo(Path, Array\<Byte>)

```cangjie
public static func appendTo(path: Path, buffer: Array<Byte>): Unit
```

功能：打开指定路径的文件并将 buffer 以追加的方式写入，文件不存在则将创建文件。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 文件路径。
- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 待写入的 bytes。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 文件打开失败或写入失败，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空或包含空字符，则抛出异常。

### static func appendTo(String, Array\<Byte>)

```cangjie
public static func appendTo(path: String, buffer: Array<Byte>): Unit
```

功能：打开指定路径的文件并将 buffer 以追加的方式写入，文件不存在则将创建文件。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径字符串。
- buffer: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Byte](../../core/core_package_api/core_package_types.md#type-byte)> - 待写入的 bytes。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 文件打开失败或写入失败，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空或包含空字符，则抛出异常。

### static func create(Path)

```cangjie
public static func create(path: Path): File
```

功能：创建指定路径的文件并返回只写模式的 [File](#class-file) 实例。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 文件路径。

返回值：

- [File](fs_package_classes.md#class-file) - [File](fs_package_classes.md#class-file) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果路径指向的文件的上级目录不存在或文件已存在，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空或包含空字符，则抛出异常。

### static func create(String)

```cangjie
public static func create(path: String): File
```

功能：创建指定路径的文件并返回只写模式的 [File](#class-file) 实例。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径字符串。

返回值：

- [File](fs_package_classes.md#class-file) - [File](fs_package_classes.md#class-file) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果路径指向的文件的上级目录不存在或文件已存在，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空字符串或包含空字符，则抛出异常。

### static func createTemp(Path)

```cangjie
public static func createTemp(directoryPath: Path): File
```

功能：在指定目录下创建临时文件。

创建的文件名称是 tmpFileXXXXXX 形式，不使用的临时文件应手动删除。

参数：

- directoryPath: [Path](fs_package_structs.md#struct-path) - 目录路径。

返回值：

- [File](fs_package_classes.md#class-file) - 临时文件 [File](fs_package_classes.md#class-file) 实例。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 创建文件失败或路径不存在则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果文件路径为空或包含空字符，则抛出异常。