## class GeoLocationManager

```cangjie
public class GeoLocationManager {}
```

**功能：** 用于提供位置服务的类。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### static func getCurrentLocation()

```cangjie
public static func getCurrentLocation(): Location
```

**功能：** 获取当前位置。

**需要权限：** ohos.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

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
    let location = GeoLocationManager.getCurrentLocation()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func getCurrentLocation(CurrentLocationRequest)

```cangjie
public static func getCurrentLocation(request: CurrentLocationRequest): Location
```

**功能：** 获取当前位置。

**需要权限：** ohos.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[CurrentLocationRequest](#class-currentlocationrequest)|是|-|设置位置请求参数。|

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
    let location = GeoLocationManager.getCurrentLocation(CurrentLocationRequest())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```