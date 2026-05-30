## class HceService

```cangjie
public class HceService {}
```

**功能：** 提供HCE卡模拟的实现，主要包括接收对端读卡设备的APDU数据，并响应APDU数据到对端读卡设备。使用HCE相关接口前，必须先判断设备是否支持HCE卡模拟能力。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

### func on(NfcEventType, Callback1Argument\<Array\<UInt8>>)

```cangjie
public func on(`type`: NfcEventType, callback: Callback1Argument<Array<UInt8>>): Unit
```

**功能：** 订阅回调，用于接收对端读卡设备发送的APDU数据。应用程序需要在HCE卡模拟页面的onCreate函数里面调用该订阅函数。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[NfcEventType](#enum-nfceventtype)|是|要订阅的回调类型，固定填hceCmd。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<UInt8>>|是|订阅的事件回调，入参是符合APDU协议的数据，每个UInt8十六进制表示，范围是0x00~0xFF。|

### func start(ElementName, Array\<String>)

```cangjie
public func start(elementName: ElementName, aidList: Array<String>): Unit
```

**功能：** 启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|elementName|[ElementName](../AbilityKit/cj-apis-ability.md#class-elementname)|是|所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。|
|aidList|Array\<String>|是|动态注册卡模拟的AID列表，允许为空。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[NFC错误码](../../errorcodes/cj-errorcode-nfc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |3100301|Card emulation running state is abnormal in service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

// 此处代码可添加在依赖项定义中
let hceCb = hceCallback()
let ele = ElementName("", "com.example.myapplication", "EntryAbility", "entry")
let hceService: HceService = HceService()

class hceCallback <: Callback1Argument<Array<UInt8>> {
    public init() {}
    public open func invoke(hceCommand: Array<UInt8>): Unit {
        realCallback(hceCommand)
    }
}

func realCallback(hceCommand: Array<UInt8>): Unit
{
  //handle the data and err
  AppLog.info("got apdu data: ${hceCommand}")
}

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onForeground(): Unit {
      AppLog.info("MainAbility onDestroy.")
      let aidList = ['D2760000850101'] // change aid tobe correct.
        hceService.start(ele, aidList)
        hceService.on(NfcEventType.HceCmd, hceCb)
    }
    // other life cycle method...
}

let json = '{ "name" : "hello" , "imgSrc" : "image"}'
let formbindingdata = createFormBindingData(obj: json)
AppLog.info("formbindingdata.data：${formbindingdata.data}")
```