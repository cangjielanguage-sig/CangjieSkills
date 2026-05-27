## func getInclination(Array\<Float32>)

```cangjie
public func getInclination(inclinationMatrix: Array<Float32>): Float32
```

**功能：** 根据倾斜矩阵计算地磁倾角，使用Callback异步方式返回结果。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|inclinationMatrix|Array\<Float32>|是|-|倾斜矩阵。|

**返回值：**

|类型|说明|
|:----|:----|
|Float32|地磁倾角，单位为弧度。|

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
    let inclinationMatrix: Array<Float32> = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    let data = getInclination(inclinationMatrix)
    AppLog.info("Succeeded in getting inclination: ${data}")
} catch (e: BusinessException) {
    AppLog.error("Failed to get inclination. Code: ${e.code}, message: ${e.message}")
}
```

## func getOrientation(Array\<Float32>)

```cangjie
public func getOrientation(rotationMatrix: Array<Float32>): Array<Float32>
```

**功能：** 根据旋转矩阵计算设备方向。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotationMatrix|Array\<Float32>|是|-|旋转矩阵。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|返回围绕z、x、y轴方向的旋转角度。|

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
    let preRotationMatrix: Array<Float32> = [1.0, 0.0, 0.0, 0.0, 0.87, -0.50, 0.0, 0.50, 0.87]
    let data = getOrientation(preRotationMatrix)
    AppLog.info("Succeeded in getting orientation: ${data}")
} catch (e: BusinessException) {
    AppLog.error("Failed to get orientation. Code: ${e.code}, message: ${e.message}")
}
```