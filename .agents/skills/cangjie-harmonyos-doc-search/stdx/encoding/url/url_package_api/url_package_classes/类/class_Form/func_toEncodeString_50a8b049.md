### func toEncodeString()

```cangjie
public func toEncodeString(): String
```

功能：对表单中的键值对进行编码，编码采用百分号编码。

未保留字符不会被编码，空格将编码为 '+'。

> **说明：**
>
> RFC 3986 协议中对未保留字符定义如下： unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"

返回值：

- String - 编码后的字符串。