## class Sensor

```cangjie
public class Sensor {
    public var sensorName: String
    public var vendorName: String
    public var firmwareVersion: String
    public var hardwareVersion: String
    public var sensorId: Int32
    public var maxRange: Float32
    public var minSamplePeriod: Int64
    public var maxSamplePeriod: Int64
    public var precision: Float32
    public var power: Float32
}
```

**功能：** 指示传感器信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var firmwareVersion

```cangjie
public var firmwareVersion: String
```

**功能：** 传感器固件版本。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var hardwareVersion

```cangjie
public var hardwareVersion: String
```

**功能：** 传感器硬件版本。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var maxRange

```cangjie
public var maxRange: Float32
```

**功能：** 传感器测量范围的最大值。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var maxSamplePeriod

```cangjie
public var maxSamplePeriod: Int64
```

**功能：** 允许的最大采样周期。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var minSamplePeriod

```cangjie
public var minSamplePeriod: Int64
```

**功能：** 允许的最小采样周期。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var power

```cangjie
public var power: Float32
```

**功能：** 传感器功率的估计值，单位：mA。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var precision

```cangjie
public var precision: Float32
```

**功能：** 传感器精度。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var sensorId

```cangjie
public var sensorId: Int32
```

**功能：** 传感器类型id。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var sensorName

```cangjie
public var sensorName: String
```

**功能：** 传感器名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var vendorName

```cangjie
public var vendorName: String
```

**功能：** 传感器供应商。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22