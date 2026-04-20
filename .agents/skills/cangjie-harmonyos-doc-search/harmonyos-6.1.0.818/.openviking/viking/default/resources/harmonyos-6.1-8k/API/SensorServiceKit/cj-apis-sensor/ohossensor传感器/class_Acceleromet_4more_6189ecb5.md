## class AccelerometerUncalibratedResponse

```cangjie
public class AccelerometerUncalibratedResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
    public var biasX: Float32
    public var biasY: Float32
    public var biasZ: Float32
}
```

**功能：** 未校准加速度计传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var biasX

```cangjie
public var biasX: Float32
```

**功能：** 施加在设备x轴未校准的加速度偏量，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var biasY

```cangjie
public var biasY: Float32
```

**功能：** 施加在设备y轴未校准的加速度偏量，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var biasZ

```cangjie
public var biasZ: Float32
```

**功能：** 施加在设备z轴未校准的加速度偏量，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var x

```cangjie
public var x: Float32
```

**功能：** 施加在设备x轴未校准的加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var y

```cangjie
public var y: Float32
```

**功能：** 施加在设备y轴未校准的加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var z

```cangjie
public var z: Float32
```

**功能：** 施加在设备z轴未校准的加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class AmbientTemperatureResponse

```cangjie
public class AmbientTemperatureResponse <: Response {
    public var temperature: Float32
}
```

**功能：** 温度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var temperature

```cangjie
public var temperature: Float32
```

**功能：** 环境温度（单位：摄氏度）。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class BarometerResponse

```cangjie
public class BarometerResponse <: Response {
    public var pressure: Float32
}
```

**功能：** 气压计传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var pressure

```cangjie
public var pressure: Float32
```

**功能：** 压力值（单位：百帕）。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class GravityResponse

```cangjie
public class GravityResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
}
```

**功能：** 重力传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** 施加在设备x轴的重力加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var y

```cangjie
public var y: Float32
```

**功能：** 施加在设备y轴的重力加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var z

```cangjie
public var z: Float32
```

**功能：** 施加在设备z轴的重力加速度，单位 : m/s²。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22