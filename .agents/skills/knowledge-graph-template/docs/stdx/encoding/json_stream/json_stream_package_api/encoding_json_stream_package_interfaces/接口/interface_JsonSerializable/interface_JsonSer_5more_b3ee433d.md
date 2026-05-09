## interface JsonSerializable

```cangjie
public interface JsonSerializable {
    func toJson(w: JsonWriter): Unit
}
```

功能：为类型提供序列化到 JSON 数据流的接口。

与 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 搭配使用，[JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 可以将实现了 [JsonSerializable](encoding_json_stream_package_interfaces.md#interface-jsonserializable) 接口的类型写入到 Stream 中。

### func toJson(JsonWriter)

```cangjie
func toJson(w: JsonWriter): Unit
```

功能：将实现了 [JsonSerializable](encoding_json_stream_package_interfaces.md#interface-jsonserializable) 接口的类型写入参数 `w` 指定的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例中。

参数：

- w: [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 写入序列化结果的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例。

### extend BigInt <: JsonSerializable

```cangjie
extend BigInt <: JsonSerializable
```

功能：为 BigInt 类型提供序列化到 JSON 数据流的接口。

父类型：

- [JsonSerializable](#interface-jsonserializable)

#### func toJson(JsonWriter)

```cangjie
public func toJson(w: JsonWriter): Unit
```

功能：将 BigInt 类型写入参数 `w` 指定的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例中。

参数：

- w: [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 写入序列化结果的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例。

### extend Bool <: JsonSerializable

```cangjie
extend Bool <: JsonSerializable
```

功能：为 Bool 类型提供序列化到 JSON 数据流的接口。

父类型：

- [JsonSerializable](#interface-jsonserializable)

#### func toJson(JsonWriter)

```cangjie
public func toJson(w: JsonWriter): Unit
```

功能：将 Bool 类型写入参数 `w` 指定的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例中。

参数：

- w: [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 写入序列化结果的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例。

### extend DateTime <: JsonSerializable

```cangjie
extend DateTime <: JsonSerializable
```

功能：为 DateTime 类型实现 JsonSerializable 接口。

父类型：

- [JsonSerializable](#interface-jsonserializable)

#### func toJson(JsonWriter)

```cangjie
public func toJson(w: JsonWriter): Unit
```

功能：提供 DateTime 类型序列化到流的功能。

该接口的功能与 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 的 [writeConfig](./encoding_json_stream_package_classes.md#var-writeconfig)中的属性 [dateTimeFormat](./encoding_json_stream_package_structs.md#prop-datetimeformat)有关联，将会把 DateTime 按照[dateTimeFormat](./encoding_json_stream_package_structs.md#prop-datetimeformat)中的格式输出到目标流中，可以通过修改[dateTimeFormat](./encoding_json_stream_package_structs.md#prop-datetimeformat)实现不同的格式控制。

参数：

- w: [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 写入序列化结果的 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 实例。