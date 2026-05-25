### prop version

```cangjie
public prop version: Protocol
```

功能：获取 http 版本，如 HTTP1_1 和 HTTP2_0，request 实例的 version 无法修改。

类型：[Protocol](http_package_enums.md#enum-protocol)

### prop writeTimeout

```cangjie
public prop writeTimeout: ?Duration
```

功能：表示该请求的请求级写超时时间，None 表示没有设置；Some(Duration) 表示设置了写超时时间。

类型：?Duration

### func toString()

```cangjie
public override func toString(): String
```

功能：把请求转换为字符串，包括 start line，headers，body size，trailers。
例如：`"GET /path HTTP/1.1\r\nhost: www.example.com\r\n\r\nbody size: 5\r\nbar: foo\r\n"`。

返回值：

- String - 请求的字符串表示。