## 以根据密钥参数生成ECC密钥为例

```cangjie
import kit.CryptoArchitectureKit.*
import std.math.numeric.BigInt
import ohos.base.BusinessException
import std.convert.*

func showBigIntInfo(bnName: String, bnValue: ResultSpec) {
    AppLog.info(bnName + ':')
    AppLog.info('. Decimal: ' + BigInt.parse(bnValue.toString()).toString(radix: 16))
}

// 根据关键规范构造EccCommonSpec结构体。EccCommonSpec结构体定义了ECC私钥和公钥的公共参数。
func genEccCommonSpec(): ECCCommonParamsSpec {
    let fieldFp: ECFieldFp = ECFieldFp(
        fieldType: 'Fp',
        p: BigInt.parse('ffffffffffffffffffffffffffffffff000000000000000000000001', radix: 16)
    )
    let G: Point = Point(
        x: BigInt.parse('b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21', radix: 16),
        y: BigInt.parse('bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34', radix: 16)
    )
    let eccCommonSpec: ECCCommonParamsSpec = ECCCommonParamsSpec(
        algName: 'ECC',
        specType: AsyKeySpecType.COMMON_PARAMS_SPEC,
        field: fieldFp,
        a: BigInt.parse('fffffffffffffffffffffffffffffffefffffffffffffffffffffffe', radix: 16),
        b: BigInt.parse('b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4', radix: 16),
        g: G,
        n: BigInt.parse('ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d', radix: 16),
        h: 1
    )
    return eccCommonSpec
}

// 打印ECC密钥规格。
func showEccSpecDetailInfo(key: PubKey, keyType: String) {
    AppLog.info('show detail of ' + keyType + ':')
    try {
        let p = key.getAsyKeySpec(AsyKeySpecItem.ECC_FP_P_BN)
        showBigIntInfo('--- p', p); // length is 224, hex : ffffffffffffffffffffffffffffffff000000000000000000000001
        let a = key.getAsyKeySpec(AsyKeySpecItem.ECC_A_BN)
        showBigIntInfo('--- a', a); // length is 224, hex : fffffffffffffffffffffffffffffffefffffffffffffffffffffffe
        let b = key.getAsyKeySpec(AsyKeySpecItem.ECC_B_BN)
        showBigIntInfo('--- b', b); // length is 224, hex : b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
        let gX = key.getAsyKeySpec(AsyKeySpecItem.ECC_G_X_BN)
        showBigIntInfo('--- gX', gX); // length is 224, hex : b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21
        let gY = key.getAsyKeySpec(AsyKeySpecItem.ECC_G_Y_BN)
        showBigIntInfo('--- gY', gY); // length is 224, hex : bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34
        let n = key.getAsyKeySpec(AsyKeySpecItem.ECC_N_BN)
        showBigIntInfo('--- n', n); // length is 224, hex : ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d
        let h = key.getAsyKeySpec(AsyKeySpecItem.ECC_H_NUM)
        AppLog.warn('--- h: ${h}') // key h: 1
        let fieldType = key.getAsyKeySpec(AsyKeySpecItem.ECC_FIELD_TYPE_STR);
        AppLog.warn('--- field type: ${fieldType}') // key field type: Fp
        let fieldSize = key.getAsyKeySpec(AsyKeySpecItem.ECC_FIELD_SIZE_NUM);
        AppLog.warn('--- field size: ${fieldSize}') // key field size: 224
        let curveName = key.getAsyKeySpec(AsyKeySpecItem.ECC_CURVE_NAME_STR);
        AppLog.warn('--- curve name: ${curveName}') // key curve name: NID_secp224r1
        let pkX = key.getAsyKeySpec(AsyKeySpecItem.ECC_PK_X_BN)
        showBigIntInfo('--- pkX', pkX)
        let pkY = key.getAsyKeySpec(AsyKeySpecItem.ECC_PK_Y_BN)
        showBigIntInfo('--- pkY', pkY)
    } catch (e: BusinessException) {
        AppLog.error("getAsyKeySpec failed, ${e.code}, ${e.message}")
    }
}