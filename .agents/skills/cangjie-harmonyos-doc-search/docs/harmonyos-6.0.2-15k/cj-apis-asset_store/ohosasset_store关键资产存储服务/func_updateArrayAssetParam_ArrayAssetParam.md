## func update(Array\<AssetParam>, Array\<AssetParam>)

```cangjie
public func update(query: Array<AssetParam>, attributesToUpdate: Array<AssetParam>): Unit
```

**功能：** 更新符合条件的一条关键资产。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|Array\<[AssetParam](#enum-assetparam)>|是|-|待更新关键资产的搜索条件，如关键资产别名、访问控制属性、自定义数据等。|
|attributesToUpdate|Array\<[AssetParam](#enum-assetparam)>|是|-|待更新关键资产的属性集合，如关键资产明文、自定义数据等。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[关键资产存储服务(ASSET)错误码](../../errorcodes/cj-errorcode-asset.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed.|
  |24000001|The ASSET service is unavailable.|
  |24000002|The asset is not found.|
  |24000005|The screen lock status does not match.|
  |24000006|Insufficient memory.|
  |24000007|The asset is corrupted.|
  |24000008|The database operation failed.|
  |24000009|The cryptography operation failed.|
  |24000010|IPC failed.|
  |24000011|Calling the Bundle Manager service failed.|
  |24000012|Calling the OS Account service failed.|
  |24000013|Calling the Access Token service failed.|
  |24000015|Getting the system time failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AssetStoreKit.*

let alias:AssetParam = AssetParam.ALIAS("demo_alias".toArray())
let query_attr: Array<AssetParam> = [alias]
let secret:AssetParam = AssetParam.SECRET("demo_pwd_new".toArray())
let data_label_n1:AssetParam = AssetParam.DATA_LABEL_NORMAL_1("demo_label_new".toArray())
let update_attr: Array<AssetParam> = [secret, data_label_n1]
update(query_attr, update_attr)
```