### func writeString(String)

```cangjie
public func writeString(v: String): Unit
```

功能：向日志输出目标中写入 String 值。

参数：

- v: String  - 待写入的 String 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。

### func writeValue(LogValue)

```cangjie
public func writeValue(v: LogValue): Unit
```

功能：将实现了 [LogValue](log_package_interfaces.md#interface-logvalue) 接口的类型写入到日志输出目标中。该接口会调用 [LogValue](log_package_interfaces.md#interface-logvalue) 的 [writeTo](log_package_interfaces.md#func-writetologwriter) 方法向日志输出目标中写入数据。

log 包已经为基础类型 Int64、Float64、Bool、String 类型扩展实现了 [LogValue](log_package_interfaces.md#interface-logvalue)，并且为 DateTime、Duration、 Collection 类型 Array、HashMap 和 TreeMap 以及 Option\<T> 扩展实现了 [LogValue](log_package_interfaces.md#interface-logvalue)。

参数：

- v: [LogValue](log_package_interfaces.md#interface-logvalue) - 待写入的 [LogValue](log_package_interfaces.md#interface-logvalue) 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。