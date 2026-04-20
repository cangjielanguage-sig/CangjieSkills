# 使用WebRTC进行Web视频会议

Web组件可以通过W3C标准协议接口拉起摄像头和麦克风，通过[onPermissionRequest](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-onpermissionrequestonpermissionrequestevent---unit)接口接收权限请求通知，需在配置文件中声明相应的音频权限。

使用摄像头和麦克风功能前请在module.json5中添加音频相关权限，权限的添加方法请参见[在配置文件中声明权限](../security/AccessToken/cj-declare-permissions.md)。

```json
// src/main/resources/base/element/string.json
{
  "string": [
    // ...
    {
      "name": "reason_for_camera",
      "value": "reason_for_camera"
    },
    {
      "name": "reason_for_microphone",
      "value": "reason_for_microphone"
    }
  ]
}
```

```json
// src/main/module.json5
{
  "module": {
    // ...
    "requestPermissions":[
      {
        "name" : "ohos.permission.CAMERA",
        "reason": "$string:reason_for_camera",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when":"inuse"
        }
      },
      {
        "name" : "ohos.permission.MICROPHONE",
        "reason": "$string:reason_for_microphone",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when":"inuse"
        }
      }
    ]
  }
}
```

通过在JavaScript中调用W3C标准协议接口navigator.mediaDevices.getUserMedia()，该接口用于拉起摄像头和麦克风。constraints参数是一个包含了video和audio两个成员的MediaStreamConstraints对象，用于说明请求的媒体类型。

在下面的示例中，点击前端页面中的开起摄像头按钮再点击onConfirm，打开摄像头和麦克风。

- 应用侧代码：

    1. 获取context

        ```cangjie
        // main_ability.cj
        import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility, UIAbilityContext}
        import kit.ArkUI.WindowStage
        import kit.UIKit.AppLog

        var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None

        class MainAbility <: UIAbility {
            public init() {
                super()
                registerSelf()
            }

            public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
                AppLog.info("MainAbility OnCreated.${want.abilityName}")

                // 获取context
                globalAbilityContext = Option<UIAbilityContext>.Some(this.context)

                match (launchParam.launchReason) {
                    case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
                    case _ => ()
                }
            }

            public override func onWindowStageCreate(windowStage: WindowStage): Unit {
                AppLog.info("MainAbility onWindowStageCreate.")
                windowStage.loadContent("EntryView")
            }
            // ...
        }
        ```

    2. 申请权限，打开摄像头和麦克风

        ```cangjie
        // index.cj
        import ohos.state_macro_manage.*
        import kit.ArkWeb.{WebviewController}
        import kit.LocalizationKit.{__GenerateResource__}
        import kit.UIKit.{Web, BusinessException, AsyncError, AlertDialog, AlertDialogParamWithButtons, AlertDialogButtonOptions
            }
        import kit.AbilityKit.*

        @Entry
        @Component
        class EntryView {
            let webController = WebviewController()

            public func aboutToAppear(): Unit {
                try {
                    // 配置Web开启调试模式
                    WebviewController.setWebDebuggingAccess(true)
                    // 获取权限请求通知，点击onConfirm按钮后，拉起摄像头和麦克风。
                    requestPermissons()
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}");
                }
            }