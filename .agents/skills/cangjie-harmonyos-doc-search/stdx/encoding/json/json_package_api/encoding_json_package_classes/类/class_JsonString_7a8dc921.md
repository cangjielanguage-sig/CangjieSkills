## class JsonString

```cangjie
public class JsonString <: JsonValue {
    public init(sv: String)
}
```

功能：此类为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 实现子类，主要用于封装字符串类型的 JSON 数据。

父类型：

- [JsonValue](#class-jsonvalue)

### init(String)

```cangjie
public init(sv: String)
```

功能：将指定的 String 类型实例封装成 [JsonString](encoding_json_package_classes.md#class-jsonstring) 实例。

参数：

- sv: String - String 类型。

### func getValue()

```cangjie
public func getValue(): String
```

功能：获取 [JsonString](encoding_json_package_classes.md#class-jsonstring) 中 value 的实际值。

返回值：

- String - value 的实际值。

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonString](encoding_json_package_classes.md#class-jsonstring) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsString）。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonString](encoding_json_package_classes.md#class-jsonstring) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsString）。

### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonString](encoding_json_package_classes.md#class-jsonstring) 转换为 JSON 格式的 (带有空格换行符) 字符串。

返回值：

- String - 转换后的 JSON 格式字符串。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [JsonString](encoding_json_package_classes.md#class-jsonstring) 转换为字符串。

返回值：

- String - 转换后的字符串。