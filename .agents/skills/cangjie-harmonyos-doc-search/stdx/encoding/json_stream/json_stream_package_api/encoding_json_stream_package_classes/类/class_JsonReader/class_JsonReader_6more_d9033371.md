## class JsonReader

```cangjie
public class JsonReader {
    public init(inputStream: InputStream)
}
```

功能：此类提供 JSON 数据流转仓颉对象的反序列化能力。

使用示例见[使用 Json Stream 进行反序列化](../json_stream_samples/sample_json_reader.md)

### init(InputStream)

```cangjie
public init(inputStream: InputStream)
```

功能：根据输入流创建一个 [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader)， [JsonReader](encoding_json_stream_package_classes.md#class-jsonreader) 从输入流中读取数据时，将跳过非 [JsonString](../../json/json_package_api/encoding_json_package_classes.md#class-jsonstring) 中的空字符（'\0', '\t', '\n', '\r'）。

参数：

- inputStream: InputStream - 输入的 JSON 数据流。

### func endArray()

```cangjie
public func endArray(): Unit
```

功能：从输入流的当前位置跳过空白字符后消耗一个 ']' 字符，[endArray](encoding_json_stream_package_classes.md#func-endarray) 必须有一个 [startArray](encoding_json_stream_package_classes.md#func-startarray) 与之对应。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。

### func endObject()

```cangjie
public func endObject(): Unit
```

功能：从输入流的当前位置跳过空白字符后消耗一个 '}' 字符，[endObject](encoding_json_stream_package_classes.md#func-endobject) 必须有一个 [startObject](encoding_json_stream_package_classes.md#func-startobject) 与之对应。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。

### func peek()

```cangjie
public func peek(): Option<JsonToken>
```

功能：获取输入流的下一个 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 的类型，不保证下一个 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 的格式一定正确。

例：如果输入流中的下一个字符为 't'，获取的 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 将为 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken).Bool，但调用 readValue\<Bool>() 不一定成功。

返回值：

- Option\<[JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken)> - 获取到的下一个 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 的类型，如果到了输入流的结尾返回 None。

异常：

- IllegalStateException - 如果输入流的下一个字符不在以下范围内：(n, t, f, ", 0~9, -, {, }, [, ])。

### func readName()

```cangjie
public func readName(): String
```

功能：从输入流的当前位置读取一个 name。

返回值：

- String - 读取出的 name 值。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。