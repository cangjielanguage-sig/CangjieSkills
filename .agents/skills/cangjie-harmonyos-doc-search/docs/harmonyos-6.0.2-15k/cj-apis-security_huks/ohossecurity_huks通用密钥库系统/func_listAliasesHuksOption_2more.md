## func listAliases(HuksOptions)

```cangjie
public func listAliases(options: HuksOptions): Array<String>
```

**功能：** 查询密钥别名集接口。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|options|[HuksOptions](#class-huksoptions)|是|listAliases操作的参数集合。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回满足options描述的所有密钥别名。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |12000004|operating file failed.|
  |12000005|IPC communication failed.|
  |12000012|external error.|
  |12000014|memory is insufficient.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.UniversalKeystoreKit.*

let keyAliases = ["list_alias_1", "list_alias_2", "list_alias_3", "list_alias_4"]
let options = HuksOptions(
    [
        HuksParam(HuksTag.HUKS_TAG_ALGORITHM, HuksKeyAlg.HUKS_ALG_AES),
        HuksParam(HuksTag.HUKS_TAG_KEY_SIZE, HuksKeySize.HUKS_AES_KEY_SIZE_128),
        HuksParam(
            HuksTag.HUKS_TAG_PURPOSE,
            HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
        )
    ],
    Option.None
)
for (keyAlias in keyAliases) {
    generateKeyItem(keyAlias, options)
}
for (keyAlias in listAliases(options)) {
    // true
    keyAliases.contains(keyAlias)
}
```

## func updateSession(HuksHandle, HuksOptions)

```cangjie
public func updateSession(handle: HuksHandle, options: HuksOptions): Option<Array<UInt8>>
```

**功能：** updateSession操作密钥接口。[security_huks.initSession](#func-initsessionstring-huksoptions)、[security_huks.updateSession](#func-updatesessionhukshandle-huksoptions)、[security_huks.finishSession](#func-finishsessionhukshandle-huksoptions)为三段式接口，需要一起使用。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|handle|[HuksHandle](#class-hukshandle)|是|updateSession操作的handle。|
|options|[HuksOptions](#class-huksoptions)|是|updateSession的参数集合。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<Array\<UInt8>>|输出密钥更新结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息      |
  | :-------- | :------------- |
  | 401 | Parameter error. |
  | 801 | Capability not supported.  |
  | 12000001 | algorithm mode is not supported. |
  | 12000002 | algorithm param is missing. |
  | 12000003 | algorithm param is invalid. |
  | 12000004 | operating file failed. |
  | 12000005 | IPC communication failed. |
  | 12000006 | error occurred in crypto engine. |
  | 12000007 | this credential is already invalidated permanently. |
  | 12000008 | verify authtoken failed. |
  | 12000009 | authtoken is already timeout. |
  | 12000011 | queried entity does not exist. |
  | 12000012 | external error. |
  | 12000014 | memory is insufficient. |