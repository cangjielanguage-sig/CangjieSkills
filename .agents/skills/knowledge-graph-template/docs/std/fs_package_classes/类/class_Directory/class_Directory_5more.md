## class Directory

```cangjie
public class Directory {}
```

功能：对应文件系统中的目录，它提供创建、移动、复制、删除、查询属性以及遍历目录等能力。

> **说明：**
>
> 非法路径指的是以下情况之一：
>
> - 路径中包含非法字符，例如空格、制表符、换行符等；
> - 路径中包含不合法的字符，例如特殊字符、控制字符等；
> - 路径中包含不存在的目录或文件；
> - 路径中包含无法访问的目录或文件，例如权限不足或被锁定等。

在输入路径时，应该避免使用非法字符，确保路径的合法性，以便正确地访问目标文件或目录。

### static func create(Path, Bool)

```cangjie
public static func create(path: Path, recursive!: Bool = false): Unit
```

功能：创建目录。

可指定是否递归创建，如果需要递归创建，将逐级创建路径中不存在的目录。

参数：

- path: [Path](fs_package_structs.md#struct-path) - 待创建的目录路径。
- recursive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否递归创建目录，true 代表递归创建，false 代表不递归创建，默认 false。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 目录已存在、非递归创建时中间有不存在的目录、权限不足或其他原因导致无法创建目录时，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 目录为空、目录为当前目录、目录为根目录或目录中存在空字符时抛出异常。

### static func create(String, Bool)

```cangjie
public static func create(path: String, recursive!: Bool = false): Unit
```

功能：创建目录。

可指定是否递归创建，如果需要递归创建，将逐级创建路径中不存在的目录。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待创建的目录路径。
- recursive!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否递归创建目录，true 代表递归创建，false 代表不递归创建，默认 false。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 目录已存在、非递归创建时中间有不存在的目录、权限不足或其他原因导致无法创建目录时，则抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 目录为空、目录为当前目录、目录为根目录或目录中存在空字符时抛出异常。

### static func createTemp(Path)

```cangjie
public static func createTemp(directoryPath: Path): Path
```

功能：在指定目录下创建临时目录。

参数：

- directoryPath: [Path](fs_package_structs.md#struct-path) - [Path](fs_package_structs.md#struct-path) 形式的目录路径。

返回值：

- [Path](./fs_package_structs.md#struct-path) - 临时目录对应的路径。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 目录不存在或其他原因导致创建失败时抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 目录为空或包含空字符时抛出异常。

### static func createTemp(String)

```cangjie
public static func createTemp(directoryPath: String): Path
```

功能：在指定目录下创建临时目录。

参数：

- directoryPath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串形式的目录路径。

返回值：

- [Path](./fs_package_structs.md#struct-path) - 临时目录对应的路径。

异常：

- [FSException](fs_package_exceptions.md#class-fsexception) - 目录不存在或其他原因导致创建失败时抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 目录为空或包含空字符时抛出异常。