### SM2

```cangjie
/*
 * 以下以SM2模式的操作使用为例
 */
import kit.UniversalKeystoreKit.*

let sm2KeyAlias = 'test_sm2KeyAlias' // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
var handle: ?HuksHandle = None
let plainText = '123456' // 待加密的明文
var cipherData: ?Array<UInt8> = None // 加密后的密文数据

func StringToUint8Array(str: String) {
    return str.toArray()
}

func Uint8ArrayToString(fileData: Array<UInt8>) {
    return String.fromUtf8(fileData)
}

func GetSm2GenerateProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_SM2
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_SM2_KEY_SIZE_256
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        )
    ]
    return properties
}

func GetSm2EncryptProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_SM2
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_SM2_KEY_SIZE_256
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
        ),
        HuksParam(
            HuksTag.HUKS_TAG_DIGEST,
            HuksKeyDigest.HUKS_DIGEST_SM3
        )
    ]
    return properties
}

func GetSm2DecryptProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_SM2
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_SM2_KEY_SIZE_256
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        ),
        HuksParam(
            HuksTag.HUKS_TAG_DIGEST,
            HuksKeyDigest.HUKS_DIGEST_SM3
        )
    ]
    return properties
}

/*
 * 模拟生成密钥场景
 */
func GenerateSm2Key() {
    // 获取生成密钥算法参数配置
    let genProperties = GetSm2GenerateProperties()
    let options: HuksOptions = HuksOptions(genProperties, None)
    // 调用generateKeyItem生成密钥，sm2KeyAlias是密钥别名，在生成密钥时进行指定的
    generateKeyItem(sm2KeyAlias, options)
}

/*
 * 模拟加密场景
 */
func EncryptDataSm2() {
    // 获取加密算法参数配置
    let encryptProperties = GetSm2EncryptProperties()
    let options: HuksOptions = HuksOptions(
        encryptProperties,
        StringToUint8Array(plainText) // plainText是待加密的明文数据
    )
    // 调用initSession获取handle，sm2KeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(sm2KeyAlias, options).handle
    // 调用finishSession获取加密后的密文
    finishSession(handle.getOrThrow(), options)
}

/*
 * 模拟解密场景
 */
func DecryptDataSm2() {
    // 获取解密算法参数配置
    let decryptOptions = GetSm2DecryptProperties()
    let options: HuksOptions = HuksOptions(
        decryptOptions,
        cipherData // 加密后的密文数据
    )
    // 调用initSession获取handle，sm2KeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(sm2KeyAlias, options).handle
    // 调用finishSession获取解密后的数据
    finishSession(handle.getOrThrow(), options)
}

/*
 * 模拟删除密钥场景
 */
func DeleteKey() {
    let emptyOptions: HuksOptions = HuksOptions.NONE
    // 调用deleteKeyItem删除密钥，sm2KeyAlias是密钥别名，在生成密钥时进行指定的
    deleteKeyItem(sm2KeyAlias, emptyOptions)
}
```