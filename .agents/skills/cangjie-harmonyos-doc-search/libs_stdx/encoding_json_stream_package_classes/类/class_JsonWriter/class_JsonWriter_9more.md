## class JsonWriter

```cangjie
public class JsonWriter {
    public var writeConfig = WriteConfig.compact
    public init(out: OutputStream)
}
```

功能：[JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 提供了将仓颉对象序列化到 OutputStream 的能力。

[JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 需要和 interface [JsonSerializable](encoding_json_stream_package_interfaces.md#interface-jsonserializable) 搭配使用，[JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 可以通过 writeValue 来将实现了 [JsonSerializable](encoding_json_stream_package_interfaces.md#interface-jsonserializable) 接口的类型写入到 Stream 中。

> **注意：**
>
> [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 中使用缓存来减少写入 Stream 时的 IO 次数，在结束使用 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 之前需要调用 flush 函数来确保缓存中的数据全部写入 Stream。

示例：

使用示例见[使用 Json Stream 进行序列化](../json_stream_samples/sample_json_writer.md)

### var writeConfig

```cangjie
public var writeConfig = WriteConfig.compact
```

功能：序列化格式配置。详见 [WriteConfig](./encoding_json_stream_package_structs.md#struct-writeconfig)。

### init(OutputStream)

```cangjie
public init(out: OutputStream)
```

功能：构造函数，构造一个将数据写入 out 的实例。

参数：

- out: OutputStream - 目标流

### func endArray()

```cangjie
public func endArray(): Unit
```

功能：结束序列化当前的 JSON 数组。

异常：

- IllegalStateException - 当前 writer 没有匹配的 startArray 时。

### func endObject()

```cangjie
public func endObject(): Unit
```

功能：结束序列化当前的 JSON object。

异常：

- IllegalStateException - 当前 writer 的状态不应该结束一个 JSON object 时。

### func flush()

```cangjie
public func flush(): Unit
```

功能：将缓存中的数据写入 out，并且调用 out 的 flush 方法。

### func jsonValue(String)

```cangjie
public func jsonValue(value: String): JsonWriter
```

功能：将符合 JSON value 规范的原始字符串写入 stream。

> **注意：**
>
> 此函数不会对值 value 进行转义，也不会为入参添加双引号。如果使用者能够保证输入的值 value 符合数据转换标准[ECMA-404 The JSON Data Interchange Standard](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/)， 建议使用该函数。

返回值：

- [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) - 为方便链式调用，返回值为当前 [JsonWriter](encoding_json_stream_package_classes.md#class-jsonwriter) 的引用。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 value 时。

### func startArray()

```cangjie
public func startArray(): Unit
```

功能：开始序列化一个新的 JSON 数组，每一个 [startArray](encoding_json_stream_package_classes.md#func-startarray-1) 都必须有一个 [endArray](encoding_json_stream_package_classes.md#func-endarray-1) 对应。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 JSON array 时。

### func startObject()

```cangjie
public func startObject(): Unit
```

功能：开始序列化一个新的 JSON object，每一个 [startObject](encoding_json_stream_package_classes.md#func-startobject-1) 都必须有一个 [endObject](encoding_json_stream_package_classes.md#func-endobject-1) 对应。

异常：

- IllegalStateException - 当前 writer 的状态不应该写入 JSON object 时。