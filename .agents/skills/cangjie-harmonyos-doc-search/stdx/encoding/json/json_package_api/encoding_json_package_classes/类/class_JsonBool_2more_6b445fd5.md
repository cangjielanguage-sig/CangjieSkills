## class JsonBool

```cangjie
public class JsonBool <: JsonValue {
    public init(bv: Bool)
}
```

功能：此类为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 实现子类，主要用于封装 true 或者 false 的 JSON 数据。

父类型：

- [JsonValue](#class-jsonvalue)

### init(Bool)

```cangjie
public init(bv: Bool)
```

功能：将指定的 Bool 类型实例封装成 [JsonBool](encoding_json_package_classes.md#class-jsonbool) 实例。

参数：

- bv: Bool - Bool 类型。

### func getValue()

```cangjie
public func getValue(): Bool
```

功能：获取 [JsonBool](encoding_json_package_classes.md#class-jsonbool) 中 value 的实际值。

返回值：

- Bool - value 的实际值。

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonBool](encoding_json_package_classes.md#class-jsonbool) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsBool）。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonBool](encoding_json_package_classes.md#class-jsonbool) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsBool）。

### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonBool](encoding_json_package_classes.md#class-jsonbool) 转换为 JSON 格式的 (带有空格换行符) 字符串。

返回值：

- String - 转换后的 JSON 格式字符串。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [JsonBool](encoding_json_package_classes.md#class-jsonbool) 转换为字符串。

返回值：

- String - 转换后的字符串。

## class JsonFloat

```cangjie
public class JsonFloat <: JsonValue {
    public init(fv: Float64)
    public init(v: Int64)
}
```

功能：此类为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 实现子类，主要用于封装浮点类型的 JSON 数据。

父类型：

- [JsonValue](#class-jsonvalue)

### init(Float64)

```cangjie
public init(fv: Float64)
```

功能：将指定的 Float64 类型实例封装成 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 实例。

参数：

- fv: Float64 - Float64 类型。

### init(Int64)

```cangjie
public init(v: Int64)
```

功能：将指定的 Int64 类型实例封装成 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 实例。

参数：

- v: Int64 - Int64 类型。

### func getValue()

```cangjie
public func getValue(): Float64
```

功能：获取 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 中 value 的实际值。

返回值：

- Float64 - value 的实际值。

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsFloat）。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsFloat）。

### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 转换为 JSON 格式的 (带有空格换行符) 字符串。

返回值：

- String - 转换后的 JSON 格式字符串。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 转换为字符串。

返回值：

- String - 转换后的字符串。