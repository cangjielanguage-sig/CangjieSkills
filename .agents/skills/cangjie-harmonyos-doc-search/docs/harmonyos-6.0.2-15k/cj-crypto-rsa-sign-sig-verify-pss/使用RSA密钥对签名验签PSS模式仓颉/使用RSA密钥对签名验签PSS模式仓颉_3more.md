# 使用RSA密钥对签名验签（PSS模式）（仓颉）

对应的算法规格请参见[签名验签算法规格：RSA](./cj-crypto-sign-sig-verify-overview.md#rsa)。

## 签名

1. 调用[createAsyKeyGeneratorBySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorbyspecasykeyspec)，指定密钥参数，生成RSA非对称密钥对（KeyPair）。

    如何生成RSA非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](./cj-crypto-asym-key-generation-conversion-spec.md#rsa)和[指定密钥参数生成非对称密钥对](./cj-crypto-generate-asym-key-pair-from-key-spec.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

2. 调用[createSign](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createsignstring)，指定字符串参数'RSA|PSS|SHA256|MGF1_SHA256'，创建非对称密钥类型为不带长度的RSA、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1_SHA256的Sign实例，用于完成签名操作。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initializeprikey)，使用私钥（PriKey）初始化Sign实例。

4. 调用[setSignSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-setsignspecsignspecitem-int32)，设置签名参数。此处设置盐值的长度（SignSpecItem.PSS_SALT_LEN_NUM）为32字节。在验签时将校验此数据。

5. 调用[getSignSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getsignspecsignspecitem)，获取其他签名参数。

6. 调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob-3)，传入待签名的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

7. 调用[sign](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-signdatablob)，生成数据签名。

## 验签

1. 调用[createVerify](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createverifystring)，指定字符串参数'RSA2048|PSS|SHA256|MGF1_SHA256'，创建非对称密钥类型为RSA2048、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1_SHA256的Verify实例，用于完成验签操作。

2. 调用[setVerifySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-setverifyspecsignspecitem-int32)，设置签名参数。需要与签名时设置的保持一致。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initializepubkey)，使用公钥（PubKey）初始化Verify实例。

4. 调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob-4)，传入待验证的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

5. 调用[verify](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-verifydatablob-datablob)，对数据进行验签。