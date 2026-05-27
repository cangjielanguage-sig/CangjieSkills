### static func getAddressesFromLocationName(GeoCodeRequest)

```cangjie
public static func getAddressesFromLocationName(request: GeoCodeRequest): Array<GeoAddress>
```

**功能：** 调用地理编码服务，将地理描述转换为具体坐标。

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[GeoCodeRequest](#class-geocoderequest)|是|-|设置地理编码请求的相关参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[GeoAddress](#class-geoaddress)>|返回地理编码查询结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.getAddressesFromLocationName} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.  |
  |3301400 | Geocoding query failed.   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let addressArr = GeoLocationManager.getAddressesFromLocationName(GeoCodeRequest("南京", locale: "zh", country: "CN"))
```

### static func getCachedGnssLocationsSize()

```cangjie
public static func getCachedGnssLocationsSize(): Int32
```

**功能：** 获取GNSS芯片缓存位置的个数。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回GNSS芯片缓存位置个数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[位置服务子系统错误码](../../errorcodes/cj-errorcode-geo_location_manager.md)。

  | 错误码ID | 错误信息 |
  |:-------- |:---------------------------------------- |
  |201 | Permission verification failed. The application does not have the permission required to call the API.                 |
  |401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.                 |
  |801 | Capability not supported. Failed to call ${GeoLocationManager.getCachedGnssLocationsSize} due to limited device capabilities.          |
  |3301000 | The location service is unavailable.  |
  |3301100 | The location switch is off.   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocationKit.*

let res = GeoLocationManager.getCachedGnssLocationsSize()
```