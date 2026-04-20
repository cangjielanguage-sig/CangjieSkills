## class HttpResponse

```cangjie
public class HttpResponse <: ToString
```

功能：Http 响应类。

此类定义了 http 中响应 Response 的相关接口，客户端用该类读取服务端返回的响应。

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

功能：获取响应 body 长度。

> - 如果未设置 body，则 bodySize 为 Some(0)；
> - 如果 body 长度已知，即通过 Array\<UInt8> 或 String 传入 body，或传入的 InputStream 有确定的 length (length >= 0)，则 bodySize 为 Some(Int64)；
> - 如果 body 长度未知，即通过用户自定义的 InputStream 实例传入 body 且 InputStream 实例没有确定的 length (length < 0)，则 bodySize 为 None。

类型：Option\<Int64>

### prop isPersistent

```cangjie
public prop isPersistent: Bool
```

功能：表示该响应是否为长连接，即响应 header 是否不包含 `Connection: close`。包含 `Connection: close` 为 false，否则为 true。

对于服务端，isPersistent 为 false 表示处理完该请求应关闭连接；

对于客户端，isPersistent 为 false 表示读完响应体后客户端应主动关闭连接。

类型：Bool

### prop headers

```cangjie
public prop headers: HttpHeaders
```

功能：获取 headers，headers 详述见 [HttpHeaders](http_package_classes.md#class-httpheaders) 类，获取后，可通过调用 [HttpHeaders](http_package_classes.md#class-httpheaders) 实例成员函数，修改该请求的 headers。

类型：[HttpHeaders](http_package_classes.md#class-httpheaders)

### prop request

```cangjie
public prop request: Option<HttpRequest>
```

功能：获取该响应对应的请求，默认为 None。

类型：Option\<[HttpRequest](http_package_classes.md#class-httprequest)>

### prop status

```cangjie
public prop status: UInt16
```

功能：获取响应的状态码，默认值为 200。状态码由 100~599 的三位数字组成，状态码所反映的具体信息可参考 [RFC 9110](https://httpwg.org/specs/rfc9110.html#status.codes)。

类型：UInt16

### prop trailers

```cangjie
public prop trailers: HttpHeaders
```

功能：获取 trailers，trailers 详述见 [HttpHeaders](http_package_classes.md#class-httpheaders) 类，获取后，可通过调用 [HttpHeaders](http_package_classes.md#class-httpheaders) 实例成员函数，修改该请求的 trailers。

类型：[HttpHeaders](http_package_classes.md#class-httpheaders)

### prop version

```cangjie
public prop version: Protocol
```

功能：获取响应的协议版本，默认值为 [HTTP1_1](./http_package_enums.md#enum-protocol)。

类型：[Protocol](http_package_enums.md#enum-protocol)

### func close()

```cangjie
public func close(): Unit
```

功能：如果用户不再需要未读完的 body 数据，可以调用此接口关闭连接以释放资源。如果是 HTTP/2 协议，会发送一个 Reset 帧关闭对应的流。

> **注意：**
>
> 如果使用者已读完 body，无需调用此接口再释放资源。

### func toString()

```cangjie
public override func toString(): String
```

功能：把响应转换为字符串，包括 status-line，headers，body size， trailers。

例如：HTTP/1.1 200 OK\r\ncontent-length: 5\r\n\r\nbody size: 5\r\nbar: foo\r\n。

返回值：

- String - 响应的字符串表示。

### extend HttpResponse

```cangjie
extend HttpResponse
```

功能：为 HttpResonse 扩展 HTTP/2.0 特有的方法。

#### func getPush()

```cangjie
public func getPush(): Option<ArrayList<HttpResponse>>
```

功能：获取服务器推送的响应，返回 None 代表未开启服务器推送功能，返回空 ArrayList 代表无服务器推送的响应。

返回值：

- Option\<ArrayList\<[HttpResponse](http_package_classes.md#class-httpresponse)>> - 服务器推送的响应列表。