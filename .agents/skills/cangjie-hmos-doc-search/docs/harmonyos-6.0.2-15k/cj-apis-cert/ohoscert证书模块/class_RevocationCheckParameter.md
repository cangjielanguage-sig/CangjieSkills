## class RevocationCheckParameter

```cangjie
public class RevocationCheckParameter {
    public var ocspRequestExtension: ?Array<Array<UInt8>> = Option.None
    public var ocspResponderURI: ?String = Option.None
    public var ocspResponderCert: ?X509Cert = Option.None
    public var ocspResponses: ?Array<UInt8> = Option.None
    public var crlDownloadURI: ?String = Option.None
    public var options: ?Array<RevocationCheckOptions> = Option.None
    public var ocspDigest: ?String = Option.None
}
```

**功能：** 表示证书链校验证书吊销状态的参数。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var crlDownloadURI

```cangjie
public var crlDownloadURI: ?String = Option.None
```

**功能：** 表示用于CRL请求的备选下载地址。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var ocspDigest

```cangjie
public var ocspDigest: ?String = Option.None
```

**功能：** 表示OCSP通信时创建证书ID使用的哈希算法。默认为SHA256，支持可配置MD5、SHA1、SHA224、SHA256、SHA384、SHA512算法。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var ocspRequestExtension

```cangjie
public var ocspRequestExtension: ?Array<Array<UInt8>> = Option.None
```

**功能：** 表示发送OCSP请求的扩展字段。

**类型：** ?Array\<Array\<UInt8>>

**读写能力：** 可读写

**起始版本：** 19

### var ocspResponderCert

```cangjie
public var ocspResponderCert: ?X509Cert = Option.None
```

**功能：** 表示用于OCSP响应的签名校验的签名证书。

**类型：** ?[X509Cert](#class-x509cert)

**读写能力：** 可读写

**起始版本：** 19

### var ocspResponderURI

```cangjie
public var ocspResponderURI: ?String = Option.None
```

**功能：** 表示用于OCSP请求的备选服务器URL地址，支持HTTP/HTTPS，具体配置由与服务器协商决定。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var ocspResponses

```cangjie
public var ocspResponses: ?Array<UInt8> = Option.None
```

**功能：** 表示用于OCSP服务器响应的备选数据。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var options

```cangjie
public var options: ?Array<RevocationCheckOptions> = Option.None
```

**功能：** 表示证书吊销状态查询的策略组合。

**类型：** ?Array\<[RevocationCheckOptions](#enum-revocationcheckoptions)>

**读写能力：** 可读写

**起始版本：** 19