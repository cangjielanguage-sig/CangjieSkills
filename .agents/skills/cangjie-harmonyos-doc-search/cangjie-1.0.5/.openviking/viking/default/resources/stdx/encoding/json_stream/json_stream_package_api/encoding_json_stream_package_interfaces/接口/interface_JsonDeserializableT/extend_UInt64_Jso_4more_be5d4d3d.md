### extend UInt64 <: JsonDeserializable\<UInt64 >

```cangjie
extend UInt64 <: JsonDeserializable<UInt64>
```

功能：为 UInt64 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<UInt64>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): UInt64
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 UInt64。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- UInt64 - UInt64 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend UInt8 <: JsonDeserializable\<UInt8>

```cangjie
extend UInt8 <: JsonDeserializable<UInt8>
```

功能：为 UInt8 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<UInt8>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): UInt8
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 UInt8。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- UInt8 - UInt8 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend UIntNative <: JsonDeserializable\<UIntNative>

```cangjie
extend UIntNative <: JsonDeserializable<UIntNative>
```

功能：为 UIntNative 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<UIntNative>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): UIntNative
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 UIntNative。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- UIntNative - UIntNative 类型的实例。

异常：

- OverflowException - 读取的数据超过范围时，抛出异常。

### extend\<T> Array\<T> <: JsonDeserializable\<Array\<T>> where T <: JsonDeserializable\<T>

```cangjie
extend<T> Array<T> <: JsonDeserializable<Array<T>> where T <: JsonDeserializable<T>
```

功能：为 Array\<T> 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Array\<T>>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Array<T>
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Array。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Array\<T> - Array 类型的实例。