### Gravity

```cangjie
Gravity
```

**功能：** 重力传感器。

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

class GravityCallback <: Callback1Argument<GravityResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: GravityResponse): Unit {
        Hilog.info(0, "test", "Gravity data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}", "")
    }
}

let callback = GravityCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.Gravity, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.Gravity, callback)

    // 取消订阅传感器数据
    off(SensorId.Gravity, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### Gyroscope

```cangjie
Gyroscope
```

**功能：** 陀螺仪传感器。

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

class GyroscopeCallback1 <: Callback1Argument<GyroscopeResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: GyroscopeResponse): Unit {
        Hilog.info(0, "test", "Gyroscope data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}", "")
    }
}

let callback = GyroscopeCallback1()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.Gyroscope, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.Gyroscope, callback)

    // 取消订阅传感器数据
    off(SensorId.Gyroscope, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### GyroscopeUncalibrated

```cangjie
GyroscopeUncalibrated
```

**功能：** 未校准陀螺仪传感器。

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

class GyroscopeUncalibratedCallback <: Callback1Argument<GyroscopeUncalibratedResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: GyroscopeUncalibratedResponse): Unit {
        Hilog.info(0, "test", "GyroscopeUncalibrated data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}, biasX: ${arg.biasX}, biasY: ${arg.biasY}, biasZ: ${arg.biasZ}", "")
    }
}

let callback = GyroscopeUncalibratedCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.GyroscopeUncalibrated, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.GyroscopeUncalibrated, callback)

    // 取消订阅传感器数据
    off(SensorId.GyroscopeUncalibrated, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```