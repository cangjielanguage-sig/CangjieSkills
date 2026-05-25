## class DateTimeFormat

```cangjie
public class DateTimeFormat {
    public static const RFC1123: String = "www, dd MMM yyyy HH:mm:ss z"
    public static const RFC3339: String = "yyyy-MM-ddTHH:mm:ssOOOO"
    public static const RFC822: String = "ww dd MMM yy HH:mm:ss z"
    public static const RFC850: String = "wwww, dd-MMM-yy HH:mm:ss z"
}
```

功能：提供时间格式的功能，用于解析和生成 [DateTime](../time_package_api/time_package_structs.md#struct-datetime) 。

### static const RFC1123

```cangjie
public static const RFC1123: String = "www, dd MMM yyyy HH:mm:ss z"
```

功能：提供 RFC1123 时间格式，时间字符串格式为 `www, dd MMM yyyy HH:mm:ss z`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const RFC3339

```cangjie
public static const RFC3339: String = "yyyy-MM-ddTHH:mm:ssOOOO"
```

功能：提供 RFC3339 时间格式，时间字符串格式为 `yyyy-MM-ddTHH:mm:ssOOOO`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const RFC822

```cangjie
public static const RFC822: String = "ww dd MMM yy HH:mm:ss z"
```

功能：提供 RFC822 时间格式，时间字符串格式为 `ww dd MMM yy HH:mm:ss z`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const RFC850

```cangjie
public static const RFC850: String = "wwww, dd-MMM-yy HH:mm:ss z"
```

功能：提供 RFC850 时间格式，时间字符串格式为 `wwww, ww-MMM-yy HH:mm:ss z`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### prop format: String <sup>(deprecated)</sup>

```cangjie
public prop format: String
```

功能：DateTimeFormat 实例的字符串格式。

> **注意：**
>
> 未来版本即将废弃不再使用。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static func of(String) <sup>(deprecated)</sup>

```cangjie
public static func of(format: String): DateTimeFormat
```

功能：根据字符串创建具体的 DateTimeFormat 类型实例。

字符串的具体格式见[时间字符串格式](../time_package_overview.md#时间字符串格式)。

> **注意：**
>
> 未来版本即将废弃不再使用。

参数：

- format: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串格式。

返回值：

- [DateTimeFormat](#class-datetimeformat) - 时间格式。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当入参格式不符合[时间字符串格式](../time_package_overview.md#时间字符串格式)中字母数量的规定时，抛出异常。