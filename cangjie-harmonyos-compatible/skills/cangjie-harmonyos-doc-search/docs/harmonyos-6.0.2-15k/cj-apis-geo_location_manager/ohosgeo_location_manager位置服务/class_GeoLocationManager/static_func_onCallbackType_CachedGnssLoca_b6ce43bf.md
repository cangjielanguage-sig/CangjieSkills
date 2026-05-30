### static func on(CallbackType, CachedGnssLocationsRequest, Callback1Argument\<Array\<Location>>)

```cangjie
public static func on(`type`: CallbackType, request: CachedGnssLocationsRequest, callback: Callback1Argument<Array<Location>>): Unit
```

**功能：** 订阅缓存GNSS定位结果上报事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CallbackType](#enum-callbacktype)|是|-|设置事件类型。type为CallbackType.cachedGnssLocationsChange，表示GNSS缓存定位结果上报|
|request|[CachedGnssLocationsRequest](#class-cachedgnsslocationsrequest)|是|-|GNSS缓存功能配置参数。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[Location](#class-location)>>|是|-|回调函数，返回GNSS缓存位置。|

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
class TestCallbackcachedGnssLocationsChange <: Callback1Argument<Array<Location>> {
    public init() {}
    public open func invoke(res: Array<Location>): Unit {
        AppLog.info("Call invoke CachedGnssLocationsChange: ${res[0].latitude}")
    }
}

let testCallbackcachedGnssLocationsChange = TestCallbackcachedGnssLocationsChange()
let requestInfo = CachedGnssLocationsRequest(10, true)
GeoLocationManager.on(CallbackType.CachedGnssLocationsChange, requestInfo,
    testCallbackcachedGnssLocationsChange)
```