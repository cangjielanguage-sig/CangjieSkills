## enum SensorId

```cangjie
public enum SensorId <: Equatable<SensorId> & ToString {
    | ACCELEROMETER
    | GYROSCOPE
    | AMBIENT_LIGHT
    | MAGNETIC_FIELD
    | BAROMETER
    | HALL
    | PROXIMITY
    | HUMIDITY
    | ORIENTATION
    | GRAVITY
    | LINEAR_ACCELEROMETER
    | ROTATION_VECTOR
    | AMBIENT_TEMPERATURE
    | MAGNETIC_FIELD_UNCALIBRATED
    | GYROSCOPE_UNCALIBRATED
    | SIGNIFICANT_MOTION
    | PEDOMETER_DETECTION
    | PEDOMETER
    | HEART_RATE
    | WEAR_DETECTION
    | ACCELEROMETER_UNCALIBRATED
    | UNSUPPORTED
    | ...
}
```

**功能：** 表示当前支持订阅或取消订阅的传感器类型。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- Equatable\<SensorId>
- ToString

### ACCELEROMETER

```cangjie
ACCELEROMETER
```

**功能：** 加速度传感器。

**起始版本：** 19

### ACCELEROMETER_UNCALIBRATED

```cangjie
ACCELEROMETER_UNCALIBRATED
```

**功能：** 未校准加速度计传感器。

**起始版本：** 19

### AMBIENT_LIGHT

```cangjie
AMBIENT_LIGHT
```

**功能：** 环境光传感器。

**起始版本：** 19

### AMBIENT_TEMPERATURE

```cangjie
AMBIENT_TEMPERATURE
```

**功能：** 环境温度传感器。

**起始版本：** 19

### BAROMETER

```cangjie
BAROMETER
```

**功能：** 气压计传感器。

**起始版本：** 19

### GRAVITY

```cangjie
GRAVITY
```

**功能：** 重力传感器。

**起始版本：** 19

### GYROSCOPE

```cangjie
GYROSCOPE
```

**功能：** 陀螺仪传感器。

**起始版本：** 19

### GYROSCOPE_UNCALIBRATED

```cangjie
GYROSCOPE_UNCALIBRATED
```

**功能：** 未校准陀螺仪传感器。

**起始版本：** 19

### HALL

```cangjie
HALL
```

**功能：** 霍尔传感器。

**起始版本：** 19

### HEART_RATE

```cangjie
HEART_RATE
```

**功能：** 心率传感器。

**起始版本：** 19

### HUMIDITY

```cangjie
HUMIDITY
```

**功能：** 湿度传感器。

**起始版本：** 19

### LINEAR_ACCELEROMETER

```cangjie
LINEAR_ACCELEROMETER
```

**功能：** 线性加速度传感器。

**起始版本：** 19

### MAGNETIC_FIELD

```cangjie
MAGNETIC_FIELD
```

**功能：** 磁场传感器。

**起始版本：** 19

### MAGNETIC_FIELD_UNCALIBRATED

```cangjie
MAGNETIC_FIELD_UNCALIBRATED
```

**功能：** 未校准磁场传感器。

**起始版本：** 19

### ORIENTATION

```cangjie
ORIENTATION
```

**功能：** 方向传感器。

**起始版本：** 19

### PEDOMETER

```cangjie
PEDOMETER
```

**功能：** 计步传感器。

**起始版本：** 19

### PEDOMETER_DETECTION

```cangjie
PEDOMETER_DETECTION
```

**功能：** 计步检测传感器。

**起始版本：** 19

### PROXIMITY

```cangjie
PROXIMITY
```

**功能：** 接近光传感器。

**起始版本：** 19

### ROTATION_VECTOR

```cangjie
ROTATION_VECTOR
```

**功能：** 旋转矢量传感器。

**起始版本：** 19

### SIGNIFICANT_MOTION

```cangjie
SIGNIFICANT_MOTION
```

**功能：** 有效运动传感器。

**起始版本：** 19

### UNSUPPORTED

```cangjie
UNSUPPORTED
```

**功能：** 未支持的传感器类型。

**起始版本：** 19

### WEAR_DETECTION

```cangjie
WEAR_DETECTION
```

**功能：** 佩戴检测传感器。

**起始版本：** 19

### func !=(SensorId)

```cangjie
public operator func !=(other: SensorId): Bool
```

**功能：** 判断两个[SensorId](#enum-sensorid) 是否不相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SensorId](#enum-sensorid)|是|-|传入的[SensorId](#enum-sensorid)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果不相等，则返回true；否则，返回false。|

### func ==(SensorId)

```cangjie
public operator func ==(other: SensorId): Bool
```

**功能：** 判断两个[SensorId](#enum-sensorid) 是否相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SensorId](#enum-sensorid)|是|-|传入的[SensorId](#enum-sensorid)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果相等，则返回true；否则，返回false。|