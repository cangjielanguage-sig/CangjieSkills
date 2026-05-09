## interface JsonDeserializable\<T>

```cangjie
public interface JsonDeserializable<T> {
    static func fromJson(r: JsonReader): T
}
```

功能：此接口用于实现从 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个仓颉对象。

支持的对象类型包括：

- 基本数据类型：整数类型、浮点类型、布尔类型、字符串类型。

- Collection 类型：Array、ArrayList、HashMap、Option。

- BigInt、Decimal 类型。

- DateTime 类型。

### static func fromJson(JsonReader)

```cangjie
static func fromJson(r: JsonReader): T
```

功能：从参数 `r` 指定的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例中读取一个 `T` 类型对象。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- T - `T` 类型的实例。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。

### extend BigInt <: JsonDeserializable\<BigInt>

```cangjie
extend BigInt <: JsonDeserializable<BigInt>
```

功能：为 BigInt 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<BigInt>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): BigInt
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 BigInt。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- BigInt - BigInt 类型的实例。

### extend Bool <: JsonDeserializable\<Bool>

```cangjie
extend Bool <: JsonDeserializable<Bool>
```

功能：为 Bool 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Bool>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Bool
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Bool。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Bool - Bool 类型的实例。

### extend DateTime <: JsonDeserializable\<DateTime>

```cangjie
extend DateTime <: JsonDeserializable<DateTime>
```

功能：为 DateTime 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<DateTime>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): DateTime
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 DateTime 实例。

该函数将会把读取到的字符串按照 `RFC3339` 的规范解析，可包含小数秒格式，函数的行为参考 DateTime 的 func parse(String)。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- DateTime - DateTime 类型的实例。

异常：

- TimeParseException - 无法正常解析时，抛出异常。