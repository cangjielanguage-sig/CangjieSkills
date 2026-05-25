### extend\<T> Option\<T> <: JsonSerializable where T <: JsonSerializable

```cangjie
extend<T> Option<T> <: JsonSerializable where T <: JsonSerializable
```

功能：为 Option\<T> 类型提供序列化到 JSON 数据流的接口。

父类型：

- [JsonSerializable](#interface-jsonserializable)

#### func toJson(JsonWriter)

```cangjie
public func toJson(w: JsonWriter): Unit
```

功能：将 Option\<T> 类型写入参数 `w` 指定的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例中。

参数：

- w: [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 写入序列化结果的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例。

### extend\<V> HashMap\<String, V> <: JsonSerializable where V <: JsonSerializable

```cangjie
extend<V> HashMap<String, V> <: JsonSerializable where V <: JsonSerializable
```

功能：为 HashMap\<String, T> 类型提供序列化到 JSON 数据流的接口。

父类型：

- [JsonSerializable](#interface-jsonserializable)

#### func toJson(JsonWriter)

```cangjie
public func toJson(w: JsonWriter): Unit
```

功能：将 HashMap\<String, T> 类型写入参数 `w` 指定的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例中。

参数：

- w: [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 写入序列化结果的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例。