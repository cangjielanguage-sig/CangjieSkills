## class AccelerometerUncalibratedResponse

```cangjie
public class AccelerometerUncalibratedResponse <: Response {
    public AccelerometerUncalibratedResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32,
        public var biasX: Float32,
        public var biasY: Float32,
        public var biasZ: Float32
    )
}
```

**功能：** 未校准加速度计传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var biasX

```cangjie
public var biasX: Float32
```

**功能：** 施加在设备x轴未校准的加速度偏量，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var biasY

```cangjie
public var biasY: Float32
```

**功能：** 施加在设备y轴未校准的加速度偏量，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var biasZ

```cangjie
public var biasZ: Float32
```

**功能：** 施加在设备z轴未校准的加速度偏量，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var x

```cangjie
public var x: Float32
```

**功能：** 施加在设备x轴未校准的加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 施加在设备y轴未校准的加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 施加在设备z轴未校准的加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### AccelerometerUncalibratedResponse(Float32, Float32, Float32, Float32, Float32, Float32)

```cangjie
public AccelerometerUncalibratedResponse(
    public var x: Float32,
        public var y: Float32,
        public var z: Float32,
        public var biasX: Float32,
        public var biasY: Float32,
        public var biasZ: Float32
)
```

**功能：** 构造未校准加速度计传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|施加在设备x轴未校准的加速度，单位：m/s²。|
|y|Float32|是|-|施加在设备y轴未校准的加速度，单位：m/s²。|
|z|Float32|是|-|施加在设备z轴未校准的加速度，单位：m/s²。|
|biasX|Float32|是|-|施加在设备x轴未校准的加速度偏量，单位：m/s²。|
|biasY|Float32|是|-|施加在设备y轴未校准的加速度偏量，单位：m/s²。|
|biasZ|Float32|是|-|施加在设备z轴未校准的加速度偏量，单位：m/s²。|