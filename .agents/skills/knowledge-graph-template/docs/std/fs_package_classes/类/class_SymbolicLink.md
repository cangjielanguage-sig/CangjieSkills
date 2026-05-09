## class SymbolicLink

```cangjie
public class SymbolicLink {}
```

功能：提供处理文件系统符号链接相关接口。

### static func create(Path, Path)

```cangjie
public static func create(link: Path, to!: Path): Unit
```

功能：创建一个新的符号链接到现有路径。

> **说明：**
>
> 在 Windows 上，创建一个目标不存在的符号链接时，会创建一个文件符号链接，如果目标路径后来被创建为目录，则符号链接将不起作用。

参数：

- link: [Path](fs_package_structs.md#struct-path) - 待创建的符号链接。
- to!: [Path](fs_package_structs.md#struct-path) - 待创建的符号链接的目标的路径。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数中路径为空、或者包含空字符时抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 创建符号链接失败时，抛出异常。

### static func create(String, String)

```cangjie
public static func create(link: String, to!: String): Unit
```

功能：创建一个新的符号链接到现有路径。

> **说明：**
>
> 在 Windows 上，创建一个目标不存在的符号链接时，会创建一个文件符号链接，如果目标路径后来被创建为目录，则符号链接将不起作用。

参数：

- link: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待创建的符号链接。
- to!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待创建的符号链接的目标的路径。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数中路径为空、或者包含空字符时抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 创建符号链接失败时，抛出异常。

### static func readFrom(Path, Bool)

```cangjie
public static func readFrom(path: Path, recursive!: Bool = false): Path
```

功能：获取指定符号链接的目标。当指定 'recursive' 为 'true' 时，表示跟踪指向最终目标的链接，并且返回目标的全路径，当指定 'recursive' 为 'false' 时，读取当前目标链接并且返回。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 符号链接的地址。
- recursive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否递归读取目标地址，默认为 'false'。

返回值：

- [Path](fs_package_structs.md#struct-path) - 符号链接的目标地址。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数中路径为空、或者包含空字符时抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 读取符号链接失败时，抛出异常。

### static func readFrom(String, Bool)

```cangjie
public static func readFrom(path: String, recursive!: Bool = false): Path
```

功能：获取指定符号链接的目标。当指定 'recursive' 为 'true' 时，表示跟踪指向最终目标的链接，并且返回目标的全路径，当指定 'recursive' 为 'false' 时，读取当前目标链接并且返回。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 符号链接的地址。
- recursive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否递归读取目标地址，默认为 'false'。

返回值：

- [Path](fs_package_structs.md#struct-path) - 符号链接的目标地址。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 参数中路径为空、或者包含空字符时抛出异常。
- [FSException](fs_package_exceptions.md#class-fsexception) - 读取符号链接失败时，抛出异常。