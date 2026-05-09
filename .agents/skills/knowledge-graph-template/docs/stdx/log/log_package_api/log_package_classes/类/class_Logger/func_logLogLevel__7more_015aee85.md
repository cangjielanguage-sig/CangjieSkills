### func log(LogLevel, () -> String, Array\<Attr>)

```cangjie
public open func log(level: LogLevel, message: () -> String, attrs: Array<Attr>): Unit
```

功能：打印日志的通用函数，需指定日志级别。

参数：

- level: [LogLevel](log_package_structs.md#struct-loglevel) - 日志级别。
- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func log(LogRecord)

```cangjie
public open func log(record: LogRecord): Unit
```

功能：打印日志的通用函数。

参数：

- record: [LogRecord](log_package_classes.md#class-logrecord) - 日志级别。

### func trace(String, Array\<Attr>)

```cangjie
public func trace(message: String, attrs: Array<Attr>): Unit
```

功能：打印 [TRACE](log_package_structs.md#static-const-trace) 级别的日志的便捷函数。

参数：

- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func trace(() -> String, Array\<Attr>)

```cangjie
public func trace(message: () -> String, attrs: Array<Attr>): Unit
```

功能：打印 [TRACE](log_package_structs.md#static-const-trace) 级别的日志的便捷函数。

参数：

- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func warn(String, Array\<Attr>)

```cangjie
public func warn(message: String, attrs: Array<Attr>): Unit
```

功能：打印 [WARN](log_package_structs.md#static-const-warn) 级别的日志的便捷函数。

参数：

- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func warn(() -> String, Array\<Attr>)

```cangjie
public func warn(message: () -> String, attrs: Array<Attr>): Unit
```

功能：打印 [WARN](log_package_structs.md#static-const-warn) 级别的日志的便捷函数。

参数：

- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func withAttrs(Array\<Attr>)

```cangjie
public open func withAttrs(attrs: Array<Attr>): Logger
```

功能：创建当前对象的副本，新的副本会包含指定的属性。

参数：

- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对属性。

返回值：

- [Logger](#class-logger) - [Logger](#class-logger) 类的对象实例。