## class TimeZone

```cangjie
public class TimeZone <: ToString & Equatable<TimeZone> {
    public static let Local: TimeZone
    public static let UTC: TimeZone
    public init(id: String, offset: Duration)
}
```

功能：TimeZone 表示时区，记录了某一地区在不同时间较零时区的时间偏移，提供了从系统加载时区、自定义时区等功能。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TimeZone](#class-timezone)>

### static let Local

```cangjie
public static let Local: TimeZone
```

功能：获取本地时区。

`Local` 从系统环境变量 TZ 中获取时区 ID，并根据该时区 ID 从系统时区文件中加载时区。其行为与函数 [load](#static-func-loadstring) 相同。

环境变量 TZ 的取值为标准时区 ID 格式（各操作系统遵循相同规范），例如“Asia/Shanghai”。

若环境变量 TZ 未设置或者为空，加载本地时区的规则如下：

- 在 Linux/Unix like 系统上：加载系统路径“/etc/localtime”链接，时区名与“/etc/localtime”指向的相对路径名相同，例如“Asia/Shanghai”。
- 如果上一条执行失败或者在 Windows 系统上，返回 ID 为 “UTC&偏移量” 的时区，例如“Asia/Shanghai”对应的时区为“UTC+08:00”。

类型：[TimeZone](time_package_classes.md#class-timezone)

### static let UTC

```cangjie
public static let UTC: TimeZone
```

功能：获取 UTC 时区。

类型：[TimeZone](time_package_classes.md#class-timezone)

### prop id

```cangjie
public prop id: String
```

功能：获取当前 [TimeZone](time_package_classes.md#class-timezone) 实例所关联的时区 ID。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### init(String, Duration)

```cangjie
public init(id: String, offset: Duration)
```

功能：使用指定的时区 ID 和偏移量构造一个自定义 [TimeZone](time_package_classes.md#class-timezone) 实例。

参数：

- id: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 时区 ID。使用“/”作为分隔符，例如“Asia/Shanghai”，各操作系统使用相同规范。
- offset: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 相对 UTC 时区的偏移量，精度为秒，向东为正、向西为负。取值范围为 (-25 * [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).hour, 26 * [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).hour)。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当输入 `id` 为空字符串，或 `offset` 超出有效区间时，抛出异常。