### static func load(String)

```cangjie
public static func load(id: String): TimeZone
```

功能：从系统中加载参数 `id` 指定的时区。

> **说明：**
>
> - 在 Linux 、 macOS 系统中，若存在环境变量 CJ_TZPATH，则使用环境变量指定的路径加载时区文件（若存在多个通过分隔符 “:” 分开的环境变量值，则按照分隔路径的先后顺序依次查找时区文件，并加载第一个找到的时区文件），否则从系统时区文件目录（Linux 和 macOS 为 "/usr/share/zoneinfo"）加载时区。
> - 在 Windows 系统中，用户需下载[时区文件](https://www.iana.org/time-zones)并编译，设置环境变量 CJ_TZPATH 指向 zoneinfo 目录（若存在多个通过分隔符 “;” 分开的环境变量值，则按照分隔路径的先后顺序依次查找时区文件，并加载第一个找到的时区文件），否则会导致异常。

参数：

- id: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时区 ID。

返回值：

- [TimeZone](time_package_classes.md#class-timezone) - 时区。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数 `id` 为空，或长度超过 4096 字节，或不符合标准时区 ID 格式时，抛出异常。
- [InvalidDataException](time_package_exceptions.md#class-invaliddataexception) - 当时区文件加载失败（找不到文件，文件解析失败等）时，抛出异常。

### static func loadFromPaths(String, Array\<String>)

```cangjie
public static func loadFromPaths(id: String, tzpaths: Array<String>): TimeZone
```

功能：根据参数 `tzpaths` 指定的时区文件目录，加载参数 `id` 指定的时区。

加载时区时，将从第一个被读取成功的时区文件路径中加载时区。时区文件格式需要满足[时区信息格式](https://datatracker.ietf.org/doc/html/rfc8536)。

参数：

- id: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时区 ID。
- tzpaths: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 时区文件路径数组。

返回值：

- [TimeZone](time_package_classes.md#class-timezone) - 加载的时区。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `id` 为空，或长度超过 4096 字节，或不符合标准时区 ID 格式时，抛出异常。
- [InvalidDataException](time_package_exceptions.md#class-invaliddataexception) - 当时区文件加载失败（找不到文件，文件解析失败等）时，抛出异常。

### static func loadFromTZData(String, Array\<UInt8>)

```cangjie
public static func loadFromTZData(id: String, data: Array<UInt8>): TimeZone
```

功能：使用指定的时区 ID 和时区数据构造一个自定义 [TimeZone](time_package_classes.md#class-timezone) 实例。`id` 可以是任何合法字符串，`data` 需要满足 IANA 时区文件格式，加载成功时获得 [TimeZone](time_package_classes.md#class-timezone) 实例，否则抛出异常。

参数：

- id: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时区 ID。
- data: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 满足[时区信息格式](https://datatracker.ietf.org/doc/html/rfc8536)的数据。

返回值：

- [TimeZone](time_package_classes.md#class-timezone) - 加载的时区。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `id` 为空时，抛出异常。
- [InvalidDataException](time_package_exceptions.md#class-invaliddataexception) - 如果 `data` 解析失败，则抛出异常。