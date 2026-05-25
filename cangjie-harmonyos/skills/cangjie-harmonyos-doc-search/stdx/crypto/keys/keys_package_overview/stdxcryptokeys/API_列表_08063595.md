## API 列表

### 类

| 类名                                                                                    | 功能                           |
| --------------------------------------------------------------------------------------- | ------------------------------ |
| [ECDSAPrivateKey](./keys_package_api/keys_package_classes.md#class-ecdsaprivatekey)     | ECDSA 私钥类。                  |
| [ECDSAPublicKey](./keys_package_api/keys_package_classes.md#class-ecdsapublickey)       | ECDSA 公钥类。                  |
| [RSAPrivateKey](./keys_package_api/keys_package_classes.md#class-rsaprivatekey)         | RSA 私钥类。                    |
| [RSAPublicKey](./keys_package_api/keys_package_classes.md#class-rsapublickey)           | RSA 公钥类。                    |
| [SM2PrivateKey](./keys_package_api/keys_package_classes.md#class-sm2privatekey)         | SM2 私钥类。                    |
| [SM2PublicKey](./keys_package_api/keys_package_classes.md#class-sm2publickey)           | SM2 公钥类。                    |

### 枚举

| 枚举名                                                               | 功能                                                         |
| -------------------------------------------------------------------- | ------------------------------------------------------------ |
| [Curve](./keys_package_api/keys_package_enums.md#enum-curve)         | 枚举类型 Curve 用于选择生成 ECDSA 密钥时使用的椭圆曲线类型。 |
| [PadOption](./keys_package_api/keys_package_enums.md#enum-padoption) | 用于设置 RSA 的填充模式。                                    |

### 结构体

| 结构体名                                                                   | 功能                 |
| -------------------------------------------------------------------------- | -------------------- |
| [OAEPOption](./keys_package_api/keys_package_structs.md#struct-oaepoption) | 最优非对称加密填充。 |
| [PSSOption](./keys_package_api/keys_package_structs.md#struct-pssoption)   | 概率签名方案。       |