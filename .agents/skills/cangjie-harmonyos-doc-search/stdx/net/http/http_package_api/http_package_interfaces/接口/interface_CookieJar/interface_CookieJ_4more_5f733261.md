## interface CookieJar

```cangjie
public interface CookieJar {
    prop isHttp: Bool
    prop rejectPublicSuffixes: ArrayList<String>
    static func createDefaultCookieJar(rejectPublicSuffixes: ArrayList<String>, isHttp: Bool): CookieJar
    static func parseSetCookieHeader(response: HttpResponse): ArrayList<Cookie>
    static func toCookieString(cookies: ArrayList<Cookie>): String
    func clear(): Unit
    func getCookies(url: URL): ArrayList<Cookie>
    func removeCookies(domain: String): Unit
    func storeCookies(url: URL, cookies: ArrayList<Cookie>): Unit
}
```

功能：[CookieJar](http_package_interfaces.md#interface-cookiejar) 是 [Client](http_package_classes.md#class-client) 用来管理 [Cookie](http_package_classes.md#class-cookie) 的工具。

其有两个静态函数：

- [toCookieString](#static-func-tocookiestringarraylistcookie) 用于将 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 转成字符串以便设置请求的 [Cookie](http_package_classes.md#class-cookie) header。
- [parseSetCookieHeader](#static-func-parsesetcookieheaderhttpresponse) 用于解析收到 response 中的 `Set-Cookie` header。

如果 [Client](http_package_classes.md#class-client) 配置了 [CookieJar](http_package_interfaces.md#interface-cookiejar)，那么 [Cookie](http_package_classes.md#class-cookie) 的解析收发都是自动的。

> **说明**
>
> - 用户可以实现自己的 [CookieJar](http_package_interfaces.md#interface-cookiejar)，实现自己的管理逻辑。
> - [CookieJar](http_package_interfaces.md#interface-cookiejar) 的管理要求见 [RFC 6265](https://httpwg.org/specs/rfc6265.html)。

### prop isHttp

```cangjie
prop isHttp: Bool
```

功能：该 [CookieJar](http_package_interfaces.md#interface-cookiejar) 是否用于 HTTP 协议。

- 若 isHttp 为 true， 则只会存储来自于 HTTP 协议的 [Cookie](http_package_classes.md#class-cookie)。
- 若 isHttp 为 false， 则只会存储来自非 HTTP 协议的 [Cookie](http_package_classes.md#class-cookie)，且不会存储发送设置了 httpOnly 的 [Cookie](http_package_classes.md#class-cookie)。

类型：Bool

### prop rejectPublicSuffixes

```cangjie
prop rejectPublicSuffixes: ArrayList<String>
```

功能：获取 [public suffixes](https://publicsuffix.org/) 配置，该配置是一个 domain 黑名单，会拒绝 domain 值为 public suffixes 的 [Cookie](http_package_classes.md#class-cookie)。

> **说明：**
>
> 如果该 [Cookie](http_package_classes.md#class-cookie) 来自于与 domain 相同的 host，黑名单就不会生效。

类型：ArrayList\<String>

### static func createDefaultCookieJar(ArrayList\<String>, Bool)

```cangjie
static func createDefaultCookieJar(rejectPublicSuffixes: ArrayList<String>, isHttp: Bool): CookieJar
```

功能：构建默认的管理 [Cookie](http_package_classes.md#class-cookie) 的 [CookieJar](http_package_interfaces.md#interface-cookiejar) 实例。

默认的 [CookieJar](http_package_interfaces.md#interface-cookiejar) 的管理要求参考 [RFC 6265 5.3.](https://httpwg.org/specs/rfc6265.html#storage-model)。

参数：

- rejectPublicSuffixes: ArrayList\<String> - 用户配置的 public suffixes，[Cookie](http_package_classes.md#class-cookie) 管理为了安全会拒绝 domain 值为 public suffixes 的 cookie（除非该 [Cookie](http_package_classes.md#class-cookie) 来自于与 domain 相同的 host），public suffixes 见 [PUBLIC SUFFIX LIST](https://publicsuffix.org/)。
- isHttp: Bool - 该 [CookieJar](http_package_interfaces.md#interface-cookiejar) 是否用于 HTTP 协议，isHttp 为 true 则只会存储来自于 HTTP 协议的 [Cookie](http_package_classes.md#class-cookie)。

返回值：

- [CookieJar](http_package_interfaces.md#interface-cookiejar) - 默认的 [CookieJar](http_package_interfaces.md#interface-cookiejar) 实例。