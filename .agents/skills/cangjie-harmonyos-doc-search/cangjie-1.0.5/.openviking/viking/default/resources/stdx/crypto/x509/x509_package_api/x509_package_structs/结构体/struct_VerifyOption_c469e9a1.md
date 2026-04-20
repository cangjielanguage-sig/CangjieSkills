## struct VerifyOption

```cangjie
public struct VerifyOption {
    public var time: DateTime = DateTime.now()
    public var dnsName: String = ""
    public var roots: Array<X509Certificate> = X509Certificate.systemRootCerts()
    public var intermediates: Array<X509Certificate> = Array<X509Certificate>()
}
```

功能：用于为 `x509` 证书验证函数 [verify](./x509_package_classes.md#func-verifyverifyoption) 提供配置选项。

### var dnsName

```cangjie
public var dnsName: String = ""
```

功能：校验域名，默认为空，只有设置域名时才会进行此处校验。

类型：String

### var intermediates

```cangjie
public var intermediates: Array<X509Certificate> = Array<X509Certificate>()
```

功能：中间证书链，默认为空。

类型：Array\<[X509Certificate](x509_package_classes.md#class-x509certificate)>

### var roots

```cangjie
public var roots: Array<X509Certificate> = X509Certificate.systemRootCerts()
```

功能：根证书链，默认为系统根证书链。

类型：Array\<[X509Certificate](x509_package_classes.md#class-x509certificate)>

### var time

```cangjie
public var time: DateTime = DateTime.now()
```

功能：校验时间，默认为创建选项的时间。

类型：DateTime