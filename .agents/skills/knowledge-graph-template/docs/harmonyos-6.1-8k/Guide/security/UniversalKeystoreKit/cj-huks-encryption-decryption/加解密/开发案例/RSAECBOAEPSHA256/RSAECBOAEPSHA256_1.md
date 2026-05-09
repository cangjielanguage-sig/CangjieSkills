### RSA/ECB/OAEP/SHA256

<!-- compile -->

```cangjie
/*
 * 以下以RSA/ECB/OAEP/SHA256模式的操作使用为例
 */
import kit.PerformanceAnalysisKit.Hilog
import kit.BasicServicesKit.*
import kit.CoreFileKit.*
import kit.AbilityKit.*
import kit.UniversalKeystoreKit.*

let rsaKeyAlias = 'test_rsaKeyAlias' // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
var handle: ?HuksHandleId = None
let plainText = 'PLAIN_TEXT' // 待加密的明文
var cipherData: ?Array<UInt8> = [] // 加密后的密文数据

func StringToUint8Array(str: String) {
    return str.toArray()
}

func Uint8ArrayToString(fileData: Array<UInt8>) {
    return String.fromUtf8(fileData)
}

func GetRsaGenerateProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_RSA)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksParamValue.Uint32Value(HuksKeySize.HUKS_RSA_KEY_SIZE_2048)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(1 | 2)
        )
    ]
    return properties
}

func GetRsaEncryptProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_RSA)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksParamValue.Uint32Value(HuksKeySize.HUKS_RSA_KEY_SIZE_2048)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_OAEP)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksParamValue.Uint32Value(HuksCipherMode.HUKS_MODE_ECB)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_DIGEST,
            HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256)
        )
    ]
    return properties
}

func GetRsaDecryptProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_RSA)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksParamValue.Uint32Value(HuksKeySize.HUKS_RSA_KEY_SIZE_2048)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_OAEP)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksParamValue.Uint32Value(HuksCipherMode.HUKS_MODE_ECB)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_DIGEST,
            HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256)
        )
    ]
    return properties
}

/*
 * 模拟生成密钥场景
 */
func GenerateRsaKey() {
    // 获取生成密钥算法参数配置
    let genProperties = GetRsaGenerateProperties()
    let options: HuksOptions = HuksOptions(properties: genProperties, inData: Bytes())
    // 调用generateKeyItem，rsaKeyAlias是密钥别名，在生成密钥时进行指定的
    generateKeyItem(rsaKeyAlias, options)
}

/*
 * 模拟加密场景
 */
func EncryptData() {
    // 获取加密算法参数配置
    let encryptProperties = GetRsaEncryptProperties()
    let options: HuksOptions = HuksOptions(
        properties: encryptProperties,
        inData: StringToUint8Array(plainText)
    )
    // 调用initSession获取handle，rsaKeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(rsaKeyAlias, options).handle
    // 调用finishSession获取加密后的密文
    finishSession(handle.getOrThrow(), options)
}