### static func getCurrentLocation(SingleLocationRequest)

```cangjie
public static func getCurrentLocation(request: SingleLocationRequest): Location
```

**功能：** 获取当前位置。

**需要权限：** ohos.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[SingleLocationRequest](#class-singlelocationrequest)|是|-|设置位置请求参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Location](#class-location)|返回当前位置信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[位置服务子系统错误码](./cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission verification failed. The application does not have the permission required to call the API. |
  | 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentLocation} due to limited device capabilities. |
  | 3301000 | The location service is unavailable. |
  | 3301100 | The location switch is off. |
  | 3301200 | Failed to obtain the geographical location. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let location = GeoLocationManager.getCurrentLocation(SingleLocationRequest(LocatingPriority.PriorityLocatingSpeed, 1000))
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func isLocationEnabled()

```cangjie
public static func isLocationEnabled(): Bool
```

**功能：** 判断位置服务是否已经开启。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：位置信息开关已开启。<br/>false：位置信息开关已关闭。|

**异常：**

- BusinessException：对应错误码如下表，详见[位置服务子系统错误码](./cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. Failed to call ${geoLocationManager.isLocationEnabled} due to limited device capabilities. |
  | 3301000 | The location service is unavailable. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let res = GeoLocationManager.isLocationEnabled()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```