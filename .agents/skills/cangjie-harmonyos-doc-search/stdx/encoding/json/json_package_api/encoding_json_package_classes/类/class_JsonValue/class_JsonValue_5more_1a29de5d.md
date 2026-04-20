## class JsonValue

```cangjie
sealed abstract class JsonValue <: ToString
```

功能：此类为 JSON 数据层，主要用于 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 和 String 数据之间的互相转换。

抽象类 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 提供了 String 类型和具体的 JSON 类型相互转换的接口，以及具体的 JSON 类型判断功能。

父类型：

- ToString

示例：

使用示例见[JsonValue 和 String 互相转换](../json_samples/json_value_sample.md)。

### static func fromStr(String)

```cangjie
public static func fromStr(s: String): JsonValue
```

功能：将字符串数据解析为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。对于整数，支持前导 '0b'，'0o'，'0x'（不区分大小写），分别表示二进制，八进制和十六进制。字符串解析失败时将打印错误字符及其行数和列数，其中列数从错误字符所在行的非空格字符起开始计算。

JSON 在解析 String 转换为 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 时，转义字符 \\ 之后只能对应 JSON 支持的转义字符（b、f、n、r、t、u、\\、\"、\/），其中 \\u 的格式为：\\uXXXX，X 为十六进制数，例：\\u0041 代表字符 'A'。

参数：

- s: String - 传入字符串，暂不支持 "?" 和特殊字符。

返回值：

- [JsonValue](encoding_json_package_classes.md#class-jsonvalue) - 转换后的 [JsonValue](encoding_json_package_classes.md#class-jsonvalue)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果内存分配失败，或解析字符串出错，抛出异常。

示例：

```cangjie
import stdx.encoding.json.*

main() {
    println(JsonString("\b | \f | \n | \r | \t | A | \\ | \" | /").toString())
    println(JsonValue.fromStr("\"\\b\"").toString())
    println(JsonValue.fromStr("\"\\f\"").toString())
    println(JsonValue.fromStr("\"\\n\"").toString())
    println(JsonValue.fromStr("\"\\r\"").toString())
    println(JsonValue.fromStr("\"\\t\"").toString())
    println(JsonValue.fromStr("\"\\u0041\"").toString())
    println(JsonValue.fromStr("\"\\\\\"").toString())
    println(JsonValue.fromStr("\"\\\"\"").toString())
    println(JsonValue.fromStr("\"\\/\"").toString())
}
```

运行结果如下：

```text
"\b | \f | \n | \r | \t | A | \\ | \" | /"
"\b"
"\f"
"\n"
"\r"
"\t"
"A"
"\\"
"\""
"/"
```

### func asArray()

```cangjie
public func asArray(): JsonArray
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 [JsonArray](encoding_json_package_classes.md#class-jsonarray) 格式。

返回值：

- [JsonArray](encoding_json_package_classes.md#class-jsonarray) - 转换后的 [JsonArray](encoding_json_package_classes.md#class-jsonarray)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果转换失败，抛出异常。

### func asBool()

```cangjie
public func asBool(): JsonBool
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 [JsonBool](encoding_json_package_classes.md#class-jsonbool) 格式。

返回值：

- [JsonBool](encoding_json_package_classes.md#class-jsonbool) - 转换后的 [JsonBool](encoding_json_package_classes.md#class-jsonbool)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果转换失败，抛出异常。

### func asFloat()

```cangjie
public func asFloat(): JsonFloat
```

功能：将 [JsonValue](encoding_json_package_classes.md#class-jsonvalue) 转换为 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) 格式。

返回值：

- [JsonFloat](encoding_json_package_classes.md#class-jsonfloat) - 转换后的 [JsonFloat](encoding_json_package_classes.md#class-jsonfloat)。

异常：

- [JsonException](encoding_json_package_exceptions.md#class-jsonexception) - 如果转换失败，抛出异常。