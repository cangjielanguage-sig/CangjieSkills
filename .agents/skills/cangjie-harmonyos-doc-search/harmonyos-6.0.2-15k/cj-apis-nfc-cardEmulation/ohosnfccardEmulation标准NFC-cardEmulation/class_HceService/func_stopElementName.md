### func stop(ElementName)

```cangjie
public func stop(elementName: ElementName): Unit
```

**功能：** 停止HCE业务功能。包括取消APDU数据接收的订阅，退出当前应用前台优先，释放动态注册的AID列表。应用程序需要在HCE卡模拟页面的onDestroy函数里调用该接口。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|elementName|[ElementName](../AbilityKit/cj-apis-ability.md#class-elementname)|是|所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[NFC错误码](../../errorcodes/cj-errorcode-nfc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |3100301|Card emulation running state is abnormal in service.|