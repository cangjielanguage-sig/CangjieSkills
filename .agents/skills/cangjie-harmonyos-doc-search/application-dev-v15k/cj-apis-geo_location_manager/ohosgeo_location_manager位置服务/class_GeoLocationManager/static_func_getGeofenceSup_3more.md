### static func getGeofenceSupportedCoordTypes()

```cangjie
public static func getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>
```

**功能：** 获取地理围栏功能支持的坐标系列表。

**系统能力：** SystemCapability.Location.Location.Geofence

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[CoordinateSystemType](#enum-coordinatesystemtype)>|地理围栏功能支持的坐标系列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.getGeofenceSupportedCoordTypes} due to limited device capabilities.          |
  |3301000 | The location service is unavailable. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let res = GeoLocationManager.getGeofenceSupportedCoordTypes()
```

### static func getLastLocation()

```cangjie
public static func getLastLocation(): Location
```

**功能：** 获取上一次位置。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Location](#class-location)|位置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.getLastLocation} due to limited device capabilities.          |
  |3301000 | The location service is unavailable. |
  |3301100 | The location switch is off.  |
  |3301200 |Failed to obtain the geographical location.  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let location = GeoLocationManager.getLastLocation()
```

### static func isGeocoderAvailable()

```cangjie
public static func isGeocoderAvailable(): Bool
```

**功能：** 判断地理编码与逆地理编码服务状态。

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：地理编码与逆地理编码服务可用；<br/>false：地理编码与逆地理编码服务不可用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.isGeocoderAvailable} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let res = GeoLocationManager.isGeocoderAvailable()
```