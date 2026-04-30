### RSA/SHA256/PKCS1_V1_5

```cangjie
/*
 * 密钥算法为RSA，摘要算法为SHA256，填充模式为PKCS1_V1_5
 */
import kit.UniversalKeystoreKit.*

let keyAlias = 'test_rsaKeyAlias'
var handle: ?HuksHandle = None
let plaintext = '123456'
var signature: ?Array<UInt8> = None

func StringToUint8Array(str: String) {
    return str.toArray()
}

func Uint8ArrayToString(fileData: Array<UInt8>) {
    return String.fromUtf8(fileData)
}

func GetRsaGenerateProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_RSA),
        HuksParam(HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_RSA_KEY_SIZE_2048),
        HuksParam(
            HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
        ),
        HuksParam(HUKS_TAG_PADDING, HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5),
        HuksParam(HUKS_TAG_DIGEST, HuksKeyDigest.HUKS_DIGEST_SHA256)
    ]
    return properties
}

func GetRsaSignProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_RSA
        ),
        HuksParam(
            HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_RSA_KEY_SIZE_2048
        ),
        HuksParam(
            HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
        ),
        HuksParam(
            HUKS_TAG_PADDING,
            HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
        ),
        HuksParam(
            HUKS_TAG_DIGEST,
            HuksKeyDigest.HUKS_DIGEST_SHA256
        )
    ]
    return properties
}

func GetRsaVerifyProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HUKS_TAG_ALGORITHM,
            HuksKeyAlg.HUKS_ALG_RSA
        ),
        HuksParam(
            HUKS_TAG_KEY_SIZE,
            HuksKeySize.HUKS_RSA_KEY_SIZE_2048
        ),
        HuksParam(
            HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
        ),
        HuksParam(
            HUKS_TAG_PADDING,
            HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
        ),
        HuksParam(
            HUKS_TAG_DIGEST,
            HuksKeyDigest.HUKS_DIGEST_SHA256
        )
    ]
    return properties
}

func GenerateRsaKey(keyAlias: String) {
    let genProperties = GetRsaGenerateProperties()
    let options: HuksOptions = HuksOptions(genProperties, None)
    generateKeyItem(keyAlias, options)
}

func Sign(keyAlias: String, plaintext: String) {
    let signProperties = GetRsaSignProperties()
    let options: HuksOptions = HuksOptions(
        signProperties,
        StringToUint8Array(plaintext)
    )
    handle = initSession(keyAlias, options).handle
    signature = finishSession(handle.getOrThrow(), options)
}

func Verify(keyAlias: String, plaintext: String, signature: Array<UInt8>) {
    let verifyProperties = GetRsaVerifyProperties()
    var options: HuksOptions = HuksOptions(
        verifyProperties,
        StringToUint8Array(plaintext)
    )
    handle = initSession(keyAlias, options).handle
    updateSession(handle.getOrThrow(), options)
    options.inData = signature
    finishSession(handle.getOrThrow(), options)
}

func DeleteRsaKey(keyAlias: String) {
    let emptyOptions: HuksOptions = HuksOptions.NONE
    deleteKeyItem(keyAlias, emptyOptions)
}

func testSignVerify() {
    GenerateRsaKey(keyAlias)
    Sign(keyAlias, plaintext)
    Verify(keyAlias, plaintext, signature.getOrThrow())
    DeleteRsaKey(keyAlias)
}
```