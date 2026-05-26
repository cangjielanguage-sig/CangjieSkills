func showEccSpecDetailInfo(key: PriKey, keyType: String) {
    AppLog.info('show detail of ' + keyType + ':')
    try {
        let p = key.getAsyKeySpec(AsyKeySpecItem.ECC_FP_P_BN)
        AppLog.error(p)
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
        let sk = key.getAsyKeySpec(AsyKeySpecItem.ECC_SK_BN);
        showBigIntInfo('--- sk', sk)
    } catch (e: BusinessException) {
        AppLog.error("getAsyKeySpec failed, ${e.code}, ${e.message}")
    }
}

// 根据EccCommonSpec实例生成ECC密钥对，获取密钥规格。
func testEccUseCommKeySpecGetSync() {
    try {
        let commKeySpec = genEccCommonSpec() // 使用参数属性，构造ECC公私钥公共密钥参数对象。
        let generatorBySpec = createAsyKeyGeneratorBySpec(commKeySpec) // 使用密钥参数对象创建生成器。
        let keyPair = generatorBySpec.generateKeyPair() // Generate an ECC key pair.
        showEccSpecDetailInfo(keyPair.priKey, 'priKey') // 对私钥获取相关密钥参数属性。
        showEccSpecDetailInfo(keyPair.pubKey, 'pubKey') // 对公钥获取相关密钥参数属性。
    } catch (e: BusinessException) {
        // 逻辑错误等异常在此捕获。
        AppLog.error("get key pair result fail, ${e.code}, ${e.message}")
    }
}
```