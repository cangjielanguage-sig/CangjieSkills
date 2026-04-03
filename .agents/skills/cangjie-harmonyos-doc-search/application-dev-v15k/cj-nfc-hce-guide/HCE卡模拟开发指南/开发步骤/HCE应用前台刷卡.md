### HCE应用前台刷卡

1. 在module.json5文件中声明NFC卡模拟权限，以及声明HCE特定的action。
2. import需要的NFC卡模拟模块和其他相关的模块。
3. 判断设备是否支持NFC能力和HCE能力。
4. 使能前台HCE应用程序优先处理NFC刷卡功能。
5. 订阅HCE APDU数据的接收。
6. 完成HCE刷卡APDU数据的接收和发送。
7. 退出应用程序NFC刷卡页面时，退出前台优先功能。

```cangjie
        "abilities": [
          {
            "name": "EntryAbility",
            "srcEntry": "./ets/entryability/EntryAbility.ts",
            "description": "$string:EntryAbility_desc",
            "icon": "$media:icon",
            "label": "$string:EntryAbility_label",
            "startWindowIcon": "$media:icon",
            "startWindowBackground": "$color:start_window_background",
            "exported": true,
            "skills": [
              {
                "entities": [
                  "entity.system.home"
                ],
                "actions": [
                  "action.system.home",

                  // actions须包含"ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
                  "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
                ]
              }
            ]
          }
        ],
        "requestPermissions": [
          {
            // 添加使用nfc卡模拟需要的权限
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
    }
    public func onForeground(): Unit {
        // Ability has brought to foreground
        AppLog.info('Ability onForeground')
        if (let Some(hceElementName) <- hceElementName) {
            try {
                // 调用接口使能前台HCE应用程序优先处理NFC刷卡功能
                let aidList = ["A0000000031010", "A0000000031011"] // change aid tobe correct.
                hceService?.start(hceElementName, aidList)

                // 订阅HCE APDU数据的接收
                hceService?.on(NfcEventType.HceCmd, HceCommandCb())
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
    }

    public func onBackground(): Unit {
        // Ability has back to background
        AppLog.info('Ability onBackground')
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