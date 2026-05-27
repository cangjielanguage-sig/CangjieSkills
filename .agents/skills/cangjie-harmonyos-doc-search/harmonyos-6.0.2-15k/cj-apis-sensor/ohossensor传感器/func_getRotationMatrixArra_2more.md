## func getRotationMatrix(Array\<Float32>, Array\<Float32>)

```cangjie
public func getRotationMatrix(gravity: Array<Float32>, geomagnetic: Array<Float32>): RotationMatrixResponse
```

**功能：** 根据重力矢量和地磁矢量计算旋转矩阵。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gravity|Array\<Float32>|是|-|重力矢量。|
|geomagnetic|Array\<Float32>|是|-|地磁矢量。|

**返回值：**

|类型|说明|
|:----|:----|
|[RotationMatrixResponse](#class-rotationmatrixresponse)|返回旋转矩阵。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[传感器错误码](../../errorcodes/cj-errorcode-sensor.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                                     |
  | -------- | ------------------------------------------------------------|
  | 401      | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
  | 14500101 | Service exception.                                           |

**示例：**

<!-- compile -->

```cangjie
//index.cj

import kit.SensorServiceKit.*
import ohos.base.*

try {
    let gravity: Array<Float32> = [-0.27775216, 0.5351276, 9.788099]
    let geomagnetic: Array<Float32> = [210.87253, -78.6096, -111.44444]
    let data = getRotationMatrix(gravity, geomagnetic)
    AppLog.info(
        "Succeeded in getting rotationMatrix. inclination: ${data.inclination}, rotation: ${data.rotation}"
    )
} catch (e: BusinessException) {
    AppLog.error("Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}")
}
```

## func getSensorList()

```cangjie
public func getSensorList(): Array<Sensor>
```

**功能：** 获取设备上的所有传感器信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Sensor](#class-sensor)>|返回传感器属性列表。|

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
    let sensors = getSensorList()
    for (index in 0..sensors.size) {
        AppLog.info("Succeeded in getting sensor${index}: ${sensors[index].sensorId} ")
    }
} catch (e: BusinessException) {
    AppLog.error("Failed to get sensor list. Code: ${e.code}, message: ${e.message}")
}
```