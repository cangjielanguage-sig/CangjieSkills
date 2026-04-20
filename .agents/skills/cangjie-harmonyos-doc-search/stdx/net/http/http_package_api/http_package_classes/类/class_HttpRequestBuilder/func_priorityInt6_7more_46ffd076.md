### func priority(Int64, Bool)

```cangjie
public func priority(urg: Int64, inc: Bool): HttpRequestBuilder
```

功能：设置 priority 头的便捷函数，调用此函数后，将生成 priority 头，形如："priority: urgency=x, i"。如果通过设置请求头的函数设置了 priority 字段，调用此函数无效。如果多次调用此函数，以最后一次为准。

参数：

- urg: Int64 - 表示请求优先级，取值范围为 [0, 7]，0 表示最高优先级。
- inc: Bool - 表示请求是否需要增量处理，为 true 表示希望服务器并发处理与之同 urg 同 inc 的请求，为 false 表示不希望服务器并发处理。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

异常：

- [HttpException](./http_package_exceptions.md#class-httpexception) - 当参数 urg 取值非法，即不在 [0, 7] 范围内时，抛出异常。

### func put()

```cangjie
public func put(): HttpRequestBuilder
```

功能：构造 method 为 "PUT" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func readTimeout(Duration)

```cangjie
public func readTimeout(timeout: Duration): HttpRequestBuilder
```

功能：设置此请求的读超时时间。如果传入的 Duration 为负，则会自动转为 0。如果用户设置了此读超时时间，那么该请求的读超时以此为准；如果用户没有设置，那么该请求的读超时以 [Client](http_package_classes.md#class-client) 为准。

参数：

- timeout: Duration - 用户设置的此请求的读超时时间。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func setHeaders(HttpHeaders)

```cangjie
public func setHeaders(headers: HttpHeaders): HttpRequestBuilder
```

功能：设置请求 header，如果已经设置过，调用该函数将替换原 header。

参数：

- headers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 header 对象。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func setTrailers(HttpHeaders)

```cangjie
public func setTrailers(trailers: HttpHeaders): HttpRequestBuilder
```

功能：设置请求 trailer，如果已经设置过，调用该函数将替换原 trailer。

参数：

- trailers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 trailer 对象。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func trace()

```cangjie
public func trace(): HttpRequestBuilder
```

功能：构造 method 为 "TRACE" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func trailer(String, String)

```cangjie
public func trailer(name: String, value: String): HttpRequestBuilder
```

功能：向请求 trailer 添加指定键值对，规则同 [HttpHeaders](http_package_classes.md#class-httpheaders) 类的 add 函数。

参数：

- name: String - 请求头的 key。
- value: String - 请求头的 value。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果传入的 name 或 value 包含不合法元素，将抛出此异常。