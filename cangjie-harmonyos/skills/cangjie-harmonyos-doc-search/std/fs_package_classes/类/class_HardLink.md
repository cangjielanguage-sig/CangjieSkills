## class HardLink

```cangjie
public class HardLink {}
```

功能：提供处理文件系统硬链接相关接口。

### static func create(Path, Path)

```cangjie
public static func create(link: Path, to!: Path): Unit
```

功能：创建一个新的硬链接到现有路径。如果新的路径存在，则不会覆盖。

参数：

- link: [Path](fs_package_structs.md#struct-path) - 新路径的名称。
- to!: [Path](fs_package_structs.md#struct-path) - 现有路径的名称。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数中路径为空、或者包含空字符时抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 创建硬链接失败时，抛出异常。

### static func create(String, String)

```cangjie
public static func create(link: String, to!: String): Unit
```

功能：创建一个新的硬链接到现有路径。如果新的路径存在，则不会覆盖。

参数：

- link: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 新路径的名称。
- to!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 现有路径的名称。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数中路径为空、或者包含空字符时抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 创建硬链接失败时，抛出异常。