### static func on(CallbackType, ContinuousLocationRequest, Callback1Argument\<Location>)

```cangjie
public static func on(`type`: CallbackType, request: ContinuousLocationRequest, callback: Callback1Argument<Location>): Unit
```

**功能：** 开启位置变化订阅，并发起定位请求。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CallbackType](#enum-callbacktype)|是|-|设置事件类型。type为CallbackType.locationChange，表示位置变化。|
|request|[ContinuousLocationRequest](#class-continuouslocationrequest)|是|-|设置位置请求参数。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[Location](#class-location)>|是|-|回调函数，返回位置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.on} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.                                           |
  |3301100 | The location switch is off.                                                 |
  |3301200 | Failed to obtain the geographical location.                                       |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.LocationKit.*

// 此处代码可添加在依赖项定义中
class TestCallbackLocationChange <: Callback1Argument<Location> {
    public init() {}
    public open func invoke(loc: Location): Unit {
        AppLog.info("Call invoke LocationChange: ${loc.latitude}")
    }
}

let testCallbackLocationChange = TestCallbackLocationChange()
GeoLocationManager.on(
    CallbackType.LocationChange,
    ContinuousLocationRequest(1, UserActivityScenario.DAILY_LIFE_SERVICE),
    testCallbackLocationChange
)
```