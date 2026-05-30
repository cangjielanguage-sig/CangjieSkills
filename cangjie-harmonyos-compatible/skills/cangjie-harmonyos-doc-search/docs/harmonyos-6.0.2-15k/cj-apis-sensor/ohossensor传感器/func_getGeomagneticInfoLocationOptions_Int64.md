## func getGeomagneticInfo(LocationOptions, Int64)

```cangjie
public func getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: Int64): GeomagneticResponse
```

**功能：** 获取某时刻地球上特定位置的地磁场信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locationOptions|[LocationOptions](#class-locationoptions)|是|-|地理位置，包括经度、纬度和海拔高度。|
|timeMillis|Int64|是|-|获取磁偏角的时间，unix时间戳，单位毫秒。|

**返回值：**

|类型|说明|
|:----|:----|
|[GeomagneticResponse](#class-geomagneticresponse)|地磁场信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[传感器错误码](../../errorcodes/cj-errorcode-sensor.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.|
  |14500101|Service exception.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

try {
    let location = LocationOptions(80.0, 0.0, 0.0)
    let data = getGeomagneticInfo(location, 1580486400000)
    AppLog.info("Succeeded in getting geomagneticInfo x: ${data.x}")
    AppLog.info("Succeeded in getting geomagneticInfo y: ${data.x}")
    AppLog.info("Succeeded in getting geomagneticInfo z: ${data.z}")
    AppLog.info("Succeeded in getting geomagneticInfo geomagneticDip: ${data.geomagneticDip}")
    AppLog.info("Succeeded in getting geomagneticInfo deflectionAngle: ${data.deflectionAngle}")
    AppLog.info("Succeeded in getting geomagneticInfo levelIntensity: ${data.levelIntensity}")
    AppLog.info("Succeeded in getting geomagneticInfo totalIntensity: ${data.totalIntensity}")
} catch (e: BusinessException) {
    AppLog.error("Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}")
}
```