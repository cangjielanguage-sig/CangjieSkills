### Hall

```cangjie
Hall
```

**功能：** 霍尔传感器。

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

class HallCallback <: Callback1Argument<HallResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: HallResponse): Unit {
        Hilog.info(0, "test", "Hall data: timestamp: ${arg.timestamp}, status: ${arg.status}", "")
    }
}

let callback = HallCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.Hall, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.Hall, callback)

    // 取消订阅传感器数据
    off(SensorId.Hall, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### HeartRate

```cangjie
HeartRate
```

**功能：** 心率传感器。

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

class HeartRateCallback <: Callback1Argument<HeartRateResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: HeartRateResponse): Unit {
        Hilog.info(0, "test", "HeartRate data: timestamp: ${arg.timestamp}, heartRate: ${arg.heartRate}", "")
    }
}

let callback = HeartRateCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.HeartRate, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.HeartRate, callback)

    // 取消订阅传感器数据
    off(SensorId.HeartRate, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### Humidity

```cangjie
Humidity
```

**功能：** 湿度传感器。

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

class HumidityCallback <: Callback1Argument<HumidityResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: HumidityResponse): Unit {
        Hilog.info(0, "test", "Humidity data: timestamp: ${arg.timestamp}, humidity: ${arg.humidity}", "")
    }
}

let callback = HumidityCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.Humidity, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.Humidity, callback)

    // 取消订阅传感器数据
    off(SensorId.Humidity, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```