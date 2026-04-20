## class SignificantMotionResponse

```cangjie
public class SignificantMotionResponse <: Response {
    public var scalar: Float32
}
```

**功能：** 有效运动传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var scalar

```cangjie
public var scalar: Float32
```

**功能：** 表示剧烈运动程度。测量三个物理轴（x、y&nbsp;和&nbsp;z）上，设备是否存在大幅度运动；若存在大幅度运动则数据上报为1。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class WearDetectionResponse

```cangjie
public class WearDetectionResponse <: Response {
    public var value: Float32
}
```

**功能：** 佩戴检测传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var value

```cangjie
public var value: Float32
```

**功能：** 表示设备是否被穿戴（1表示已穿戴，0表示未穿戴）。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22