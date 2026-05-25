### func updateCA(Array\<X509Certificate>)

```cangjie
public func updateCA(newCa: Array<X509Certificate>): Unit
```

功能：对 CA 证书进行热更新。

参数：

- newCa: Array\<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)> - CA 证书。

异常：

- IllegalArgumentException - 参数包含空字符时抛出异常。
- [HttpException](http_package_exceptions.md#class-httpexception) - 服务端未配置 tlsConfig 时抛出异常。

### func updateCA(String)

```cangjie
public func updateCA(newCaFile: String): Unit
```

功能：对 CA 证书进行热更新。

参数：

- newCaFile: String - CA 证书文件。

异常：

- IllegalArgumentException - 参数包含空字符时抛出异常。
- [HttpException](http_package_exceptions.md#class-httpexception) - 服务端未配置 tlsConfig 时抛出异常。

### func updateCert(Array\<X509Certificate>, PrivateKey)

```cangjie
public func updateCert(certChain: Array<X509Certificate>, certKey: PrivateKey): Unit
```

功能：对 TLS 证书进行热更新。

参数：

- certChain: Array\<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)> - 证书链。
- certKey: [PrivateKey](../../../crypto/x509/x509_package_api/x509_package_interfaces.md#interface-privatekey) - 证书匹配的私钥。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 服务端未配置 tlsConfig 时抛出异常。

### func updateCert(String, String)

```cangjie
public func updateCert(certificateChainFile: String, privateKeyFile: String): Unit
```

功能：对 TLS 证书进行热更新。

参数：

- certificateChainFile: String - 证书链文件。
- privateKeyFile: String - 证书匹配的私钥文件。

异常：

- IllegalArgumentException - 参数包含空字符时抛出异常。
- [HttpException](http_package_exceptions.md#class-httpexception) - 服务端未配置 tlsConfig 时抛出异常。