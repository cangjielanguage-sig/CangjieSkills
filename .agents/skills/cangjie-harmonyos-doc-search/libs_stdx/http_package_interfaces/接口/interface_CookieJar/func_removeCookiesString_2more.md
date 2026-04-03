### func removeCookies(String)

```cangjie
func removeCookies(domain: String): Unit
```

功能：从 [CookieJar](http_package_interfaces.md#interface-cookiejar) 中移除某个 domain 的 [Cookie](http_package_classes.md#class-cookie)。

> **说明：**
>
> 默认实现 CookieJarImpl 的移除某个 domain 的 [Cookie](http_package_classes.md#class-cookie) 只会移除特定 domain 的 [Cookie](http_package_classes.md#class-cookie)，domain 的 subdomain 的 [Cookie](http_package_classes.md#class-cookie) 并不会移除。

参数：

- domain: String - 所要移除 [Cookie](http_package_classes.md#class-cookie) 的域名。

异常：

- IllegalArgumentException - 如果传入的 domain 为空字符串或者非法，则抛出该异常，合法的 domain 规则见 [Cookie](http_package_classes.md#class-cookie) 的参数文档。

### func storeCookies(URL, ArrayList\<Cookie>)

```cangjie
func storeCookies(url: URL, cookies: ArrayList<Cookie>): Unit
```

功能：将 ArrayList\<[Cookie](http_package_classes.md#class-cookie)> 存进 [CookieJar](http_package_interfaces.md#interface-cookiejar)。

如果往 [CookieJar](http_package_interfaces.md#interface-cookiejar) 中存 [Cookie](http_package_classes.md#class-cookie) 时超过了上限（3000 条），那么至少清除 [CookieJar](http_package_interfaces.md#interface-cookiejar) 中 1000 条 [Cookie](http_package_classes.md#class-cookie) 再往里存储。清除 [CookieJar](http_package_interfaces.md#interface-cookiejar) 中 [Cookie](http_package_classes.md#class-cookie) 的优先级见 [RFC 6265 5.3.12.](https://httpwg.org/specs/rfc6265.html#storage-model)。

[Cookie](http_package_classes.md#class-cookie) 按如下顺序清除：

- 过期的 [Cookie](http_package_classes.md#class-cookie)；
- 相同 domain 中超过 50 条以上的部分；
- 所有 [Cookie](http_package_classes.md#class-cookie) 具有相同优先级的 [Cookie](http_package_classes.md#class-cookie) 则优先删除 `last-access` 属性更早的。

参数：

- url: [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) - 产生该 [Cookie](http_package_classes.md#class-cookie) 的 url。
- cookies: ArrayList\<[Cookie](http_package_classes.md#class-cookie)> - 需要存储的 ArrayList\<[Cookie](http_package_classes.md#class-cookie)>。