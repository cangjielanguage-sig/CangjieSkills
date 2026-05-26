## enum DeviceUsage

```cangjie
public enum DeviceUsage <: Equatable<DeviceUsage> & ToString {
    | MEDIA_OUTPUT_DEVICES
    | MEDIA_INPUT_DEVICES
    | ALL_MEDIA_DEVICES
    | CALL_OUTPUT_DEVICES
    | CALL_INPUT_DEVICES
    | ALL_CALL_DEVICES
    | ...
}
```

**功能：** 可获取的设备种类。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**父类型：**

- Equatable\<[DeviceUsage](#enum-deviceusage)>
- ToString

### ALL_CALL_DEVICES

```cangjie
ALL_CALL_DEVICES
```

**功能：** 所有通话设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ALL_MEDIA_DEVICES

```cangjie
ALL_MEDIA_DEVICES
```

**功能：** 所有媒体设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CALL_INPUT_DEVICES

```cangjie
CALL_INPUT_DEVICES
```

**功能：** 通话输入设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CALL_OUTPUT_DEVICES

```cangjie
CALL_OUTPUT_DEVICES
```

**功能：** 通话输出设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### MEDIA_INPUT_DEVICES

```cangjie
MEDIA_INPUT_DEVICES
```

**功能：** 媒体输入设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### MEDIA_OUTPUT_DEVICES

```cangjie
MEDIA_OUTPUT_DEVICES
```

**功能：** 媒体输出设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(DeviceUsage)

```cangjie
public operator func !=(other: DeviceUsage): Bool
```

**功能：** 对设备种类枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceUsage](#enum-deviceusage)|是|-|可获取的设备种类。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备种类不同，返回true，否则返回false。|

### func ==(DeviceUsage)

```cangjie
public operator func ==(other: DeviceUsage): Bool
```

**功能：** 对设备种类枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceUsage](#enum-deviceusage)|是|-|可获取的设备种类。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备种类相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取设备种类枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|设备种类枚举值的字符串表示。|