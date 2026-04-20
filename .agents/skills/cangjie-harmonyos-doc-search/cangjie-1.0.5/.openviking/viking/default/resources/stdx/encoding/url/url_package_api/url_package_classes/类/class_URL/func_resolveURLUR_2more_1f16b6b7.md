### func resolveURL(URL)

```cangjie
public func resolveURL(ref: URL): URL
```

功能：以当前 [URL](url_package_classes.md#class-url) 实例为基础 [URL](url_package_classes.md#class-url)，以传入的 [URL](url_package_classes.md#class-url) 为参考 [URL](url_package_classes.md#class-url)，根据 RFC 3986 协议生成一个新的 [URL](url_package_classes.md#class-url) 实例。

例如：<http://a/b/c/d;p?q> 为基础 [URL](url_package_classes.md#class-url)，以下 = 左边为参考 [URL](url_package_classes.md#class-url)，右边为生成的新 [URL](url_package_classes.md#class-url)：

- "g"      =  "<http://a/b/c/g>"
- "/g"     =  "<http://a/g>"
- "g?y"    =  "<http://a/b/c/g?y>"
- "g?y#s"  =  "<http://a/b/c/g?y#s>"
- "../"    =  "<http://a/b/>"

更多详细的 URL 生成规则，请参见 RFC 3968 协议。

参数：

- ref: [URL](url_package_classes.md#class-url) - 参考 [URL](url_package_classes.md#class-url) 对象。

返回值：

- [URL](url_package_classes.md#class-url) - 新的 [URL](url_package_classes.md#class-url) 实例。

### func toString()

```cangjie
public func toString(): String
```

功能：获取当前 [URL](url_package_classes.md#class-url) 实例的字符串值。

会把 hostName 编码，其余部分取 rawXXX (此处泛指前缀是 raw 的 URL 属性)属性值，按照 URL 组件构成顺序进行拼接而获得该函数返回值。

返回值：

- String - 当前 [URL](url_package_classes.md#class-url) 实例的字符串值。