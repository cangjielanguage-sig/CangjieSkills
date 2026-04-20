## class OrientationResponse

```cangjie
public class OrientationResponse <: Response {
    public OrientationResponse(
        public var alpha: Float32,
        public var beta: Float32,
        public var gamma: Float32
    )
}
```

**功能：** 方向传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var alpha

```cangjie
public var alpha: Float32
```

**功能：** 设备围绕Z轴的旋转角度，单位：度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var beta

```cangjie
public var beta: Float32
```

**功能：** 设备围绕X轴的旋转角度，单位：度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var gamma

```cangjie
public var gamma: Float32
```

**功能：** 设备围绕Y轴的旋转角度，单位：度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### OrientationResponse(Float32, Float32, Float32)

```cangjie
public OrientationResponse(
    public var alpha: Float32,
    public var beta: Float32,
    public var gamma: Float32
)
```

**功能：** 构造方向传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alpha|Float32|是|-|设备围绕Z轴的旋转角度，单位：度。|
|beta|Float32|是|-|设备围绕X轴的旋转角度，单位：度。|
|gamma|Float32|是|-|设备围绕Y轴的旋转角度，单位：度。|

## class PedometerDetectionResponse

```cangjie
public class PedometerDetectionResponse <: Response {
    public PedometerDetectionResponse(
        public var scalar: Float32)
}
```

**功能：** 计步检测传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var scalar

```cangjie
public var scalar: Float32
```

**功能：** 计步器检测。检测用户的计步动作，如果取值为1则代表用户产生了计步行走的动作，取值为0则代表用户没有发生运动。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### PedometerDetectionResponse(Float32)

```cangjie
public PedometerDetectionResponse(
    public var scalar: Float32)
```

**功能：** 构造计步检测传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scalar|Float32|是|-|计步器检测。检测用户的计步动作，如果取值为1则代表用户产生了计步行走的动作，取值为0则代表用户没有发生运动。|

## class PedometerResponse

```cangjie
public class PedometerResponse <: Response {
    public PedometerResponse(
        public var steps: Float32
    )
}
```

**功能：** 计步传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var steps

```cangjie
public var steps: Float32
```

**功能：** 用户的行走步数。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### PedometerResponse(Float32)

```cangjie
public PedometerResponse(
    public var steps: Float32)
```

**功能：** 构造计步传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|steps|Float32|是|-|用户的行走步数。|