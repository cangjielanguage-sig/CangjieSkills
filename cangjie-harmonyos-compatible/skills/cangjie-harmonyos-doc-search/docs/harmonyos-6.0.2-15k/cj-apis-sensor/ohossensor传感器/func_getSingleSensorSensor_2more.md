## func getSingleSensor(SensorId)

```cangjie
public func getSingleSensor(`type`: SensorId): Sensor
```

**功能：** 获取指定类型的传感器信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[SensorId](#enum-sensorid)|是|-|传感器类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[Sensor](#class-sensor)|返回传感器信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[传感器错误码](../../errorcodes/cj-errorcode-sensor.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.|
  |14500101|Service exception.|
  |14500102|The sensor is not supported by the device.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

try {
    let sensors = getSingleSensor(SensorId.ACCELEROMETER)
    AppLog.info("Succeeded in getting sensor: ${sensors.sensorName} ")
} catch (e: BusinessException) {
    AppLog.error("Failed to get sensor. Code: ${e.code}, message: ${e.message}")
}
```

## func off(SensorId, ?CallbackObject)

```cangjie
public func off(`type`: SensorId, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[SensorId](#enum-sensorid)|是|-|传感器类型。|
|callback|[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 回调函数，异步上报的传感器数据，每种传感器类型对应的数据类型不同。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class SensorCallback <: Callback1Argument<OrientationResponse> {
    init() {}
    public func invoke(arg: OrientationResponse): Unit {
        AppLog.info(
            "Succeeded in getting SensorCallback1 arg: steps: ${arg.timestamp}, alpha: ${arg.alpha},  beta: ${arg.beta},  gamma: ${arg.gamma}"
        )
    }
}

let callback1 = SensorCallback()
let callback2 = SensorCallback()
try {
    on(SensorId.ORIENTATION, callback1)
    on(SensorId.ORIENTATION, callback2)
    // 仅取消callback1的注册
    off(SensorId
        .ORIENTATION, callback: callback1)
    // 取消注册SensorId.ORIENTATION的所有回调
    off(SensorId.ORIENTATION)
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```