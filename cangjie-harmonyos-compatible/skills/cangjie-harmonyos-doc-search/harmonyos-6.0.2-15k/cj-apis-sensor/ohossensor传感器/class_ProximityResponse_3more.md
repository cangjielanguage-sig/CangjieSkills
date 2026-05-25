## class ProximityResponse

```cangjie
public class ProximityResponse <: Response {
    public ProximityResponse(
        public var distance: Float32)
}
```

**功能：** 接近光传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var distance

```cangjie
public var distance: Float32
```

**功能：** 可见物体与设备显示器的接近程度。0表示接近，大于0表示远离。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### ProximityResponse(Float32)

```cangjie
public ProximityResponse(
    public var distance: Float32)
```

**功能：** 构造接近光传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|distance|Float32|是|-|可见物体与设备显示器的接近程度。0表示接近，大于0表示远离。|

## class Response

```cangjie
public abstract class Response {
    public Response(
        public var timestamp: Int64,
        public var accuracy: SensorAccuracy
    )
}
```

**功能：** 传感器数据的时间戳。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

### var accuracy

```cangjie
public var accuracy: SensorAccuracy
```

**功能：** 传感器数据上报的精度档位值。

**类型：** [SensorAccuracy](#enum-sensoraccuracy)

**读写能力：** 可读写

**起始版本：** 19

### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 传感器数据上报的时间戳。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### Response(Int64, SensorAccuracy)

```cangjie
public Response(
    public var timestamp: Int64,
    public var accuracy: SensorAccuracy
)
```

**功能：** 构造加速度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timestamp|Int64|是|-|传感器数据上报的时间戳。|
|accuracy|[SensorAccuracy](#enum-sensoraccuracy)|是|-|传感器数据上报的精度档位值。|

## class RotationVectorResponse

```cangjie
public class RotationVectorResponse <: Response {
    public RotationVectorResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32,
        public var w: Float32
    )
}
```

**功能：** 旋转矢量传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var w

```cangjie
public var w: Float32
```

**功能：** 标量。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var x

```cangjie
public var x: Float32
```

**功能：** 旋转矢量x轴分量。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 旋转矢量y轴分量。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 旋转矢量z轴分量。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### RotationVectorResponse(Float32, Float32, Float32, Float32)

```cangjie
public RotationVectorResponse(
    public var x: Float32,
    public var y: Float32,
    public var z: Float32,
    public var w: Float32
)
```

**功能：** 构造旋转矢量传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|旋转矢量x轴分量。|
|y|Float32|是|-|旋转矢量y轴分量。|
|z|Float32|是|-|旋转矢量z轴分量。|
|w|Float32|是|-|标量。|