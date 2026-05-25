## 根据椭圆曲线名生成SM2密钥对

对应的算法规格请参见[非对称密钥生成和转换规格：SM2](./cj-crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 构造[ECCCommonParamsSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-ecccommonparamsspec)接口传入相应的NID字符串名称生成相应的非对称公共密钥参数。

    使用密钥参数生成密钥时，用到的bigint类型需要以大端模式输入，且必须为正数。

2. 创建[ECCKeyPairSpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#struct-ecckeypairspec)对象，并且algName设置为SM2，用于指定SM2算法中密钥对包含的参数。

3. 调用[createAsyKeyGeneratorBySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createasykeygeneratorbyspecasykeyspec)，将ECCKeyPairSpec对象传入，创建非对称密钥生成器。

4. 调用[generateKeyPair](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-generatekeypair-1)，得到各项数据与密钥参数一致的密钥对（KeyPair）。

5. 调用[getAsyKeySpec](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-getasykeyspecasykeyspecitem)，获取SM2算法中的椭圆曲线参数。

根据椭圆曲线名生成SM2密钥对的示例如下：

```cangjie
import kit.CryptoArchitectureKit.*
import std.math.numeric.BigInt
import ohos.base.BusinessException

func genSM2KeyPairSpec() {
    var sm2CommonParamsSpec = ECCKeyUtil.genECCCommonParamsSpec('NID_sm2')
    sm2CommonParamsSpec.specType = AsyKeySpecType.KEY_PAIR_SPEC
    let sm2KeyPairSpec: ECCKeyPairSpec = ECCKeyPairSpec(
        params: sm2CommonParamsSpec,
        sk: BigInt.parse('6330B599ECD23ABDC74B9A5B7B5E00E553005F72743101C5FAB83AEB579B7074', radix: 16),
        pk: Point(
            x: BigInt.parse('67F3B850BDC0BA5D3A29D8A0883C4B17612AB84F87F18E28F77D824A115C02C4', radix: 16),
            y: BigInt.parse('D48966CE754BBBEDD6501A1385E1B205C186E926ADED44287145E8897D4B2071', radix: 16)
        )
    )
    return sm2KeyPairSpec
}

func sm2Test() {
    let sm2KeyPairSpec = genSM2KeyPairSpec()
    let generatorBySpec = createAsyKeyGeneratorBySpec(sm2KeyPairSpec)
    try {
        let keyPair = generatorBySpec.generateKeyPair()
        let sm2CurveName = keyPair.priKey.getAsyKeySpec(AsyKeySpecItem.ECC_CURVE_NAME_STR)
        AppLog.info('ECC_CURVE_NAME_STR: ${sm2CurveName}') // NID_sm2
    } catch (e: BusinessException) {
        AppLog.error("get key pair result fail, ${e.code}, ${e.message}")
    }
}
```