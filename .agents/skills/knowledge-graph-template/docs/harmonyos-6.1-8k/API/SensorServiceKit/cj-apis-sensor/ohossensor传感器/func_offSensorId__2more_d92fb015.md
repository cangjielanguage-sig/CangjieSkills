## func off(SensorId, ?CallbackObject)

```cangjie
public func off(sensorType: SensorId, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名 | 类型 | 必填  | 默认值  | 说明 |
|:---------- |:--- |:--- |:---- |:----- |
| sensorType | [SensorId](#enum-sensorid)| 是   | -    | 传感器类型。|
| callback   | ?[CallbackObject](../arkinterop/cj-api-callback_invoke.md#class-callbackobject) | 否   | None | **命名参数。** 需要取消订阅的回调函数，若无此参数，则取消订阅当前类型的所有回调函数。 |

**异常：**

- BusinessException：对应错误码如下表，详见[传感器错误码](./cj-errorcode-sensor.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission verification failed. The application does not have permission to call the API. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

class SensorCallback <: Callback1Argument<OrientationResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: OrientationResponse): Unit {
        Hilog.info(0, "test", "Succeeded in getting SensorCallback1 arg: steps: ${arg.timestamp}, alpha: ${arg.alpha},  beta: ${arg.beta},  gamma: ${arg.gamma}", "")
    }
}

let callback1 = SensorCallback()
let callback2 = SensorCallback()
try {
    on(SensorId.Orientation, callback1)
    on(SensorId.Orientation, callback2)
    // 仅取消callback1的注册
    off(SensorId.Orientation, callback: callback1)
    // 取消注册SensorId.ORIENTATION的所有回调
    off(SensorId.Orientation)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

## func on\<T>(SensorId, Callback1Argument\<T>, ?Options) where T \<: Response

```cangjie
public func on<T>(sensorType: SensorId, callback: Callback1Argument<T>, option!: ?Options = None): Unit where T <: Response
```

**功能：** 订阅传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名        | 类型 | 必填  | 默认值  | 说明 |
|:---------- |:--------- |:--- |:---- |:---- |
| sensorType | [SensorId](#enum-sensorid) | 是   | -    | 传感器类型。|
| callback   | [Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<T> | 是   | -    | 回调函数。|
| option     | ?[Options](#class-options) | 否   | None | **命名参数。** 可选参数列表，用于设置传感器上报频率，默认值为200000000ns。 |

**异常：**

- BusinessException：对应错误码如下表，详见[传感器错误码](./cj-errorcode-sensor.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission verification failed. The application does not have permission to call the API. |
  | 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; 2. Sensor service ipc exception;3. Sensor data channel exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

class AccelerometerCallback <: Callback1Argument<AccelerometerResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: AccelerometerResponse): Unit {
        Hilog.info(0, "test", "Succeeded in getting AccelerometerCallback arg: timestamp: ${arg.timestamp}, x: ${arg.x},  y: ${arg.y},  z: ${arg.z}", "")
    }
}

let callback = AccelerometerCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    on(SensorId.Accelerometer, callback, option: options)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```