## class LogWriter

```cangjie
public abstract class LogWriter {
}
```

功能：[LogWriter](log_package_classes.md#class-logwriter) 提供了将仓颉对象序列化成日志输出目标的能力。

[LogWriter](log_package_classes.md#class-logwriter) 需要和 interface [LogValue](log_package_interfaces.md#interface-logvalue) 搭配使用，[LogWriter](log_package_classes.md#class-logwriter) 可以通过 writeValue 系列方法来将实现了 [LogValue](log_package_interfaces.md#interface-logvalue) 接口的类型写入到日志输出目标中。

### func endArray()

```cangjie
public func endArray(): Unit
```

功能：结束序列化当前的 [LogValue](log_package_interfaces.md#interface-logvalue) 数组。

异常：

- IllegalStateException - 当前 writer 没有匹配的 startArray 时。

### func endObject()

```cangjie
public func endObject(): Unit
```

功能：结束序列化当前的 [LogValue](log_package_interfaces.md#interface-logvalue) object。

异常：

- IllegalStateException - 当前 writer 的状态不应该结束一个 [LogValue](log_package_interfaces.md#interface-logvalue) object 时。

### func startArray()

```cangjie
public func startArray(): Unit
```

功能：开始序列化一个新的 [LogValue](log_package_interfaces.md#interface-logvalue) 数组，每一个 startArray 都必须有一个 endArray 对应。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 [LogValue](log_package_interfaces.md#interface-logvalue) array 时。

### func startObject()

```cangjie
public func startObject(): Unit
```

功能：开始序列化一个新的 [LogValue](log_package_interfaces.md#interface-logvalue) object，每一个 startObject 都必须有一个 endObject 对应。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 [LogValue](log_package_interfaces.md#interface-logvalue) object 时。

### func writeBool(Bool)

```cangjie
public func writeBool(v: Bool): Unit
```

功能：向日志输出目标中写入 Bool 值。

参数：

- v: Bool - 待写入的 Bool 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。

### func writeFloat(Float64)

```cangjie
public func writeFloat(v: Float64): Unit
```

功能：向日志输出目标中写入 Float64 值。

参数：

- v: Float64 - 待写入的 Float64 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。

### func writeDateTime(DateTime)

```cangjie
public func writeDateTime(v: DateTime): Unit
```

功能：向日志输出目标中写入 DateTime 值。

参数：

- v: DateTime - 待写入的 DateTime 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。

### func writeDuration(Duration)

```cangjie
public func writeDuration(v: Duration): Unit
```

功能：向日志输出目标中写入 Duration 值。

参数：

- v: Duration - 待写入的 Duration 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。

### func writeException(Exception)

```cangjie
public func writeException(v: Exception): Unit
```

功能：向日志输出目标中写入 Exception 值。

参数：

- v: Exception - 待写入的 Exception 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时，抛出该异常。

### func writeInt(Int64)

```cangjie
public func writeInt(v: Int64): Unit
```

功能：向日志输出目标中写入 Int64 值。

参数：

- v: Int64 - 待写入的 Int64 值。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。

### func writeKey(String)

```cangjie
public func writeKey(v: String): Unit
```

功能：向日志输出目标中写入 name。

参数：

- v: String - 待写入的 Key 值。

异常：

- IllegalStateException - 当前 writer 的状态不应写入参数 `name` 指定字符串时。

### func writeNone()

```cangjie
public func writeNone(): Unit
```

功能：向日志输出目标中写入 None，具体写成什么格式由 Logger 的提供者自行决定。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。