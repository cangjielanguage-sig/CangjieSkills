## class HttpResponseBuilder

```cangjie
public class HttpResponseBuilder {
    public init()
}
```

功能：用于构造 [HttpResponse](http_package_classes.md#class-httpresponse) 实例。

### init()

```cangjie
public init()
```

功能：构造一个新 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder)。

### func addHeaders(HttpHeaders)

```cangjie
public func addHeaders(headers: HttpHeaders): HttpResponseBuilder
```

功能：向响应 header 添加参数 [HttpHeaders](http_package_classes.md#class-httpheaders) 中的键值对。

参数：

- headers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 header 对象。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func addTrailers(HttpHeaders)

```cangjie
public func addTrailers(trailers: HttpHeaders): HttpResponseBuilder
```

功能：向响应 trailer 添加参数 [HttpHeaders](http_package_classes.md#class-httpheaders) 中的键值对。

参数：

- trailers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 trailer 对象。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func body(Array\<UInt8>)

```cangjie
public func body(body: Array<UInt8>): HttpResponseBuilder
```

功能：设置响应 body，如果已经设置过，调用该函数将替换原 body。

参数：

- body: Array\<UInt8> - 字节数组形式的响应体。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func body(InputStream)

```cangjie
public func body(body: InputStream): HttpResponseBuilder
```

功能：设置响应 body，如果已经设置过，调用该函数将替换原 body 调用该函数设置请求 body。

参数：

- body: InputStream - 流形式的响应体。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func body(String)

```cangjie
public func body(body: String): HttpResponseBuilder
```

功能：设置响应 body，如果已经设置过，调用该函数将替换原 body 调用该函数设置请求 body。

参数：

- body: String - 字符串形式的响应体。

返回值：

- [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) - 当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例的引用。

### func build()

```cangjie
public func build(): HttpResponse
```

功能：根据 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例生成一个 [HttpResponse](http_package_classes.md#class-httpresponse) 实例。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 根据当前 [HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder) 实例构造出来的 [HttpResponse](http_package_classes.md#class-httpresponse) 实例。