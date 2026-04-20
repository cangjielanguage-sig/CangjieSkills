## func once\<T>(SensorId, Callback1Argument\<T>) where T \<: Response

```cangjie
public func once<T>(sensorType: SensorId, callback: Callback1Argument<T>): Unit where T <: Response
```

**功能：** 获取一次传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| sensorType | [SensorId](#enum-sensorid) | 是 | - | 传感器类型。 |
| callback   | [Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<T> | 是   | -   | **命名参数。** 回调函数，异步上报的传感器数据，每种传感器类型对应的数据类型不同。 |

**异常：**

- BusinessException：对应错误码如下表，详见[传感器错误码](./cj-errorcode-sensor.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission verification failed. The application does not have permission to call the API. |
  | 14500101 | Service exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

class GyroscopeCallback <: Callback1Argument<GyroscopeResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: GyroscopeResponse): Unit {
        Hilog.info(0, "test", "Succeeded in getting GyroscopeCallback arg: timestamp: ${arg.timestamp}, x: ${arg.x},  y: ${arg.y},  z: ${arg.z}", "")
    }
}

let callback = GyroscopeCallback()
try {
    once(SensorId.Gyroscope, callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

## class AccelerometerResponse

```cangjie
public class AccelerometerResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
}
```

**功能：** 加速度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** 施加在设备x轴的线性加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var y

```cangjie
public var y: Float32
```

**功能：** 施加在设备y轴的线性加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var z

```cangjie
public var z: Float32
```

**功能：** 施加在设备z轴的线性加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22