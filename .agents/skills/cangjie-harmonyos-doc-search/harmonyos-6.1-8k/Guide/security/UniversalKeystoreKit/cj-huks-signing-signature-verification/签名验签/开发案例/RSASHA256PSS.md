### RSA/SHA256/PSS

<!-- compile -->

```cangjie
/*
 * 密钥算法为RSA，摘要算法为SHA256，填充模式为PSS
 */
import kit.UniversalKeystoreKit.*

let keyAlias = 'test_rsaKeyAlias'
var handle: ?HuksHandleId = None
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
            HuksParamValue.Uint32Value(4 | 8)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_PSS)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_DIGEST,
            HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256)
        )
    ]
    return properties
}

func GetRsaSignProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_RSA)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_PSS)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_DIGEST,
            HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN)
        )
    ]
    return properties
}

func GetRsaVerifyProperties() {
    let properties: Array<HuksParam> = [
        HuksParam(
            HuksTag.HUKS_TAG_ALGORITHM,
            HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_RSA)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PADDING,
            HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_PSS)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_DIGEST,
            HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256)
        ),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY)
        )
    ]
    return properties
}

func GenerateRsaKey(keyAlias: String) {
    let genProperties = GetRsaGenerateProperties()
    let options: HuksOptions = HuksOptions(properties: genProperties, inData: Bytes())
    generateKeyItem(keyAlias, options)
}

func Sign(keyAlias: String, plaintext: String) {
    let signProperties = GetRsaSignProperties()
    let options: HuksOptions = HuksOptions(
        properties: signProperties,
        inData: StringToUint8Array(plaintext)
    )
    handle = initSession(keyAlias, options).handle

    if (let Some(handle) <- handle) {
        signature = finishSession(handle, options)
    }
}

func Verify(keyAlias: String, plaintext: String, signature: Array<UInt8>) {
    let verifyProperties = GetRsaVerifyProperties()
    var options: HuksOptions = HuksOptions(
        properties: verifyProperties,
        inData: StringToUint8Array(plaintext)
    )
    handle = initSession(keyAlias, options).handle

    if (let Some(handle) <- handle) {
        updateSession(handle, options)

        options.inData = signature
        finishSession(handle, options)
    }
}

func DeleteRsaKey(keyAlias: String) {
    let emptyOptions: HuksOptions = HuksOptions()
    deleteKeyItem(keyAlias, emptyOptions)
}

func testSignVerify() {
    GenerateRsaKey(keyAlias)
    Sign(keyAlias, plaintext)
    Verify(keyAlias, plaintext, signature.getOrThrow())
    DeleteRsaKey(keyAlias)
}
```