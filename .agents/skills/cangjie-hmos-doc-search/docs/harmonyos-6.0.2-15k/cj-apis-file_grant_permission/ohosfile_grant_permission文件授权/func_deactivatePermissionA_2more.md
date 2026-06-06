## func deactivatePermission(Array\<PolicyInfo>)

```cangjie
public func deactivatePermission(policies: Array<PolicyInfo>): Option<ErrorResult>
```

**功能：** 取消使能授权过的多个文件或目录。该接口仅对具有该系统能力的设备开放（此接口不支持媒体类URI及远端URI的持久化）。

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
let res = deactivatePermission(policies)
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

## func persistPermission(Array\<PolicyInfo>)

```cangjie
public func persistPermission(policies: Array<PolicyInfo>): Option<ErrorResult>
```

**功能：** 对所选择的多个文件或目录URI持久化授权。该接口仅对具有该系统能力的设备开放（此接口不支持媒体类URI及远端URI的持久化）。

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
import kit.AbilityKit.*

let dso = DocumentSelectOptions()
let actualContext: AbilityContext = Global.getAbilityContext()
let documentPicker = DocumentViewPicker(actualContext)
let documentSelectCallback = {
    errorCode: Option<AsyncError>, data: Option<Array<String>> => match (errorCode) {
        case Some(e) => AppLog.info("document select error: errcode is ${e.code}")
        case _ => match (data) {
            case Some(value) =>
                AppLog.info("documentUris is ${value}")
                let policyInfo = PolicyInfo(value[0], READ_MODE)
                let policies = [policyInfo]
                persistPermission(policies)
            case _ => AppLog.info("document select error: data is null")
        }
    }
}
let uris = documentPicker.select(documentSelectCallback, option: dso)
```