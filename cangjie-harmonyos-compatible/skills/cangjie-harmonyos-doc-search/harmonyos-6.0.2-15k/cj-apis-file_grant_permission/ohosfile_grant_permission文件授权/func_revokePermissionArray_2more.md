## func revokePermission(Array\<PolicyInfo>)

```cangjie
public func revokePermission(policies: Array<PolicyInfo>): Option<ErrorResult>
```

**功能：** 对所选择的多个文件或目录uri取消持久化授权。该接口仅对具有该系统能力的设备开放（此接口不支持媒体类URI及远端URI的持久化）。

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
                revokePermission(policies)
            case _ => AppLog.info("document select error: data is null")
        }
    }
}
let uris = documentPicker.select(documentSelectCallback, option: dso)
```

## class ErrorResult

```cangjie
public class ErrorResult {
    public let code: Int32
    public let message: String
    public let results: Array<PolicyErrorResult>
}
```

**功能：** 返回授予或使能权限失败的URI策略结果。支持persistPermission、revokePermission、activatePermission、deactivatePermission接口错误时使用。
对应错误码如下表，详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。code，message信息如下：

| code | message              |
| :-------- | :--------------------- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken.|
| 801 | Capability not supported.|
| 13900001 | Operation not permitted.|
| 13900042 | Unknown error. |

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**起始版本：** 20

### let code

```cangjie
public let code: Int32
```

**功能：** persistPermission、revokePermission、activatePermission、deactivatePermission接口错误时返回的错误码。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** Int32

**读写能力：** 只读

**起始版本：** 20

### let message

```cangjie
public let message: String
```

**功能：** persistPermission、revokePermission、activatePermission、deactivatePermission接口错误时返回的错误信息。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### let results

```cangjie
public let results: Array<PolicyErrorResult>
```

**功能：** 授予或使能权限失败的URI策略结果。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**类型：** Array\<[PolicyErrorResult](#class-policyerrorresult)>

**读写能力：** 只读

**起始版本：** 20