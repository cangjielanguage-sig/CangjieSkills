## class GeoLocationManager

```cangjie
public class GeoLocationManager {}
```

**功能：** 用于提供位置服务的类。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### static func flushCachedGnssLocations()

```cangjie
public static func flushCachedGnssLocations(): Unit
```

**功能：** 读取并清空GNSS芯片所有缓存位置。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.flushCachedGnssLocations} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.  |
  |3301100 | The location switch is off.   |
  |3301200 | Failed to obtain the geographical location.   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

GeoLocationManager.flushCachedGnssLocations()
```

### static func getAddressesFromLocation(ReverseGeoCodeRequest)

```cangjie
public static func getAddressesFromLocation(request: ReverseGeoCodeRequest): Array<GeoAddress>
```

**功能：** 调用逆地理编码服务，将坐标转换为地理描述。

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[ReverseGeoCodeRequest](#class-reversegeocoderequest)|是|-|设置逆地理编码请求的相关参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[GeoAddress](#class-geoaddress)>|返回地理描述信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.getAddressesFromLocation} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.  |
  |3301300 | Reverse geocoding query failed.   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let addressArr = GeoLocationManager.getAddressesFromLocation(
    ReverseGeoCodeRequest(32.0, 119.0, locale: "zh", country: "CN"))
```