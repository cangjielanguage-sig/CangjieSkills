### LinearAccelerometer

```cangjie
LinearAccelerometer
```

**功能：** 线性加速度传感器。

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

class LinearAccelerometerCallback <: Callback1Argument<LinearAccelerometerResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: LinearAccelerometerResponse): Unit {
        Hilog.info(0, "test", "LinearAccelerometer data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}", "")
    }
}

let callback = LinearAccelerometerCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.LinearAccelerometer, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.LinearAccelerometer, callback)

    // 取消订阅传感器数据
    off(SensorId.LinearAccelerometer, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### MagneticField

```cangjie
MagneticField
```

**功能：** 磁场传感器。

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

class MagneticFieldCallback <: Callback1Argument<MagneticFieldResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: MagneticFieldResponse): Unit {
        Hilog.info(0, "test", "MagneticField data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}", "")
    }
}

let callback = MagneticFieldCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.MagneticField, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.MagneticField, callback)

    // 取消订阅传感器数据
    off(SensorId.MagneticField, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### MagneticFieldUncalibrated

```cangjie
MagneticFieldUncalibrated
```

**功能：** 未校准磁场传感器。

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

class MagneticFieldUncalibratedCallback <: Callback1Argument<MagneticFieldUncalibratedResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: MagneticFieldUncalibratedResponse): Unit {
        Hilog.info(0, "test", "MagneticFieldUncalibrated data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}, biasX: ${arg.biasX}, biasY: ${arg.biasY}, biasZ: ${arg.biasZ}", "")
    }
}

let callback = MagneticFieldUncalibratedCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.MagneticFieldUncalibrated, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.MagneticFieldUncalibrated, callback)

    // 取消订阅传感器数据
    off(SensorId.MagneticFieldUncalibrated, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```