### static func mergePaths(String, String)

```cangjie
public static func mergePaths(basePath: String, refPath: String): String
```

功能：合并两个路径。

合并规则：将引用路径 refPath 追加到基础路径 basePath 的最后一段。如果 refPath 是绝对路径，结果就是 refPath 原本的值。如果 refPath 不是绝对路径，则将自身拼接至 basePath 最后一个 `/` 后，所有结果最终都会进行标准化（路径中的`.`字符，`..`字符，以及多个连续的 `/` 字符都会被优化）。具体行为可以参照下面示例。更详细行为参考 RFC 3986 协议。

如需合并 URL 请使用 [resolveURL](#func-resolveurlurl)。

例如：

- `/a/b/c` 合并 `/d` 输出 `/d`。
- `/a/b/c` 合并 `d` 输出 `/a/b/d`。
- `/a/b/` 合并 `d/e/../f` 输出 `/a/b/d/f`。
- `/a/b/c/` 合并 `./../../g` 输出 `/a/g`。

参数：

- basePath: String - 基础路径。
- refPath: String - 引用路径。

返回值：

- String - 合并且标准化后的路径。

### static func parse(String)

```cangjie
public static func parse(rawUrl: String): URL
```

功能：将原始 URL 字符串解析成 [URL](url_package_classes.md#class-url) 对象。

这个函数会将 [URL](url_package_classes.md#class-url) 按照组件分解，然后分别进行解码并存储在相应的组件属性中，而 rawXXX (此处泛指前缀是 raw 的 URL 属性)属性部分存储的是原始值，不做编解码处理。

使用示例请参见[URL 解析函数 parse 的使用](./../url_samples/url_parse.md)。

> **注意：**
>
> 该函数可以解析 URL 中的用户名和密码（如果存在），这是符合 RFC 3986 协议的解析功能的，但是 RFC 3986 也明确指出，任何场景下，明文保存用户信息存在被泄露风险，所以建议不要在 URL 中明文保存用户信息。

参数：

- rawUrl: String - [URL](url_package_classes.md#class-url) 字符串。

返回值：

- [URL](url_package_classes.md#class-url) - 解析字符串得到的 [URL](url_package_classes.md#class-url) 实例。

异常：

- [UrlSyntaxException](url_package_exceptions.md#class-urlsyntaxexception) - 当 [URL](url_package_classes.md#class-url) 字符串中包含非法字符时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 `UTF-8` 的字节序列规则时，抛出异常。

### func isAbsoluteURL()

```cangjie
public func isAbsoluteURL(): Bool
```

功能：判断 [URL](url_package_classes.md#class-url) 是否为绝对 [URL](url_package_classes.md#class-url)（scheme 存在时，[URL](url_package_classes.md#class-url) 是绝对 [URL](url_package_classes.md#class-url)）。

返回值：

- Bool - scheme 存在时返回 true，不存在时返回 false。

### func replace(Option\<String>, Option\<String>, Option\<String>, Option\<String>, Option\<String>, Option\<String>, Option\<String>)

```cangjie
public func replace(scheme!: Option<String> = None, userInfo!: Option<String> = None,
 hostName!: Option<String> = None, port!: Option<String> = None, path!: Option<String> = None, 
 query!: Option<String> = None, fragment!: Option<String> = None): URL
```

功能：替换 [URL](url_package_classes.md#class-url) 对象的各组件，并且返回一个新的 [URL](url_package_classes.md#class-url) 对象。

替换时需要满足以下要求：

- 方案 scheme 为空时，主机名必须为空。
- 主机名为空时，用户信息或端口号必须为空。
- 方案 scheme 不为空时，主机名和路径不能同时为空。
- 方案 scheme 不为空时，路径必须是绝对路径。
- 任意组件均为合法字符。

参数：

- scheme!: Option\<String> - 协议组件。
- userInfo!: Option\<String> - 用户信息。
- hostName!: Option\<String> - 主机名。
- port!: Option\<String> - 端口号。
- path!: Option\<String> - 资源路径。
- query!: Option\<String> - 查询组件。
- fragment!: Option\<String> - 锚点组件。

返回值：

- [URL](url_package_classes.md#class-url) - 新的 [URL](url_package_classes.md#class-url) 对象。

异常：

- [UrlSyntaxException](url_package_exceptions.md#class-urlsyntaxexception) - 不满足替换要求时，抛出异常。