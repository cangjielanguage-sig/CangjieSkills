## func on\<T>(SensorId, Callback1Argument\<T>, ?SensorOptions) where T <: Response

```cangjie
public func on<T>(`type`: SensorId, callback: Callback1Argument<T>, option!: ?SensorOptions = None): Unit where T <: Response
```

**功能：** 订阅传感器数据。

**需要权限：** ohos.permission.ACCELEROMETER

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[SensorId](#enum-sensorid)|是|-|传感器类型。|
|callback|[Callback1Argument\<T>](../BasicServicesKit/cj-apis-base.md#class-callback1argument)|是|-|回调函数，异步上报的传感器数据，每种传感器类型对应的数据类型不同。|
|option|?[SensorOptions](#class-sensoroptions)|否|None| **命名参数。** 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。|

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
  | 14500101 | Service exception.                                           |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*