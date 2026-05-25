# 使用3DES对称密钥（ECB模式）加解密（仓颉）

对应的算法规格请参见[对称密钥加解密算法规格：3DES](./cj-crypto-sym-encrypt-decrypt-spec.md#3des)。

## 加密

1. 调用[createSymKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createsymkeygeneratorstring)、[convertKey](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-convertkeydatablob)，生成密钥算法为3DES、密钥长度为192位的对称密钥（SymKey）。

   如何生成3DES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：3DES](./cj-crypto-sym-key-generation-conversion-spec.md#3des)和[指定二进制数据转换对称密钥](./cj-crypto-convert-binary-data-to-sym-key.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

2. 调用[createCipher](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createcipherstring)，指定字符串参数'3DES192|ECB|PKCS7'，创建对称密钥类型为3DES192、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成加密操作。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initcryptomode-key-paramsspec)，设置模式为加密（CryptoMode.ENCRYPT_MODE），指定加密密钥（SymKey），初始化加密Cipher实例。

   ECB模式无加密参数，直接传入None。

4. 调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob)，更新数据（明文）。

   - 当数据量较小时，可以在init完成后直接调用doFinal。
   - 当数据量较大时，可以多次调用update，即分段加解密。
   - 数据量大小可以使用者自行决定。比如大于20字节使用update。

5. 调用[doFinal](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-dofinaldatablob)，获取加密后的数据。

   由于已使用update传入数据，此处data传入None。

## 解密

1. 调用[createCipher](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createcipherstring)，指定字符串参数'3DES192|ECB|PKCS7'，创建对称密钥类型为3DES192、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成解密操作。

2. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initcryptomode-key-paramsspec)，设置模式为解密（CryptoMode.DECRYPT_MODE），指定解密密钥（SymKey）初始化解密Cipher实例。ECB模式无加密参数，直接传入None。

3. 调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob)，更新数据（密文）。

4. 调用[doFinal](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-dofinaldatablob)，获取解密后的数据。