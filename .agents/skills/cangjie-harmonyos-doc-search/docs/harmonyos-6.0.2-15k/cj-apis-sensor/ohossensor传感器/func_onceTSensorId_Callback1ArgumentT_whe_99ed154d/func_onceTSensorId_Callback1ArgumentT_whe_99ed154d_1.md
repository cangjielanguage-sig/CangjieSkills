## func once\<T>(SensorId, Callback1Argument\<T>) where T <: Response

```cangjie
public func once<T>(`type`: SensorId, callback: Callback1Argument<T>): Unit where T <: Response
```

**功能：** 获取一次传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[SensorId](#enum-sensorid)|是|-|传感器类型。|
|callback|[Callback1Argument\<T>](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<T>|是|-|回调函数，异步上报的传感器数据，每种传感器类型对应的数据类型不同。|

目前支持的传感器类型如下表：

|传感器类型|异步上报的传感器数据类型|需要权限|
|---|---|---|
|ACCELEROMETER|[AccelerometerResponse](#class-accelerometerresponse)|ohos.permission.ACCELEROMETER|
|ACCELEROMETER_UNCALIBRATED|[AccelerometerUncalibratedResponse](#class-accelerometeruncalibratedresponse)|ohos.permission.ACCELEROMETER|
|AMBIENT_LIGHT|[LightResponse](#class-lightresponse)|NA|
|AMBIENT_TEMPERATURE|[AmbientTemperatureResponse](#class-ambienttemperatureresponse)|NA|
|BAROMETER|[BarometerResponse](#class-barometerresponse)|NA|
|GRAVITY|[GravityResponse](#class-gravityresponse)|NA|
|GYROSCOPE|[GyroscopeResponse](#class-gyroscoperesponse)|ohos.permission.GYROSCOPE|
|GYROSCOPE_UNCALIBRATED|[GyroscopeUncalibratedResponse](#class-gyroscopeuncalibratedresponse)|ohos.permission.GYROSCOPE|
|HALL|[HallResponse](#class-hallresponse)|NA|
|HEART_RATE|[HeartRateResponse](#class-heartrateresponse)|ohos.permission.READ_HEALTH_DATA|
|HUMIDITY|[HumidityResponse](#class-humidityresponse)|NA|
|LINEAR_ACCELEROMETER|[LinearAccelerometerResponse](#class-linearaccelerometerresponse)|ohos.permission.ACCELEROMETER|
|MAGNETIC_FIELD|[MagneticFieldResponse](#class-magneticfieldresponse)|NA|
|MAGNETIC_FIELD_UNCALIBRATED|[MagneticFieldUncalibratedResponse](#class-magneticfielduncalibratedresponse)|NA|
|ORIENTATION|[OrientationResponse](#class-orientationresponse)|NA|
|PEDOMETER|[PedometerResponse](#class-pedometerresponse)|ohos.permission.ACTIVITY_MOTION|
|PEDOMETER_DETECTION|[PedometerDetectionResponse](#class-pedometerdetectionresponse)|ohos.permission.ACTIVITY_MOTION|
|PROXIMITY|[ProximityResponse](#class-proximityresponse)|NA|
|ROTATION_VECTOR|[RotationVectorResponse](#class-rotationvectorresponse)|NA|
|SIGNIFICANT_MOTION|[SignificantMotionResponse](#class-significantmotionresponse)|NA|
|WEAR_DETECTION|[WearDetectionResponse](#class-weardetectionresponse)|NA|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[传感器错误码](../../errorcodes/cj-errorcode-sensor.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                                     |
  | -------- | ------------------------------------------------------------ |
  | 201      | Permission denied.                                           |
  | 401      | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
  | 14500101 | Service exception.                   |

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
        AppLog.error(
            "Succeeded in getting SensorCallback arg: steps: ${arg.timestamp}, alpha: ${arg.alpha},  beta: ${arg.beta},  gamma: ${arg.gamma}"
        )
    }
}

let callback = SensorCallback()
try {
    once(SensorId.ORIENTATION, callback)
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```