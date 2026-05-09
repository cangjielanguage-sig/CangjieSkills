## class NoopLogger

```cangjie
public class NoopLogger <: Logger {
    public init()
}
```

功能：[Logger](#class-logger) 的 NO-OP（无操作）实现，会丢弃所有的日志。

父类型：

- [Logger](#class-logger)

### init()

```cangjie
public init()
```

功能：创建一个 [NoopLogger](log_package_classes.md#class-nooplogger) 实例。

### prop level

```cangjie
public mut prop level: LogLevel
```

功能：永远只能获取到 OFF 日志打印级别，设置日志打印级别不会生效。

类型：[LogLevel](log_package_structs.md#struct-loglevel)

### func close()

```cangjie
public func close(): Unit
```

功能：NOOP 实现。

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：NOOP 实现。

返回值：

- Bool - 是否关闭。

### func log(LogLevel, String, Array\<Attr>)

```cangjie
public func log(level: LogLevel, message: String, attrs: Array<Attr>): Unit
```

功能：NOOP 实现。

参数：

- level: [LogLevel](log_package_structs.md#struct-loglevel) - 日志级别。
- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func log(LogLevel, () -> String, Array\<Attr>)

```cangjie
public func log(level: LogLevel, message: () -> String, attrs: Array<Attr>): Unit
```

功能：NOOP 实现。

参数：

- level: [LogLevel](log_package_structs.md#struct-loglevel) - 日志级别。
- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func log(LogRecord)

```cangjie
public func log(record: LogRecord): Unit
```

功能：NOOP 实现。

参数：

- record: [LogRecord](log_package_classes.md#class-logrecord) - 日志级别。

### func withAttrs(Array\<Attr>)

```cangjie
public func withAttrs(attrs: Array<Attr>): Logger
```

功能：NOOP 实现。

参数：

- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

返回值：

- [Logger](#class-logger) - Logger