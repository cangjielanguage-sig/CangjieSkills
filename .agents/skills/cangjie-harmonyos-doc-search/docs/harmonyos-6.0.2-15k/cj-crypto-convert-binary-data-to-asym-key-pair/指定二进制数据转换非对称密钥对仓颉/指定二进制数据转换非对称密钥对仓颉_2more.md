# 指定二进制数据转换非对称密钥对（仓颉）

以RSA、ECC、SM2为例，根据指定的对称密钥二进制数据，生成非对称密钥对（KeyPair），即将外部或存储的二进制数据转换为算法库的密钥对象，该对象可用于后续的加解密等操作。

> **说明：**
>
> 针对非对称密钥的convertKey操作：
>
> - 公钥需满足：ASN.1语法、X.509规范、DER编码格式。
>
> - 私钥需满足：ASN.1语法、PKCS\#8规范、DER编码格式。

## 指定二进制数据转换RSA密钥对

对应的算法规格请参见[非对称密钥生成和转换规格：RSA](./cj-crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 获取RSA公钥或私钥二进制数据，封装成DataBlob对象。

   公钥和私钥可只传入其中一个，此处示例以传入公钥为例。

2. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)，指定字符串参数'RSA1024'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（AsyKeyGenerator）。

   生成RSA非对称密钥时，默认素数为2，此处省略了参数PRIMES_2。

3. 调用[convertKey](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-convertkeydatablob-datablob)，传入二进制密钥数据，生成非对称密钥对象（KeyPair）。

以生成RSA密钥对为例：

```cangjie
import kit.CryptoArchitectureKit.*
import ohos.base.BusinessException

func convertAsyKey() {
    let rsaGenerator = createAsyKeyGenerator('RSA1024')
    let pkVal: Array<UInt8> = [48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48,
        129, 137, 2, 129, 129, 0, 174, 203, 113, 83, 113, 3, 143, 213, 194, 79, 91, 9, 51, 142, 87, 45, 97, 65, 136, 24,
        166, 35, 5, 179, 42, 47, 212, 79, 111, 74, 134, 120, 73, 67, 21, 19, 235, 80, 46, 152, 209, 133, 232, 87, 192,
        140, 18, 206, 27, 106, 106, 169, 106, 46, 135, 111, 118, 32, 129, 27, 89, 255, 183, 116, 247, 38, 12, 7, 238,
        77, 151, 167, 6, 102, 153, 126, 66, 28, 253, 253, 216, 64, 20, 138, 117, 72, 15, 216, 178, 37, 208, 179, 63,
        204, 39, 94, 244, 170, 48, 190, 21, 11, 73, 169, 156, 104, 193, 3, 17, 100, 28, 60, 50, 92, 235, 218, 57, 73,
        119, 19, 101, 164, 192, 161, 197, 106, 105, 73, 2, 3, 1, 0, 1]
    let pkBlob: DataBlob = DataBlob(pkVal)
    try {
        let keyPair = rsaGenerator.convertKey(pkBlob, None)
        AppLog.info('convertKeySync success')
    } catch (e: BusinessException) {
        AppLog.error("get key pair failed, ${e.code}, ${e.message}")
    }
}
```