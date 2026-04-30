### static func on(CallbackType, Callback1Argument\<String>)

```cangjie
public static func on(`type`: CallbackType, callback: Callback1Argument<String>): Unit
```

**功能：** 订阅GNSS NMEA信息上报事件。

**需要权限：** ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CallbackType](#enum-callbacktype)|是|-|设置事件类型。type为CallbackType.nmeaMessage，表示订阅GNSS NMEA信息上报。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<String>|是|-|回调函数，返回GNSS NMEA信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.on} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.                                           |
  |3301100 | The location switch is off.                                                 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.LocationKit.*

// 此处代码可添加在依赖项定义中
class TestCallbacknmeaMessage <: Callback1Argument<String> {
    public init() {}
    public open func invoke(res: String): Unit {
        AppLog.info("Call invoke NmeaMessage: ${res}")
    }
}

let testCallbacknmeaMessage = TestCallbacknmeaMessage()
GeoLocationManager.on(CallbackType.NmeaMessage, testCallbacknmeaMessage)
```