### func build()

```cangjie
public func build(): HttpRequest
```

功能：根据 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例生成一个 [HttpRequest](http_package_classes.md#class-httprequest) 实例。

返回值：

- [HttpRequest](http_package_classes.md#class-httprequest) - 根据当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例构造出来的 [HttpRequest](http_package_classes.md#class-httprequest) 实例。

### func connect()

```cangjie
public func connect(): HttpRequestBuilder
```

功能：构造 method 为 "CONNECT" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func delete()

```cangjie
public func delete(): HttpRequestBuilder
```

功能：构造 method 为 "DELETE" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func get()

```cangjie
public func get(): HttpRequestBuilder
```

功能：构造 method 为 "GET" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func head()

```cangjie
public func head(): HttpRequestBuilder
```

功能：构造 method 为 "HEAD" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func header(String, String)

```cangjie
public func header(name: String, value: String): HttpRequestBuilder
```

功能：向请求 header 添加指定键值对，规则同 [HttpHeaders](http_package_classes.md#class-httpheaders) 类的 add 函数。

参数：

- name: String - 请求头的 key。
- value: String - 请求头的 value。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果传入的 name 或 value 包含不合法元素，将抛出此异常。

### func method(String)

```cangjie
public func method(method: String): HttpRequestBuilder
```

功能：设置请求 method，默认请求 method 为 "GET"。

参数：

- method: String - 请求方法，必须由 token 字符组成，如果传入空字符串，method 值将自动设置为 "GET"。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 参数 method 非法时抛出此异常。

### func options()

```cangjie
public func options(): HttpRequestBuilder
```

功能：构造 method 为 "OPTIONS" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。

### func post()

```cangjie
public func post(): HttpRequestBuilder
```

功能：构造 method 为 "POST" 的请求的便捷函数。

返回值：

- [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) - 当前 [HttpRequestBuilder](http_package_classes.md#class-httprequestbuilder) 实例的引用。