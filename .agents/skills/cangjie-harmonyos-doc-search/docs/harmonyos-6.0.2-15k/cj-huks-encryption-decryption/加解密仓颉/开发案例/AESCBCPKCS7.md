### AES/CBC/PKCS7

```cangjie
/*
 * 以下以AES/CBC/PKCS7的操作使用为例
 */
import kit.UniversalKeystoreKit.*

let aesKeyAlias = 'test_aesKeyAlias' // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
var handle: ?HuksHandle = None
let plainText = '123456' // 待加密的明文
let IV = 'TEST_IV' // 此处为样例代码，实际使用需采用随机值
var cipherData: ?Array<UInt8> = None // 加密后的密文数据

func StringToUint8Array(str: String) {
    return str.toArray()
}

func Uint8ArrayToString(fileData: Array<UInt8>) {
    return String.fromUtf8(fileData)
}

func GetAesGenerateProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_AES
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_AES_KEY_SIZE_128
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        )
    ]
    return properties
}

func GetAesEncryptProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_AES
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_AES_KEY_SIZE_128
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksKeyPadding.HUKS_PADDING_PKCS7
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksCipherMode.HUKS_MODE_CBC
        ),
        HuksParam(
            HuksTag.HUKS_TAG_IV,
            bytes(StringToUint8Array(IV))
        )
    ]
    return properties
}

func GetAesDecryptProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_AES
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_AES_KEY_SIZE_128
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksKeyPadding.HUKS_PADDING_PKCS7
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksCipherMode.HUKS_MODE_CBC
        ),
        HuksParam(
            HuksTag.HUKS_TAG_IV,
            bytes(StringToUint8Array(IV))
        )
    ]
    return properties
}

/*
 * 模拟生成密钥场景
 */
func GenerateAesKey() {
    // 获取生成密钥算法参数配置
    let genProperties = GetAesGenerateProperties()
    let options: HuksOptions = HuksOptions(genProperties, None)

    // 调用generateKeyItem，aesKeyAlias是密钥别名，由用户指定
    generateKeyItem(aesKeyAlias, options)
}

/*
 * 模拟加密场景
 */
func EncryptData() {
    // 获取加密算法参数配置
    let encryptProperties = GetAesEncryptProperties()
    let options: HuksOptions = HuksOptions(
        encryptProperties,
        StringToUint8Array(plainText) // plainText是待加密的数据
    )
    // 调用initSession获取handle，aesKeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(aesKeyAlias, options).handle
    // 调用finishSession获取加密后的密文
    cipherData = finishSession(handle.getOrThrow(), options)
}

/*
 * 模拟解密场景
 */
func DecryptData() {
    // 获取解密算法参数配置
    let decryptOptions = GetAesDecryptProperties()
    let options: HuksOptions = HuksOptions(
        decryptOptions,
        cipherData
    )
    // 调用initSession获取handle，aesKeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(aesKeyAlias, options).handle
    // 调用finishSession获取解密后的数据
    let result = finishSession(handle.getOrThrow(), options)
}

/*
 * 模拟删除密钥场景
 */
func DeleteKey() {
    let emptyOptions: HuksOptions = HuksOptions.NONE
    // 调用deleteKeyItem删除密钥，aesKeyAlias是密钥别名，在生成密钥时进行指定的
    deleteKeyItem(aesKeyAlias, emptyOptions)
}
```