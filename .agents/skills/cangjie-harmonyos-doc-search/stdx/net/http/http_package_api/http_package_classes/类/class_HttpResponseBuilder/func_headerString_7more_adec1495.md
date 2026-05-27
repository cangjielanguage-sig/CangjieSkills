### func header(String, String)

```cangjie
public func header(name: String, value: String): HttpResponseBuilder
```

功能：向响应 header 添加指定键值对，规则同 [HttpHeaders](http_package_classes.md#class-httpheaders) 类的 add 函数。

参数：

- name: String - 响应头的 key。
- value: String - 响应头的 value。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果传入的 name 或 value 包含不合法元素，将抛出此异常。

### func request(HttpRequest)

```cangjie
public func request(request: HttpRequest): HttpResponseBuilder
```

功能：设置响应对应的请求。

参数：

- request: [HttpRequest](http_package_classes.md#class-httprequest) - 响应对应的请求。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func setHeaders(HttpHeaders)

```cangjie
public func setHeaders(headers: HttpHeaders): HttpResponseBuilder
```

功能：设置响应 header，如果已经设置过，调用该函数将替换原 header。

参数：

- headers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 header 对象。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func setTrailers(HttpHeaders)

```cangjie
public func setTrailers(trailers: HttpHeaders): HttpResponseBuilder
```

功能：设置响应 trailer，如果已经设置过，调用该函数将替换原 trailer。

参数：

- trailers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 trailer 对象。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func status(UInt16)

```cangjie
public func status(status: UInt16): HttpResponseBuilder
```

功能：设置 http 响应状态码。

参数：

- status: UInt16 - 传入的状态码的值。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果设置响应状态码不在 100~599 这个区间内，则抛出此异常。

### func trailer(String, String)

```cangjie
public func trailer(name: String, value: String): HttpResponseBuilder
```

功能：向响应 trailer 添加指定键值对，规则同 [HttpHeaders](http_package_classes.md#class-httpheaders) 类的 add 函数。

参数：

- name: String - 响应头的 key。
- value: String - 响应头的 value。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果传入的 name 或 value 包含不合法元素，将抛出此异常。

### func version(Protocol)

```cangjie
public func version(version: Protocol): HttpResponseBuilder
```

功能：设置 http 响应协议版本。

参数：

- version: [Protocol](http_package_enums.md#enum-protocol) - 协议版本。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。