### func options(String)

```cangjie
public func options(url: String): HttpResponse
```

功能：请求方法为 OPTIONS 的便捷请求函数。

参数：

- url: String - 请求的 url。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。

### func post(String, Array\<UInt8>)

```cangjie
public func post(url: String, body: Array<UInt8>): HttpResponse
```

功能：请求方法为 POST 的便捷请求函数。

参数：

- url: String - 请求的 url。
- body: Array\<UInt8> - 请求体。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。

### func post(String, InputStream)

```cangjie
public func post(url: String, body: InputStream): HttpResponse
```

功能：请求方法为 POST 的便捷请求函数。

参数：

- url: String - 请求的 url。
- body: InputStream - 请求体。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。

### func post(String, String)

```cangjie
public func post(url: String, body: String): HttpResponse
```

功能：请求方法为 POST 的便捷请求函数。

参数：

- url: String - 请求的 url。
- body: String - 请求体。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。

### func put(String, Array\<UInt8>)

```cangjie
public func put(url: String, body: Array<UInt8>): HttpResponse
```

功能：请求方法为 PUT 的便捷请求函数。

参数：

- url: String - 请求的 url。
- body: Array\<UInt8> - 请求体。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。