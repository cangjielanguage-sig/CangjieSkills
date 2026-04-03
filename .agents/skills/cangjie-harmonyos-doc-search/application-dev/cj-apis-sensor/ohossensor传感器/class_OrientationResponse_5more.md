## class OrientationResponse

```cangjie
public class OrientationResponse <: Response {
    public var alpha: Float32
    public var beta: Float32
    public var gamma: Float32
}
```

**功能：** 方向传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var alpha

```cangjie
public var alpha: Float32
```

**功能：** 设备围绕Z轴的旋转角度，单位：度；取值范围为0-360度。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var beta

```cangjie
public var beta: Float32
```

**功能：** 设备围绕X轴的旋转角度，单位：度；取值范围为0-±180度。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var gamma

```cangjie
public var gamma: Float32
```

**功能：** 设备围绕Y轴的旋转角度，单位：度；取值范围为0-±90度。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class PedometerDetectionResponse

```cangjie
public class PedometerDetectionResponse <: Response {
    public var scalar: Float32
}
```

**功能：** 计步检测传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var scalar

```cangjie
public var scalar: Float32
```

**功能：** 计步器检测。检测用户的计步动作，如果取值为1则代表用户产生了计步行走的动作，取值为0则代表用户没有发生运动。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class PedometerResponse

```cangjie
public class PedometerResponse <: Response {
    public var steps: Float32
}
```

**功能：** 计步传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var steps

```cangjie
public var steps: Float32
```

**功能：** 用户的行走步数。步数初始值是0。用户订阅计步传感器后，每行走一步，步数累计加一。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class ProximityResponse

```cangjie
public class ProximityResponse <: Response {
    public var distance: Float32
}
```

**功能：** 接近光传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var distance

```cangjie
public var distance: Float32
```

**功能：** 可见物体与设备显示器的接近程度。0表示接近，大于0表示远离。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class Response

```cangjie
public open class Response {
    public var timestamp: Int64
    public var accuracy: SensorAccuracy
}
```

**功能：** 传感器数据的时间戳。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var accuracy

```cangjie
public var accuracy: SensorAccuracy
```

**功能：** 传感器数据上报的精度挡位值。

**类型：** [SensorAccuracy](#enum-sensoraccuracy)

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 传感器数据上报的时间戳。从设备开机开始计时到上报数据的时间，单位 : ns。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22