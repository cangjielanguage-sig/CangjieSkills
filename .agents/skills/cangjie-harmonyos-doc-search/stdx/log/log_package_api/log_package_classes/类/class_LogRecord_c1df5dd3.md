## class LogRecord

```cangjie
public class LogRecord {
    public init(time: DateTime, level: LogLevel, msg: String, attrs: Array<Attr>)
}
```

功能：日志消息的“负载”。

记录结构作为参数传递给 [Logger](#class-logger) 类的 [log](#func-loglogrecord) 方法。日志提供者处理这些结构以显示日志消息。记录是由日志对象自动创建，因此日志用户看不到。

### init(DateTime, LogLevel, String, Array\<Attr>)

```cangjie
public init(time: DateTime, level: LogLevel, msg: String, attrs: Array<Attr>)
```

功能：创建一个 [LogRecord](log_package_classes.md#class-logrecord) 实例，指定时间戳，日志打印级别，日志消息和日志数据键值对。

参数：

- time: DateTime - 记录日志时的时间戳
- level: [LogLevel](log_package_structs.md#struct-loglevel) - 日志级别。
- msg: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### prop attrs

```cangjie
public mut prop attrs: Array<Attr>
```

功能：获取或设置日志数据键值对。

类型：Array\<[Attr](log_package_types.md#type-attr)>

### prop level

```cangjie
public prop level: LogLevel
```

功能：获取日志打印级别，只有级别小于等于该值的日志会被打印。

类型：[LogLevel](log_package_structs.md#struct-loglevel)

### prop message

```cangjie
public mut prop message: String
```

功能：获取或设置日志消息。

类型：String

### prop time

```cangjie
public prop time: DateTime
```

功能：获取日志打印时的时间戳。

类型：DateTime

### func clone()

```cangjie
public func clone(): LogRecord
```

功能：创建当前对象的副本。

返回值：

- [LogRecord](log_package_classes.md#class-logrecord) - 当前对象的副本。