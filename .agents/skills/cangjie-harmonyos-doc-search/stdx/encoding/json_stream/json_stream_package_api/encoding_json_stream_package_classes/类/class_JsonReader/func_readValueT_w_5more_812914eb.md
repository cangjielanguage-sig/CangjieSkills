### func readValue\<T>() where T <: JsonDeserializable\<T>

```cangjie
public func readValue<T>(): T where T <: JsonDeserializable<T>
```

功能：从输入流的当前位置读取一个 value。

> **注意：**
>
> 当泛型 T 是 String 类型时，根据下一个 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 的不同，该函数的返回值将会不同：
>
> - 当下一个 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 是 [JsonString](../../json/json_package_api/encoding_json_package_classes.md#class-jsonstring) 时， 反序列化过程会按照标准 [ECMA-404 The JSON Data Interchange Standard](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/) 对读到的 String 进行转义。
>
> - 当下一个 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 是 [JsonInt](../../json/json_package_api/encoding_json_package_classes.md#class-jsonint) [JsonFloat](../../json/json_package_api/encoding_json_package_classes.md#class-jsonfloat) [JsonBool](../../json/json_package_api/encoding_json_package_classes.md#class-jsonbool) [JsonNull](../../json/json_package_api/encoding_json_package_classes.md#class-jsonnull) 其中一个时，将会读取下一个 `value` 字段的原始字符串并返回。
>
> - 当下一个 [JsonToken](encoding_json_stream_package_enums.md#enum-jsontoken) 是其它类型时，调用此接口会抛异常。

返回值：

- T - 读取出的 value 值。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。

### func readValueBytes()

```cangjie
public func readValueBytes(): Array<Byte>
```

功能：读取输入流的下一组原始数据(字节数组)，不进行转义等操作。

> **说明：**
>
> readValueBytes 的规则如下：
>
> - 如果 next token 是 value，则读取这个 value 的所有原始字节，直到读取到代表结束的符号，如 ',' '}' ']'。
>
> - 如果 next token 是 Name，读取 (name + value) 这一个组合的原始字节数组。
>
> - 如果 next token 是 BeginArray，读取 Array 内的内的所有原始字节。
>
> - 如果 next token 是 BeginObject，读取 Object 内的内的所有原始字节。
>
> - 如果 next token 是 EndArray 或者 EndObject 或者 None，不做任何操作，返回空的数组，再次执行 peek() 仍返回 EndArray 或者 EndObject 或者 None。

返回值：

- Array\<Byte> - 下一组数据对应的原始字节数据。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。

### func skip()

```cangjie
public func skip(): Unit
```

功能：从输入流的当前位置跳过一组数据。

> **说明：**
>
> Skip 的规则如下：
>
> - 如果 next token 是 value，跳过这个 value, 跳过 value 时不检查该 value 格式是否正确。
>
> - 如果 next token 是 Name，跳过 (name + value) 这一个组合。
>
> - 如果 next token 是 BeginArray，跳过这个 array。
>
> - 如果 next token 是 BeginObject，跳过这个 object。
>
> - 如果 next token 是 EndArray 或者 EndObject 或者 None，不做任何操作，peek 仍返回 EndArray 或者 EndObject 或者 None。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。

### func startArray()

```cangjie
public func startArray(): Unit
```

功能：从输入流的当前位置跳过空白字符后消耗一个 '[' 字符。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。

### func startObject()

```cangjie
public func startObject(): Unit
```

功能：从输入流的当前位置跳过空白字符后消耗一个 '{' 字符。

异常：

- IllegalStateException - 如果输入流的 JSON 数据不符合格式，抛出异常。