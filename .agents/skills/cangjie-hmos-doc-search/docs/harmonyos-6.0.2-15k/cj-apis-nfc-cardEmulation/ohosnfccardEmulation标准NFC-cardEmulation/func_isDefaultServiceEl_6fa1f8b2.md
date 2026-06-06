## func isDefaultService(ElementName, CardType)

```cangjie
public func isDefaultService(elementName: ElementName, `type`: CardType): Bool
```

**功能：** 判断指定的应用是否为指定业务类型的默认应用。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|elementName|[ElementName](../AbilityKit/cj-apis-ability.md#class-elementname)|是|所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。|
|\`type`|[CardType](#enum-cardtype)|是|卡模拟业务类型。目前只支持默认支付应用查询。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 是默认支付应用，false: 不是默认支付应用。|

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

import kit.ConnectivityKit.*

// init elementName here, bundleName and abilityName are required.
let ele = ElementName("", "com.example.myapplication", "EntryAbility", "entry")
let isDefaultService: Bool = isDefaultService(ele, CardType.PAYMENT)
// do something according to the isDefaultService value
```