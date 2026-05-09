## class GyroscopeResponse

```cangjie
public class GyroscopeResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
}
```

**功能：** 陀螺仪传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** 设备x轴的旋转角速度，单位rad/s；取值为实际上报物理量。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var y

```cangjie
public var y: Float32
```

**功能：** 设备y轴的旋转角速度，单位rad/s；取值为实际上报物理量。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var z

```cangjie
public var z: Float32
```

**功能：** 设备z轴的旋转角速度，单位rad/s；取值为实际上报物理量。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class GyroscopeUncalibratedResponse

```cangjie
public class GyroscopeUncalibratedResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
    public var biasX: Float32
    public var biasY: Float32
    public var biasZ: Float32
}
```

**功能：** 未校准陀螺仪传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var biasX

```cangjie
public var biasX: Float32
```

**功能：** 设备x轴未校准的旋转角速度偏量，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var biasY

```cangjie
public var biasY: Float32
```

**功能：** 设备y轴未校准的旋转角速度偏量，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var biasZ

```cangjie
public var biasZ: Float32
```

**功能：** 设备z轴未校准的旋转角速度偏量，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var x

```cangjie
public var x: Float32
```

**功能：** 设备x轴未校准的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var y

```cangjie
public var y: Float32
```

**功能：** 设备y轴未校准的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var z

```cangjie
public var z: Float32
```

**功能：** 设备z轴未校准的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class HallResponse

```cangjie
public class HallResponse <: Response {
    public var status: Float32
}
```

**功能：** 霍尔传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var status

```cangjie
public var status: Float32
```

**功能：** 显示霍尔状态。测量设备周围是否存在磁力吸引，0表示没有，大于0表示有。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class HeartRateResponse

```cangjie
public class HeartRateResponse <: Response {
    public var heartRate: Float32
}
```

**功能：** 心率传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var heartRate

```cangjie
public var heartRate: Float32
```

**功能：** 心率值。测量用户的心率数值，单位：bpm。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22