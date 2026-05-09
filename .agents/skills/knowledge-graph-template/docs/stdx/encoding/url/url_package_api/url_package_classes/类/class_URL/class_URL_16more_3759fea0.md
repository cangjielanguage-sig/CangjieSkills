## class URL

```cangjie
public class URL <: ToString {
    public init(scheme!: String, hostName!: String, path!: String)
}
```

功能：该类提供解析 [URL](url_package_classes.md#class-url) 的函数以及其他相关函数。

字符串中被百分号`%`编码的内容会被解码，保存在相应的组件之中，而初始值保存在相应的 `raw` 属性之中。[URL](url_package_classes.md#class-url) 中的用户名和密码部分（如果存在的话）也会按照 RFC 3986 协议的说明被解析。

> **注意：**
>
> RFC 3986 明确说明在任何场景下，明文保存用户信息存在被泄露风险，所以建议不要在 URL 中明文保存用户信息。

父类型：

- ToString

### prop fragment

```cangjie
public prop fragment: ?String
```

功能：获取解码后的锚点组件，用字符串表示。

类型：?String

### prop host

```cangjie
public prop host: String
```

功能：获取解码后的主机名和端口部分，用字符串表示。

类型：String

### prop hostName

```cangjie
public prop hostName: String
```

功能：获取解码后的主机名，用字符串表示。

类型：String

### prop opaque

```cangjie
public prop opaque: String
```

功能：获取 [URL](url_package_classes.md#class-url) 中未被解析的部分，用字符串表示。

类型：String

示例：

```cangjie
import stdx.encoding.url.*

main () {
    let url = URL.parse("https:\\\\/example.com/foo/bar") // '\' 不是协议规定的分割符，无法被解析。
    println("url.scheme=${url.scheme}")
    println("url.host=${url.host}")
    println("url.opaque=${url.opaque}")
}
```

运行结果：

```text
url.scheme=https
url.host=
url.opaque=\\/example.com/foo/bar
```

### prop path

```cangjie
public prop path: String
```

功能：获取解码后的路径，用字符串表示。

类型：String

### prop port

```cangjie
public prop port: String
```

功能：获取端口号，用字符串表示，空字符串表示无端口号。

类型：String

### prop query

```cangjie
public prop query: ?String
```

功能：获取解码后的查询组件，用字符串表示。

类型：?String

### prop queryForm

```cangjie
public prop queryForm: Form
```

功能：获取解码后的查询组件，用 [Form](url_package_classes.md#class-form) 实例表示。

类型：[Form](url_package_classes.md#class-form)

### prop rawFragment

```cangjie
public prop rawFragment: ?String
```

功能：获取解码前的锚点组件，用字符串表示。

类型：?String

### prop rawPath

```cangjie
public prop rawPath: String
```

功能：获取解码前的路径，用字符串表示。

类型：String

### prop rawQuery

```cangjie
public prop rawQuery: ?String
```

功能：获取解码前的查询组件，用字符串表示。

类型：?String

### prop rawUserInfo

```cangjie
public prop rawUserInfo: UserInfo
```

功能：获取解码前的用户名和密码信息，用 [UserInfo](url_package_classes.md#class-userinfo) 实例表示。

类型：[UserInfo](url_package_classes.md#class-userinfo)

### prop scheme

```cangjie
public prop scheme: String
```

功能：获取 [URL](url_package_classes.md#class-url) 中协议部分，用字符串表示。

类型：String

### prop userInfo

```cangjie
public prop userInfo: UserInfo
```

功能：获取解码后的用户名和密码信息，用 [UserInfo](url_package_classes.md#class-userinfo) 实例表示。

类型：[UserInfo](url_package_classes.md#class-userinfo)

### init(String, String, String)

```cangjie
public init(scheme!: String, hostName!: String, path!: String)
```

功能：构造一个 [URL](url_package_classes.md#class-url) 实例。

构造实例时需要满足要求：

- 拥有主机名 hostName 时，需要有协议 scheme。
- 不能只存在协议 scheme。
- 存在协议和路径的情况下，路径 path 必须是绝对路径。

参数：

- scheme!: String - 协议类型。
- hostName!: String - 不包含端口号的主机名。
- path!: String - 请求资源的路径。

异常：

- [UrlSyntaxException](url_package_exceptions.md#class-urlsyntaxexception) - 当构造实例不满足要求时，抛出异常。