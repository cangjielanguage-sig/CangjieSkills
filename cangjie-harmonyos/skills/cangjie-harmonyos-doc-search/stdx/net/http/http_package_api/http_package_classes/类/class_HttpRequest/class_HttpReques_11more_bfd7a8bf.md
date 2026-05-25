## class HttpRequest

```cangjie
public class HttpRequest <: ToString
```

功能：此类为 Http 请求类。

客户端发送请求时，需要构造一个 [HttpRequest](http_package_classes.md#class-httprequest) 实例，再编码成字节报文发出。

服务端处理请求时，需要把收到的请求解析成 [HttpRequest](http_package_classes.md#class-httprequest) 实例，并传给 handler 处理函数。

父类型：

- ToString

### prop body

```cangjie
public prop body: InputStream
```

功能：获取 body。

> **注意：**
>
> - body 不支持并发读取；
> - 默认 InputStream 实现类的 read 函数不支持多次读取。

类型：InputStream

### prop bodySize

```cangjie
public prop bodySize: Option<Int64>
```

功能：获取请求 body 长度。

- 如果未设置 body，则 bodySize 为 Some(0)；
- 如果 body 长度已知，即通过 Array\<UInt8> 或 String 传入 body，或传入的 InputStream 有确定的 length (length >= 0)，则 bodySize 为 Some(Int64)；
- 如果 body 长度未知，即通过用户自定义的 InputStream 实例传入 body 且 InputStream 实例没有确定的 length (length < 0)，则 bodySize 为 None。

类型：Option\<Int64>

### prop isPersistent

```cangjie
public prop isPersistent: Bool
```

功能：表示该请求是否为长连接，即请求 header 是否不包含 `Connection: close`。包含 `Connection: close` 为 false，否则为 true。

- 对于服务端，isPersistent 为 false 表示处理完该请求应该关闭连接。
- 对于客户端，isPersistent 为 false 表示如果收到响应后服务端未关闭连接，客户端应主动关闭连接。

类型：Bool

### prop form

```cangjie
public prop form: Form
```

功能：获取请求中的表单信息。

- 如果请求方法为 POST，PUT，PATCH，且 content-type 包含 application/x-www-form-urlencoded，获取请求 body 部分，用 form 格式解析；
- 如果请求方法不为 POST，PUT，PATCH，获取请求 url 中 query 部分。

> **注意：**
>
> - 如果用该接口读取了 body，body 已被消费完，后续将无法通过 body.read 读取 body；
> - 如果 form 不符合 [Form](../../../encoding/url/url_package_api/url_package_classes.md#class-form) 格式，抛 [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) 异常。

类型：[Form](../../../encoding/url/url_package_api/url_package_classes.md#class-form)

### prop headers

```cangjie
public prop headers: HttpHeaders
```

功能：获取 headers，headers 详述见 [HttpHeaders](http_package_classes.md#class-httpheaders) 类，获取后，可通过调用 [HttpHeaders](http_package_classes.md#class-httpheaders) 实例成员函数，修改该请求的 headers。

类型：[HttpHeaders](http_package_classes.md#class-httpheaders)

### prop method

```cangjie
public prop method: String
```

功能：获取 method，如 "GET", "POST"，request 实例的 method 无法修改。

类型：String

### prop readTimeout

```cangjie
public prop readTimeout: ?Duration
```

功能：表示该请求的请求级读超时时间。None 表示没有设置；Some(Duration) 表示设置了读超时时间。

类型：?Duration

### prop remoteAddr

```cangjie
public prop remoteAddr: String
```

功能：用于服务端，获取对端地址，即客户端地址，格式为 ip: port，用户无法设置，自定义的 request 对象调用该属性返回 ""，服务端 handler 中调用该属性返回客户端地址。

类型：String

### prop trailers

```cangjie
public prop trailers: HttpHeaders
```

功能：获取 trailers，trailers 详述见 [HttpHeaders](http_package_classes.md#class-httpheaders) 类，获取后，可通过调用 [HttpHeaders](http_package_classes.md#class-httpheaders) 实例成员函数，修改该请求的 trailers。

类型：[HttpHeaders](http_package_classes.md#class-httpheaders)

### prop url

```cangjie
public prop url: URL
```

功能：获取 url，表示客户端访问的 url。

类型：[URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url)