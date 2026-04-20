## API 列表

### 类型别名

| 类型别名                                              | 功能                             |
| ----------------------------------------------------- | -------------------------------- |
| [IP](./x509_package_api/x509_package_type.md#type-ip) | x509 用 Array\<Byte> 来记录 IP。 |

### 接口

| 接口名                                              | 功能                             |
| ----------------------------------------------------- | -------------------------------- |
| [DHParameters](./x509_package_api/x509_package_interfaces.md#interface-dhparameters) | 提供 DH 密钥接口。 |
| [Key](./x509_package_api/x509_package_interfaces.md#interface-key) | 提供密钥接口。 |
| [PrivateKey](./x509_package_api/x509_package_interfaces.md#interface-privatekey) | 提供私钥接口。 |
| [PublicKey](./x509_package_api/x509_package_interfaces.md#interface-publickey) | 提供公钥接口。 |

### 类

| 类名                                                                                              | 功能                                        |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| [X509Certificate](./x509_package_api/x509_package_classes.md#class-x509certificate)               | X509 数字证书是一种用于加密通信的数字证书。 |
| [X509CertificateRequest](./x509_package_api/x509_package_classes.md#class-x509certificaterequest) | 数字证书签名请求。                          |
| [X509Name](./x509_package_api/x509_package_classes.md#class-x509name)                             | 证书实体可辨识名称。                        |

### 枚举

| 枚举名                                                                                 | 功能                       |
| -------------------------------------------------------------------------------------- | -------------------------- |
| [PublicKeyAlgorithm](./x509_package_api/x509_package_enums.md#enum-publickeyalgorithm) | 数字证书中包含的公钥信息。 |
| [SignatureAlgorithm](./x509_package_api/x509_package_enums.md#enum-signaturealgorithm) | 证书签名算法。             |

### 结构体

| 结构体名                                                                                                   | 功能                                             |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [DerBlob](./x509_package_api/x509_package_structs.md#struct-derblob)                                       | Crypto 支持配置二进制证书流。                               |
| [ExtKeyUsage](./x509_package_api/x509_package_structs.md#struct-extkeyusage)                               | 数字证书扩展字段。                               |
| [KeyUsage](./x509_package_api/x509_package_structs.md#struct-keyusage)                                     | 数字证书扩展字段中通常会包含携带公钥的用法说明。 |
| [Pem](./x509_package_api/x509_package_structs.md#struct-pem)                                               | Pem 结构体。 |
| [PemEntry](./x509_package_api/x509_package_structs.md#struct-pementry)                                     | Pem 文本格式。 |
| [SerialNumber](./x509_package_api/x509_package_structs.md#struct-serialnumber)                             | 数字证书的序列号。                               |
| [Signature](./x509_package_api/x509_package_structs.md#struct-signature)                                   | 数字证书的签名。                                 |
| [VerifyOption](./x509_package_api/x509_package_structs.md#struct-verifyoption)                             | 校验选项。                                       |
| [X509CertificateInfo](./x509_package_api/x509_package_structs.md#struct-x509certificateinfo)               | 证书信息。                                       |
| [X509CertificateRequestInfo](./x509_package_api/x509_package_structs.md#struct-x509certificaterequestinfo) | 证书请求信息。                                   |

### 异常类

| 异常类名                                                                           | 功能                |
| ---------------------------------------------------------------------------------- | ------------------- |
| [X509Exception](./x509_package_api/x509_package_exceptions.md#class-x509exception) | `x509` 包的异常类。 |