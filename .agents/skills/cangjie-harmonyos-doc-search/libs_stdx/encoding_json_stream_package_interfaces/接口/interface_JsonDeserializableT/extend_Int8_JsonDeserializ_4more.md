### extend Int8 <: JsonDeserializable\<Int8>

```cangjie
extend Int8 <: JsonDeserializable<Int8>
```

功能：为 Int8 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Int8>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Int8
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Int8。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Int8 - Int8 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend IntNative <: JsonDeserializable\<IntNative>

```cangjie
extend IntNative <: JsonDeserializable<IntNative>
```

功能：为 IntNative 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<IntNative>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): IntNative
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 IntNative。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- IntNative - IntNative 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend UInt16 <: JsonDeserializable\<UInt16>

```cangjie
extend UInt16 <: JsonDeserializable<UInt16>
```

功能：为 UInt16 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<UInt16>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): UInt16
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 UInt16。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- UInt16 - UInt16 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend UInt32 <: JsonDeserializable\<UInt32>

```cangjie
extend UInt32 <: JsonDeserializable<UInt32>
```

功能：为 UInt32 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<UInt32>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): UInt32
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 UInt32。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- UInt32 - UInt32 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。