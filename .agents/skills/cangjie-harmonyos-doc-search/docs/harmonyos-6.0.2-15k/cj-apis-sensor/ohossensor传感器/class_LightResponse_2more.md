## class LightResponse

```cangjie
public class LightResponse <: Response {
    public LightResponse(
        public var intensity: Float32,
        public var colorTemperature!: ?Float32 = None,
        public var infraredLuminance!: ?Float32 = None
    )
}
```

**功能：** 环境光传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var colorTemperature

```cangjie
public var colorTemperature: ?Float32 = None
```

**功能：** 色温（单位：开尔文），可选参数，如果该参数不支持在js层返回未定义，支持则返回正常数值。

**类型：** ?Float32

**读写能力：** 可读写

**起始版本：** 19

### var infraredLuminance

```cangjie
public var infraredLuminance: ?Float32 = None
```

**功能：** 红外亮度（单位：cd/m²），可选参数，如果该参数不支持在js层返回未定义，支持则返回正常数值。

**类型：** ?Float32

**读写能力：** 可读写

**起始版本：** 19

### var intensity

```cangjie
public var intensity: Float32
```

**功能：** 光强（单位：勒克斯）。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### LightResponse(Float32, ?Float32, ?Float32)

```cangjie
public LightResponse(
    public var intensity: Float32,
    public var colorTemperature!: ?Float32 = None,
    public var infraredLuminance!: ?Float32 = None
)
```

**功能：** 构造环境光传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|intensity|Float32|是|-|光强（单位：勒克斯）。|
|colorTemperature|?Float32|否|None| **命名参数。** 色温（单位：开尔文），可选参数，如果该参数不支持在js层返回未定义，支持则返回正常数值。|
|infraredLuminance|?Float32|否|None| **命名参数。** 红外亮度（单位：cd/m²），可选参数，如果该参数不支持在js层返回未定义，支持则返回正常数值。|

## class LinearAccelerometerResponse

```cangjie
public class LinearAccelerometerResponse <: Response {
    public LinearAccelerometerResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32
    )
}
```

**功能：** 线性加速度传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** 施加在设备x轴的线性加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 施加在设备y轴的线性加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 施加在设备z轴的线性加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### LinearAccelerometerResponse(Float32, Float32, Float32)

```cangjie
public LinearAccelerometerResponse(
    public var x: Float32,
    public var y: Float32,
    public var z: Float32
)
```

**功能：** 构造线性加速度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|施加在设备x轴的线性加速度，单位：m/s²。|
|y|Float32|是|-|施加在设备y轴的线性加速度，单位：m/s²。|
|z|Float32|是|-|施加在设备z轴的线性加速度，单位：m/s²。|