### func requestPermissionOnSetting(Context, Array\<Permissions>, AsyncCallback\<Array\<GrantStatus>>)

```cangjie
public func requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>,
    callback: AsyncCallback<Array<GrantStatus>>): Unit
```

**功能：** 用于二次拉起权限设置弹框。

在调用此接口前，应用需要先调用[requestPermissionsFromUser](#func-requestpermissionsfromuserstagecontext-arraypermissions-asynccallbackaccessctrlpermissionrequestresult)，如果用户在首次弹窗授权时已授权，调用当前接口将无法拉起弹窗。

> **说明：**
>
> 仅支持Ability。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](cj-apis-ability.md#class-context)|是|-|请求权限的Ability的Context。|
|permissionList|Array\<[Permissions](#type-permissions)>|是|-|需要校验的权限名称，合法的权限名取值可在[应用权限列表](../../../../Dev_Guide/security/AccessToken/cj-app-permissions.md#应用权限列表)中查询。|
|callback|AsyncCallback\<Array\<[GrantStatus](#enum-grantstatus)>>|是|-|回调函数，返回授权状态结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[访问控制错误码](../../errorcodes/cj-errorcode-access-token.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |12100001|Invalid parameter. Possible causes: 1. The context is invalid because it does not belong to the application itself; 2. The permission list contains the permission that is not declared in the module.json file; 3. The permission list is invalid because the permissions in it do not belong to the same permission group.|
  |12100010|The request already exists.|
  |12100011|All permissions in the permission list have been granted.|
  |12100012|The permission list contains the permission that has not been revoked by the user.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.base.AsyncCallback
import ohos.base.AsyncError

// 此处代码可添加在依赖项定义中
var resCallback = {
    errorCode: Option<AsyncError>, data: Option<Array<GrantStatus>> => match (errorCode) {
        case Some(e) => AppLog.info("CallBack request error: errcode is ${e.code}")
        case _ =>
            match (data) {
                case Some(value) =>
                    for (i in (0..value.size)) {
                        AppLog.info("CallBack GrantStatus: ${value[i].toString()}")
                    }
                case _ => AppLog.info("CallBack request error: data is null")
            }
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let atManager = AbilityAccessCtrl.createAtManager()
let permissionList = ["ohos.permission.READ_CONTACTS", "ohos.permission.CAMERA"]
atManager.requestPermissionOnSetting(ctx, permissionList, resCallback)
```