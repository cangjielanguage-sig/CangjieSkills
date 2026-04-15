### func url(String)

```cangjie
public func url(rawUrl: String): HttpRequestBuilder
```

功能：设置请求 url，默认 url 为空的 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 对象。

参数：

- rawUrl: String - 待解析成 url 对象的字符串，该字符串格式详见 [URL.parse](../../../encoding/url/url_package_api/url_package_classes.md#static-func-parsestring) 函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

异常：

- IllegalArgumentException - 当被编码的字符不符合 UTF8 的字节序列规则时，抛出异常。
- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当传入字符串不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 格式时，抛出异常。

### func url(URL)

```cangjie
public func url(url: URL): HttpRequestBuilder
```

功能：设置请求 url，默认 url 为空的 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 对象，即 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url).parse("")。

参数：

- url: [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) - URL 对象。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func version(Protocol)

```cangjie
public func version(version: Protocol): HttpRequestBuilder
```

功能：设置请求的 http 协议版本，默认为 UnknownProtocol("")，客户端会根据 tls 配置自动选择协议。

参数：

- version: [Protocol](http_package_enums.md#enum-protocol) - 协议版本。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func writeTimeout(Duration)

```cangjie
public func writeTimeout(timeout: Duration): HttpRequestBuilder
```

功能：设置此请求的写超时时间。如果传入的 Duration 为负，则会自动转为 0。如果用户设置了此写超时时间，那么该请求的写超时以此为准；如果用户没有设置，那么该请求的写超时以 [Client](http_package_classes.md#class-client) 为准。

参数：

- timeout: Duration - 用户设置的此请求的写超时时间。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。