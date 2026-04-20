## struct Path

```cangjie
public struct Path <: Equatable<Path> & Hashable & ToString {
    public static const Separator: String = PATH_SEPARATOR
    public static const ListSeparator: String = PATH_LISTSEPARATOR
    public init(rawPath: String)
}
```

功能：提供路径相关的函数。

Path 用来表示本地路径（Windows 平台已支持 DOS 设备路径和 UNC 路径，长度限制跟随系统）。 路径的字符串最大支持 4096 个字节（包括结束符 `\0`）。

> **说明：**
>
> 非法路径指的是以下情况之一：
>
> - 路径中包含非法字符，例如空格、制表符、换行符等；
> - 路径中包含不合法的字符，例如特殊字符、控制字符等；
> - 路径中包含不存在的目录或文件；
> - 路径中包含无法访问的目录或文件，例如权限不足或被锁定等。

在输入路径时，应该避免使用非法字符，确保路径的合法性，以便正确地访问目标文件或目录。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[Path](#struct-path)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### static const ListSeparator

```cangjie
public static const ListSeparator: String = PATH_LISTSEPARATOR
```

功能：获取路径列表分隔符，用于分隔路径列表中的不同路径。

Windows 系统中路径列表分隔符为 ";"，非 Windows 系统中为 ":"。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Separator

```cangjie
public static const Separator: String = PATH_SEPARATOR
```

功能：获取路径分隔符，用于分隔多级目录。

Windows 系统中分隔符为 "\\"，非 Windows 系统中为 "/"。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop extensionName

```cangjie
public prop extensionName: String
```

功能：获得 [Path](fs_package_structs.md#struct-path) 的文件扩展名部分。

文件名 fileName 根据最后一个 r'.' 被划分为不带扩展名的文件名 fileNameWithoutExtension 和扩展名 extensionName 两部分。无扩展名时返回空字符串。

- 对于路径 "./NewFile.txt"，此属性返回 `"txt"`。
- 对于路径 "./.gitignore"，此属性返回 `"gitignore"`。
- 对于路径 "./noextension"，此属性返回 `""`。
- 对于路径 "./a.b.c"，此属性返回 `"c"`。
- 对于路径 "./NewFile.txt/"，此属性返回 `"txt"`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当路径为空或包含字符串结束符则抛出异常。