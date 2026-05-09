### func toJsonString(Int64, Bool, String)

```cangjie
public func toJsonString(depth: Int64, bracketInNewLine!: Bool = false, indent!: String = "  "): String
```

功能：将 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 转换为 Json 格式的字符串。该函数将指定初始的缩进深度、第一个括号后是否换行以及缩进字符串。

参数：

- depth: Int64 - 缩进深度。
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

功能：将 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 转换为字符串。

返回值：

- String - 转换后的字符串。

### operator func [](String)

```cangjie
public operator func [](key: String): JsonValue
```

功能：获取 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 中 key 对应的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。

参数：

- key: String - 指定的 key。

返回值：

- [JsonValue](encoding_json_package_classes.md#class-jsonvalue) - key 对应的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果 key 不是 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 的有效键，抛出异常。