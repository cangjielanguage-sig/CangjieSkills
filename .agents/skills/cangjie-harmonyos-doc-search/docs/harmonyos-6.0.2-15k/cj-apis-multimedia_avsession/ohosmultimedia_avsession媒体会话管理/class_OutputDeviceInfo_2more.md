## class OutputDeviceInfo

```cangjie
public class OutputDeviceInfo {
    public OutputDeviceInfo(
        public var devices: Array<DeviceInfo>
    )
}
```

**功能：** 播放设备的相关信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var devices

```cangjie
public var devices: Array<DeviceInfo>
```

**功能：** 播放设备的集合。

**类型：** Array\<[DeviceInfo](#class-deviceinfo)>

**读写能力：** 可读写

**起始版本：** 19

### OutputDeviceInfo(Array\<DeviceInfo>)

```cangjie
public OutputDeviceInfo(
    public var devices: Array<DeviceInfo>
)
```

**功能：** [OutputDeviceInfo](#class-outputdeviceinfo)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|devices|Array\<[DeviceInfo](#class-deviceinfo)>|是|-|播放设备的集合。|

## class PlaybackPosition

```cangjie
public class PlaybackPosition {
    public var elapsedTime: Int64
    public var updateTime: Int64
    public init(elapsedTime: Int64, updateTime: Int64)
}
```

**功能：** 媒体播放位置的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var elapsedTime

```cangjie
public var elapsedTime: Int64
```

**功能：** 已用时间，单位毫秒（ms）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var updateTime

```cangjie
public var updateTime: Int64
```

**功能：** 更新时间，单位毫秒（ms）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### init(Int64, Int64)

```cangjie
public init(elapsedTime: Int64, updateTime: Int64)
```

**功能：** 媒体播放位置的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elapsedTime|Int64|是|-|已用时间，单位毫秒（ms）。|
|updateTime|Int64|是|-|更新时间，单位毫秒（ms）。|