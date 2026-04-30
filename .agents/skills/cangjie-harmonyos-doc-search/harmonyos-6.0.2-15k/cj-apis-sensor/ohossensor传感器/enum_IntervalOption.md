## enum IntervalOption

```cangjie
public enum IntervalOption <: Equatable<IntervalOption> & ToString {
    | SensorNumber(Int64)
    | GameMode
    | UIMode
    | NormalMode
    | ...
}
```

**功能：** 传感器上报频率的选项。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- Equatable\<IntervalOption>
- ToString

### GameMode

```cangjie
GameMode
```

**功能：** 用于指定传感器上报频率，频率值为20000000ns，该频率被设置在硬件支持的频率范围内时会生效。

**起始版本：** 19

### NormalMode

```cangjie
NormalMode
```

**功能：** 用于指定传感器上报频率，频率值为200000000ns，该频率被设置在硬件支持的频率范围内时会生效，值固定为'normal'字符串。

**起始版本：** 19

### SensorNumber(Int64)

```cangjie
SensorNumber(Int64)
```

**功能：** 用于指定传感器上报频率，该频率被设置在硬件支持的频率范围内时会生效。

**起始版本：** 19

### UIMode

```cangjie
UIMode
```

**功能：** 用于指定传感器上报频率，频率值为60000000ns，该频率被设置在硬件支持的频率范围内时会生效。

**起始版本：** 19

### func !=(IntervalOption)

```cangjie
public operator func !=(other: IntervalOption): Bool
```

**功能：** 判断两个[IntervalOption](#enum-intervaloption) 是否不相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[IntervalOption](#enum-intervaloption)|是|-|传入的[IntervalOption](#enum-intervaloption)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果不相等，则返回true；否则，返回false。|

### func ==(IntervalOption)

```cangjie
public operator func ==(other: IntervalOption): Bool
```

**功能：** 判断两个[IntervalOption](#enum-intervaloption) 是否相等。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[IntervalOption](#enum-intervaloption)|是|-|传入的[IntervalOption](#enum-intervaloption)。|

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