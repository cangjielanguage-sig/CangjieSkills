## class MagneticFieldUncalibratedResponse

```cangjie
public class MagneticFieldUncalibratedResponse <: Response {
    public var x: Float32
    public var y: Float32
    public var z: Float32
    public var biasX: Float32
    public var biasY: Float32
    public var biasZ: Float32
}
```

**功能：** 未校准磁场传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**父类型：**

- [Response](#class-response)

### var biasX

```cangjie
public var biasX: Float32
```

**功能：** x轴未校准环境磁场强度偏量，单位 : μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var biasY

```cangjie
public var biasY: Float32
```

**功能：** y轴未校准环境磁场强度偏量，单位 : μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var biasZ

```cangjie
public var biasZ: Float32
```

**功能：** z轴未校准环境磁场强度偏量，单位 : μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var x

```cangjie
public var x: Float32
```

**功能：** x轴未校准环境磁场强度，单位 : μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var y

```cangjie
public var y: Float32
```

**功能：** y轴未校准环境磁场强度，单位 : μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var z

```cangjie
public var z: Float32
```

**功能：** z轴未校准环境磁场强度，单位 : μT。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

## class Options

```cangjie
public class Options {
    public var interval: IntervalOption
    public var sensorInfoParam:?SensorInfoParam
    public init(interval!: IntervalOption = NormalMode, sensorInfoParam!: ?SensorInfoParam = None)
}
```

**功能：** 设置传感器上报频率。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var interval

```cangjie
public var interval: IntervalOption
```

**功能：** 表示传感器的上报频率。该属性有最小值和最大值的限制，由硬件支持的上报频率决定，当设置频率大于最大值时以最大值上报数据，小于最小值时以最小值上报数据。

**类型：** [IntervalOption](#enum-intervaloption)

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var sensorInfoParam

```cangjie
public var sensorInfoParam:?SensorInfoParam
```

**功能：** 传感器传入设置参数，可指定deviceId、sensorIndex。

**类型：** ?[SensorInfoParam](#class-sensorinfoparam)

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### init(IntervalOption, ?SensorInfoParam)

```cangjie
public init(interval!: IntervalOption = NormalMode, sensorInfoParam!: ?SensorInfoParam = None)
```

**功能：** 构造函数，创建Options实例。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名 | 类型 | 必填  | 默认值  | 说明       |
|:--------------- |:------ |:--- |:---------- |:-------- |
| interval        | [IntervalOption](#enum-intervaloption)     | 否   | NormalMode | **命名参数。** 表示传感器的上报频率，默认值为NormalMode。该属性有最小值和最大值的限制，由硬件支持的上报频率决定，当设置频率大于最大值时以最大值上报数据，小于最小值时以最小值上报数据。 |
| sensorInfoParam | ?[SensorInfoParam](#class-sensorinfoparam) | 否   | None       | **命名参数。** 传感器传入设置参数，可指定deviceId、sensorIndex。 |