### extend\<T> ArrayList\<T> <: JsonDeserializable\<ArrayList\<T>> where T <: JsonDeserializable\<T>

```cangjie
extend<T> ArrayList<T> <: JsonDeserializable<ArrayList<T>> where T <: JsonDeserializable<T>
```

功能：为 ArrayList 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<ArrayList\<T>>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): ArrayList<T>
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 ArrayList。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- ArrayList \<T> - ArrayList 类型的实例。

### extend\<T> Option \<T> <: JsonDeserializable\<Option\<T>> where T <: JsonDeserializable\<T>

```cangjie
extend<T> Option<T> <: JsonDeserializable<Option<T>> where T <: JsonDeserializable<T>
```

功能：为 Option 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<Option\<T>>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): Option<T>
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 Option。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- Option\<T> - Option 类型的实例。

### extend\<T> HashMap\<String, T> <: JsonDeserializable\<HashMap\<String, T>> where T <: JsonDeserializable\<T>

```cangjie
extend<T> HashMap<String, T> <: JsonDeserializable<HashMap<String, T>> where T <: JsonDeserializable<T>
```

功能：为 HashMap 类型实现 JsonDeserializable 接口。

父类型：

- [JsonDeserializable](#interface-jsondeserializablet)\<HashMap\<String, T>>

#### static func fromJson(JsonReader)

```cangjie
public static func fromJson(r: JsonReader): HashMap<String, T>
```

功能：从 [JsonReader](../json_stream_package_api/encoding_json_stream_package_classes.md#class-jsonreader) 中读取一个 HashMap。

参数：

- r: [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) - 读取反序列化结果的 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 实例。

返回值：

- HashMap\<String, T> - HashMap\<String, T> 类型的实例。