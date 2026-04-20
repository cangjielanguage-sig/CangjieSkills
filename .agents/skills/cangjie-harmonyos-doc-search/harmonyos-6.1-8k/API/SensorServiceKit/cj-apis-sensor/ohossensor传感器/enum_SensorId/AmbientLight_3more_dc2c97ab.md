### AmbientLight

```cangjie
AmbientLight
```

**功能：** 环境光传感器。

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

class LightCallback <: Callback1Argument<LightResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: LightResponse): Unit {
        Hilog.info(0, "test", "Light data: timestamp: ${arg.timestamp}, intensity: ${arg.intensity}", "")
    }
}

let callback = LightCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.AmbientLight, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.AmbientLight, callback)

    // 取消订阅传感器数据
    off(SensorId.AmbientLight, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### AmbientTemperature

```cangjie
AmbientTemperature
```

**功能：** 环境温度传感器。

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

class AmbientTemperatureCallback <: Callback1Argument<AmbientTemperatureResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: AmbientTemperatureResponse): Unit {
        Hilog.info(0, "test", "AmbientTemperature data: timestamp: ${arg.timestamp}, temperature: ${arg.temperature}", "")
    }
}

let callback = AmbientTemperatureCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.AmbientTemperature, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.AmbientTemperature, callback)

    // 取消订阅传感器数据
    off(SensorId.AmbientTemperature, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### Barometer

```cangjie
Barometer  
```

**功能：** 气压计传感器。

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

class BarometerCallback <: Callback1Argument<BarometerResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: BarometerResponse): Unit {
        Hilog.info(0, "test", "Barometer data: timestamp: ${arg.timestamp}, pressure: ${arg.pressure}", "")
    }
}

let callback = BarometerCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.Barometer, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.Barometer, callback)

    // 取消订阅传感器数据
    off(SensorId.Barometer, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```