### init(?SerialNumber, ?DateTime, ?DateTime, ?X509Name, Array\<String>, Array\<String>, Array\<IP>, ?KeyUsage, ?ExtKeyUsage)

```cangjie
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
```

功能：构造 [X509CertificateInfo](x509_package_structs.md#struct-x509certificateinfo) 对象。

参数：

- serialNumber!: ?[SerialNumber](x509_package_structs.md#struct-serialnumber) - 数字证书序列号，默认值为 None，使用默认值时默认的序列号长度为 128 比特。
- notBefore!: ?DateTime - 数字证书有效期开始时间，默认值为 None，使用默认值时默认的时间为 [X509CertificateInfo](x509_package_structs.md#struct-x509certificateinfo) 创建的时间。
- notAfter!: ?DateTime - 数字证书有效期截止时间，默认值为 None，使用默认值时默认的时间为 notBefore 往后 1 年的时间。
- subject!: ?[X509Name](x509_package_classes.md#class-x509name) - 数字证书使用者信息，默认值为 None。
- dnsNames!: Array\<String> - 域名列表，需要用户保证输入域名的有效性，默认值为空的字符串数组。
- emailAddresses!: Array\<String> - email 地址列表，需要用户保证输入 email 的有效性，默认值为空的字符串数组。
- IPAddresses!: Array\<[IP](x509_package_type.md#type-ip)> - [IP](x509_package_type.md#type-ip) 地址列表，默认值为空的 [IP](x509_package_type.md#type-ip) 数组。
- keyUsage!: ?[KeyUsage](x509_package_structs.md#struct-keyusage) - 密钥用法，默认值为 None。
- extKeyUsage!: ?[ExtKeyUsage](x509_package_structs.md#struct-extkeyusage) - 扩展密钥用法，默认值为 None。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 输入的 [IP](x509_package_type.md#type-ip) 地址列表中包含无效的 [IP](x509_package_type.md#type-ip) 地址，则抛出异常。