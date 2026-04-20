## class AmbientTemperatureResponse

```cangjie
public class AmbientTemperatureResponse <: Response {
    public AmbientTemperatureResponse(
        public var temperature: Float32)
}
```

**功能：** 温度传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var temperature

```cangjie
public var temperature: Float32
```

**功能：** 环境温度（单位：摄氏度）。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### AmbientTemperatureResponse(Float32)

```cangjie
public AmbientTemperatureResponse(
    public var temperature: Float32)
```

**功能：** 构造温度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|temperature|Float32|是|-|环境温度（单位：摄氏度）。|

## class BarometerResponse

```cangjie
public class BarometerResponse <: Response {
    public BarometerResponse(
        public var pressure: Float32)
}
```

**功能：** 气压计传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var pressure

```cangjie
public var pressure: Float32
```

**功能：** 压力值（单位：百帕）。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### BarometerResponse(Float32)

```cangjie
public BarometerResponse(
    public var pressure: Float32
    )
```

**功能：** 构造气压计传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pressure|Float32|是|-|压力值（单位：百帕）。|

## class GravityResponse

```cangjie
public class GravityResponse <: Response {
    public GravityResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32
    )
}
```

**功能：** 重力传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** 施加在设备x轴的重力加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 施加在设备y轴的重力加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 施加在设备z轴的重力加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### GravityResponse(Float32, Float32, Float32)

```cangjie
public GravityResponse(
    public var x: Float32,
    public var y: Float32,
    public var z: Float32
)
```

**功能：** 构造重力传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|施加在设备x轴的重力加速度，单位：m/s²。|
|y|Float32|是|-|施加在设备y轴的重力加速度，单位：m/s²。|
|z|Float32|是|-|施加在设备z轴的重力加速度，单位：m/s²。|