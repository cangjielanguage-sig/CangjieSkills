## class GyroscopeUncalibratedResponse

```cangjie
public class GyroscopeUncalibratedResponse <: Response {
    public GyroscopeUncalibratedResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32,
        public var biasX: Float32,
        public var biasY: Float32,
        public var biasZ: Float32
    )
}
```

**功能：** 未校准陀螺仪传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var biasX

```cangjie
public var biasX: Float32
```

**功能：** 设备x轴未校准的旋转角速度偏量，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var biasY

```cangjie
public var biasY: Float32
```

**功能：** 设备y轴未校准的旋转角速度偏量，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var biasZ

```cangjie
public var biasZ: Float32
```

**功能：** 设备z轴未校准的旋转角速度偏量，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var x

```cangjie
public var x: Float32
```

**功能：** 设备x轴未校准的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 设备y轴未校准的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 设备z轴未校准的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### GyroscopeUncalibratedResponse(Float32, Float32, Float32, Float32, Float32, Float32)

```cangjie
public GyroscopeUncalibratedResponse(
    public var x: Float32,
    public var y: Float32,
    public var z: Float32,
    public var biasX: Float32,
    public var biasY: Float32,
    public var biasZ: Float32
)
```

**功能：** 构造未校准陀螺仪传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|设备x轴未校准的旋转角速度，单位rad/s。|
|y|Float32|是|-|设备y轴未校准的旋转角速度，单位rad/s。|
|z|Float32|是|-|设备z轴未校准的旋转角速度，单位rad/s。|
|biasX|Float32|是|-|设备x轴未校准的旋转角速度偏量，单位rad/s。|
|biasY|Float32|是|-|设备y轴未校准的旋转角速度偏量，单位rad/s。|
|biasZ|Float32|是|-|设备z轴未校准的旋转角速度偏量，单位rad/s。|