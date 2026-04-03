# 随机生成非对称密钥对（仓颉）

以RSA和SM2为例，随机生成非对称密钥对（KeyPair），并获得二进制数据。

非对称密钥对可用于后续加解密等操作，二进制数据可用于存储或传输。

## 随机生成RSA密钥对

对应的算法规格请参见[非对称密钥生成和转换规格：RSA](./cj-crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)，指定字符串参数'RSA1024|PRIMES_2'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（AsyKeyGenerator）。

2. 调用[generateKeyPair](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatekeypair)，随机生成非对称密钥对象（KeyPair）。

   KeyPair对象中包括公钥PubKey和私钥PriKey。

3. 调用[getEncoded](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getencoded)，分别获取密钥对象的二进制数据。

以随机生成RSA密钥对为例：

```cangjie
import kit.CryptoArchitectureKit.*
import ohos.base.BusinessException

func generateAsyKey() {
    // 创建一个AsyKeyGenerator实例。
    let rsaGenerator = createAsyKeyGenerator('RSA1024|PRIMES_2')
    // 使用密钥生成器随机生成非对称密钥对。
    try {
        let keyPair = rsaGenerator.generateKeyPair()
        let pubKey = keyPair.pubKey
        let priKey = keyPair.priKey
        // 获取非对称密钥对的二进制数据。
        let pkBlob = pubKey.getEncoded()
        let skBlob = priKey.getEncoded()
        AppLog.info('pk bin data' + pkBlob.data.toString())
        AppLog.info('sk bin data' + skBlob.data.toString())
    } catch (e: BusinessException) {
        AppLog.error("get key pair failed, ${e.code}, ${e.message}")
    }
}
```

## 随机生成SM2密钥对

对应的算法规格请参见[非对称密钥生成和转换规格：SM2](./cj-crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)，指定字符串参数'SM2_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。

2. 调用[generateKeyPair](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatekeypair)，随机生成非对称密钥对象（KeyPair）。

   KeyPair对象中包括公钥PubKey和私钥PriKey。

3. 调用[getEncoded](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getencoded)，分别获取密钥对象的二进制数据。

以随机生成SM2密钥对为例：

```cangjie
import kit.CryptoArchitectureKit.*
import ohos.base.BusinessException

func generateSM2Key() {
    // 创建一个AsyKeyGenerator实例。
    let rsaGenerator = createAsyKeyGenerator('SM2_256')
    // 使用密钥生成器随机生成非对称密钥对。
    try {
        let keyPair = rsaGenerator.generateKeyPair()
        let pubKey = keyPair.pubKey
        let priKey = keyPair.priKey
        // 获取非对称密钥对的二进制数据。
        let pkBlob = pubKey.getEncoded()
        let skBlob = priKey.getEncoded()
        AppLog.info('pk bin data' + pkBlob.data.toString())
        AppLog.info('sk bin data' + skBlob.data.toString())
    } catch (e: BusinessException) {
        AppLog.error("get key pair failed, ${e.code}, ${e.message}")
    }
}
```
