### func writeName(String)

```cangjie
public func writeName(name: String): JsonWriter
```

功能：在 object 结构中写入 name。

返回值：

- [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 当前 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 引用。

异常：

- IllegalStateException - 当前 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 的状态不应写入参数 `name` 指定字符串时。

### func writeNullValue()

```cangjie
public func writeNullValue(): JsonWriter
```

功能：向流中写入 JSON value null。

返回值：

- [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 为方便链式调用，返回值为当前 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 的引用。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时

### func writeValue\<T>(T) where T <: JsonSerializable

```cangjie
public func writeValue<T>(v: T): JsonWriter where T <: JsonSerializable
```

功能：将实现了 [JsonSerializable](encoding_json_stream_package_interfaces.md#interface-jsonserializable) 接口的类型写入到 Stream 中。该接口会调用泛型 T 的 toJson 方法向输出流中写入数据。

json.stream 包已经为基础类型 Int64、UInt64、Float64、Bool、String 类型扩展实现了 [JsonSerializable](encoding_json_stream_package_interfaces.md#interface-jsonserializable)， 并且为 Collection 类型 Array、ArrayList 和 HashMap 扩展实现了 [JsonSerializable](encoding_json_stream_package_interfaces.md#interface-jsonserializable)。

返回值：

- [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 返回当前 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 的引用。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。