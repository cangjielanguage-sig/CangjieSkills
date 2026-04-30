## func anonAttestKeyItem(String, HuksOptions)

```cangjie
public func anonAttestKeyItem(keyAlias: String, options: HuksOptions): Array<String>
```

**功能：** 获取匿名化密钥证书。该操作需要联网进行，且耗时较长。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|keyAlias|String|是|密钥别名，存放待获取证书密钥的别名。|
|options|[HuksOptions](#class-huksoptions)|是|用于获取证书时指定所需参数与数据。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回密钥证书链。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |801|Capability not supported.|
  |12000001|algorithm mode is not supported.|
  |12000002|algorithm param is missing.|
  |12000003|algorithm param is invalid.|
  |12000004|operating file failed.|
  |12000005|IPC communication failed.|
  |12000006|error occurred in crypto engine.|
  |12000011|queried entity does not exist.|
  |12000012|external error.|
  |12000014|memory is insufficient.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.UniversalKeystoreKit.*

let keyAlias = "test_rsa_anno"
// generate key
generateKeyItem(
    keyAlias,
    HuksOptions(
        [
            HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_RSA),
            HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_RSA_KEY_SIZE_2048),
            HuksParam(HuksTag.HUKS_TAG_PURPOSE, HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY),
            HuksParam(HuksTag.HUKS_TAG_DIGEST, HuksKeyDigest.HUKS_DIGEST_SHA256),
            HuksParam(HuksTag.HUKS_TAG_PADDING, HuksKeyPadding.HUKS_PADDING_PSS),
            HuksParam(HuksTag.HUKS_TAG_BLOCK_MODE, HuksCipherMode.HUKS_MODE_ECB)
        ],
        None
    )
)

let challenge = "hi_challenge_data"
let chains = anonAttestKeyItem(
    keyAlias,
    HuksOptions(
        [
            HuksParam(HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE, HuksParamValue.bytes(challenge.toArray())),
            HuksParam(HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS, HuksParamValue.bytes(keyAlias.toArray()))
        ],
        None
    )
)
```