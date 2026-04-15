### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 转换为 JSON 格式的 (带有空格换行符) 的字符串。

返回值：

- String - 转换后的 JSON 格式字符串。

### func toJsonString(Int64, Bool, String)

```cangjie
public func toJsonString(depth: Int64, bracketInNewLine!: Bool = false, indent!: String = "  "): String
```

功能：将 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 转换为 JSON 格式的字符串。该函数将指定初始的缩进深度、第一个括号后是否换行以及缩进字符串。

参数：

- depth: Int64 - 指定的缩进深度。
- bracketInNewLine!: Bool - 第一个括号是否换行，如果为 `true`，第一个括号将另起一行并且按照指定的深度缩进。
- indent!: String - 指定的缩进字符串，缩进字符串中只允许空格和制表符的组合，默认为两个空格。

返回值：

- String - 转换后的 JSON 格式字符串。

异常：

- IllegalArgumentException - 如果 depth 为负数，或 indent 中存在 ' ' 和 '\t' 以外的字符，则抛出异常。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [JsonString](encoding_json_package_classes.md#class-jsonstring) 转换为字符串。

返回值：

- String - 转换后的字符串。

### operator func [](Int64)

```cangjie
public operator func [](index: Int64): JsonValue
```

功能：获取 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 中指定索引的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。

参数：

- index: Int64 - 指定的索引。

返回值：

- [JsonValue](encoding_json_package_classes.md#class-jsonvalue) - 对应索引的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果 index 不是 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 的有效索引，抛出异常。