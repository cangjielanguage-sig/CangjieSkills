## 指定密钥参数生成ECC密钥对

对应的算法规格请参见[非对称密钥生成和转换规格：ECC](./cj-crypto-asym-key-generation-conversion-spec.md#ecc)。

1. 构造[ECCCommonParamsSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-ecccommonparamsspec)对象，用于指定ECC算法中公私钥包含的公共参数。
   ECCCommonParamsSpec是AsyKeySpec的子类。需要通过参数algName指定算法'ECC'；指定密钥参数类型AsyKeySpecType.COMMON_PARAMS_SPEC，表示是公私钥中包含的公共参数。

   使用密钥参数生成密钥时，用到的bigint类型需要以大端模式输入，且必须为正数。

2. 调用[createAsyKeyGeneratorBySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorbyspecasykeyspec)，将ECCCommonParamsSpec对象传入，创建非对称密钥生成器（AsyKeyGeneratorBySpec）。

3. 调用[generateKeyPair](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatekeypair-1)，得到随机生成的密钥对（KeyPair）。

4. 分别传入密钥对中的私钥和公钥，调用[getAsyKeySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getasykeyspecasykeyspecitem)，获取ECC算法中私钥和公钥的各种密钥参数。