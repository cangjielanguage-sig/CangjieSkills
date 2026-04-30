### static func getCurrentLocation(CurrentLocationRequest)

```cangjie
public static func getCurrentLocation(request: CurrentLocationRequest): Location
```

**功能：** 获取当前位置。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[CurrentLocationRequest](#class-currentlocationrequest)|是|-|设置位置请求参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Location](#class-location)|返回当前位置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.getCurrentLocation} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.                                           |
  |3301100 | The location switch is off.                                                 |
  |3301200 | Failed to obtain the geographical location.  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let location = GeoLocationManager.getCurrentLocation(CurrentLocationRequest())
```

### static func getCurrentLocation(SingleLocationRequest)

```cangjie
public static func getCurrentLocation(request: SingleLocationRequest): Location
```

**功能：** 获取当前位置。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[SingleLocationRequest](#class-singlelocationrequest)|是|-|设置位置请求参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Location](#class-location)|返回当前位置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.getCurrentLocation} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.                                           |
  |3301100 | The location switch is off.                                                 |
  |3301200 | Failed to obtain the geographical location.  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let location = GeoLocationManager.getCurrentLocation(
    SingleLocationRequest(LocatingPriority.PRIORITY_LOCATING_SPEED, 1000))
```