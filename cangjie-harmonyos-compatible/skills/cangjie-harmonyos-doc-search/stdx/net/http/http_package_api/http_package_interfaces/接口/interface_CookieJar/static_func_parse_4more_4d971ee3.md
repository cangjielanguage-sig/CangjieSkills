### static func parseSetCookieHeader(HttpResponse)

```cangjie
static func parseSetCookieHeader(response: HttpResponse): ArrayList<Cookie>
```

功能：解析 response 中的 `Set-Cookie` header。

该函数解析 response 中的 `Set-Cookie` header，并返回解析出的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)>，解析 `Set-Cookie` header 的具体规则见 [RFC 6265 5.2.](https://httpwg.org/specs/rfc6265.html#set-cookie)。

参数：

- response: [HttpResponse](http_package_classes.md#class-httpresponse) - 所需要解析的 response。

返回值：

- ArrayList\<[Cookie](http_package_classes.md#class-cookie)> - 从 response 中解析出的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 数组。

### static func toCookieString(ArrayList\<Cookie>)

```cangjie
static func toCookieString(cookies: ArrayList<Cookie>): String
```

功能：将 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 转成字符串，用于 [Cookie](http_package_classes.md#class-cookie) header。

该函数会将传入的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 数组转成协议规定的 [Cookie](http_package_classes.md#class-cookie) header 的字符串形式，见 [RFC 6265 5.4.4.](https://httpwg.org/specs/rfc6265.html#cookie)。

参数：

- cookies: ArrayList\<[Cookie](http_package_classes.md#class-cookie)> - 所需转成 [Cookie](http_package_classes.md#class-cookie) header 字符串的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)>。

返回值：

- String - 用于 [Cookie](http_package_classes.md#class-cookie) header 的字符串。

### func clear()

```cangjie
func clear(): Unit
```

功能：清除全部 [Cookie](http_package_classes.md#class-cookie)。

默认实现 CookieJarImpl 会清除 [CookieJar](http_package_interfaces.md#interface-cookiejar) 中的所有 [Cookie](http_package_classes.md#class-cookie)。

### func getCookies(URL)

```cangjie
func getCookies(url: URL): ArrayList<Cookie>
```

功能：从 [CookieJar](http_package_interfaces.md#interface-cookiejar) 中取出 ArrayList\<[Cookie](http_package_classes.md#class-cookie)>。

> 默认实现 cookieJarImpl 的取 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 函数的具体要求见 [RFC 6265 5.4.](https://httpwg.org/specs/rfc6265.html#cookie)，对取出的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 调用 toCookieString 可以将取出的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 转成 [Cookie](http_package_classes.md#class-cookie) header 的 value 字符串。

参数：

- url: [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) - 所要取出 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 的 url。

返回值：

- ArrayList\<[Cookie](http_package_classes.md#class-cookie)> - [CookieJar](http_package_interfaces.md#interface-cookiejar) 中存储的对应此 url 的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)>。