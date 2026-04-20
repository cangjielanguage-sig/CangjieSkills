## struct X509CertificateInfo

```cangjie
public struct X509CertificateInfo {
    public var serialNumber: SerialNumber
    public var notBefore: DateTime
    public var notAfter: DateTime
    public var subject: ?X509Name
    public var dnsNames: Array<String>
    public var emailAddresses: Array<String>
    public var IPAddresses: Array<IP>
    public var keyUsage: ?KeyUsage
    public var extKeyUsage: ?ExtKeyUsage

    public init(
        serialNumber!: ?SerialNumber = None,
        notBefore!: ?DateTime = None,
        notAfter!: ?DateTime = None,
        subject!: ?X509Name = None,
        dnsNames!: Array<String> = Array<String>(),
        emailAddresses!: Array<String> = Array<String>(),
        IPAddresses!: Array<IP> = Array<IP>(),
        keyUsage!: ?KeyUsage = None,
        extKeyUsage!: ?ExtKeyUsage = None
    )
}
```

功能：[X509CertificateInfo](x509_package_structs.md#struct-x509certificateinfo) 结构包含了证书信息，包括证书序列号、有效期、实体可辨识名称、域名、email 地址、[IP](x509_package_type.md#type-ip) 地址、密钥用法和扩展密钥用法。

### var IPAddresses

```cangjie
public var IPAddresses: Array<IP>
```

功能：记录证书的 [IP](x509_package_type.md#type-ip) 地址。

类型：Array\<[IP](./x509_package_type.md#type-ip)>

### var dnsNames

```cangjie
public var dnsNames: Array<String>
```

功能：记录证书的 DNS 域名。

类型：Array\<String>

### var emailAddresses

```cangjie
public var emailAddresses: Array<String>
```

功能：记录证书的 email 地址。

类型：Array\<String>

### var extKeyUsage

```cangjie
public var extKeyUsage: ?ExtKeyUsage
```

功能：记录证书的扩展密钥用法。

类型：?[ExtKeyUsage](./x509_package_structs.md#struct-extkeyusage)

### var keyUsage

```cangjie
public var keyUsage: ?KeyUsage
```

功能：记录证书的密钥用法。

类型：?[KeyUsage](./x509_package_structs.md#struct-keyusage)

### var notAfter

```cangjie
public var notAfter: DateTime
```

功能：记录证书有效期的结束日期。

类型：DateTime

### var notBefore

```cangjie
public var notBefore: DateTime
```

功能：记录证书有效期的起始日期。

类型：DateTime

### var serialNumber

```cangjie
public var serialNumber: SerialNumber
```

功能：记录证书的序列号。

类型：[SerialNumber](x509_package_structs.md#struct-serialnumber)

### var subject

```cangjie
public var subject: ?X509Name
```

功能：记录证书实体可辨识名称。

类型：?[X509Name](x509_package_classes.md#class-x509name)