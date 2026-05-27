let keyAlias = "test_encrypt_decrypt_cbc_pkcs7"
let plainText = "123456"
let iv = "xxxxxxxxxxxxxxxx" // 用户自定义密钥初始化的向量
let options = HuksOptions(
    [
        HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
        HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_128),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        ),
        HuksParam(HuksTag.HUKS_TAG_PADDING, HuksKeyPadding.HUKS_PADDING_PKCS7),
        HuksParam(HuksTag.HUKS_TAG_BLOCK_MODE, HuksCipherMode.HUKS_MODE_CBC),
        HuksParam(HuksTag.HUKS_TAG_IV, HuksParamValue.bytes(iv.toArray()))
    ],
    None
)
let encOptions = HuksOptions(
    [
        HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
        HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_128),
        HuksParam(HuksTag.HUKS_TAG_PURPOSE, HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT),
        HuksParam(HuksTag.HUKS_TAG_PADDING, HuksKeyPadding.HUKS_PADDING_PKCS7),
        HuksParam(HuksTag.HUKS_TAG_BLOCK_MODE, HuksCipherMode.HUKS_MODE_CBC),
        HuksParam(HuksTag.HUKS_TAG_IV, HuksParamValue.bytes(iv.toArray()))
    ],
    plainText.toArray()
)
generateKeyItem(keyAlias, options)
// encrypt
let handle1 = initSession(keyAlias, encOptions).handle
let cipherData = finishSession(handle1, encOptions)
let decOptions = HuksOptions(
    [
        HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
        HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_128),
        HuksParam(HuksTag.HUKS_TAG_PURPOSE, HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT),
        HuksParam(HuksTag.HUKS_TAG_PADDING, HuksKeyPadding.HUKS_PADDING_PKCS7),
        HuksParam(HuksTag.HUKS_TAG_BLOCK_MODE, HuksCipherMode.HUKS_MODE_CBC),
        HuksParam(HuksTag.HUKS_TAG_IV, HuksParamValue.bytes(iv.toArray()))
    ],
    cipherData
)
// decrypt
let handle2 = initSession(keyAlias, decOptions).handle
let decData = finishSession(handle2, decOptions)
let dec = String.fromUtf8(decData.getOrThrow())
Hilog.info(0, "Hks testEntry", "${plainText == dec}")
abortSession(handle1, HuksOptions([], None))
abortSession(handle2, HuksOptions([], None))
```