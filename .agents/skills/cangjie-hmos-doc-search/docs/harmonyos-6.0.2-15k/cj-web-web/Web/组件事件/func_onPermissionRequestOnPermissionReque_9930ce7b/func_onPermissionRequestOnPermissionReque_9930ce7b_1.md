### func onPermissionRequest((OnPermissionRequestEvent) -> Unit)

```cangjie
public func onPermissionRequest(callback: (OnPermissionRequestEvent) -> Unit): This
```

**功能：** 通知收到获取权限请求。

**需要权限：** 需配置"ohos.permission.CAMERA"、"ohos.permission.MICROPHONE"权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnPermissionRequestEvent](#class-onpermissionrequestevent))->Unit|是|-|回调函数，通知收到获取权限请求触发。|

**示例：**

```cangjie
// main_ability.cj
internal import kit.UIKit.*
internal import kit.AbilityKit.*

var globalAbilityContext = Option<AbilityContext>.None
class MainAbility <: Ability {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
        globalAbilityContext = Option<AbilityContext>.Some(this.context)
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
    }
}

//index.cj
package ohos_app_cangjie_entry

import ohos.state_macro_manage.*
import kit.LocalizationKit.*
import kit.ArkWeb.*

let webController = WebviewController()
func getContext(): AbilityContext {
    match (globalAbilityContext) {
        case Some(context) =>
            AppLog.info("get globalAbilityContext successfully")
            context
        case None =>
            AppLog.error("get globalAbilityContext failed")
            throw Exception("get globalAbilityContext failed")
    }
}

@Entry
@Component
class EntryView {
    public func aboutToAppear() {
        WebviewController.setWebDebuggingAccess(true)
        var resultCallback = {
            errorCode: Option<AsyncError>, data: Option<AccessCtrlPermissionRequestResult> => match (errorCode) {
                case Some(e) => AppLog.info("permissionResultCallBack request error: errcode is ${e.code}")
                case _ => match (data) {
                    case Some(value) => for (i in (0..value.permissions.size)) {
                        AppLog.info("permissionResultCallBack: ${value.permissions[i]} - ${value.authResults[i]}")
                    }
                    case _ => AppLog.info("permissionResultCallBack request error: data is null")
                }
            }
        }
        let abilityAccessCtrl = AbilityAccessCtrl.createAtManager()
        let stageContext = getStageContext(getContext())
        abilityAccessCtrl.requestPermissionsFromUser(stageContext, ["ohos.permission.CAMERA", "ohos.permission.MICROPHONE"], resultCallback)
    }
    func build() {
        Column(40) {
            Web(src: @rawfile("index.html"), controller: webController)
                .onControllerAttached({
                    => AppLog.info("controller attachec")
                })
                .enableNativeMediaPlayer(enable: true, shouldOverlay: true)
                .onPermissionRequest {
                    event => AlertDialog.show(
                        AlertDialogParamWithButtons(
                            "text",
                            title: 'title',
                            primaryButton: AlertDialogButtonOptions(
                                value: 'deny',
                                action: {
                                    => event.request.deny();
                                }
                            ),
                            secondaryButton: AlertDialogButtonOptions(
                                value: 'onConfirm',
                                action: {
                                    => event.request.grant(event.request.getAccessibleResource());
                                }
                            ),
                            cancel: {
                                => event.request.deny();
                            }
                        )
                    )
                }
        }.width(100.percent)
    }
}
```

加载的html文件。