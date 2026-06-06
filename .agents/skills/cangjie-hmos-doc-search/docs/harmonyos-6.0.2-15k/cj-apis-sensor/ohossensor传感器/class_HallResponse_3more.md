## class HallResponse

```cangjie
public class HallResponse <: Response {
    public HallResponse(
        public var status: Float32
    )
}
```

**功能：** 霍尔传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var status

```cangjie
public var status: Float32
```

**功能：** 显示霍尔状态。测量设备周围是否存在磁力吸引，0表示没有，大于0表示有。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### HallResponse(Float32)

```cangjie
public HallResponse(
    public var status: Float32)
```

**功能：** 构造霍尔传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|status|Float32|是|-|显示霍尔状态。测量设备周围是否存在磁力吸引，0表示没有，大于0表示有。|

## class HeartRateResponse

```cangjie
public class HeartRateResponse <: Response {
    public HeartRateResponse(
        public var heartRate: Float32)
}
```

**功能：** 心率传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var heartRate

```cangjie
public var heartRate: Float32
```

**功能：** 心率值。测量用户的心率数值，单位：bpm。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### HeartRateResponse(Float32)

```cangjie
public HeartRateResponse(
    public var heartRate: Float32)
```

**功能：** 构造心率传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|heartRate|Float32|是|-|心率值。测量用户的心率数值，单位：bpm。|

## class HumidityResponse

```cangjie
public class HumidityResponse <: Response {
    public HumidityResponse(
        public var humidity: Float32
    )
}
```

**功能：** 湿度传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var humidity

```cangjie
public var humidity: Float32
```

**功能：** 湿度值。测量环境的相对湿度，以百分比&nbsp;(%)&nbsp;表示。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### HumidityResponse(Float32)

```cangjie
public HumidityResponse(
    public var humidity: Float32)
```

**功能：** 构造湿度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|humidity|Float32|是|-|湿度值。测量环境的相对湿度，以百分比&nbsp;(%)&nbsp;表示。|