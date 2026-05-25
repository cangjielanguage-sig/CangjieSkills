## func importWrappedKeyItem(String, String, HuksOptions)

```cangjie
public func importWrappedKeyItem(keyAlias: String, wrappingKeyAlias: String, options: HuksOptions): Unit
```

**功能：** 导入加密密钥。

**系统能力：** SystemCapability.Security.Huks.Extension

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyAlias|String|是|-|密钥别名，存放待导入密钥的别名。|
|wrappingKeyAlias|String|是|-|密钥别名，对应密钥用于解密加密的密钥数据。|
|options|[HuksOptions](#class-huksoptions)|是|-|用于导入时所需TAG和需要导入的加密的密钥数据。其中密钥使用的算法、密钥用途、密钥长度为必选参数。|

**异常：**

- BusinessException：对应错误码如下表，详见[HUKS错误码](./cj-errorcode-huks.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | check permission failed. |
  | 801 | api is not supported. |
  | 12000001 | algorithm mode is not supported. |
  | 12000002 | algorithm param is missing. |
  | 12000003 | algorithm param is invalid. |
  | 12000004 | operating file failed. |
  | 12000005 | IPC communication failed. |
  | 12000006 | error occurred in crypto engine. |
  | 12000011 | queried entity does not exist. |
  | 12000012 | Device environment or input parameter abnormal. |
  | 12000013 | queried credential does not exist. |
  | 12000014 | memory is insufficient. |
  | 12000015 | Failed to obtain the security information via UserIAM. |
  | 12000017 | The key with same alias is already exist. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.UniversalKeystoreKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

let keyAlias = "KEY_ALIAS" // 密钥别名，在生成密钥时指定，在加密、解密和删除密钥时使用
let wrappingKeyAlias = "test_import_wrapped_wrong_wrapping_key"

try {
    importWrappedKeyItem(
        keyAlias,
        wrappingKeyAlias,
        HuksOptions(
            properties:  [
                HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksParamValue.Uint32Value(HuksKeyAlg.HUKS_ALG_AES)),
                HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksParamValue.Uint32Value( HuksKeySize.HUKS_AES_KEY_SIZE_256)),
                HuksParam(
                    HuksTag.HUKS_TAG_PURPOSE,
                    HuksParamValue.Uint32Value(HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT)
                )
            ],
            inData: Bytes()
        )
    )} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```