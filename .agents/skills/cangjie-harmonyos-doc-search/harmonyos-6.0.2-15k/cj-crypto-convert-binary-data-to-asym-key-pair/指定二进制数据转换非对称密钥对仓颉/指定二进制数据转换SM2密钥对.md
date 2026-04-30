## 指定二进制数据转换SM2密钥对

对应的算法规格请参见[非对称密钥生成和转换规格：SM2](./cj-crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 获取SM2公钥或私钥二进制数据，封装成DataBlob对象。

   公钥和私钥可只传入其中一个，此处示例以传入公钥、私钥为例。

2. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)，指定字符串参数'SM2_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。

3. 调用[convertKey](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-convertkeydatablob-datablob)，传入公钥二进制和私钥二进制，生成非对称密钥对象（KeyPair）。

以生成SM2密钥对为例：

```cangjie
import kit.CryptoArchitectureKit.*
import ohos.base.BusinessException

func convertSM2AsyKey() {
    let pubKeyArray: Array<UInt8> = [48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1,
        7, 3, 66, 0, 4, 83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81,
        58, 202, 121, 26, 105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66,
        0, 167, 99, 92, 235, 215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]
    let priKeyArray: Array<UInt8> = [48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210,
        16, 27, 4, 171, 57, 10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72,
        206, 61, 3, 1, 7]
    let pubKeyBlob: DataBlob = DataBlob(pubKeyArray)
    let priKeyBlob: DataBlob = DataBlob(priKeyArray)
    let generator = createAsyKeyGenerator('SM2_256');
    try {
        let keyPair = generator.convertKey(pubKeyBlob, priKeyBlob);
        AppLog.info('convertKeySync success')
    } catch (e: BusinessException) {
        AppLog.error("get key pair failed, ${e.code}, ${e.message}")
    }
}
```