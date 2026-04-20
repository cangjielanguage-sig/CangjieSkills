### AES/GCM/NoPadding

<!-- compile -->

```cangjie
/*
 * 以下以AES/GCM/NoPadding的操作使用为例
 */
import kit.PerformanceAnalysisKit.Hilog
import kit.BasicServicesKit.*
import kit.CoreFileKit.*
import kit.AbilityKit.*
import kit.UniversalKeystoreKit.*

let aesKeyAlias = 'test_aesKeyAlias' // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
var handle: ?HuksHandleId = None
let plainText = 'PLAIN_TEXT' // 待加密的明文数据
var cipherData: ?Array<UInt8> = [] // 加密后的密文数据
let AAD = 'TEST_AAD' // 此处为样例代码，实际使用需采用随机值
let NONCE = 'TEST_NONCE' // 此处为样例代码，实际使用需采用随机值

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
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_AES)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksParamValue.Uint32Value(HuksKeySize.HUKS_AES_KEY_SIZE_128)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(1 | 2)
        )
    ]
    return properties
}

func GetAesGcmEncryptProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_AES)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksParamValue.Uint32Value(HuksKeySize.HUKS_AES_KEY_SIZE_128)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_NONE)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksParamValue.Uint32Value(HuksCipherMode.HUKS_MODE_GCM)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_NONCE,
            HuksParamValue.BytesValue(NONCE.toArray())
        ),
        HuksParam(
            HuksTag.HUKS_TAG_ASSOCIATED_DATA,
            HuksParamValue.BytesValue(AAD.toArray())
        )
    ]
    return properties
}

func GetAesGcmDecryptProperties(cipherData: Array<UInt8>) {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_AES)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_KEY_SIZE,
            HuksParamValue.Uint32Value(HuksKeySize.HUKS_AES_KEY_SIZE_128)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_NONE)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_BLOCK_MODE,
            HuksParamValue.Uint32Value(HuksCipherMode.HUKS_MODE_GCM)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_NONCE,
            HuksParamValue.BytesValue(NONCE.toArray())
        ),
        HuksParam(
            HuksTag.HUKS_TAG_ASSOCIATED_DATA,
            HuksParamValue.BytesValue(AAD.toArray())
        ),
        HuksParam(
            HuksTag.HUKS_TAG_AE_TAG,
            HuksParamValue.BytesValue(cipherData.slice(cipherData.size - 16, 16).toArray())
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
    let options: HuksOptions = HuksOptions(properties: genProperties, inData: Bytes())
    // 调用generateKeyItem，aesKeyAlias是密钥别名，由用户指定
    generateKeyItem(aesKeyAlias, options)
}