func rsaUsePubKeySpecGet() {
    let rsaPubKeySpec = genRsa2048PubKeySpec()
    let rsaGeneratorSpec = createAsyKeyGeneratorBySpec(rsaPubKeySpec)
    try {
        let pubKey = rsaGeneratorSpec.generatePubKey()
        let nBN = pubKey.getAsyKeySpec(AsyKeySpecItem.RSA_N_BN)
        let eBN = pubKey.getAsyKeySpec(AsyKeySpecItem.RSA_PK_BN)
        if (compareRsaPubKeyBySpec(rsaPubKeySpec, nBN, eBN) != true) {
            AppLog.error('error pub key big number')
        }
        AppLog.info('n, e in the pubKey are same as the spec.')
    } catch (e: BusinessException) {
        AppLog.error("get pub key result fail, ${e.code}, ${e.message}")
    }
}
```