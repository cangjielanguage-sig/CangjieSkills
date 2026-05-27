## 指定密钥参数生成RSA公钥

对应的算法规格请参见[非对称密钥生成和转换规格：RSA](./cj-crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 构造[RSACommonParamsSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-rsacommonparamsspec)对象，用于指定RSA算法中公私钥包含的公共参数（n）。

   RSACommonParamsSpec是AsyKeySpec的子类。需要通过参数algName指定算法'RSA'；指定密钥参数类型AsyKeySpecType.COMMON_PARAMS_SPEC，表示是公私钥中包含的公共参数。

   使用密钥参数生成密钥时，用到的bigint类型需要以大端模式输入，且必须为正数。

2. 创建[RSAPubKeySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-rsapubkeyspec)对象，用于指定RSA算法中公钥包含的参数（n, pk）。

   RSAPubKeySpec是AsyKeySpec的子类。通过参数algName指定算法'RSA'；指定密钥参数类型AsyKeySpecType.PUBLIC_KEY_SPEC，表示是公钥中包含的参数。

3. 调用[createAsyKeyGeneratorBySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorbyspecasykeyspec)，将RSAPubKeySpec对象传入，创建非对称密钥生成器（AsyKeyGeneratorBySpec）。

4. 调用[generatePubKey](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatepubkey)，获得指定的公钥（PubKey）。

5. 调用[getAsyKeySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getasykeyspecasykeyspecitem-1)，获取模数n和公钥pk（即公钥指数e）。

以根据密钥参数生成RSA公钥为例：

```cangjie
import kit.CryptoArchitectureKit.*
import std.math.numeric.BigInt
import ohos.base.BusinessException

// 完整的明文被拆分为input1和input2。
let input1: DataBlob = DataBlob("This is Sign test plan1".toArray())
let input2: DataBlob = DataBlob("This is Sign test plan2".toArray())

func genRsaPubKeySpec(nIn: BigInt, eIn: BigInt): RSAPubKeySpec {
    let rsaCommSpec: RSACommonParamsSpec = RSACommonParamsSpec(
        n: nIn,
        algName: 'RSA',
        specType: AsyKeySpecType.PUBLIC_KEY_SPEC
    )
    let rsaPubKeySpec: RSAPubKeySpec = RSAPubKeySpec(
        params: rsaCommSpec,
        pk: eIn
    )
    return rsaPubKeySpec
}

func genRsa2048PubKeySpec() {
    let nIn = BigInt.parse(
        '9260d0750ae117eee55c3f3deaba74917521a262ee76007cdf8a56755ad73a1598a1408410a01434c3f5bc54a88b57fa19fc4328daea0750a4c44e88cff3b2382621b80f670464433e4336e6d003e8cd65bff211da144b88291c2259a00a72b711c116ef7686e8fee34e4d933c868187bdc26f7be071493c86f7a5941c3510806ad67b0f94d88f5cf5c02a092821d8626e8932b65c5bd8c92049c210932b7afa7ac59c0e886ae5c1edb00d8ce2c57633db26bd6639bff73cee82be9275c402b4cf2a4388da8cf8c64eefe1c5a0f5ab8057c39fa5c0589c3e253f0960332300f94bea44877b588e1edbde97cf2360727a09b775262d7ee552b3319b9266f05a25',
        radix: 16
    )
    let eIn = BigInt.parse('010001', radix: 16)
    return genRsaPubKeySpec(nIn, eIn)
}

func compareRsaPubKeyBySpec(rsaKeySpec: RSAPubKeySpec, n: ResultSpec, e: ResultSpec) {
    if (rsaKeySpec.params.n.toString() != n.toString()) {
        return false
    }
    if (rsaKeySpec.pk.toString() != e.toString()) {
        return false
    }
    return true
}