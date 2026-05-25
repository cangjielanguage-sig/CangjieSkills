### init(String, String, ?DateTime, ?Int64, String, String, Bool, Bool)

```cangjie
public init(name: String, value: String, expires!: ?DateTime = None, maxAge!: ?Int64 = None,
    domain!: String = "", path!: String = "", secure!: Bool = false, httpOnly!: Bool = false)
```

功能：[Cookie](http_package_classes.md#class-cookie) 构造器。该构造器会检查传入的各项属性是否满足协议要求，如果不满足则会产生 IllegalArgumentException。具体要求见 [RFC 6265 4.1.1.](https://httpwg.org/specs/rfc6265.html#sane-set-cookie-syntax)。

> **注意：**
>
> [Cookie](http_package_classes.md#class-cookie) 各属性中只有 cookie-name，cookie-value 是必需的，必须传入 name，value 参数，但 value 参数可以传入空字符串。

参数：

- name: String - cookie-name 属性。

    ```cangjie
    name         = token
    token        = 1*tchar
    tchar        = "!" / "#" / "$" / "%" / "&" / "'" / "*"
                   / "+" / "-" / "." / "^" / "_" / "`" / "|" / "~"
                   / DIGIT / ALPHA
    ```

- value: String - cookie-value 属性。

    ```cangjie
    value        = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE )
    cookie-octet = %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E
                ; US-ASCII characters excluding CTLs,
                ; whitespace DQUOTE, comma, semicolon,
                ; and backslash
    ```

- expires!: ?DateTime - 设置 [Cookie](http_package_classes.md#class-cookie) 的过期时间，默认为 None，时间必须在 1601 年之后。
- maxAge!: ?Int64 - [Cookie](http_package_classes.md#class-cookie) 的最大生命周期，默认为 None，如果 [Cookie](http_package_classes.md#class-cookie) 既有 expires 属性，也有 maxAge，则表示该 [Cookie](http_package_classes.md#class-cookie) 只维护到会话结束（维护到 [Client](http_package_classes.md#class-client) 关闭之前，[Client](http_package_classes.md#class-client) 关闭之后设置了过期的 [Cookie](http_package_classes.md#class-cookie) 也不再维护）。

    ```cangjie
    max-age-av     = "Max-Age=" non-zero-digit *DIGIT
    non-zero-digit = %x31-39
                    ; digits 1 through 9
    DIGIT          = %x30-39
                    ; digits 0 through 9
    ```

- domain!: String - 默认为空字符串，表示该收到该 [Cookie](http_package_classes.md#class-cookie) 的客户端只会发送该 [Cookie](http_package_classes.md#class-cookie) 给原始服务器。如果设置了合法的 domain，则收到该 [Cookie](http_package_classes.md#class-cookie) 的客户端只会发送该 [Cookie](http_package_classes.md#class-cookie) 给所有该 domain 的子域（且满足其他属性条件要求才会发）。

    ```cangjie
    domain          = <subdomain> | " "
    <subdomain>   ::= <label> | <subdomain> "." <label>
    <label>       ::= <letter> [ [ <ldh-str> ] <let-dig> ]
    <ldh-str>     ::= <let-dig-hyp> | <let-dig-hyp> <ldh-str>
    <let-dig-hyp> ::= <let-dig> | "-"
    <let-dig>     ::= <letter> | <digit>
    <letter>      ::= any one of the 52 alphabetic characters A through Z in upper case and a through z in lower case
    <digit>       ::= any one of the ten digits 0 through 9
    RFC 1035 2.3.1.
    而 RFC 1123 2.1. 放松了对 label 首字符必须是 letter 的限制
    因此，对 domain 的要求为：
    1、总长度小于等于 255，由若干个 label 组成
    2、label 与 label 之间通过 "." 分隔，每个 label 长度小于等于 63
    3、label 的开头和结尾必须是数字或者字母，label 的中间字符必须是数字、字母或者 "-"
    ```

- path!: String - 默认为空字符串，客户端会根据 url 计算出默认的 path 属性，见 RFC 6265 5.1.4.。 收到该 [Cookie](http_package_classes.md#class-cookie) 的客户端只会发送该 [Cookie](http_package_classes.md#class-cookie) 给所有该 path 的子目录（且满足其他属性条件要求才会发）。

    ```cangjie
    path            = <any RUNE except CTLs or ";">
    RUNE            = <any [USASCII] character>
    CTLs            = <controls>
    ```

- secure!: Bool - 默认为 false，如果设置为 true，该 [Cookie](http_package_classes.md#class-cookie) 只会在安全协议请求中发送。
- httpOnly!: Bool - 默认为 false，如果设置为 true，该 [Cookie](http_package_classes.md#class-cookie) 只会在 HTTP 协议请求中发送。

异常：