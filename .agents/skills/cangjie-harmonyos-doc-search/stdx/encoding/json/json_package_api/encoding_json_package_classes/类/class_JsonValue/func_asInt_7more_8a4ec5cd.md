### func asInt()

```cangjie
public func asInt(): JsonInt
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 [JsonInt](encoding_json_package_classes.md#class-jsonint) 格式。

返回值：

- [JsonInt](encoding_json_package_classes.md#class-jsonint) - 转换后的 [JsonInt](encoding_json_package_classes.md#class-jsonint)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果转换失败，抛出异常。

### func asNull()

```cangjie
public func asNull(): JsonNull
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 [JsonNull](encoding_json_package_classes.md#class-jsonnull) 格式。

返回值：

- [JsonNull](encoding_json_package_classes.md#class-jsonnull) - 转换后的 [JsonNull](encoding_json_package_classes.md#class-jsonnull)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果转换失败，抛出异常。

### func asObject()

```cangjie
public func asObject(): JsonObject
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 格式。

返回值：

- [JsonObject](encoding_json_package_classes.md#class-jsonobject) - 转换后的 [JsonObject](encoding_json_package_classes.md#class-jsonobject)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果转换失败，抛出异常。

### func asString()

```cangjie
public func asString(): JsonString
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 [JsonString](encoding_json_package_classes.md#class-jsonstring) 格式。

返回值：

- [JsonString](encoding_json_package_classes.md#class-jsonstring) - 转换后的 [JsonString](encoding_json_package_classes.md#class-jsonstring)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果转换失败，抛出异常。

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型。

### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 JSON 格式的 (带有空格换行符) 字符串。

返回值：

- String - 转换后的 JSON 格式字符串。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为字符串。

返回值：

- String - 转换后的字符串。