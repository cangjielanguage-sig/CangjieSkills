# 使用SM4对称密钥（GCM模式）加解密（仓颉）

对应的算法规格请参见[对称密钥加解密算法规格：SM4](./cj-crypto-sym-encrypt-decrypt-spec.md#sm4)。

## 加密

1. 调用[createSymKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createsymkeygeneratorstring)，生成密钥算法为SM4、密钥长度为128位的对称密钥（SymKey）。

    如何生成SM4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：SM4](./cj-crypto-sym-key-generation-conversion-spec.md#sm4)和[随机生成对称密钥](./cj-crypto-generate-sym-key-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

2. 调用[createCipher](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createcipherstring)，指定字符串参数'SM4_128|GCM|PKCS7'，创建对称密钥类型为SM4_128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initcryptomode-key-paramsspec)，设置模式为加密（CryptoMode.ENCRYPT_MODE），指定加密密钥（SymKey）和GCM模式对应的加密参数（GcmParamsSpec），初始化加密Cipher实例。

4. 调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob)，更新数据（明文）。

    当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

    - 当数据量较小时，可以在init完成后直接调用doFinal。
    - 当数据量较大时，可以多次调用update，即分段加解密。

5. 调用[doFinal](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-dofinaldatablob)，获取加密后的数据。

    由于已使用update传入数据，此处data传入None。

6. 读取[GcmParamsSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-gcmparamsspec).authTag作为解密的认证信息。

    在GCM模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。示例中authTag恰好为16字节。