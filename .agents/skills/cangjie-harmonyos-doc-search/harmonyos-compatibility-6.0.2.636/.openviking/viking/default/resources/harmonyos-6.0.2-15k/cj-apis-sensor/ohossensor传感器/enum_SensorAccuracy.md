## enum SensorAccuracy

```cangjie
public enum SensorAccuracy <: Equatable<SensorAccuracy> & ToString {
    | ACCURACY_UNRELIABLE
    | ACCURACY_LOW
    | ACCURACY_MEDIUM
    | ACCURACY_HIGH
    | ...
}
```

**功能：** 传感器数据的精度。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- Equatable\<SensorAccuracy>
- ToString

### ACCURACY_HIGH

```cangjie
ACCURACY_HIGH
```

**功能：** 传感器高档位精度。

**起始版本：** 19

### ACCURACY_LOW

```cangjie
ACCURACY_LOW
```

**功能：** 传感器低档位精度。

**起始版本：** 19

### ACCURACY_MEDIUM

```cangjie
ACCURACY_MEDIUM
```

**功能：** 传感器中档位精度。

**起始版本：** 19

### ACCURACY_UNRELIABLE

```cangjie
ACCURACY_UNRELIABLE
```

**功能：** 传感器数据不可信。

**起始版本：** 19

### func !=(SensorAccuracy)

```cangjie
public operator func !=(other: SensorAccuracy): Bool
```

**功能：** 判断两个[SensorAccuracy](#enum-sensoraccuracy) 是否不相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SensorAccuracy](#enum-sensoraccuracy)|是|-|传入的[SensorAccuracy](#enum-sensoraccuracy)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果不相等，则返回true；否则，返回false。|

### func ==(SensorAccuracy)

```cangjie
public operator func ==(other: SensorAccuracy): Bool
```

**功能：** 判断两个[SensorAccuracy](#enum-sensoraccuracy) 是否相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SensorAccuracy](#enum-sensoraccuracy)|是|-|传入的[SensorAccuracy](#enum-sensoraccuracy)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果相等，则返回true；否则，返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将枚举值转换为字符串。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的字符串。|