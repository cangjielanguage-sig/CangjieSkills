### func requestPermissionsFromUser(StageContext, Array\<Permissions>, AsyncCallback\<AccessCtrlPermissionRequestResult>)

```cangjie
public func requestPermissionsFromUser(context: StageContext, permissionList: Array<Permissions>,
    callback: AsyncCallback<AccessCtrlPermissionRequestResult>): Unit
```

**功能：** 用于拉起弹框请求用户授权。

如果用户拒绝授权，将无法再次拉起弹框，需要用户在系统应用“设置”的界面中，手动授予权限。或是调用[requestPermissionOnSetting](#func-requestpermissiononsettingcontext-arraypermissions-asynccallbackarraygrantstatus)，拉起权限设置弹框，引导用户授权。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|请求权限的Ability的Context。|
|permissionList|Array\<[Permissions](#type-permissions)>|是|-|需要校验的权限名称，合法的权限名取值可在[应用权限列表](../../../../Dev_Guide/security/AccessToken/cj-app-permissions.md#应用权限列表)中查询。|
|callback|AsyncCallback\<[AccessCtrlPermissionRequestResult](#class-accessctrlpermissionrequestresult)>|是|-|回调函数，返回接口调用是否成功的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[访问控制错误码](../../errorcodes/cj-errorcode-access-token.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |12100001|The parameter is invalid. The context is invalid when it does not belong to the application itself.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.base.AsyncCallback
import ohos.base.AsyncError

// 此处代码可添加在依赖项定义中
var resultCallback = {
    errorCode: Option<AsyncError>, data: Option<AccessCtrlPermissionRequestResult> => match (errorCode) {
        case Some(e) => AppLog.info("permissionResultCallBack request error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    for (i in (0..value.permissions.size)) {
                        AppLog.info("CallBack: ${value.permissions[i]} - ${value.authResults[i]}")
                    }
                case _ => AppLog.info("permissionResultCallBack request error: data is null")
            }
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let atManager = AbilityAccessCtrl.createAtManager()
let stageContext = getStageContext(ctx)
let permissionList = ["ohos.permission.READ_CONTACTS", "ohos.permission.CAMERA"]
atManager.requestPermissionsFromUser(stageContext, permissionList, resultCallback)
```