### extend Duration <: LogValue

```cangjie
extend Duration <: LogValue
```

功能：为 Duration 类型实现 LogValue 接口。

父类型：

- [LogValue](#interface-logvalue)

#### func writeTo(LogWriter)

```cangjie
public func writeTo(w: LogWriter): Unit
```

功能：提供 Duration 类型序列化到流的功能。

参数：

- w:  [LogWriter](log_package_classes.md#class-logwriter) - 写入序列化结果的 [LogWriter](log_package_classes.md#class-logwriter) 实例。

### extend\<T> Array\<T> <: LogValue where T <: LogValue

```cangjie
extend<T> Array<T> <: LogValue where T <: LogValue
```

功能：为 Array\<T> 类型实现 LogValue 接口。

父类型：

- [LogValue](#interface-logvalue)

#### func writeTo(LogWriter)

```cangjie
public func writeTo(w: LogWriter): Unit
```

功能：提供 Array\<T> 类型序列化到流的功能。

参数：

- w:  [LogWriter](log_package_classes.md#class-logwriter) - 写入序列化结果的 [LogWriter](log_package_classes.md#class-logwriter) 实例。

### extend\<V> HashMap\<String, V> <: LogValue where V <: LogValue

```cangjie
extend<V> HashMap<String, V> <: LogValue where V <: LogValue
```

功能：为 HashMap\<K, V> 类型实现 LogValue 接口。

父类型：

- [LogValue](#interface-logvalue)

#### func writeTo(LogWriter)

```cangjie
public func writeTo(w: LogWriter): Unit
```

功能：提供 HashMap\<K, V> 类型序列化到流的功能。

参数：

- w:  [LogWriter](log_package_classes.md#class-logwriter) - 写入序列化结果的 [LogWriter](log_package_classes.md#class-logwriter) 实例。

### extend\<V> TreeMap\<String, V> <: LogValue where V <: LogValue

```cangjie
extend<V> TreeMap<String, V> <: LogValue where V <: LogValue
```

功能：为 TreeMap\<K, V> 类型实现 LogValue 接口。

父类型：

- [LogValue](#interface-logvalue)

#### func writeTo(LogWriter)

```cangjie
public func writeTo(w: LogWriter): Unit
```

功能：提供 TreeMap\<K, V> 类型序列化到流的功能。

参数：

- w:  [LogWriter](log_package_classes.md#class-logwriter) - 写入序列化结果的 [LogWriter](log_package_classes.md#class-logwriter) 实例。

### extend\<T> Option\<T> <: LogValue where T <: LogValue

```cangjie
extend<T> Option<T> <: LogValue where T <: LogValue
```

功能：为 Option\<T> 类型实现 LogValue 接口。

父类型：

- [LogValue](#interface-logvalue)

#### func writeTo(LogWriter)

```cangjie
public func writeTo(w: LogWriter): Unit
```

功能：提供 Option\<T> 类型序列化到流的功能。

参数：

- w:  [LogWriter](log_package_classes.md#class-logwriter) - 写入序列化结果的 [LogWriter](log_package_classes.md#class-logwriter) 实例。