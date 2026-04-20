## class Cookie

```cangjie
public class Cookie {
    public init(name: String, value: String, expires!: ?DateTime = None, maxAge!: ?Int64 = None,
        domain!: String = "", path!: String = "", secure!: Bool = false, httpOnly!: Bool = false)
}
```

功能：HTTP 本身是无状态的，server 为了知道 client 的状态，提供个性化的服务，便可以通过 [Cookie](http_package_classes.md#class-cookie) 来维护一个有状态的会话。

> **说明：**
>
> - 用户首次访问某站点时，server 通过 `Set-Cookie` header 将 name/value 对，以及 attribute-value 传给用户代理；用户代理随后对该站点的请求中便可以将 name/value 加入到 Cookie header 中；
> - [Cookie](http_package_classes.md#class-cookie) 类提供了构建 [Cookie](http_package_classes.md#class-cookie) 对象，并将 [Cookie](http_package_classes.md#class-cookie) 对象转成 `Set-Cookie` header 值的函数，提供了获取 [Cookie](http_package_classes.md#class-cookie) 对象各属性值的函数；
> - [Cookie](http_package_classes.md#class-cookie) 的各个属性的要求和作用见 [RFC 6265](https://httpwg.org/specs/rfc6265.html)；
> - 下文中 cookie-name，cookie-value，expires-av 等名字采用 [RFC 6265](https://httpwg.org/specs/rfc6265.html) 中的术语，详情请见协议。

### prop cookieName

```cangjie
public prop cookieName: String
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 cookie-name 值。

类型：String

### prop cookieValue

```cangjie
public prop cookieValue: String
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 cookie-value 值。

类型：String

### prop domain

```cangjie
public prop domain: String
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 domain-av 值。

类型：String

### prop expires

```cangjie
public prop expires: ?DateTime
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 expires-av 值。

类型：?DateTime

### prop httpOnly

```cangjie
public prop httpOnly: Bool
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 httpOnly-av 值。

类型：Bool

### prop maxAge

```cangjie
public prop maxAge: ?Int64
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 max-age-av 值。

类型：?Int64

### prop others

```cangjie
public prop others: ArrayList<String>
```

功能：获取未被解析的属性。

类型：ArrayList\<String>

### prop path

```cangjie
public prop path: String
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 path-av 值。

类型：String

### prop secure

```cangjie
public prop secure: Bool
```

功能：获取 [Cookie](http_package_classes.md#class-cookie) 对象的 secure-av 值。

类型：Bool