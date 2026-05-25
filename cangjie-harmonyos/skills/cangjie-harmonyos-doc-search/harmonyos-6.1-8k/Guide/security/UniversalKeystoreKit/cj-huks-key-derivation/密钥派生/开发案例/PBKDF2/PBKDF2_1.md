### PBKDF2

<!-- compile -->

```cangjie
/*
 * 以下以PBKDF2密钥的操作使用为例
 */
import kit.PerformanceAnalysisKit.Hilog
import kit.UniversalKeystoreKit.*

func loggerInfo(str: String) {
    Hilog.info(0, "CangjieTest", str)
}

/*
 * 确定密钥别名和封装密钥属性参数集
 */
let srcKeyAlias = "pbkdf2_Key"
let salt = "mySalt"
let iterationCount: UInt32 = 10000
let derivedKeySize: UInt32 = 32
var handle: ?HuksHandleId = None
var finishOutData: ?Array<UInt8> = None

/* 集成生成密钥参数集 */
let properties: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_AES),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DIGEST,
        HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_SIZE,
        HuksParamValue.Uint32Value(HuksKeySize.HUKS_AES_KEY_SIZE_128),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
        HuksParamValue.Uint32Value(HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS),
    )
]
let huksOptions: HuksOptions = HuksOptions(
    properties: properties,
    inData: Bytes()
)

/* 集成init时密钥参数集 */
let initProperties: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_PBKDF2),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DIGEST,
        HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_SHA256),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DERIVE_KEY_SIZE,
        HuksParamValue.Uint32Value(derivedKeySize),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_ITERATION,
        HuksParamValue.Uint32Value(iterationCount),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_SALT,
        HuksParamValue.BytesValue(salt.toArray()),
    )
]
let initOptions: HuksOptions = HuksOptions(
    properties: initProperties,
    inData: Bytes()
)

/* 集成finish时密钥参数集 */
let finishProperties: Array<HuksParam> = [
    HuksParam(
        HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
        HuksParamValue.Uint32Value(HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_IS_KEY_ALIAS,
        HuksParamValue.BooleanValue(true),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_ALGORITHM,
        HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_AES),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_SIZE,
        HuksParamValue.Uint32Value(HuksKeySize.HUKS_AES_KEY_SIZE_256),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PURPOSE,
        HuksParamValue.Uint32Value(1 | 2),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_DIGEST,
        HuksParamValue.Uint32Value(HuksKeyDigest.HUKS_DIGEST_NONE),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_KEY_ALIAS,
        HuksParamValue.BytesValue(srcKeyAlias.toArray()),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_PADDING,
        HuksParamValue.Uint32Value(HuksKeyPadding.HUKS_PADDING_NONE),
    ),
    HuksParam(
        HuksTag.HUKS_TAG_BLOCK_MODE,
        HuksParamValue.Uint32Value(HuksCipherMode.HUKS_MODE_ECB),
    )
]
let finishOptions: HuksOptions = HuksOptions(
    properties: finishProperties,
    inData: Bytes()
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
    loggerInfo("enter generateKeyItem")
    let throwObject: throwObject = throwObject(false)
    try {
        generateKeyItem(keyAlias, huksOptions, throwObject)
    } catch (e: Exception) {
        loggerInfo("generateKeyItem input arg invalid, ${e}")
    }
}