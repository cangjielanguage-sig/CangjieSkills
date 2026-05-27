### static func off(CallbackType, Callback1Argument\<SatelliteStatusInfo>)

```cangjie
public static func off(`type`: CallbackType, callback: Callback1Argument<SatelliteStatusInfo>): Unit
```

**功能：** 取消订阅GNSS卫星状态信息上报事件。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CallbackType](#enum-callbacktype)|是|-|设置事件类型。type为CallbackType.satelliteStatusChange，表示订阅GNSS卫星状态信息上报。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[SatelliteStatusInfo](#class-satellitestatusinfo)>|是|-|需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.off} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.                                           |
  |3301100 | The location switch is off.                                                 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.LocationKit.*

// 此处代码可添加在依赖项定义中
class TestCallbacksatelliteStatusChange <: Callback1Argument<SatelliteStatusInfo> {
    public init() {}
    public open func invoke(res: SatelliteStatusInfo): Unit {
        AppLog.info("Call invoke SatelliteStatusChange: ${res.satellitesNumber}")
    }
}

let testCallbacksatelliteStatusChange = TestCallbacksatelliteStatusChange()
GeoLocationManager.on(CallbackType.SatelliteStatusChange, testCallbacksatelliteStatusChange)
GeoLocationManager.off(CallbackType.SatelliteStatusChange, testCallbacksatelliteStatusChange)
```