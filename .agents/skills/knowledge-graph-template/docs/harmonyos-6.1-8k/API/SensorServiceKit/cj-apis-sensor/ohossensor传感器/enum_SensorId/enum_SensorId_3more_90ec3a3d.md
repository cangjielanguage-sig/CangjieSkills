## enum SensorId

```cangjie
public enum SensorId <: Equatable<SensorId> & ToString {
    | Accelerometer
    | Gyroscope
    | AmbientLight
    | MagneticField
    | Barometer
    | Hall
    | Proximity
    | Humidity
    | Orientation
    | Gravity
    | LinearAccelerometer
    | RotationVector
    | AmbientTemperature
    | MagneticFieldUncalibrated
    | GyroscopeUncalibrated
    | SignificantMotion
    | PedometerDetection
    | Pedometer
    | HeartRate
    | WearDetection
    | AccelerometerUncalibrated
    | ...
}
```

**功能：** 表示当前支持订阅或取消订阅的传感器类型。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- Equatable\<[SensorId](#enum-sensorid)>
- ToString

### Accelerometer

```cangjie
Accelerometer
```

**功能：** 加速度传感器。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

class AccelerometerCallback1 <: Callback1Argument<AccelerometerResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: AccelerometerResponse): Unit {
        Hilog.info(0, "test", "Accelerometer data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}", "")
    }
}

let callback = AccelerometerCallback1()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.Accelerometer, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.Accelerometer, callback)

    // 取消订阅传感器数据
    off(SensorId.Accelerometer, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### AccelerometerUncalibrated

```cangjie
AccelerometerUncalibrated
```

**功能：** 未校准加速度传感器。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

class AccelerometerUncalibratedCallback <: Callback1Argument<AccelerometerUncalibratedResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: AccelerometerUncalibratedResponse): Unit {
        Hilog.info(0, "test", "AccelerometerUncalibrated data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}, biasX: ${arg.biasX}, biasY: ${arg.biasY}, biasZ: ${arg.biasZ}", "")
    }
}

let callback = AccelerometerUncalibratedCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.AccelerometerUncalibrated, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.AccelerometerUncalibrated, callback)

    // 取消订阅传感器数据
    off(SensorId.AccelerometerUncalibrated, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```