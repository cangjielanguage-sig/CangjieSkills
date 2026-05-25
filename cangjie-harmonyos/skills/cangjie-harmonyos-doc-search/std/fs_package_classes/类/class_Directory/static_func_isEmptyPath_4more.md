### static func isEmpty(Path)

```cangjie
public static func isEmpty(path: Path): Bool
```

功能：判断指定目录是否为空。

参数：

- path: [Path](./fs_package_structs.md#struct-path) - 待判断是否为空的目录对应的路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 为 true 时目录为空，为 false 时不为空。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果指定路径不存在、指定路径不是目录或判断过程中底层接口发生错误，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当指定路径为空或包含空字符时，抛出异常。

### static func isEmpty(String)

```cangjie
public static func isEmpty(path: String): Bool
```

功能：判断指定目录是否为空。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待判断是否为空的目录对应的路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 为 true 时目录为空，为 false 时不为空。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 如果指定路径不存在、指定路径不是目录或判断过程中底层接口发生错误，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当指定路径为空或包含空字符时，抛出异常。

### static func readFrom(Path)

```cangjie
public static func readFrom(path: Path): Array<FileInfo>
```

功能：获取当前目录的子项目列表。

子项目在数组中的顺序取决于文件在系统中的排序。

参数：

- path: [Path](./fs_package_structs.md#struct-path) - 待读取其子项的目录对应的路径。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[FileInfo](fs_package_structs.md#struct-fileinfo)> - 当前目录的子项目列表。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 当指定路径不存在、指定路径不是目录或获取目录的成员信息失败时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当指定路径为空或包含空字符时，抛出异常。

### static func readFrom(String)

```cangjie
public static func readFrom(path: String): Array<FileInfo>
```

功能：获取当前目录的子项目列表。

子项目在数组中的顺序取决于文件在系统中的排序。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待读取其子项目的目录对应的路径。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[FileInfo](./fs_package_structs.md#struct-fileinfo)> - 当前目录的子项目列表。

异常：

- [FSException](./fs_package_exceptions.md#class-fsexception) - 当指定路径不存在、指定路径不是目录或获取目录的成员信息失败时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当指定路径为空或包含空字符时，抛出异常。