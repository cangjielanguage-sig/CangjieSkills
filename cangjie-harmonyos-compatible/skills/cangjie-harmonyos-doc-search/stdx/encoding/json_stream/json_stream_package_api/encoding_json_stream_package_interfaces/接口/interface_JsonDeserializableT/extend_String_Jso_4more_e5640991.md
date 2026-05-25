### extend String <: JsonDeserializable\<String>

```cangjie
extend String <: JsonDeserializable<String>
```

功能：为 String 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<String>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): String
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 String。

根据下一个 `JsonToken` 的不同，`String` 的反序列化结果将会不同：

- 当下一个 `JsonToken` 是 `JsonString` 时， 反序列化过程会按照标准[ECMA-404 The JSON Data Interchange Standard](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/)对读到的 `String` 进行转义。
- 当下一个 `JsonToken` 是 `JsonNumber` `JsonBool` `JsonNull` 其中一个时，将会读取下一个 `value` 字段的原始字符串并返回。
- 当下一个 `JsonToken` 是其它类型时，调用此接口会抛异常。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- String - String 类型的实例。

### extend Int16 <: JsonDeserializable\<Int16>

```cangjie
extend Int16 <: JsonDeserializable<Int16>
```

功能：为 Int16 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Int16>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Int16
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Int16。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Int16 - Int16 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend Int32 <: JsonDeserializable\<Int32>

```cangjie
extend Int32 <: JsonDeserializable<Int32>
```

功能：为 Int32 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Int32>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Int32
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Int32。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Int32 - Int32 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend Int64 <: JsonDeserializable\<Int64>

```cangjie
extend Int64 <: JsonDeserializable<Int64>
```

功能：为 Int64 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Int64>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Int64
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Int64。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Int64 - Int64 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。