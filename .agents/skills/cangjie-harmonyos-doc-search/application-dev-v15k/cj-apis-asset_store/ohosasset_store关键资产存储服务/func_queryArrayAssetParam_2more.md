## func query(Array\<AssetParam>)

```cangjie
public func query(query: Array<AssetParam>): Array<Array<AssetParam>>
```

**功能：** 查询一条或多条符合条件的关键资产。若查询需要用户认证的关键资产，则需要在本函数前调用[preQuery](#func-prequeryarrayassetparam)，在本函数后调用[postQuery](#func-postqueryarrayassetparam)。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|Array\<[AssetParam](#enum-assetparam)>|是|-|关键资产的查询条件，如别名、访问控制属性、自定义数据等。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Array\<[AssetParam](#enum-assetparam)>>|返回查询结果列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[关键资产存储服务(ASSET)错误码](../../errorcodes/cj-errorcode-asset.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:1. Incorrect parameter types.2. Parameter verification failed.|
  |24000001|The ASSET service is unavailable.|
  |24000002|The asset is not found.|
  |24000004|Access denied.|
  |24000005|The screen lock status does not match.|
  |24000006|Insufficient memory.|
  |24000007|The asset is corrupted.|
  |24000008|The database operation failed.|
  |24000009|The cryptography operation failed.|
  |24000010|IPC failed.|
  |24000011|Calling the Bundle Manager service failed.|
  |24000012|Calling the OS Account service failed.|
  |24000013|Calling the Access Token service failed.|
  |24000017|The capability is not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AssetStoreKit.*

let qry_alias: AssetParam = AssetParam.ALIAS("demo_alias".toArray())
let query_attr: Array<AssetParam> = [qry_alias]
let query_res: Array<Array<AssetParam>> = query(query_attr)
```

## func remove(Array\<AssetParam>)

```cangjie
public func remove(query: Array<AssetParam>): Unit
```

**功能：** 删除符合条件的一条或多条关键资产。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|Array\<[AssetParam](#enum-assetparam)>|是|-|待删除关键资产的搜索条件，如别名、访问控制属性、自定义数据等。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[关键资产存储服务(ASSET)错误码](../../errorcodes/cj-errorcode-asset.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:1. Incorrect parameter types.2. Parameter verification failed.|
  |24000001|The ASSET service is unavailable.|
  |24000002|The asset is not found.|
  |24000006|Insufficient memory.|
  |24000007|The asset is corrupted.|
  |24000008|The database operation failed.|
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
let remove_attr: Array<AssetParam> = [alias]
let query_res: Array<Array<AssetParam>> = query(remove_attr)
if(!query_res.isEmpty()){
    remove(remove_attr)
}
```