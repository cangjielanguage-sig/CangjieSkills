# ohos.asset_store（关键资产存储服务）

关键资产存储服务提供了用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、其他关键明文（如银行卡号）等长度较短的用户敏感数据。

## 导入模块

```cangjie
import kit.AssetStoreKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func add(Array\<AssetParam>)

```cangjie
public func add(attributes: Array<AssetParam>): Unit
```

**功能：** 新增一条关键资产。

如果要设置[IS_PERSISTENT](#enum-assetparam)属性，需要申请ohos.permission.STORE_PERSISTENT_DATA权限。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|attributes|Array\<[AssetParam](#enum-assetparam)>|是|-|待新增关键资产的属性集合，包括关键资产明文、访问控制属性、自定义数据等。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[关键资产存储服务(ASSET)错误码](../../errorcodes/cj-errorcode-asset.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|The caller doesn't have the permission.|
  |401|Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed.|
  |24000001|The ASSET service is unavailable.|
  |24000003|The asset already exists.|
  |24000005|The screen lock status does not match.|
  |24000006|Insufficient memory.|
  |24000007|The asset is corrupted.|
  |24000008|The database operation failed.|
  |24000009|The cryptography operation failed.|
  |24000010|IPC failed.|
  |24000011|Calling the Bundle Manager service failed.|
  |24000012|Calling the OS Account service failed.|
  |24000013|Calling the Access Token service failed.|
  |24000014|The file operation failed.|
  |24000015|Getting the system time failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AssetStoreKit.*
import kit.PerformanceAnalysisKit.*

let qry_alias:AssetParam = AssetParam.ALIAS("demo_alias".toArray())
let query_attr: Array<AssetParam> = [qry_alias]

try{
    let query_res: Array<Array<AssetParam>> = query(query_attr)
    if(!query_res.isEmpty()){
        remove(query_attr)
    }
} catch(e: Exception) {
    Hilog.info(0, "asset_test_add", "[asset_test_add] ${e.message.toString()}")
}

let secret: AssetParam = AssetParam.SECRET("demo_pwd".toArray())
let data_label_n1: AssetParam = AssetParam.DATA_LABEL_NORMAL_1("demo_label".toArray())
let alias: AssetParam = AssetParam.ALIAS("demo_alias".toArray())
let access: AssetParam = AssetParam.ACCESSIBILITY(AssetAccessibility.DEVICE_FIRST_UNLOCKED)
let add_attr: Array<AssetParam> = [secret, data_label_n1, alias, access]
add(add_attr)
```