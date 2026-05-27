# 使用PBKDF2进行密钥派生

对应的算法规格请参见[密钥派生算法规格：PBKDF2](./cj-crypto-key-derivation-overview.md#pbkdf2算法)。

## 开发步骤

1. 构造[PBKDF2Spec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-pbkdf2spec)对象，作为密钥派生参数进行密钥派生。

    PBKDF2Spec是[KdfSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#interface-kdfspec)的子类，需要指定：

    - algName：指定算法'PBKDF2'。
    - password：用于生成派生密钥的原始密码。
       如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。
    - salt：盐值。
    - iterations：重复运算的次数，需要为正整数。
    - keySize：目标密钥的字节长度，需要为正整数。

2. 调用[createKdf](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createkdfstring)，指定字符串参数'PBKDF2|SHA256'，创建密钥派生算法为PBKDF2、HMAC函数摘要算法为SHA256的密钥派生函数对象（Kdf）。

3. 输入PBKDF2Spec对象，调用[generateSecret](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatesecretkdfspec)进行密钥派生。

    Kdf.generateSecret的调用形式如表所示。

    | 接口名 | 返回方式 |
    | :-------- | :-------- |
    | generateSecretSync(params: KdfSpec): DataBlob | 同步生成 |

## 示例

同步方法示例如下：

```cangjie
import kit.CryptoArchitectureKit.*

func kdf() {
    let spec: PBKDF2Spec = PBKDF2Spec(
        algName: 'PBKDF2',
        password: '123456'.toArray(),
        salt: Array<UInt8>(16, repeat: 0),
        iterations: 10000,
        keySize: 32
    )
    let kdf = createKdf('PBKDF2|SHA256')
    let secret = kdf.generateSecret(spec)
    AppLog.info("key derivation output is ${secret.data}")
}
```
