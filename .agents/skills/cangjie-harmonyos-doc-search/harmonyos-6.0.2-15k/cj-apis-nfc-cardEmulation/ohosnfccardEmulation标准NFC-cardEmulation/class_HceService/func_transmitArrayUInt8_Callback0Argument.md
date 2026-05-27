### func transmit(Array\<UInt8>, Callback0Argument)

```cangjie
public func transmit(responseApdu: Array<UInt8>, callback: Callback0Argument): Unit
```

**功能：** 发送APDU数据到对端读卡设备，使用Callback异步回调。应用程序必须在[on](cj-apis-bluetooth-baseProfile.md#func-onprofilecallbacktype-callback1argumentstatechangeparam)收到读卡设备发送的APDU数据后，才调用该接口响应数据。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|responseApdu|Array\<UInt8>|是|发送到对端读卡设备的符合APDU协议的数据，每个UInt8十六进制表示，范围是0x00~0xFF。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|以callback形式异步返回发送APDU数据的结果。|

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
let transmitCb = transmitCallback()
let ele = ElementName("", "com.example.myapplication", "EntryAbility", "entry")
let hceService: HceService = HceService()

class hceCallback <: Callback1Argument<Array<UInt8>> {
    public init() {}
    public open func invoke(hceCommand: Array<UInt8>): Unit {
        realCallback(hceCommand)
    }
}

class transmitCallback <: Callback0Argument {
    public init() {}
    public open  func invoke(): Unit {
        AppLog.info("transmit success")
    }
}

func realCallback(hceCommand: Array<UInt8>): Unit
{
    AppLog.info("got apdu data: ${hceCommand}")
    // the data app wanna send, just a example data
    let responseData: Array<UInt8> = [0x1, 0x2]
    hceService.transmit(responseData, transmitCb)
}

class MainAbility <: UIAbility {
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
        hceService.on(NfcEventType.HceCmd, hceCb)
    }
    public override func onDestroy(): Unit {
        AppLog.info("MainAbility onDestroy.")
        hceService.stop(ele)
    }
    // other life cycle method...
}

let json = '{ "name" : "hello" , "imgSrc" : "image"}'
let formbindingdata = createFormBindingData(obj: json)
AppLog.info("formbindingdata.data：${formbindingdata.data}")
```