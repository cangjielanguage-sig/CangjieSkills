## 解密

1. 调用[createCipher](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-createcipherstring)，指定字符串参数'AES128|CCM'，创建对称密钥类型为AES128且分组模式为CCM的Cipher实例，用于完成解密操作。

2. 调用[init](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-initcryptomode-key-paramsspec)，设置模式为解密（CryptoMode.DECRYPT_MODE），指定解密密钥（SymKey）和CCM模式对应的解密参数（CcmParamsSpec），初始化解密Cipher实例。

3. 调用[doFinal](../../../API_Reference/source_zh_cn/apis/CryptoArchitectureKit/cj-apis-crypto.md#func-dofinaldatablob)，获取解密后的数据。

## 示例

同步方法示例如下：

```cangjie
import kit.CryptoArchitectureKit.*

func genCcmParamsSpec() {
    let rand: Random = createRandom()
    let ivBlob: DataBlob = rand.generateRandom(7)
    let aadBlob: DataBlob = rand.generateRandom(8)
    let dataTag: Array<UInt8> = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] // 12 bytes
    let tagBlob: DataBlob = DataBlob(dataTag)
    // CCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中。
    let ccmParamsSpec: CcmParamsSpec = CcmParamsSpec("CcmParamsSpec", ivBlob, aadBlob, tagBlob)
    return ccmParamsSpec
}

var ccmParams = genCcmParamsSpec()
// 加密消息。
func encryptMessage(symKey: SymKey, plainText: DataBlob) {
    let cipher = createCipher('AES128|CCM')
    cipher.`init`(ENCRYPT_MODE, symKey, ccmParams)
    let encryptUpdate = cipher.update(plainText);
    // ccm模式加密doFinal时传入空，获得tag数据，并更新至ccmParams对象中。
    ccmParams.authTag = cipher.doFinal(None)
    return encryptUpdate
}

// 解密消息。
func decryptMessage(symKey: SymKey, cipherText: DataBlob) {
    let decoder = createCipher('AES128|CCM')
    decoder.`init`(DECRYPT_MODE, symKey, ccmParams)
    let decryptData = decoder.doFinal(cipherText)
    return decryptData
}

func genSymKeyByData(symKeyData: Array<UInt8>) {
    let symKeyBlob: DataBlob = DataBlob(symKeyData)
    let aesGenerator = createSymKeyGenerator('AES128')
    let symKey = aesGenerator.convertKey(symKeyBlob)
    AppLog.info('convertKey success')
    return symKey
}
```