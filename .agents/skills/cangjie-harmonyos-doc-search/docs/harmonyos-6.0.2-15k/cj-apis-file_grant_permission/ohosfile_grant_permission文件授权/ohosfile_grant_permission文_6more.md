# ohos.file_grant_permission（文件授权）

对文件授予永久性权限。

## 导入模块

```cangjie
import kit.CoreFileKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## 权限列表

ohos.permission.FILE_ACCESS_PERSIST

## func activatePermission(Array\<PolicyInfo>)

```cangjie
public func activatePermission(policies: Array<PolicyInfo>): Option<ErrorResult>
```

**功能：** 使能多个已经永久授权过的文件或目录。该接口仅对具有该系统能力的设备开放（此接口不支持媒体类URI及远端URI的持久化）。

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|policies|Array\<[PolicyInfo](#class-policyinfo)>|是|-|需要授权URI的策略信息，policies数组大小上限为500。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<[ErrorResult](#class-errorresult)>|接口出现错误返回具体的错误码和错误信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let uri = "file://docs/storage/Users/username/tmp.txt"
let policyInfo = PolicyInfo(uri, READ_MODE)
let policies = [policyInfo]
let res = activatePermission(policies)
if (let Some(v) <- res) {
    AppLog.info("the code is ${v.code}")
    AppLog.info("the message is ${v.message}")
    for (i in 0..v.results.size) {
        AppLog.info("the res code is ${v.results[i].code.value}")
        AppLog.info("the res uri is ${v.results[i].uri}")
        AppLog.info("the res message is ${v.results[i].message}")
    }
}
```

## func checkPersistentPermission(Array\<PolicyInfo>)

```cangjie
public func checkPersistentPermission(policies: Array<PolicyInfo>): Array<Bool>
```

**功能：** 校验所选择的多个文件或目录URI持久化授权。

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|policies|Array\<[PolicyInfo](#class-policyinfo)>|是|-|需要授权URI的策略信息，policies数组大小上限为500。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Bool>|返回true表示有持久化授权；false表示不具有持久化授权。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息              |
  | :-------- | :--------------------- |
  | 201 | Permission verification failed, usually the result returned by VerifyAccessToken.|
  | 801 | Capability not supported.|
  | 13900001 | Operation not permitted.|
  | 13900042 | Unknown error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let uri = "file://docs/storage/Users/username/tmp.txt"
let policyInfo = PolicyInfo(uri, READ_MODE)
let policies = [policyInfo]
let res = checkPersistentPermission(policies)
```