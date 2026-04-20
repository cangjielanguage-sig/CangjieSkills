## class SensorOptions

```cangjie
public class SensorOptions {
    public SensorOptions(
        public var interval: IntervalOption
    )
}
```

**功能：** 设置传感器上报频率。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

### var interval

```cangjie
public var interval: IntervalOption
```

**功能：** 表示传感器的上报频率，默认值为200000000ns。该属性有最小值和最大值的限制，由硬件支持的上报频率决定，当设置频率大于最大值时以最大值上报数据，小于最小值时以最小值上报数据。

**类型：** [IntervalOption](#enum-intervaloption)

**读写能力：** 可读写

**起始版本：** 19

### SensorOptions(IntervalOption)

```cangjie
public SensorOptions(
    public var interval: IntervalOption
)
```

**功能：** 构造设置传感器上报频率。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interval|[IntervalOption](#enum-intervaloption)|是|-|表示传感器的上报频率，默认值为200000000ns。该属性有最小值和最大值的限制，由硬件支持的上报频率决定，当设置频率大于最大值时以最大值上报数据，小于最小值时以最小值上报数据。|

## class SignificantMotionResponse

```cangjie
public class SignificantMotionResponse <: Response {
    public SignificantMotionResponse(
        public var scalar: Float32
    )
}
```

**功能：** 有效运动传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var scalar

```cangjie
public var scalar: Float32
```

**功能：** 表示剧烈运动程度。测量三个物理轴（x、y&nbsp;和&nbsp;z）上，设备是否存在大幅度运动；若存在大幅度运动则数据上报为1。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### SignificantMotionResponse(Float32)

```cangjie
public SignificantMotionResponse(
    public var scalar: Float32)
```

**功能：** 构造有效运动传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scalar|Float32|是|-|表示剧烈运动程度。测量三个物理轴（x、y&nbsp;和&nbsp;z）上，设备是否存在大幅度运动；若存在大幅度运动则数据上报为1。|

## class WearDetectionResponse

```cangjie
public class WearDetectionResponse <: Response {
    public WearDetectionResponse(
        public var value: Float32
    )
}
```

**功能：** 佩戴检测传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var value

```cangjie
public var value: Float32
```

**功能：** 表示设备是否被穿戴（1表示已穿戴，0表示未穿戴）。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### WearDetectionResponse(Float32)

```cangjie
public WearDetectionResponse(
    public var value: Float32
    )
```

**功能：** 构造佩戴检测传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float32|是|-|表示设备是否被穿戴（1表示已穿戴，0表示未穿戴）。|