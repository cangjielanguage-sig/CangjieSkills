# ohos.nfc.cardEmulation（标准NFC-cardEmulation）

本模块主要提供NFC卡模拟业务，包括判断支持哪种卡模拟类型，HCE卡模拟的业务实现等。

HCE(Host Card Emulation)，称为基于主机的卡模拟，表示不依赖安全单元芯片，应用程序模拟NFC卡片，可以通过NFC服务和NFC读卡器通信。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 权限列表

ohos.permission.NFC_CARD_EMULATION

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

开发HCE卡模拟相关应用时，需要在应用的属性配置文件中，声明与NFC相关的属性值，比如，在module.json5文件中，声明下面属性值：

```json
{
  "module": {
    // other declared attributes.
    "abilities": [
      {
        // other declared attributes.
        "skills": [
          {
            "actions": [
              "ohos.nfc.card_emulation.action.HOST_APDU_SERVICE"
            ]
          }
        ],
        "metadata": [
          {
            "name": "payment-aid",
            "value": "D2760000850101"// change aid tobe correct.
          },
          {
            "name": "other-aid",
            "value": "D2760000850101"// change aid tobe correct.
          }
        ]
      }
    ],
    "requestPermissions": [
      {
        "name": "ohos.permission.NFC_CARD_EMULATION",
        // should add variable card_emulation_reason in string.json
        "reason": "$string:card_emulation_reason",
      }
    ]
  }
}
```

> **注意：**
>
> - 声明"actions"字段的内容填写，必须包含"ohos.nfc.card_emulation.action.HOST_APDU_SERVICE"，不能更改。
> - 声明aid时，name必须为payment-aid，或者other-aid。填写错误会造成解析失败。
> - 声明权限时"requestPermissions"中的"name"字段的内容填写，必须是"ohos.permission.NFC_CARD_EMULATION"，不能更改。

## func hasHceCapability()

```cangjie
public func hasHceCapability(): Bool
```

**功能：** 判断设备是否支持HCE卡模拟功能。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 支持HCE，false: 不支持HCE。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let hasHceCap: Bool = hasHceCapability()
if (!hasHceCap) {
    AppLog.info("this device hasHceCapability false, ignore it.")
}
```