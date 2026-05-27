# ohos.sensor（传感器）

sensor模块提供了获取传感器数据的能力，包括获取传感器属性列表，订阅传感器数据，以及一些通用的传感器算法。

## 导入模块

```cangjie
import kit.SensorServiceKit.*
```

## 权限列表

ohos.permission.ACCELEROMETER

ohos.permission.GYROSCOPE

ohos.permission.READ_HEALTH_DATA

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getAngleVariation(Array\<Float32>, Array\<Float32>)

```cangjie
public func getAngleVariation(currentRotationMatrix: Array<Float32>, preRotationMatrix: Array<Float32>): Array<Float32>
```

**功能：** 计算两个旋转矩阵之间的角度变化。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|currentRotationMatrix|Array\<Float32>|是|-|当前旋转矩阵。|
|preRotationMatrix|Array\<Float32>|是|-|相对旋转矩阵。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|返回绕z、x、y轴方向的旋转角度。|

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
    let currentRotationMatrix: Array<Float32> = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    let preRotationMatrix: Array<Float32> = [1.0, 0.0, 0.0, 0.0, 0.87, -0.50, 0.0, 0.50, 0. 87]
    let data = getAngleVariation(currentRotationMatrix, preRotationMatrix)
    AppLog.info("Succeeded in getting angle variation: ${data}")
} catch (e: BusinessException) {
    AppLog.error("Failed to get angle variation. Code: ${e.code}, message: ${e.message}")
}
```

## func getDeviceAltitude(Float32, Float32)

```cangjie
public func getDeviceAltitude(seaPressure: Float32, currentPressure: Float32): Float32
```

**功能：** 根据气压值获取海拔高度。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|seaPressure|Float32|是|-|海平面气压值，单位为hPa。|
|currentPressure|Float32|是|-|指定的气压值，单位为hPa。|

**返回值：**

|类型|说明|
|:----|:----|
|Float32|指定的气压值对应的海拔高度，单位为米。|

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
    let seaPressure = 1013.2f32
    let currentPressure = 1500.0f32
    let data = getDeviceAltitude(seaPressure, currentPressure)
    AppLog.info("Succeeded in getting altitude: ${data}")
} catch (e: BusinessException) {
    AppLog.error("Failed to get altitude. Code: ${e.code}, message: ${e.message}")
}
```