# 使用AES对称密钥（GCM模式）分段加解密（仓颉）

对应的算法规格请参见[对称密钥加解密算法规格：AES](./cj-crypto-sym-encrypt-decrypt-spec.md#aes)。

## 加密

1. 调用[createSymKeyGenerator](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createsymkeygeneratorstring)，生成密钥算法为AES、密钥长度为128位的对称密钥（SymKey）。

   如何生成AES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：AES](./cj-crypto-sym-key-generation-conversion-spec.md#aes)和[随机生成对称密钥](./cj-crypto-generate-sym-key-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

2. 调用[createCipher](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createcipherstring)，指定字符串参数'AES128|GCM|PKCS7'，创建对称密钥类型为AES128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。

3. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initcryptomode-key-paramsspec)，设置模式为加密（CryptoMode.ENCRYPT_MODE），指定加密密钥（SymKey）和GCM模式对应的加密参数（GcmParamsSpec），初始化加密Cipher实例。

4. 将一次传入数据量设置为20字节，多次调用[update](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-updatedatablob)，更新数据（明文）。

   当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

      1）比如ECB和CBC模式，始终以分组作为基本单位来加密，并输出本次update产生的加密分组结果。即当本次update操作凑满一个分组就输出密文，没有凑满则此次update输出空Datablob，将未加密的数据与下次输入的数据拼接凑分组再输出。等到最后doFinal的时候，将未加密的数据，根据指定的填充模式进行填充，在输出剩余加密结果。解密过程中的update同理。

      2）对于流加密模式（比如CTR和OFB模式），通常密文长度和明文长度相等。

5. 调用[doFinal](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-dofinaldatablob)，获取加密后的数据。

   由于已使用update传入数据，此处data传入None。

6. 读取[GcmParamsSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-gcmparamsspec).authTag作为解密的认证信息。

   在GCM模式下，算法库当前只支持16字节的authTag，作为解密时初始化的认证信息。示例中authTag恰好为16字节。