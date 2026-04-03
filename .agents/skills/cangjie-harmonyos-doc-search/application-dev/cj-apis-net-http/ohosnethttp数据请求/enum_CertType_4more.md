## enum CertType

```cangjie
public enum CertType {
    | Pem
    | Der
    | P12
    | ...
}
```

**功能：** 枚举，证书类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Der

```cangjie
Der
```

**功能：** 证书类型Der。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### P12

```cangjie
P12
```

**功能：** 证书类型P12。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Pem

```cangjie
Pem
```

**功能：** 证书类型Pem。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

## enum HttpData

```cangjie
public enum HttpData {
    | StringData(String)
    | ArrayData(Array<Byte>)
    | ...
}
```

**功能：** HTTP的数据。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### ArrayData(Array\<Byte>)

```cangjie
ArrayData(Array<Byte>)
```

**功能：** 二进制数组。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### StringData(String)

```cangjie
StringData(String)
```

**功能：** 字符串。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

## enum HttpDataType

```cangjie
public enum HttpDataType {
    | StringValue
    | ArrayBuffer
    | ...
}
```

**功能：** HTTP的数据类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### ArrayBuffer

```cangjie
ArrayBuffer
```

**功能：** 二进制数组类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### StringValue

```cangjie
StringValue
```

**功能：** 字符串类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

## enum HttpProtocol

```cangjie
public enum HttpProtocol {
    | Http1_1
    | Http2
    | Http3
    | ...
}
```

**功能：** HTTP协议版本。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Http1_1

```cangjie
Http1_1
```

**功能：** 协议HTTP1.1。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Http2

```cangjie
Http2
```

**功能：** 协议HTTP2。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### Http3

```cangjie
Http3
```

**功能：** 协议HTTP3，若系统或服务器不支持，则使用低版本的HTTP协议请求。<br />**注意：** 仅对HTTPS的URL生效，HTTP则会请求失败。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22