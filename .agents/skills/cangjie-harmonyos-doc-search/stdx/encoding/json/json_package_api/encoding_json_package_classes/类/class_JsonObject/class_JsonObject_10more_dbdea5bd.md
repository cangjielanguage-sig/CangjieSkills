## class JsonObject

```cangjie
public class JsonObject <: JsonValue {
    public init()
    public init(map: HashMap<String, JsonValue>)
}
```

功能：此类为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 实现子类，主要用于封装 object 类型的 JSON 数据。

父类型：

- [JsonValue](#class-jsonvalue)

### init()

```cangjie
public init()
```

功能：创建空 [JsonObject](encoding_json_package_classes.md#class-jsonobject)。

### init(HashMap\<String, JsonValue>)

```cangjie
public init(map: HashMap<String, JsonValue>)
```

功能：将指定的 HashMap 类型实例封装成 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 实例。

参数：

- map: HashMap\<String, [JsonValue](encoding_json_package_classes.md#class-jsonvalue)> - data 数据。

### func containsKey(String)

```cangjie
public func containsKey(key: String): Bool
```

功能：判断 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 中是否存在 key。

参数：

- key: String - 指定的 key。

返回值：

- Bool - 存在返回 true，不存在返回 false。

### func get(String)

```cangjie
public func get(key: String): Option<JsonValue>
```

功能：获取 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 中 key 对应的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)，并用 Option\<[JsonValue](encoding_json_package_classes.md#class-jsonvalue)> 封装。

参数：

- key: String - 指定的 key。

返回值：

- Option\<[JsonValue](encoding_json_package_classes.md#class-jsonvalue)> - key 对应的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 的封装形式。

### func getFields()

```cangjie
public func getFields(): HashMap<String, JsonValue>
```

功能：获取 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 中的 fields 数据。

返回值：

- HashMap\<String, [JsonValue](encoding_json_package_classes.md#class-jsonvalue)> - [JsonObject](encoding_json_package_classes.md#class-jsonobject) 的 fields 数据。

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsObject）。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsObject）。

### func put(String, JsonValue)

```cangjie
public func put(key: String, v: JsonValue): Unit
```

功能：向 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 中加入 key-[JsonValue](encoding_json_package_classes.md#class-jsonvalue) 数据。

参数：

- key: String - 需要加入的 key。
- v: [JsonValue](encoding_json_package_classes.md#class-jsonvalue) - 对应 key 的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。

### func size()

```cangjie
public func size(): Int64
```

功能：获取 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 中 fields 存入 string-[JsonValue](encoding_json_package_classes.md#class-jsonvalue) 的数量。

返回值：

- Int64 - [JsonObject](encoding_json_package_classes.md#class-jsonobject) 中 fields 的大小。

### func toJsonString()

```cangjie
public func toJsonString(): String
```

功能：将 [JsonObject](encoding_json_package_classes.md#class-jsonobject) 转换为 JSON 格式的 (带有空格换行符) 字符串。

返回值：

- String - 转换后的 JSON 格式字符串。