## class GyroscopeResponse

```cangjie
public class GyroscopeResponse <: Response {
    public GyroscopeResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32
    )
}
```

**功能：** 陀螺仪传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** 设备x轴的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 设备y轴的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 设备z轴的旋转角速度，单位rad/s。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### GyroscopeResponse(Float32, Float32, Float32)

```cangjie
public GyroscopeResponse(
    public var x: Float32,
    public var y: Float32,
    public var z: Float32
)
```

**功能：** 构造陀螺仪传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|设备x轴的旋转角速度，单位rad/s。|
|y|Float32|是|-|设备y轴的旋转角速度，单位rad/s。|
|z|Float32|是|-|设备z轴的旋转角速度，单位rad/s。|