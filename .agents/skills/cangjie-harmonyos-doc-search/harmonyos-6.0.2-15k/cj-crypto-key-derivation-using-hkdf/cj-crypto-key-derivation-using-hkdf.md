# 使用HKDF进行密钥派生

对应算法规格请参见[密钥派生算法规格：HKDF](./cj-crypto-key-derivation-overview.md#hkdf算法)。

## 开发步骤

1. 构造[HKDFSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-hkdfspec)对象，作为密钥派生参数进行密钥派生。

    HKDFSpec是[KdfSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#interface-kdfspec)的子类，需要指定：

    - algName：指定算法'HKDF'。
    - key：原始密钥材料。
        如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。
    - salt：盐值。
    - info：可选的上下文与应用相关信息， 可为空，用于拓展短密钥。
    - keySize：目标密钥的字节长度，需要为正整数。

2. 调用[createKdf](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createkdfstring)，指定字符串参数'HKDF|SHA256|EXTRACT_AND_EXPAND'，创建密钥派生算法为HKDF、HMAC函数摘要算法为SHA256、模式为提取和拓展的密钥派生函数对象（Kdf）。

3. 输入HKDFSpec对象，调用[generateSecret](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatesecretkdfspec)进行密钥派生。

    Kdf.generateSecret的调用形式如表所示：

    | 接口名 | 返回方式 |
    | :-------- | :-------- |
    | generateSecretSync(params: KdfSpec): DataBlob | 同步生成 |

## 示例

同步方法示例如下：

```cangjie
func kdf() {
    let keyData = "012345678901234567890123456789".toArray()
    let saltData = "0123456789".toArray()
    let infoData = "infostring".toArray()
    let spec: HKDFSpec = HKDFSpec(
        algName: 'HKDF',
        key: keyData,
        salt: saltData,
        info: infoData,
        keySize: 32
    )
    let kdf = createKdf('HKDF|SHA256|EXTRACT_AND_EXPAND')
    let secret = kdf.generateSecret(spec)
    AppLog.info("[Sync]key derivation output is ${secret.data}")
}
```
