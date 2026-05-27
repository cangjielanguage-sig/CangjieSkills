## enum AudioStreamDeviceChangeReason

```cangjie
public enum AudioStreamDeviceChangeReason <: Equatable<AudioStreamDeviceChangeReason> & ToString {
    | REASON_UNKNOWN
    | REASON_NEW_DEVICE_AVAILABLE
    | REASON_OLD_DEVICE_UNAVAILABLE
    | REASON_OVERRODE
    | ...
}
```

**功能：** 流设备变更原因。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**父类型：**

- Equatable\<[AudioStreamDeviceChangeReason](#enum-audiostreamdevicechangereason)>
- ToString

### REASON_NEW_DEVICE_AVAILABLE

```cangjie
REASON_NEW_DEVICE_AVAILABLE
```

**功能：** 新设备可用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### REASON_OLD_DEVICE_UNAVAILABLE

```cangjie
REASON_OLD_DEVICE_UNAVAILABLE
```

**功能：** 旧设备不可用。当报告此原因时，应用程序应考虑暂停音频播放。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### REASON_OVERRODE

```cangjie
REASON_OVERRODE
```

**功能：** 强选。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### REASON_UNKNOWN

```cangjie
REASON_UNKNOWN
```

**功能：** 未知原因。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioStreamDeviceChangeReason)

```cangjie
public operator func !=(other: AudioStreamDeviceChangeReason): Bool
```

**功能：** 对流设备变更原因枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioStreamDeviceChangeReason](#enum-audiostreamdevicechangereason)|是|-|流设备变更原因。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果流设备变更原因不同，返回true，否则返回false。|

### func ==(AudioStreamDeviceChangeReason)

```cangjie
public operator func ==(other: AudioStreamDeviceChangeReason): Bool
```

**功能：** 对流设备变更原因枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioStreamDeviceChangeReason](#enum-audiostreamdevicechangereason)|是|-|流设备变更原因。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果流设备变更原因相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取流设备变更原因枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|流设备变更原因枚举值的字符串表示。|