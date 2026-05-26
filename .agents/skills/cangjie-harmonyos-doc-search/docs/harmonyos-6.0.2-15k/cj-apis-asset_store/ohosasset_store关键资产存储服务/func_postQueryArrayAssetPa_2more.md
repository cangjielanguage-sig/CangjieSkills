## func postQuery(Array\<AssetParam>)

```cangjie
public func postQuery(handle: Array<AssetParam>): Unit
```

**功能：** 查询的后置处理，用于需要用户认证的关键资产。需与[preQuery](#func-prequeryarrayassetparam)函数成对出现。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|handle|Array\<[AssetParam](#enum-assetparam)>|是|-|待处理的查询句柄，当前包含preQuery执行成功返回的挑战值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[关键资产存储服务(ASSET)错误码](../../errorcodes/cj-errorcode-asset.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed.|
  |24000001|The ASSET service is unavailable.|
  |24000006|Insufficient memory.|
  |24000010|IPC failed.|
  |24000011|Calling the Bundle Manager service failed.|
  |24000012|Calling the OS Account service failed.|
  |24000013|Calling the Access Token service failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AssetStoreKit.*

let alias: AssetParam = AssetParam.ALIAS("demo_alias".toArray())
let pre_query: Array<AssetParam> = [alias]
let res = preQuery(pre_query)
let challenge: AssetParam = AssetParam.ALIAS(res.toArray())
postQuery(challenge)
```

## func preQuery(Array\<AssetParam>)

```cangjie
public func preQuery(query: Array<AssetParam>): Array<UInt8>
```

**功能：** 查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[query](#func-queryarrayassetparam)、[postQuery](#func-postqueryarrayassetparam)。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|query|Array\<[AssetParam](#enum-assetparam)>|是|-|关键资产的查询条件，如别名、访问控制属性、自定义数据等。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回挑战值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[关键资产存储服务(ASSET)错误码](../../errorcodes/cj-errorcode-asset.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:1. Incorrect parameter types.2. Parameter verification failed.|
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
  |24000016|The cache exceeds the limit.|
  |24000017|The capability is not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AssetStoreKit.*

let alias: AssetParam = AssetParam.ALIAS("demo_alias".toArray())
let pre_query: Array<AssetParam> = [alias]
let challenge = preQuery(pre_query)
```