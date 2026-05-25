### WearDetection

```cangjie
WearDetection
```

**功能：** 佩戴检测传感器。

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

class WearDetectionCallback <: Callback1Argument<WearDetectionResponse> {
    init() {}
    public func invoke(err: ?BusinessException, arg: WearDetectionResponse): Unit {
        Hilog.info(0, "test", "WearDetection data: timestamp: ${arg.timestamp}, value: ${arg.value}", "")
    }
}

let callback = WearDetectionCallback()
let options = Options(interval: IntervalOption.SensorNumber(100000000))
try {
    // 订阅传感器数据
    on(SensorId.WearDetection, callback, option: options)

    // 获取一次传感器数据
    once(SensorId.WearDetection, callback)

    // 取消订阅传感器数据
    off(SensorId.WearDetection, callback: callback)
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```

### func !=(SensorId)

```cangjie
public operator func !=(other: SensorId): Bool
```

**功能：** 判断两个[SensorId](#enum-sensorid) 是否不相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名   | 类型                         | 必填  | 默认值 | 说明                             |
|:----- |:-------------------------- |:--- |:--- |:------------------------------ |
| other | [SensorId](#enum-sensorid) | 是   | -   | 传入的[SensorId](#enum-sensorid)。 |

**返回值：**

| 类型   | 说明                        |
|:---- |:------------------------- |
| Bool | 如果不相等，则返回true；否则，返回false。 |

### func ==(SensorId)

```cangjie
public operator func ==(other: SensorId): Bool
```

**功能：** 判断两个[SensorId](#enum-sensorid) 是否相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名   | 类型                         | 必填  | 默认值 | 说明                             |
|:----- |:-------------------------- |:--- |:--- |:------------------------------ |
| other | [SensorId](#enum-sensorid) | 是   | -   | 传入的[SensorId](#enum-sensorid)。 |

**返回值：**

| 类型   | 说明                       |
|:---- |:------------------------ |
| Bool | 如果相等，则返回true；否则，返回false。 |

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举值。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**返回值：**

| 类型    | 说明   |
|:----- |:---- |
| Int32 | 枚举值。 |

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将枚举值转换为字符串。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**返回值：**

| 类型     | 说明       |
|:------ |:-------- |
| String | 转换后的字符串。 |