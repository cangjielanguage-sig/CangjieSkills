# 使用RSA密钥对（PKCS1模式）签名及签名恢复（仓颉）

对应的算法规格请参见[签名验签算法规格：RSA](./cj-crypto-sign-sig-verify-overview.md#rsa)。

## 签名

1. 调用[createAsyKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorstring)，生成密钥算法为RSA、密钥长度为1024位、素数个数为2的非对称密钥对象（KeyPair），包括公钥（PubKey）和私钥（PriKey）。

    如何生成RSA非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](./cj-crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对](./cj-crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

2. 调用[createSign](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createsignstring)，指定字符串参数'RSA1024|PKCS1|SHA256|SignOnly'，创建非对称密钥类型为RSA1024、填充模式为PKCS1、摘要算法为SHA256的Sign实例，用于完成仅签名操作。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initializeprikey)，使用私钥（PriKey）初始化Sign实例。

4. 调用[sign](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-signdatablob)，生成数据签名。

## 验签

1. 调用[createVerify](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createverifystring)，指定字符串参数'RSA1024|PKCS1|SHA256|Recover'，与签名的Sign实例保持一致。创建Verify实例，用于完成验签操作。

2. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initializepubkey)，使用公钥（PubKey）初始化Verify实例。

3. 调用[recover](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-recoverdatablob)，对数据进行签名恢复。

## 示例

同步方法示例如下：

```cangjie
import kit.CryptoArchitectureKit.*

let input1: DataBlob = DataBlob("This is Sign test plan1".toArray())

func signMessage(priKey: PriKey) {
    let signAlg = "RSA1024|PKCS1|NoHash|OnlySign"
    let signer = createSign(signAlg)
    signer.initialize(priKey)
    let signData = signer.sign(input1)
    return signData
}

func verifyMessage(signMessageBlob: DataBlob, pubKey: PubKey) {
    let verifyAlg = "RSA1024|PKCS1|NoHash|Recover"
    let verifier = createVerify(verifyAlg)
    verifier.initialize(pubKey)
    let rawSignData = verifier.recover(signMessageBlob)
    return rawSignData
}

func test() {
    let keyGenAlg = "RSA1024"
    let generator = createAsyKeyGenerator(keyGenAlg)
    let keyPair = generator.generateKeyPair()
    let signData = signMessage(keyPair.priKey)
    let rawSignData = verifyMessage(signData, keyPair.pubKey)
    if (let Some(v) <- rawSignData) {
        AppLog.info('recover result: ' + v.data.toString())
    } else {
        AppLog.error("get verify recover result fail!")
    }
}
```
