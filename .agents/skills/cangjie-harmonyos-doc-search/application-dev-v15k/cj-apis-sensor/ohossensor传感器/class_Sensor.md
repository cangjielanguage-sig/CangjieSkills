## class Sensor

```cangjie
public class Sensor {
    public Sensor(
        public var sensorName: String,
        public var vendorName: String,
        public var firmwareVersion: String,
        public var hardwareVersion: String,
        public var sensorId: SensorId,
        public var maxRange: Float32,
        public var minSamplePeriod: Int64,
        public var maxSamplePeriod: Int64,
        public var precision: Float32,
        public var power: Float32
    )
}
```

**功能：** 指示传感器信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

### var firmwareVersion

```cangjie
public var firmwareVersion: String
```

**功能：** 传感器固件版本。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var hardwareVersion

```cangjie
public var hardwareVersion: String
```

**功能：** 传感器硬件版本。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var maxRange

```cangjie
public var maxRange: Float32
```

**功能：** 传感器测量范围的最大值。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var maxSamplePeriod

```cangjie
public var maxSamplePeriod: Int64
```

**功能：** 允许的最大采样周期。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var minSamplePeriod

```cangjie
public var minSamplePeriod: Int64
```

**功能：** 允许的最小采样周期。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var power

```cangjie
public var power: Float32
```

**功能：** 传感器功率的估计值，单位：mA。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var precision

```cangjie
public var precision: Float32
```

**功能：** 传感器精度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var sensorId

```cangjie
public var sensorId: SensorId
```

**功能：** 传感器类型id。

**类型：** [SensorId](#enum-sensorid)

**读写能力：** 可读写

**起始版本：** 19

### var sensorName

```cangjie
public var sensorName: String
```

**功能：** 传感器名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var vendorName

```cangjie
public var vendorName: String
```

**功能：** 传感器供应商。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Sensor(String, String, String, String, SensorId, Float32, Int64, Int64, Float32, Float32)

```cangjie
public Sensor(
    public var sensorName: String,
        public var vendorName: String,
        public var firmwareVersion: String,
        public var hardwareVersion: String,
        public var sensorId: SensorId,
        public var maxRange: Float32,
        public var minSamplePeriod: Int64,
        public var maxSamplePeriod: Int64,
        public var precision: Float32,
        public var power: Float32
)
```

**功能：** 指示传感器信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sensorName|String|是|-|传感器名称。|
|vendorName|String|是|-|传感器供应商。|
|firmwareVersion|String|是|-|传感器固件版本。|
|hardwareVersion|String|是|-|传感器硬件版本。|
|sensorId|[SensorId](#enum-sensorid)|是|-|传感器类型id。|
|maxRange|Float32|是|-|传感器测量范围的最大值。|
|minSamplePeriod|Int64|是|-|允许的最小采样周期。|
|maxSamplePeriod|Int64|是|-|允许的最大采样周期。|
|precision|Float32|是|-|传感器精度。|
|power|Float32|是|-|传感器功率的估计值，单位：mA。|