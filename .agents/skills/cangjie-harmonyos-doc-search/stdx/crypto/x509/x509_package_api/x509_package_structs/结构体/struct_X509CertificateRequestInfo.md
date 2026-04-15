## struct X509CertificateRequestInfo

```cangjie
public struct X509CertificateRequestInfo {
    public var subject: ?X509Name
    public var dnsNames: Array<String>
    public var emailAddresses: Array<String>
    public var IPAddresses: Array<IP>

    public init(
        subject!: ?X509Name = None,
        dnsNames!: Array<String> = Array<String>(),
        emailAddresses!: Array<String> = Array<String>(),
        IPAddresses!: Array<IP> = Array<IP>()
    )
}
```

功能：[X509CertificateRequestInfo](x509_package_structs.md#struct-x509certificaterequestinfo) 结构包含了证书请求信息，包括证书实体可辨识名称、域名、email 地址和 [IP](x509_package_type.md#type-ip) 地址。

### var IPAddresses

```cangjie
public var IPAddresses: Array<IP>
```

功能：记录证书签名请求的 [IP](x509_package_type.md#type-ip) 地址。

类型：Array\<[IP](./x509_package_type.md#type-ip)>

### var dnsNames

```cangjie
public var dnsNames: Array<String>
```

功能：记录证书签名请求的 DNS 域名。

类型：Array\<String>

### var emailAddresses

```cangjie
public var emailAddresses: Array<String>
```

功能：记录证书签名请求的 email 地址。

类型：Array\<String>

### var subject

```cangjie
public var subject: ?X509Name
```

功能：记录证书签名请求的实体可辨识名称。

### init(?X509Name, Array\<String>, Array\<String>, Array\<IP>)

```cangjie
public init(
    subject!: ?X509Name = None,
    dnsNames!: Array<String> = Array<String>(),
    emailAddresses!: Array<String> = Array<String>(),
    IPAddresses!: Array<IP> = Array<IP>()
)
```

功能：构造 [X509CertificateRequestInfo](x509_package_structs.md#struct-x509certificaterequestinfo) 对象。

参数：

- subject!: ?[X509Name](x509_package_classes.md#class-x509name) - 数字证书的使用者信息，默认值为 None。
- dnsNames!: Array\<String> - 域名列表，需要用户保证输入域名的有效性，默认值为空的字符串数组。
- emailAddresses!: Array\<String> - email 地址列表，需要用户保证输入 email 的有效性，默认值为空的字符串数组。
- IPAddresses!: Array\<[IP](x509_package_type.md#type-ip)> - [IP](x509_package_type.md#type-ip) 地址列表，默认值为空的 [IP](x509_package_type.md#type-ip) 数组。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 输入的 [IP](x509_package_type.md#type-ip) 地址列表中包含无效的 [IP](x509_package_type.md#type-ip) 地址，则抛出异常。