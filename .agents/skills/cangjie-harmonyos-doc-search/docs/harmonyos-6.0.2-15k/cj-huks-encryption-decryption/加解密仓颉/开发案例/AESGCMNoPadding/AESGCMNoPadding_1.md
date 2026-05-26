### AES/GCM/NoPadding

```cangjie
/*
 * 以下以AES/GCM/NoPadding的操作使用为例
 */
import kit.UniversalKeystoreKit.*

let aesKeyAlias = 'test_aesKeyAlias' // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
var handle: ?HuksHandle = None
let plainText = '123456' // 待加密的明文数据
var cipherData: ?Array<UInt8> = None // 加密后的密文数据
let AAD = '1234567890123456'
let NONCE = '001122334455' // 此处为样例代码，实际使用需采用随机值

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

func GetAesGcmEncryptProperties() {
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
            HuksKeyPadding.HUKS_PADDING_NONE
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksCipherMode.HUKS_MODE_GCM
        ),
        HuksParam(
            HuksTag.HUKS_TAG_NONCE,
            bytes(StringToUint8Array(NONCE))
        ),
        HuksParam(
            HuksTag.HUKS_TAG_ASSOCIATED_DATA,
            bytes(StringToUint8Array(AAD))
        )
    ]
    return properties
}

func GetAesGcmDecryptProperties(cipherData: Array<UInt8>) {
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
            HuksKeyPadding.HUKS_PADDING_NONE
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksCipherMode.HUKS_MODE_GCM
        ),
        HuksParam(
            HuksTag.HUKS_TAG_NONCE,
            bytes(StringToUint8Array(NONCE))
        ),
        HuksParam(
            HuksTag.HUKS_TAG_ASSOCIATED_DATA,
            bytes(StringToUint8Array(AAD))
        ),
        HuksParam(
            HuksTag.HUKS_TAG_AE_TAG,
            bytes(cipherData.slice(cipherData.size - 16, 16))
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
    let encryptProperties = GetAesGcmEncryptProperties()
    let options: HuksOptions = HuksOptions(
        encryptProperties,
        StringToUint8Array(plainText)
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
    let decryptOptions = GetAesGcmDecryptProperties(cipherData.getOrThrow())
    let options: HuksOptions = HuksOptions(
        decryptOptions,
        cipherData.getOrThrow().slice(
            0,
            cipherData.getOrThrow().size - 16
        )
    )
    // 调用initSession获取handle，aesKeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(aesKeyAlias, options).handle
    // 调用finishSession获取解密后的数据
    let result = finishSession(handle.getOrThrow(), options)
}