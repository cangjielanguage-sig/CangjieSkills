## class HttpRequestBuilder

```cangjie
public class HttpRequestBuilder {
    public init()
    public init(request: HttpRequest)
}
```

功能：[HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 类用于构造 [HttpRequest](http_package_classes.md#class-httprequest) 实例。

### init()

```cangjie
public init()
```

功能：构造一个新 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder)。

### init(HttpRequest)

```cangjie
public init(request: HttpRequest)
```

功能： 通过 request 构造一个具有 request 属性的 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder)。由于 body 成员是一个 InputStream，对原始的 request 的 body 的操作会影响到复制得到的 [HttpRequest](http_package_classes.md#class-httprequest) 的 body。[HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 的 headers 和 trailers 是入参 request 的深拷贝。其余元素都是入参 request 的浅拷贝（因为是不可变对象，无需深拷贝）。

参数：

- request: [HttpRequest](http_package_classes.md#class-httprequest) - 传入的 [HttpRequest](http_package_classes.md#class-httprequest) 对象。

### func addHeaders(HttpHeaders)

```cangjie
public func addHeaders(headers: HttpHeaders): HttpRequestBuilder
```

功能：向请求 header 添加参数 [HttpHeaders](http_package_classes.md#class-httpheaders) 中的键值对。

参数：

- headers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 header 对象。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func addTrailers(HttpHeaders)

```cangjie
public func addTrailers(trailers: HttpHeaders): HttpRequestBuilder
```

功能：向请求 trailer 添加参数 [HttpHeaders](http_package_classes.md#class-httpheaders) 中的键值对。

参数：

- trailers: [HttpHeaders](http_package_classes.md#class-httpheaders) - 传入的 trailer 对象。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func body(Array\<UInt8>)

```cangjie
public func body(body: Array<UInt8>): HttpRequestBuilder
```

功能：设置请求 body。如果已经设置过，调用该函数将替换原 body。

参数：

- body: Array\<UInt8> - 字节数组形式的请求体。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func body(InputStream)

```cangjie
public func body(body: InputStream): HttpRequestBuilder
```

功能：设置请求 body。如果已经设置过，调用该函数将替换原 body。

参数：

- body: InputStream - 流形式的请求体。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func body(String)

```cangjie
public func body(body: String): HttpRequestBuilder
```

功能：设置请求 body，如果已经设置过，调用该函数将替换原 body 调用该函数设置请求 body，则 body 将以内置的 InputStream 实现类表示，其大小已知。

参数：

- body: String - 字符串形式的请求体。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。