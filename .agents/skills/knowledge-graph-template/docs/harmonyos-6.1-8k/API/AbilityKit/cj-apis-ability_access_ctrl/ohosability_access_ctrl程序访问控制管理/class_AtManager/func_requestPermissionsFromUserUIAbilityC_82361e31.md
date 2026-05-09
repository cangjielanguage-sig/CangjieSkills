### func requestPermissionsFromUser(UIAbilityContext, Array\<Permissions>, AsyncCallback\<PermissionRequestResult>)

```cangjie
public func requestPermissionsFromUser(context: UIAbilityContext, permissionList: Array<Permissions>,
    requestCallback: AsyncCallback<PermissionRequestResult>): Unit
```

**功能：** 用于拉起弹框请求用户授权。

如果用户拒绝授权，将无法再次拉起弹框，需要用户在系统应用“设置”的界面中，手动授予权限。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|请求权限的UIAbility的Context。|
|permissionList|Array\<[Permissions](#type-permissions)>|是|-|权限名列表，合法的权限名取值可在[应用权限列表](../../security/AccessToken/cj-app-permissions.md)中查询。|
|requestCallback|AsyncCallback\<[PermissionRequestResult](cj-apis-sercurity-permission_request_result.md#class-permissionrequestresult)>|是|-|回调函数，返回接口调用是否成功的结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[访问控制错误码](./cj-errorcode-access-token.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 12100001 | Invalid parameter. The context is invalid when it does not belong to the application itself. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.*
import ohos.business_exception.BusinessException

try {
    // 此处代码可添加在依赖项定义中
    var resultCallback = {
        errorCode: Option<BusinessException>, data: Option<PermissionRequestResult> => match (errorCode) {
            case Some(e) => Hilog.error(0, "AppLogCj", "permissionResultCallBack request error: errcode is ${e.code}")
            case _ =>
                match (data) {
                    case Some(value) =>
                        for (i in (0..value.permissions.size)) {
                            Hilog.info(0, "AppLogCj", "CallBack: ${value.permissions[i]} - ${value.authResults[i]}")
                        }
                    case _ => Hilog.error(0, "AppLogCj", "permissionResultCallBack request error: data is null")
                }
        }
    }

    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let atManager = AbilityAccessCtrl.createAtManager()
    let permissionList = ["ohos.permission.READ_CONTACTS", "ohos.permission.CAMERA"]
    atManager.requestPermissionsFromUser(ctx, permissionList, resultCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```