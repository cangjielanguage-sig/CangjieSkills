## class MagneticFieldUncalibratedResponse

```cangjie
public class MagneticFieldUncalibratedResponse <: Response {
    public MagneticFieldUncalibratedResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32,
        public var biasX: Float32,
        public var biasY: Float32,
        public var biasZ: Float32
    )
}
```

**功能：** 未校准磁场传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var biasX

```cangjie
public var biasX: Float32
```

**功能：** x轴未校准环境磁场强度偏量，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var biasY

```cangjie
public var biasY: Float32
```

**功能：** y轴未校准环境磁场强度偏量，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var biasZ

```cangjie
public var biasZ: Float32
```

**功能：** z轴未校准环境磁场强度偏量，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var x

```cangjie
public var x: Float32
```

**功能：** x轴未校准环境磁场强度，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** y轴未校准环境磁场强度，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** z轴未校准环境磁场强度，单位：μT。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### MagneticFieldUncalibratedResponse(Float32, Float32, Float32, Float32, Float32, Float32)

```cangjie
public MagneticFieldUncalibratedResponse(
    public var x: Float32,
        public var y: Float32,
        public var z: Float32,
        public var biasX: Float32,
        public var biasY: Float32,
        public var biasZ: Float32
)
```

**功能：** 构造未校准磁场传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|x轴未校准环境磁场强度，单位：μT。  |
|y|Float32|是|-|y轴未校准环境磁场强度，单位：μT。  |
|z|Float32|是|-|z轴未校准环境磁场强度，单位：μT。  |
|biasX|Float32|是|-|x轴未校准环境磁场强度偏量，单位：μT。|
|biasY|Float32|是|-|y轴未校准环境磁场强度偏量，单位：μT。|
|biasZ|Float32|是|-|z轴未校准环境磁场强度偏量，单位：μT。|