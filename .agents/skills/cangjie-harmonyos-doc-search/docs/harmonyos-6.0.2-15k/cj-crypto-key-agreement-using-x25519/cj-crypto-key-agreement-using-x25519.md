# 使用X25519进行密钥协商

对应的算法规格请参见[密钥协商算法规格：X25519](./cj-crypto-key-agreement-overview.md#x25519)。

## 开发步骤

1. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)生成密钥算法为X25519的非对称密钥（KeyPair）。

    如何生成X25519非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：X25519](./cj-crypto-asym-key-generation-conversion-spec.md#x25519)和[随机生成非对称密钥对](./cj-crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

2. 调用[createKeyAgreement](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createkeyagreementstring)，指定字符串参数'X25519'，创建密钥算法为X25519的密钥协议生成器（KeyAgreement）。

3. 调用[generateSecret](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatesecretprikey-pubkey)，基于传入的私钥（KeyPair.priKey）与公钥（KeyPair.pubKey）进行密钥协商，返回共享秘钥。

## 示例

同步方法示例如下：

```cangjie
import kit.CryptoArchitectureKit.*

func x25519Agreement() {
    // 假设此公私钥对数据为外部传入。
    let pubKeyArray: Array<UInt8> = [48, 42, 48, 5, 6, 3, 43, 101, 110, 3, 33, 0, 36, 98, 216, 106, 74, 99, 179, 203,
        81, 145, 147, 101, 139, 57, 74, 225, 119, 196, 207, 0, 50, 232, 93, 147, 188, 21, 225, 228, 54, 251, 230, 52]
    let priKeyArray: Array<UInt8> = [48, 46, 2, 1, 0, 48, 5, 6, 3, 43, 101, 110, 4, 34, 4, 32, 112, 65, 156, 73, 65, 89,
        183, 39, 119, 229, 110, 12, 192, 237, 186, 153, 21, 122, 28, 176, 248, 108, 22, 242, 239, 179, 106, 175, 85, 65,
        214, 90]
    let keyGen = createAsyKeyGenerator('X25519')
    // 外部传入的公私钥对A。
    let keyPairA = keyGen.convertKey(DataBlob(pubKeyArray), DataBlob(priKeyArray))
    // 内部生成的公私钥对B。
    let keyPairB = keyGen.generateKeyPair()
    let keyAgreement = createKeyAgreement('X25519')
    // 使用A的公钥和B的私钥进行密钥协商。
    let secret1 = keyAgreement.generateSecret(keyPairB.priKey, keyPairA.pubKey)
    // 使用A的私钥和B的公钥进行密钥协商。
    let secret2 = keyAgreement.generateSecret(keyPairA.priKey, keyPairB.pubKey)
    // 两种协商的结果应当一致。
    if (secret1.data.toString() == secret2.data.toString()) {
        AppLog.info('x25519 success')
        AppLog.info('x25519 output is ${secret1.data}')
    } else {
        AppLog.error('x25519 result is not equal')
    }
}
```
