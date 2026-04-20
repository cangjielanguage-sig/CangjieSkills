### extend Decimal <: JsonDeserializable\<Decimal>

```cangjie
extend Decimal <: JsonDeserializable<Decimal>
```

功能：为 Decimal 类型实现 [JsonDeserializable](./encoding_json_stream_package_interfaces.md#interface-jsondeserializablet) 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Decimal>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Decimal
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Decimal。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Decimal - Decimal 类型的实例。

### extend Float16 <: JsonDeserializable\<Float16>

```cangjie
extend Float16 <: JsonDeserializable<Float16>
```

功能：为 Float16 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Float16>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Float16
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Float16。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Float16 - Float16 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend Float32 <: JsonDeserializable\<Float32>

```cangjie
extend Float32 <: JsonDeserializable<Float32>
```

功能：为 Float32 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Float32>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Float32
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Float32。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Float32 - Float32 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend Float64 <: JsonDeserializable\<Float64>

```cangjie
extend Float64 <: JsonDeserializable<Float64>
```

功能：为 Float64 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Float64>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Float64
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Float64。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Float64 - Float64 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。