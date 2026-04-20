### func verify(VerifyOption)

```cangjie
public func verify(verifyOption: VerifyOption): Bool
```

功能：根据验证选项验证当前证书的有效性。

验证优先级：

1. 优先验证有效期；
2. 可选验证 DNS 域名；
3. 最后根据根证书和中间证书验证其有效性。

参数：

- verifyOption: [VerifyOption](x509_package_structs.md#struct-verifyoption) - 证书验证选项。

返回值：

- Bool - 证书有效返回 true，否则返回 false。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 检验过程中失败，比如内存分配异常等内部错误，则抛出异常。

### operator func !=(X509Certificate)

```cangjie
public override operator func !=(other: X509Certificate): Bool
```

功能：判不等。

参数：

- other: [X509Certificate](x509_package_classes.md#class-x509certificate) - 被比较的证书对象。

返回值：

- Bool - 若证书不同，返回 true；否则，返回 false。

### operator func ==(X509Certificate)

```cangjie
public override operator func ==(other: X509Certificate): Bool
```

功能：判等。

参数：

- other: [X509Certificate](x509_package_classes.md#class-x509certificate) - 被比较的证书对象。

返回值：

- Bool - 若证书相同，返回 true；否则，返回 false。