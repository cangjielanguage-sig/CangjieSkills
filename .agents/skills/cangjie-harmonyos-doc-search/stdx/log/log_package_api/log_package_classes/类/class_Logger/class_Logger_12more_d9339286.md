## class Logger

```cangjie
public abstract class Logger <: Resource {
}
```

功能：此抽象类提供基础的日志打印和管理功能。

父类型：

- Resource

### prop level

```cangjie
public open mut prop level: LogLevel
```

功能：获取和修改日志打印级别。

类型：[LogLevel](log_package_structs.md#struct-loglevel)

### func debug(String, Array\<Attr>)

```cangjie
public func debug(message: String, attrs: Array<Attr>): Unit
```

功能：打印 [DEBUG](log_package_structs.md#static-const-debug) 级别的日志的便捷函数。

参数：

- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func debug(() -> String, Array\<Attr>)

```cangjie
public func debug(message: () -> String, attrs: Array<Attr>): Unit
```

功能：打印 [DEBUG](log_package_structs.md#static-const-debug) 级别的日志的便捷函数。

参数：

- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func enabled(LogLevel)

```cangjie
public func enabled(level: LogLevel): Bool
```

功能：确定是否记录指定日志级别的日志消息。

这个函数允许调用者提前判断日志是否会被丢弃，以避免耗时的日志消息参数计算。

参数：

- level: [LogLevel](log_package_structs.md#struct-loglevel) - 日志级别。

返回值：

- Bool - 如果指定的日志级别处于使能状态，则返回 `true`；否则，返回 `false`。

### func error(String, Array\<Attr>)

```cangjie
public func error(message: String, attrs: Array<Attr>): Unit
```

功能：打印 [ERROR](log_package_structs.md#static-const-error) 级别的日志的便捷函数。

参数：

- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func error(() -> String, Array\<Attr>)

```cangjie
public func error(message: () -> String, attrs: Array<Attr>): Unit
```

功能：打印 [ERROR](log_package_structs.md#static-const-error) 级别的日志的便捷函数。

参数：

- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func fatal(String, Array\<Attr>)

```cangjie
public func fatal(message: String, attrs: Array<Attr>): Unit
```

功能：打印 [FATAL](log_package_structs.md#static-const-fatal) 级别的日志的便捷函数。

参数：

- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func fatal(() -> String, Array\<Attr>)

```cangjie
public func fatal(message: () -> String, attrs: Array<Attr>): Unit
```

功能：打印 [FATAL](log_package_structs.md#static-const-fatal) 级别的日志的便捷函数。

参数：

- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func info(String, Array\<Attr>)

```cangjie
public func info(message: String, attrs: Array<Attr>): Unit
```

功能：打印 [INFO](log_package_structs.md#static-const-info) 级别的日志的便捷函数。

参数：

- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func info(() -> String, Array\<Attr>)

```cangjie
public func info(message: () -> String, attrs: Array<Attr>): Unit
```

功能：打印 [INFO](log_package_structs.md#static-const-info) 级别的日志的便捷函数。

参数：

- message: () -> String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。

### func log(LogLevel, String, Array\<Attr>)

```cangjie
public open func log(level: LogLevel, message: String, attrs: Array<Attr>): Unit
```

功能：打印日志的通用函数，需指定日志级别。

参数：

- level: [LogLevel](log_package_structs.md#struct-loglevel) - 日志级别。
- message: String - 日志消息。
- attrs: Array\<[Attr](log_package_types.md#type-attr)> - 日志数据键值对。