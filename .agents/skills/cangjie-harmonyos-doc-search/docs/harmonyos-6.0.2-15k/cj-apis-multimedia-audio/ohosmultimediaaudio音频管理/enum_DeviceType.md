## enum DeviceType

```cangjie
public enum DeviceType <: Equatable<DeviceType> & ToString {
    | INVALID
    | EARPIECE
    | SPEAKER
    | WIRED_HEADSET
    | WIRED_HEADPHONES
    | BLUETOOTH_SCO
    | BLUETOOTH_A2DP
    | MIC
    | USB_HEADSET
    | DISPLAY_PORT
    | REMOTE_CAST
    | DEFAULT
    | UNKNOWN
    | ...
}
```

**功能：** 设备类型。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**父类型：**

- Equatable\<[DeviceType](#enum-devicetype)>
- ToString

### BLUETOOTH_A2DP

```cangjie
BLUETOOTH_A2DP
```

**功能：** 蓝牙设备A2DP（Advanced Audio Distribution Profile）连接。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### BLUETOOTH_SCO

```cangjie
BLUETOOTH_SCO
```

**功能：** 蓝牙设备SCO（Synchronous Connection Oriented）连接。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 默认设备类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### DISPLAY_PORT

```cangjie
DISPLAY_PORT
```

**功能：** DisplayPort（显示接口，简称DP），用于外接扩展设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### EARPIECE

```cangjie
EARPIECE
```

**功能：** 听筒。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INVALID

```cangjie
INVALID
```

**功能：** 无效设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### MIC

```cangjie
MIC
```

**功能：** 麦克风。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### REMOTE_CAST

```cangjie
REMOTE_CAST
```

**功能：** 音频被系统应用投送到其他远程的设备。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SPEAKER

```cangjie
SPEAKER
```

**功能：** 扬声器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### USB_HEADSET

```cangjie
USB_HEADSET
```

**功能：** USB耳机，带麦克风。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知类型设备。

**起始版本：** 19

### WIRED_HEADPHONES

```cangjie
WIRED_HEADPHONES
```

**功能：** 有线耳机, 无麦克风。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### WIRED_HEADSET

```cangjie
WIRED_HEADSET
```

**功能：** 有线耳机, 带麦克风。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(DeviceType)

```cangjie
public operator func !=(other: DeviceType): Bool
```

**功能：** 对设备类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceType](#enum-devicetype)|是|-|设备类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备类型不同，返回true，否则返回false。|

### func ==(DeviceType)

```cangjie
public operator func ==(other: DeviceType): Bool
```

**功能：** 对设备类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeviceType](#enum-devicetype)|是|-|设备类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取设备类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|设备类型枚举值的字符串表示。|