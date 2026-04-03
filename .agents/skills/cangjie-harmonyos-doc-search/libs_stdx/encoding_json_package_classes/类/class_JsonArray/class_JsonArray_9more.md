## class JsonArray

```cangjie
public class JsonArray <: JsonValue {
    public init()
    public init(list: ArrayList<JsonValue>)
    public init(list: Array<JsonValue>)
}
```

功能：此类为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 实现子类，主要用于封装数组类型的 JSON 数据。

父类型：

- [JsonValue](#class-jsonvalue)

示例：

使用示例见 [JsonArray 使用示例](../json_samples/json_array_sample.md)。

### init()

```cangjie
public init()
```

功能：创建空 [JsonArray](encoding_json_package_classes.md#class-jsonarray)。

### init(ArrayList\<JsonValue>)

```cangjie
public init(list: ArrayList<JsonValue>)
```

功能：将指定的 ArrayList 类型实例封装成 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 实例。

参数：

- list: ArrayList\<[JsonValue](encoding_json_package_classes.md#class-jsonvalue)> - 用于创建 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 的 ArrayList。

### init(Array\<JsonValue>)

```cangjie
public init(list: Array<JsonValue>)
```

功能：将指定的 Array 类型实例封装成 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 实例。

参数：

- list: Array\<[JsonValue](encoding_json_package_classes.md#class-jsonvalue)> - 用于创建 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 的 Array。

### func add(JsonValue)

```cangjie
public func add(jv: JsonValue): JsonArray
```

功能：向 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 中加入 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 数据。

参数：

- jv: [JsonValue](encoding_json_package_classes.md#class-jsonvalue) - 需要加入的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。

返回值：

- [JsonArray](encoding_json_package_classes.md#class-jsonarray) - 加入数据后的 [JsonArray](encoding_json_package_classes.md#class-jsonarray)。

### func get(Int64)

```cangjie
public func get(index: Int64): Option<JsonValue>
```

功能：获取 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 中指定索引的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)，并用 Option\<[JsonValue](encoding_json_package_classes.md#class-jsonvalue)> 封装。

参数：

- index: Int64 - 指定的索引。

返回值：

- Option\<[JsonValue](encoding_json_package_classes.md#class-jsonvalue)> - 对应索引的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 数据的封装形式。

### func getItems()

```cangjie
public func getItems(): ArrayList<JsonValue>
```

功能：获取 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 中的 items 数据。

返回值：

- ArrayList\<[JsonValue](encoding_json_package_classes.md#class-jsonvalue)> - [JsonArray](encoding_json_package_classes.md#class-jsonarray) 的 items 数据。

### func kind()

```cangjie
public func kind(): JsonKind
```

功能：返回当前 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsArray）。

返回值：

- [JsonKind](encoding_json_package_enums.md#enum-jsonkind) - 当前 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 所属的 [JsonKind](encoding_json_package_enums.md#enum-jsonkind) 类型（JsArray）。

### func size()

```cangjie
public func size(): Int64
```

功能：获取 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 中 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 的数量。

返回值：

- Int64 - [JsonArray](encoding_json_package_classes.md#class-jsonarray) 中 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 的数量。