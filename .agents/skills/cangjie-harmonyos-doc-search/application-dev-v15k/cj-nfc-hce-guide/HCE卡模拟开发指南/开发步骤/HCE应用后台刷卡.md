### HCE应用后台刷卡

1. 在module.json5文件中声明NFC卡模拟权限，声明HCE特定的action，声明应用能够处理的AID。
2. import需要的NFC卡模拟模块和其他相关的模块。
3. 判断设备是否支持NFC能力和HCE能力。
4. 订阅HCE APDU数据的接收。
5. 完成HCE刷卡APDU数据的接收和发送。
6. 退出应用程序时，退出订阅功能。

```cangjie
        "abilities": [
          {
            "name": "EntryAbility",
            "srcEntry": "ohos_app_cangjie_entry.MainAbility",
            "description": "$string:EntryAbility_desc",
            "icon": "$media:layered_image",
            "label": "$string:EntryAbility_label",
            "startWindowIcon": "$media:startIcon",
            "startWindowBackground": "$color:start_window_background",
            "exported": true,
            "skills": [
              {
                "entities": [
                  "entity.system.home"
                ],
                "actions": [
                  "action.system.home",
                  // Add the nfc card emulation action to filter out for this application.
                  "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
                ]
              }
            ],
            "metadata": [
              {
                "name": "payment-aid",
                "value": "A0000000031010" // change it tobe correct
              },
              {
                "name": "other-aid",
                "value": "A0000000031011" // change it tobe correct
              }
            ]
          }
        ],
        "requestPermissions": [
          {
            // Add the permission for nfc card emulation.
            "name": "ohos.permission.NFC_CARD_EMULATION",
            "reason": "$string:app_name",
          }
        ]
    ```

```cangjie
import kit.ConnectivityKit.*
import ohos.base.{Callback0Argument, Callback1Argument, BusinessException}

var hceElementName: ?ElementName = None
var hceService: ?HceService = None

class ZCb <: Callback0Argument {
    public func invoke(): Unit {
        AppLog.info('hceService transmit Promise success.')
    }
}

class HceCommandCb <: Callback1Argument<Array<UInt8>> {
    public func invoke(hceCommand: Array<UInt8>): Unit {
        if (hceCommand.size == 0) {
            AppLog.error('hceCommandCb has invalid hceCommand.')
            return
        }
        // check the command, then transmit the response.
        AppLog.info('hceCommand = ${hceCommand}')
        let responseData: Array<UInt8> = [0x90, 0x00] // change the response depend on different received command.
        hceService?.transmit(responseData, ZCb())
    }
}

class EntryAbility <: UIAbility {
    public func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info('Ability onCreate')

        // 判断设备是否支持NFC能力和HCE能力
        // ...
        if (!hasHceCapability()) {
            AppLog.info('hce unavailable.')
            return
        }

        hceElementName = ElementName(
            "",
            want.bundleName,
            want.abilityName,
            want.moduleName
        )
        hceService = HceService()
        hceService?.on(NfcEventType.HceCmd, HceCommandCb())
    }
    public func onForeground(): Unit {
        // Ability has brought to foreground
        AppLog.info('Ability onForeground')
    }

    public func onDestroy(): Unit {
        // Ability has back to destroy
        AppLog.info('Ability onDestroy')
        // 退出应用程序NFC标签页面时，调用tag模块退出前台优先功能
        if (let Some(hceElementName) <- hceElementName) {
            try {
                hceService?.stop(hceElementName)
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
    }
}
```