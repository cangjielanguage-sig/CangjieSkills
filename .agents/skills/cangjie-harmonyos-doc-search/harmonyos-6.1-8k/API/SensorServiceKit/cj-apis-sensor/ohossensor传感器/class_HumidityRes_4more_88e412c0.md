## class HumidityResponse

```cangjie
public class HumidityResponse <: Response {
    public var humidity: Float32
}
```

**功能：** 湿度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var humidity

```cangjie
public var humidity: Float32
```

**功能：** 湿度值。测量环境的相对湿度，以百分比&nbsp;(%)&nbsp;表示。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class LightResponse

```cangjie
public class LightResponse <: Response {
    public var intensity: Float32
    public var colorTemperature:?Float32
    public var infraredLuminance:?Float32
}
```

**功能：** 环境光传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var colorTemperature

```cangjie
public var colorTemperature:?Float32
```

**功能：** 色温（单位：开尔文），如果不支持该属性则返回固定值（固定值由传感器自定义），支持则返回正常数值。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var infraredLuminance

```cangjie
public var infraredLuminance:?Float32
```

**功能：** 红外亮度（单位：cd/m²），如果不支持该属性则返回固定值（固定值由传感器自定义），支持则返回正常数值。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var intensity

```cangjie
public var intensity: Float32
```

**功能：** 光强（单位：勒克斯）。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class LinearAccelerometerResponse

```cangjie
public class LinearAccelerometerResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
}
```

**功能：** 线性加速度传感器数据。

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

## class MagneticFieldResponse

```cangjie
public class MagneticFieldResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
}
```

**功能：** 磁场传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** x轴环境磁场强度，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var y

```cangjie
public var y: Float32
```

**功能：** y轴环境磁场强度，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var z

```cangjie
public var z: Float32
```

**功能：** z轴环境磁场强度，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22