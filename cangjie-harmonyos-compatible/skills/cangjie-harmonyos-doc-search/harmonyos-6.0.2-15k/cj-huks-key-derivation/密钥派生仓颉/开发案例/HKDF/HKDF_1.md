### HKDF

```cangjie
/*
 * 以下以HKDF密钥的操作使用为例
 */
import kit.UniversalKeystoreKit.*

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let srcKeyAlias = "hkdf_Key"
let deriveHkdfInData = "deriveHkdfTestIndata"
var handle: ?HuksHandle = None
var finishOutData: ?Array<UInt8> = None
let HuksKeyDeriveKeySize: UInt32 = 32
/* 集成生成密钥参数集 */
let properties: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksKeyAlg.HUKS_ALG_AES,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DIGEST,
        HuksKeyDigest.HUKS_DIGEST_SHA256,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_SIZE,
        HuksKeySize.HUKS_AES_KEY_SIZE_128,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
        HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
    )
]
let huksOptions: HuksOptions = HuksOptions(
    properties,
    []
)
/* 集成init时密钥参数集 */
let initProperties: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksKeyAlg.HUKS_ALG_HKDF,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DIGEST,
        HuksKeyDigest.HUKS_DIGEST_SHA256,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DERIVE_KEY_SIZE,
        uint32(HuksKeyDeriveKeySize),
    )
]
var initOptions: HuksOptions = HuksOptions(
    initProperties,
    None
)
/* 集成finish时密钥参数集 */
let finishProperties: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
        HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_IS_KEY_ALIAS,
        boolean(true),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksKeyAlg.HUKS_ALG_AES,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_SIZE,
        HuksKeySize.HUKS_AES_KEY_SIZE_256,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DIGEST,
        HuksKeyDigest.HUKS_DIGEST_NONE,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_ALIAS,
        bytes(StringToUint8Array(srcKeyAlias)),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PADDING,
        HuksKeyPadding.HUKS_PADDING_NONE,
    ),
    HuksParam(
        HuksTag.HUKS_TAG_BLOCK_MODE,
        HuksCipherMode.HUKS_MODE_ECB,
    )
]
let finishOptions: HuksOptions = HuksOptions(
    finishProperties,
    []
)

func StringToUint8Array(str: String) {
    return str.toArray()
}

class throwObject {
    var isThrow: Bool = false

    init(isThrow: Bool) {
        this.isThrow = isThrow
    }
}

func generateKeyItem(keyAlias: String, huksOptions: HuksOptions, throwObject: throwObject) {
    try {
        generateKeyItem(keyAlias, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}

func publicGenKeyFunc(keyAlias: String, huksOptions: HuksOptions) {
    AppLog.info("enter generateKeyItem")
    let throwObject: throwObject = throwObject(false)
    try {
        generateKeyItem(keyAlias, huksOptions, throwObject)
    } catch (e: Exception) {
        AppLog.error("generateKeyItem input arg invalid, ${e}")
    }
}

func initSession(keyAlias: String, huksOptions: HuksOptions, throwObject: throwObject) {
    return try {
        initSession(keyAlias, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}

func publicInitFunc(keyAlias: String, huksOptions: HuksOptions) {
    AppLog.info("enter doInit")
    let throwObject: throwObject = throwObject(false)
    try {
        handle = initSession(keyAlias, huksOptions, throwObject).handle
    } catch (e: Exception) {
        AppLog.error("doInit input arg invalid, ${e}")
    }
}

func updateSession(handle: HuksHandle, huksOptions: HuksOptions, throwObject: throwObject) {
    return try {
        updateSession(handle, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}