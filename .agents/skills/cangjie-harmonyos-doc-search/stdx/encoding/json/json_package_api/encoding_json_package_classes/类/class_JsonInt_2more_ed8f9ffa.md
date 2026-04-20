## class JsonInt

```cangjie
public class JsonInt <: JsonValue {
    public init(iv: Int64)
}
```

功能：此类为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 实现子类，主要用于封装整数类型的 JSON 数据。

父类型：

- [JsonValue](#class-jsonvalue)

### init(Int64)

```cangjie
public init(iv: Int64)
```

功能：将指定的 Int64 类型实例封装成 [JsonInt](encoding_json_package_classes.md#class-jsonint) 实例。

参数：

- iv: Int64 - 用于创建 [JsonInt](encoding_json_package_classes.md#class-jsonint) 的 Int64。

### func getValue()

```cangjie
public func getValue(): Int64
```

功能：获取 [JsonInt](encoding_json_package_classes.md#class-jsonint) 中 value 的实际值。

返回值：

- Int64 - value 的实际值。

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonInt](encoding_json_package_classes.md#class-jsonint) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsInt）。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonInt](encoding_json_package_classes.md#class-jsonint) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsInt）。

### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonInt](encoding_json_package_classes.md#class-jsonint) 转换为 JSON 格式的 (带有空格换行符) 字符串。

返回值：

- String - 转换后的 JSON 格式字符串。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [JsonInt](encoding_json_package_classes.md#class-jsonint) 转换为字符串。

返回值：

- String - 转换后的字符串。

## class JsonNull

```cangjie
public class JsonNull <: JsonValue
```

功能：此类为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 实现子类，主要用于封装 null 的 JSON 数据。

父类型：

- [JsonValue](#class-jsonvalue)

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonNull](encoding_json_package_classes.md#class-jsonnull) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsNull）。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonNull](encoding_json_package_classes.md#class-jsonnull) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsNull）。

### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonNull](encoding_json_package_classes.md#class-jsonnull) 转换为 JSON 格式的 (带有空格换行符) 字符串。

返回值：

- String - 转换后的 JSON 格式字符串。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [JsonNull](encoding_json_package_classes.md#class-jsonnull) 转换为字符串。

返回值：

- String - 转换后的字符串。