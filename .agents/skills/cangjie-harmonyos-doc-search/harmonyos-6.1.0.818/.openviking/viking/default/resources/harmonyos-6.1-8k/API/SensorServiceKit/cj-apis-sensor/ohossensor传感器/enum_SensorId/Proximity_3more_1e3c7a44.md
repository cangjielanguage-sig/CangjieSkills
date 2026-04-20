### Proximity

```cangjie
Proximity
```

**功能：** 接近光传感器。

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

class ProximityCallback <: Callback1Argument<ProximityResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: ProximityResponse): Unit {
        Hilog.info(0, "test", "Proximity data: timestamp: ${arg.timestamp}, distance: ${arg.distance}", "")
    }
}

let callback = ProximityCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.Proximity, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.Proximity, callback)

    // 取消订阅传感器数据
    off(SensorId.Proximity, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### RotationVector

```cangjie
RotationVector
```

**功能：** 旋转矢量传感器。

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

class RotationVectorCallback <: Callback1Argument<RotationVectorResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: RotationVectorResponse): Unit {
        Hilog.info(0, "test", "RotationVector data: timestamp: ${arg.timestamp}, x: ${arg.x}, y: ${arg.y}, z: ${arg.z}, w: ${arg.w}", "")
    }
}

let callback = RotationVectorCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.RotationVector, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.RotationVector, callback)

    // 取消订阅传感器数据
    off(SensorId.RotationVector, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### SignificantMotion

```cangjie
SignificantMotion
```

**功能：** 有效运动传感器。

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

class SignificantMotionCallback <: Callback1Argument<SignificantMotionResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: SignificantMotionResponse): Unit {
        Hilog.info(0, "test", "SignificantMotion data: timestamp: ${arg.timestamp}, scalar: ${arg.scalar}", "")
    }
}

let callback = SignificantMotionCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.SignificantMotion, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.SignificantMotion, callback)

    // 取消订阅传感器数据
    off(SensorId.SignificantMotion, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```